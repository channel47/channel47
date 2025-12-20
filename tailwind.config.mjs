/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				coral: {
					50: '#fff5f5',
					100: '#ffe0e0',
					200: '#ffc7c7',
					300: '#ffa3a3',
					400: '#ff7a7a',
					500: '#e85c5c',  // Primary coral
					600: '#d44545',
					700: '#b33636',
					800: '#942d2d',
					900: '#7a2828',
				},
				cream: {
					50: '#fffdf9',
					100: '#fef9f0',
					200: '#fdf3e1',
					300: '#faecd0',
					400: '#f5e1b8',
				},
				charcoal: {
					700: '#374151',
					800: '#1f2937',
					900: '#111827',
				},
			},
			fontFamily: {
				sans: ['Inter', 'system-ui', 'sans-serif'],
				mono: ['JetBrains Mono', 'monospace'],
			},
		},
	},
	plugins: [require('@tailwindcss/typography')],
}
