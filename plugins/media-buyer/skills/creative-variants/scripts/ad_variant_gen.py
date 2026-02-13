#!/usr/bin/env python3
"""
ad_variant_gen.py — CLI for generating ad creative variations.

Takes a reference ad image and produces variants at configurable divergence
levels using OpenAI gpt-image-1.5 or Google Imagen/Gemini as the generation
backend.

Usage:
    python3 scripts/ad_variant_gen.py \
        --reference path/to/winning-ad.png \
        --divergence moderate \
        --variants 4 \
        --out-dir output/ad-variants/

Requirements:
    - openai>=1.0.0          (for OpenAI provider)
    - google-genai>=1.0.0    (for Google provider)
    - Pillow>=10.0.0
    - OPENAI_API_KEY or GEMINI_API_KEY / GOOGLE_API_KEY env var set

API references verified against (Feb 2026):
    - OpenAI: https://platform.openai.com/docs/api-reference/images
    - Google: https://googleapis.github.io/python-genai/
    - Google: https://ai.google.dev/gemini-api/docs/imagen

Never paste API keys in chat. Set them as environment variables.
"""

import argparse
import base64
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROVIDERS = ("openai", "google")
DIVERGENCE_LEVELS = ("subtle", "moderate", "dramatic")

# Default models per provider
DEFAULT_MODELS = {
    "openai": "gpt-image-1.5",
    "google-generate": "imagen-4.0-generate-001",
    "google-edit": "imagen-3.0-capability-001",  # Imagen 4 does NOT support editing
    "google-gemini": "gemini-3-pro-image-preview",  # Nano Banana Pro — gen+edit via Gemini API
}

# OpenAI supported sizes (only these work with GPT Image models)
OPENAI_SIZES = {
    "1024x1024": "1024x1024",
    "1536x1024": "1536x1024",  # landscape
    "1024x1536": "1024x1536",  # portrait
    "auto":      "auto",
}

# Google Imagen aspect ratios
GOOGLE_ASPECT_RATIOS = {
    "1:1":  "1:1",
    "4:3":  "4:3",
    "3:4":  "3:4",
    "16:9": "16:9",
    "9:16": "9:16",
}

# Platform -> best size/ratio mappings
PLATFORM_SPECS = {
    "facebook-feed":    {"openai": "1024x1024", "google_ratio": "1:1"},
    "facebook-story":   {"openai": "1024x1536", "google_ratio": "9:16"},
    "instagram-feed":   {"openai": "1024x1024", "google_ratio": "1:1"},
    "instagram-story":  {"openai": "1024x1536", "google_ratio": "9:16"},
    "google-display":   {"openai": "1536x1024", "google_ratio": "16:9"},
    "google-square":    {"openai": "1024x1024", "google_ratio": "1:1"},
    "tiktok":           {"openai": "1024x1536", "google_ratio": "9:16"},
    "linkedin-feed":    {"openai": "1536x1024", "google_ratio": "16:9"},
    "linkedin-square":  {"openai": "1024x1024", "google_ratio": "1:1"},
    "twitter":          {"openai": "1536x1024", "google_ratio": "16:9"},
    "pinterest":        {"openai": "1024x1536", "google_ratio": "3:4"},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)
    return path


def load_image_bytes(path):
    if not path.exists():
        die(f"Reference image not found: {path}")
    return path.read_bytes()


def save_image(data, path):
    path.write_bytes(data)
    return path


def resolve_openai_size(size_arg, platform):
    """Resolve to an OpenAI-supported size string."""
    if size_arg and size_arg in OPENAI_SIZES:
        return OPENAI_SIZES[size_arg]
    if size_arg:
        print(
            f"WARNING: '{size_arg}' is not a supported OpenAI size. "
            f"Supported: {list(OPENAI_SIZES.keys())}. Using 'auto'.",
            file=sys.stderr,
        )
        return "auto"
    if platform:
        key = platform.lower().replace(" ", "-")
        if key in PLATFORM_SPECS:
            return PLATFORM_SPECS[key]["openai"]
    return "1024x1024"


