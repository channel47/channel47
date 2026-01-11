# Changelog

All notable changes to the Nano Banana Pro plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-01-10

### Added
- **Style Frameworks**: On-demand guides for 5 visual styles
  - Photography: Photorealism, lighting, composition, depth of field
  - Illustration: Digital art, clean lines, stylization, color palettes
  - 3D Render: CGI, materials, lighting setups, render quality
  - Painting: Traditional art, brushwork, color theory, fine art
  - Sketch: Hand-drawn, concept art, line weight, ideation
- **Platform Presets**: Auto-configure settings for social platforms via `--platform` flag
  - `instagram-post` (1:1)
  - `instagram-story` (9:16)
  - `youtube-thumbnail` (16:9)
  - `twitter-post` (16:9)
  - `linkedin-post` (2:1)
  - `tiktok` (9:16)
  - `facebook-cover` (21:9)

### Changed
- SKILL.md now references frameworks via `@frameworks/styles/[style].md`
- Platform aspect ratios section replaced with interactive presets
- agent.md updated with framework references and platform preset table

## [2.1.0] - 2026-01-10

### Changed
- Consolidated prompt tips and aspect ratio guide into SKILL.md
- Condensed agent documentation (210 -> 88 lines)

### Removed
- `tests/test_utils.py` (tests for removed MCP server code)
- `skills/image-gen/prompt-tips.md` (merged into SKILL.md)
- `skills/image-gen/aspect-ratio-guide.md` (merged into SKILL.md)
- `GETTING_STARTED.md` (essentials already in README)

## [2.0.0] - 2026-01-09

### Changed
- **BREAKING: MCP Server Extracted to PyPI Package**
  - The MCP server is now distributed as a standalone PyPI package: `nano-banana-mcp`
  - Plugin now uses `uvx nano-banana-mcp` instead of embedded Python script
  - First activation may take 3-5 seconds to download; subsequent uses are instant
  - No changes to tool names or functionality - all tools still accessible as `mcp__nano-banana__*`

### Benefits
- Independent versioning: MCP server can be updated without plugin release
- Lighter plugin: Skills, agents, and commands only (no server code)
- Reusable: MCP server can be used by Claude SDK agents and other tools
- Faster updates: Server bug fixes deploy immediately via PyPI

### Migration
No action required for users. The plugin automatically uses the new package via uvx.

### Removed
- Embedded `src/nanobanana_mcp.py` (moved to `nano-banana-mcp` PyPI package)
- Plugin no longer requires MCP server dependencies in pyproject.toml

## [1.3.0] - 2026-01-08

### Changed
- **MCP Server Renamed**: The MCP server is now named `nano-banana` (was `creative-designer`)
  - Tools are now accessed as `mcp__nano-banana__generate_image`, `mcp__nano-banana__list_files`, etc.
  - Updated all documentation to reflect the new tool naming convention

## [1.2.0] - 2025-12-28

### Added
- **Future-Ready Architecture**: New `number_of_images` parameter implemented for future API support (currently limited to 1 by Gemini API)
- **Content Safety Controls**: New `safety_level` parameter with four filtering levels:
  - `STRICT` (default): Maximum content filtering (BLOCK_LOW_AND_ABOVE)
  - `MODERATE`: Balanced filtering (BLOCK_MEDIUM_AND_ABOVE)
  - `PERMISSIVE`: Minimal filtering (BLOCK_ONLY_HIGH)
  - `OFF`: No filtering (BLOCK_NONE, may be overridden by API)
- **Reproducible Generation**: New `seed` parameter for deterministic image generation
- Safety settings mapping function to convert user-friendly levels to Gemini API format

### Changed
- Updated `GenerateImageInput` model with new optional parameters
- Enhanced generation config to include `candidateCount` and `seed` values
- All API requests now include explicit safety settings
- Fixed `aspectRatio` parameter structure (now correctly nested in `imageConfig`)

### Known Limitations
- **Multiple Images**: Gemini image models (gemini-2.5-flash-image, gemini-3-pro-image-preview) currently only support `candidateCount=1`. Google's separate Imagen API does support multiple images if needed.
- The code is architected to support multiple images when/if the Gemini API adds this capability

### Documentation
- Added examples for multiple image generation, seed usage, and safety levels
- Updated README.md with Advanced Parameters section
- Updated SKILL.md with detailed parameter documentation
- Enhanced usage examples in documentation

## [1.1.1] - 2025-12-28

### Fixed
- Fixed bug where `aspect_ratio` parameter was being ignored by the API because it was missing from the generation configuration.

## [1.1.0] - 2025-12-28

### Changed
- Updated Gemini models to latest state-of-the-art versions:
  - Pro Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-3-pro-image-preview`
  - Flash Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-2.5-flash-image`
- Updated documentation to reflect 4K generation capabilities of the new Pro model.

## [1.0.0] - 2025-01-01

### Added
- Initial release of Nano Banana Pro plugin
- MCP server integration with Gemini API for image generation
- `generate_image` tool with full control over generation parameters
  - Model selection (Flash/Pro/Auto)
  - Aspect ratio control (1:1, 16:9, 9:16, 21:9, 4:3, 3:4, 2:1)
  - Thinking level configuration (LOW/HIGH)
  - Google Search grounding support
  - File output option
- `list_files` tool for viewing uploaded files
- `upload_file` tool for adding files to Gemini Files API
- `delete_file` tool for removing uploaded files
- Smart model selection based on prompt analysis
- Image generation skill with comprehensive workflow
- Image creator agent for guided image creation
- Setup command wizard for easy configuration
- Detailed documentation (README, GETTING_STARTED)
- Prompt engineering tips and aspect ratio guide
- Authentication test script

### Technical
- FastMCP-based MCP server implementation
- Async HTTP client (httpx) for API communication
- Pydantic models for input validation
- Comprehensive error handling and reporting

### Note
- The `quick_generate` tool mentioned in early documentation was never implemented in the initial release
