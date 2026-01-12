/**
 * Generate PNG assets from the logo SVG
 *
 * Creates:
 * - apple-touch-icon.png (180x180)
 * - og-image.png (1200x630)
 * - logo-square.png (512x512)
 */

import sharp from 'sharp';
import { writeFileSync, mkdirSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const publicDir = join(__dirname, '../public');

// Design tokens
const colors = {
  bg: '#1a1816',      // oklch(15% 0.01 60) - warm dark
  fg: '#f5f0e8',      // oklch(93% 0.02 90) - warm off-white
};

// Logo SVG (46x24 viewBox) - the "47" shape
const logoSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 46 24">
  <rect x="0" y="0" width="7" height="18" fill="${colors.fg}"/>
  <rect x="7" y="12" width="7" height="6" fill="${colors.fg}"/>
  <rect x="14" y="0" width="7" height="24" fill="${colors.fg}"/>
  <rect x="25" y="0" width="14" height="6" fill="${colors.fg}"/>
  <rect x="39" y="0" width="7" height="12" fill="${colors.fg}"/>
  <rect x="32" y="12" width="7" height="12" fill="${colors.fg}"/>
</svg>
`;

// Create SVG with logo centered on background
function createCenteredLogoSvg(width: number, height: number, logoScale: number): string {
  const logoWidth = 46 * logoScale;
  const logoHeight = 24 * logoScale;
  const x = (width - logoWidth) / 2;
  const y = (height - logoHeight) / 2;

  return `
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <rect width="${width}" height="${height}" fill="${colors.bg}"/>
  <g transform="translate(${x}, ${y}) scale(${logoScale})">
    <rect x="0" y="0" width="7" height="18" fill="${colors.fg}"/>
    <rect x="7" y="12" width="7" height="6" fill="${colors.fg}"/>
    <rect x="14" y="0" width="7" height="24" fill="${colors.fg}"/>
    <rect x="25" y="0" width="14" height="6" fill="${colors.fg}"/>
    <rect x="39" y="0" width="7" height="12" fill="${colors.fg}"/>
    <rect x="32" y="12" width="7" height="12" fill="${colors.fg}"/>
  </g>
</svg>
`;
}

async function generateAssets() {
  console.log('Generating logo assets...\n');

  // Apple Touch Icon (180x180)
  // Logo should take up ~60% of the space
  const appleIconSize = 180;
  const appleLogoScale = (appleIconSize * 0.6) / 46; // 60% width
  const appleSvg = createCenteredLogoSvg(appleIconSize, appleIconSize, appleLogoScale);

  await sharp(Buffer.from(appleSvg))
    .png()
    .toFile(join(publicDir, 'apple-touch-icon.png'));
  console.log('✓ apple-touch-icon.png (180x180)');

  // Logo Square (512x512)
  const squareSize = 512;
  const squareLogoScale = (squareSize * 0.6) / 46;
  const squareSvg = createCenteredLogoSvg(squareSize, squareSize, squareLogoScale);

  await sharp(Buffer.from(squareSvg))
    .png()
    .toFile(join(publicDir, 'logo-square.png'));
  console.log('✓ logo-square.png (512x512)');

  // OG Image (1200x630)
  const ogWidth = 1200;
  const ogHeight = 630;
  const ogLogoScale = (ogHeight * 0.35) / 24; // Logo height is ~35% of image height
  const ogSvg = createCenteredLogoSvg(ogWidth, ogHeight, ogLogoScale);

  await sharp(Buffer.from(ogSvg))
    .png()
    .toFile(join(publicDir, 'og-image.png'));
  console.log('✓ og-image.png (1200x630)');

  console.log('\nDone! Assets generated in site/public/');
}

generateAssets().catch(console.error);