def resolve_google_ratio(ratio_arg, platform):
    """Resolve to a Google-supported aspect ratio."""
    if ratio_arg and ratio_arg in GOOGLE_ASPECT_RATIOS:
        return ratio_arg
    if ratio_arg:
        print(
            f"WARNING: '{ratio_arg}' is not a supported Google ratio. "
            f"Supported: {list(GOOGLE_ASPECT_RATIOS.keys())}. Using '1:1'.",
            file=sys.stderr,
        )
        return "1:1"
    if platform:
        key = platform.lower().replace(" ", "-")
        if key in PLATFORM_SPECS:
            return PLATFORM_SPECS[key]["google_ratio"]
    return "1:1"


def build_variant_filename(index, divergence, ext="png"):
    return f"variant-{index:02d}-{divergence}.{ext}"


# ---------------------------------------------------------------------------
# Provider: OpenAI (gpt-image-1.5)
#
# API ref: https://platform.openai.com/docs/api-reference/images
# Guide:   https://platform.openai.com/docs/guides/image-generation
#
# Key facts:
#   - Latest model: gpt-image-1.5 (Dec 2025)
#   - Sizes: 1024x1024, 1536x1024, 1024x1536, auto
#   - Quality: low, medium, high, auto
#   - input_fidelity: low (default), high -- preserves faces/logos/details
#   - output_format: png, jpeg, webp (GPT Image models always return b64)
#   - output_compression: 0-100 (for jpeg/webp only)
#   - background: transparent, opaque, auto
#   - n: 1-10 images per call
#   - Edit accepts up to 16 input images; first image gets highest fidelity
#     (gpt-image-1.5 preserves first 5 images with higher fidelity)
#   - Edit supports mask (PNG, transparent areas = edit zone)
# ---------------------------------------------------------------------------

def generate_openai(prompt, reference_path, model, size, quality, mode,
                    input_fidelity, output_format):
    """Generate or edit an image via OpenAI Images API. Returns image bytes."""
    try:
        import openai
    except ImportError:
        die("openai package not installed. Run: pip install 'openai>=1.0.0'")

    client = openai.OpenAI()  # Uses OPENAI_API_KEY env var

    if reference_path is not None:
        # Use the edit endpoint with the reference image
        # GPT Image models accept png, webp, or jpg < 50MB
        with open(reference_path, "rb") as img_file:
            response = client.images.edit(
                model=model,
                image=img_file,
                prompt=prompt,
                size=size,
                quality=quality,
                input_fidelity=input_fidelity,
                output_format=output_format,
            )
    else:
        # Pure generation (no reference image provided)
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            output_format=output_format,
        )

    # GPT Image models always return base64-encoded image data
    b64_data = response.data[0].b64_json
    return base64.b64decode(b64_data)


# ---------------------------------------------------------------------------
# Provider: Google
#
# Two paths available:
#
# 1. Imagen API (via google-genai SDK)
#    - Generate: imagen-4.0-generate-001 (also: ultra, fast variants)
#    - Edit: imagen-3.0-capability-001 (Imagen 4 does NOT support editing)
#    - Edit requires Vertex AI (not available on Gemini Developer API)
#    - Uses: client.models.generate_images() / client.models.edit_image()
#    - Sizes: aspect_ratio (1:1, 4:3, 3:4, 16:9, 9:16) or image_size ("2K")
#
# 2. Gemini Image Generation (Nano Banana)
#    - Model: gemini-2.5-flash-image
#    - Supports both gen and edit via client.models.generate_content()
#    - Accepts image input alongside prompt for editing
#    - Simpler API, works with Gemini Developer API key
#    - No Vertex AI required for basic usage
#
# API refs:
#   https://ai.google.dev/gemini-api/docs/imagen
#   https://googleapis.github.io/python-genai/
#   https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md
#
# Auth: GEMINI_API_KEY or GOOGLE_API_KEY env var (Gemini Developer API)
#       OR Vertex AI: GOOGLE_GENAI_USE_VERTEXAI + GOOGLE_CLOUD_PROJECT +
#       GOOGLE_CLOUD_LOCATION
# ---------------------------------------------------------------------------

def generate_google_imagen(prompt, reference_path, model_generate, model_edit,
                           aspect_ratio, mode):
    """Generate or edit via Google Imagen API. Returns image bytes."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        die("google-genai package not installed. Run: pip install 'google-genai>=1.0.0'")

    client = genai.Client()  # Uses GEMINI_API_KEY or GOOGLE_API_KEY env var

    if mode == "edit" and reference_path is not None:
        # Imagen edit requires Vertex AI and uses imagen-3.0-capability-001
        from google.genai.types import (
            RawReferenceImage,
            MaskReferenceImage,
            MaskReferenceConfig,
            EditImageConfig,
            Image as GenAIImage,
        )

        raw_ref = RawReferenceImage(
            reference_id=1,
            reference_image=GenAIImage.from_file(location=str(reference_path)),
        )
        # Use background mask mode -- model auto-detects background
        mask_ref = MaskReferenceImage(
            reference_id=2,
            config=MaskReferenceConfig(
                mask_mode="MASK_MODE_BACKGROUND",
                mask_dilation=0.0,
            ),
        )

        response = client.models.edit_image(
            model=model_edit,
            prompt=prompt,
            reference_images=[raw_ref, mask_ref],
            config=EditImageConfig(
                edit_mode="EDIT_MODE_INPAINT_INSERTION",
                number_of_images=1,
                output_mime_type="image/png",
            ),
        )
    else:
        # Pure generation with Imagen 4
        response = client.models.generate_images(
            model=model_generate,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=aspect_ratio,
                output_mime_type="image/png",
            ),
        )

    if not response.generated_images:
        die("Google Imagen returned no images. The prompt may have been filtered.")

    return response.generated_images[0].image.image_bytes


def generate_google_gemini(prompt, reference_path, model, mode, aspect_ratio="1:1"):
    """Generate or edit via Gemini image generation (Nano Banana).

    Simpler API -- works with Gemini Developer API key, no Vertex AI needed.
    Supports image input for edit-style workflows.

    IMPORTANT SDK notes (verified Feb 2026):
    - response_modalities=["IMAGE"] MUST be set or the model may return text
    - part.inline_data.data is ALREADY raw bytes (SDK decodes base64 internally)
    - Do NOT call base64.b64decode() on it -- that double-decodes and corrupts
    - Use part.as_image() or part.inline_data.data directly
    See: https://ai.google.dev/gemini-api/docs/image-generation
    See: https://googleapis.github.io/python-genai/
    """
    try:
        from google import genai
        from google.genai import types
        from PIL import Image as PILImage
        from io import BytesIO
    except ImportError:
        die(
            "Missing packages. Run:\n"
            "  pip install 'google-genai>=1.0.0' Pillow"
        )

    client = genai.Client()

    contents = [prompt]

    if reference_path is not None:
        # Always pass reference image alongside the prompt
        ref_image = PILImage.open(reference_path)
        contents = [ref_image, prompt]

    response = client.models.generate_content(
        model=model,
        contents=contents,
        # CRITICAL: response_modalities must include "IMAGE" or the model
        # may return a text description instead of generating an image.
        # image_config controls aspect ratio and resolution.
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
            ),
        ),
    )

    # Extract image from response parts.
    # inline_data.data is ALREADY raw bytes in the Python SDK --
    # the SDK decodes base64 internally. Do NOT base64.b64decode() it.
    for part in response.parts:
        if part.inline_data is not None:
            # part.inline_data.data is raw image bytes (png/jpeg)
            # Validate it's a real image before returning
            img_bytes = part.inline_data.data
            try:
                img = PILImage.open(BytesIO(img_bytes))
                img.verify()  # Raises if not a valid image
            except Exception as e:
                die(f"Gemini returned data that isn't a valid image: {e}")
            return img_bytes

    die("Gemini returned no image in the response. Try adjusting the prompt.")


# ---------------------------------------------------------------------------
# Unified generation dispatcher
# ---------------------------------------------------------------------------

def generate_variant(provider, google_backend, prompt, reference_path, model,
                     size, aspect_ratio, quality, mode, input_fidelity,
                     output_format):
    """Route to the correct provider and return image bytes."""

    if provider == "openai":
        return generate_openai(
            prompt=prompt,
            reference_path=reference_path,
            model=model or DEFAULT_MODELS["openai"],
            size=size,
            quality=quality,
            mode=mode,
            input_fidelity=input_fidelity,
            output_format=output_format,
        )
    elif provider == "google":
        if google_backend == "gemini":
            return generate_google_gemini(
                prompt=prompt,
                reference_path=reference_path,
                model=model or DEFAULT_MODELS["google-gemini"],
                mode=mode,
                aspect_ratio=aspect_ratio,
            )
        else:
            return generate_google_imagen(
                prompt=prompt,
                reference_path=reference_path,
                model_generate=model or DEFAULT_MODELS["google-generate"],
                model_edit=DEFAULT_MODELS["google-edit"],
                aspect_ratio=aspect_ratio,
                mode=mode,
            )
    else:
        die(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def write_manifest(manifest, out_dir):
    """Write both JSON and Markdown manifests."""
    json_path = out_dir / "manifest.json"
    json_path.write_text(json.dumps(manifest, indent=2, default=str))

    md_lines = [
        "# Ad Creative Variants — Manifest",
        "",
        f"**Generated:** {manifest['timestamp']}",
        f"**Reference:** `{manifest['reference']}`",
        f"**Provider:** {manifest['provider']}"
        + (f" ({manifest.get('google_backend', '')})" if manifest['provider'] == 'google' else ''),
        f"**Model:** {manifest['model']}",
        f"**Divergence:** {manifest['divergence']}",
        f"**Size/Ratio:** {manifest.get('size', '')} / {manifest.get('aspect_ratio', '')}",
        "",
        "---",
        "",
    ]

    for v in manifest.get("variants", []):
        status = "FAILED" if "error" in v else "OK"
        md_lines.extend([
            f"## {v['filename']} [{status}]",
            "",
            f"- **Divergence:** {v['divergence']}",
            f"- **Strategy:** {v.get('strategy', 'auto')}",
            f"- **Preserved:** {v.get('preserved', 'auto')}",
            f"- **Changed:** {v.get('changed', 'auto')}",
            "",
        ])
        if "error" in v:
            md_lines.append(f"- **Error:** {v['error']}\n")

    md_path = out_dir / "manifest.md"
    md_path.write_text("\n".join(md_lines))
    print(f"Manifest written to {json_path} and {md_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate ad creative variations from a winning reference ad.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 4 moderate variants via Google Gemini (default)
  python3 scripts/ad_variant_gen.py --reference ad.png --divergence moderate --variants 4

  # 6 subtle variants via OpenAI
  python3 scripts/ad_variant_gen.py --reference ad.png --provider openai --divergence subtle --variants 6

  # Google Imagen 4 for generation (dramatic only -- edit needs Vertex AI)
  python3 scripts/ad_variant_gen.py --reference ad.png --google-backend imagen --divergence dramatic

  # Facebook feed sizing with OpenAI high input fidelity
  python3 scripts/ad_variant_gen.py --reference ad.png --provider openai --platform facebook-feed --input-fidelity high

  # Dry run to preview prompts
  python3 scripts/ad_variant_gen.py --reference ad.png --divergence moderate --variants 4 --dry-run
        """,
    )

    parser.add_argument(
        "--reference", required=True, type=Path,
        help="Path to the winning ad image (PNG, JPG, WebP).",
    )
    parser.add_argument(
        "--divergence", choices=DIVERGENCE_LEVELS, default="moderate",
        help="How different the variants should be (default: moderate).",
    )
    parser.add_argument(
        "--variants", type=int, default=4,
        help="Number of variants to generate (default: 4).",
    )
    parser.add_argument(
        "--provider", choices=PROVIDERS, default="google",
        help="Image generation provider (default: google).",
    )
    parser.add_argument(
        "--google-backend", choices=("gemini", "imagen"), default="gemini",
        help="Google sub-provider: 'gemini' (Nano Banana, simpler, no Vertex AI needed) "
             "or 'imagen' (Imagen 4 generate + Imagen 3 edit, edit needs Vertex AI). "
             "Default: gemini.",
    )
    parser.add_argument(
        "--model", default=None,
        help="Model override. Defaults: "
             "OpenAI=gpt-image-1.5, "
             "Google Gemini=gemini-3-pro-image-preview, "
             "Google Imagen=imagen-4.0-generate-001",
    )
    parser.add_argument(
        "--platform", default=None,
        help="Target ad platform for auto-sizing. Options: "
             + ", ".join(PLATFORM_SPECS.keys()),
    )
    parser.add_argument(
        "--size", default=None,
        help="OpenAI size override. Supported: "
             + ", ".join(OPENAI_SIZES.keys()),
    )
    parser.add_argument(
        "--aspect-ratio", default=None,
        help="Google aspect ratio override. Supported: "
             + ", ".join(GOOGLE_ASPECT_RATIOS.keys()),
    )
    parser.add_argument(
        "--quality", choices=("low", "medium", "high", "auto"), default="high",
        help="Image quality (default: high). 'low' is faster/cheaper.",
    )
    parser.add_argument(
        "--input-fidelity", choices=("low", "high"), default="high",
        help="OpenAI only. How closely to preserve reference image details like faces, "
             "logos, and brand elements (default: high). 'high' uses more tokens.",
    )
    parser.add_argument(
        "--output-format", choices=("png", "jpeg", "webp"), default="png",
        help="Output image format (default: png). jpeg is faster for OpenAI.",
    )
    parser.add_argument(
        "--prompt", default=None,
        help="Override the auto-generated prompt. Use for manual control.",
    )
    parser.add_argument(
        "--strategy", default=None,
        help="1-line description of what this batch of variants tests.",
    )
    parser.add_argument(
        "--preserve", default=None,
        help="Comma-separated list of elements to preserve from the original.",
    )
    parser.add_argument(
        "--change", default=None,
        help="Comma-separated list of elements to change in variants.",
    )
    parser.add_argument(
        "--out-dir", type=Path, default=Path("output/ad-variants"),
        help="Output directory (default: output/ad-variants/).",
    )
    parser.add_argument(
        "--out", type=Path, default=None,
        help="Output path for a single variant (overrides --out-dir for 1 image).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the prompt(s) without calling the API.",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print extra debug info.",
    )

    args = parser.parse_args()

    # --- Validate environment ---
    if not args.dry_run:
        if args.provider == "openai":
            if not os.environ.get("OPENAI_API_KEY"):
                die(
                    "OPENAI_API_KEY is not set. Set it as an environment variable:\n"
                    "  export OPENAI_API_KEY='sk-...'\n"
                    "Never paste your key in chat."
                )
        elif args.provider == "google":
            has_gemini = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            has_vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI")
            if not has_gemini and not has_vertex:
                die(
                    "No Google credentials found. Set one of:\n"
                    "  export GEMINI_API_KEY='...'       # Gemini Developer API\n"
                    "  export GOOGLE_API_KEY='...'       # Also works\n"
                    "  # OR for Vertex AI:\n"
                    "  export GOOGLE_GENAI_USE_VERTEXAI=true\n"
                    "  export GOOGLE_CLOUD_PROJECT='your-project'\n"
                    "  export GOOGLE_CLOUD_LOCATION='us-central1'\n"
                    "Never paste your key in chat."
                )
            # Warn if using Imagen edit without Vertex AI
            if (
                args.google_backend == "imagen"
                and args.divergence != "dramatic"
                and not has_vertex
            ):
                print(
                    "WARNING: Google Imagen editing (subtle/moderate) requires Vertex AI. "
                    "Falling back to Gemini backend for edit mode. "
                    "Set GOOGLE_GENAI_USE_VERTEXAI=true for Imagen editing.",
                    file=sys.stderr,
                )
                args.google_backend = "gemini"

    # --- Resolve parameters ---
    openai_size = resolve_openai_size(args.size, args.platform)
    google_ratio = resolve_google_ratio(args.aspect_ratio, args.platform)

    # For subtle/moderate, use edit mode; for dramatic, use generate mode
    mode = "generate" if args.divergence == "dramatic" else "edit"

    # --- Resolve effective model for display ---
    if args.model:
        effective_model = args.model
    elif args.provider == "openai":
        effective_model = DEFAULT_MODELS["openai"]
    elif args.google_backend == "gemini":
        effective_model = DEFAULT_MODELS["google-gemini"]
    else:
        effective_model = (DEFAULT_MODELS["google-generate"]
                          if mode == "generate"
                          else DEFAULT_MODELS["google-edit"])

    file_ext = args.output_format if args.provider == "openai" else "png"

    # --- Prepare output ---
    out_dir = ensure_dir(args.out_dir)

    # Copy reference to output dir for comparison
    import shutil
    ref_dest = out_dir / f"reference{args.reference.suffix}"
    shutil.copy2(args.reference, ref_dest)

    # --- Build manifest ---
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "reference": str(args.reference),
        "provider": args.provider,
        "google_backend": args.google_backend if args.provider == "google" else None,
        "model": effective_model,
        "divergence": args.divergence,
        "size": openai_size if args.provider == "openai" else None,
        "aspect_ratio": google_ratio if args.provider == "google" else None,
        "quality": args.quality,
        "input_fidelity": args.input_fidelity if args.provider == "openai" else None,
        "output_format": args.output_format,
        "platform": args.platform,
        "mode": mode,
        "variants": [],
    }

    if args.verbose:
        print(f"Provider:        {args.provider}")
        if args.provider == "google":
            print(f"Google backend:  {args.google_backend}")
        print(f"Model:           {effective_model}")
        print(f"Mode:            {mode}")
        print(f"Divergence:      {args.divergence}")
        if args.provider == "openai":
            print(f"Size:            {openai_size}")
            print(f"Input fidelity:  {args.input_fidelity}")
        else:
            print(f"Aspect ratio:    {google_ratio}")
        print(f"Quality:         {args.quality}")
        print(f"Output format:   {args.output_format}")
        print(f"Variants:        {args.variants}")
        print(f"Output dir:      {out_dir}")
        print()

    # --- Build prompt ---
    prompt_base = args.prompt

    if not prompt_base:
        prompt_base = (
            f"Create a variation of this advertisement image. "
            f"Divergence level: {args.divergence}. "
        )
        if args.preserve:
            prompt_base += f"Preserve these elements exactly: {args.preserve}. "
        if args.change:
            prompt_base += f"Change these elements: {args.change}. "
        if args.strategy:
            prompt_base += f"Variation strategy: {args.strategy}. "
        prompt_base += (
            "Maintain professional advertising quality. "
            "All text must be sharp, legible, and correctly spelled. "
            "CTA must be clearly visible and prominent. "
            "No watermarks, no AI artifacts, no distorted text or faces."
        )

    # --- Generate variants ---
    for i in range(1, args.variants + 1):
        filename = build_variant_filename(i, args.divergence, ext=file_ext)
        out_path = args.out if (args.out and args.variants == 1) else (out_dir / filename)

        # Per-variant prompt
        prompt = f"{prompt_base} (Variant {i} of {args.variants} -- introduce a distinct variation.)"

        if args.dry_run:
            print(f"\n--- Variant {i} ---")
            print(f"  File:            {out_path}")
            prov_label = args.provider
            if args.provider == "google":
                prov_label += f" ({args.google_backend})"
            print(f"  Provider:        {prov_label}")
            print(f"  Mode:            {mode}")
            print(f"  Model:           {effective_model}")
            if args.provider == "openai":
                print(f"  Size:            {openai_size}")
                print(f"  Input fidelity:  {args.input_fidelity}")
            else:
                print(f"  Aspect ratio:    {google_ratio}")
            print(f"  Prompt:          {prompt[:200]}...")
            manifest["variants"].append({
                "filename": filename,
                "divergence": args.divergence,
                "strategy": args.strategy or "auto",
                "preserved": args.preserve or "auto",
                "changed": args.change or "auto",
                "prompt": prompt,
                "dry_run": True,
            })
            continue

        print(f"Generating variant {i}/{args.variants} ({args.divergence})...",
              end=" ", flush=True)
        t0 = time.time()

        try:
            img_bytes = generate_variant(
                provider=args.provider,
                google_backend=args.google_backend,
                prompt=prompt,
                reference_path=args.reference,
                model=args.model,
                size=openai_size,
                aspect_ratio=google_ratio,
                quality=args.quality,
                mode=mode,
                input_fidelity=args.input_fidelity,
                output_format=args.output_format,
            )
            save_image(img_bytes, out_path)
            elapsed = time.time() - t0
            print(f"OK {out_path} ({elapsed:.1f}s)")

            manifest["variants"].append({
                "filename": filename,
                "divergence": args.divergence,
                "strategy": args.strategy or "auto",
                "preserved": args.preserve or "auto",
                "changed": args.change or "auto",
                "prompt": prompt,
                "elapsed_seconds": round(elapsed, 2),
            })

        except Exception as e:
            elapsed = time.time() - t0
            print(f"FAILED ({elapsed:.1f}s): {e}")
            manifest["variants"].append({
                "filename": filename,
                "divergence": args.divergence,
                "error": str(e),
                "elapsed_seconds": round(elapsed, 2),
            })

    # --- Write manifest ---
    write_manifest(manifest, out_dir)

    # --- Summary ---
    success = sum(1 for v in manifest["variants"] if "error" not in v)
    total = len(manifest["variants"])
    print(f"\nDone. {success}/{total} variants generated in {out_dir}/")


if __name__ == "__main__":
    main()
