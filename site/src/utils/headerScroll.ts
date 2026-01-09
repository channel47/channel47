/**
 * Header Scroll Hide/Show Utility
 *
 * Manages the scroll-based hide/show behavior for a sticky header.
 * Uses requestAnimationFrame for performance optimization.
 */

export interface HeaderScrollConfig {
  /** Minimum scroll delta to trigger hide/show (default: 10) */
  threshold?: number;
  /** Minimum scroll position before hiding is enabled (default: 100) */
  hideOffset?: number;
  /** CSS class applied when header is hidden (default: 'header--hidden') */
  hiddenClass?: string;
  /** CSS class indicating menu is open (default: 'header--menu-open') */
  menuOpenClass?: string;
}

const DEFAULT_CONFIG: Required<HeaderScrollConfig> = {
  threshold: 10,
  hideOffset: 100,
  hiddenClass: 'header--hidden',
  menuOpenClass: 'header--menu-open',
};

/**
 * Initializes scroll-based header visibility behavior.
 *
 * The header hides when scrolling down and shows when scrolling up,
 * with configurable thresholds. Respects reduced motion preferences.
 *
 * @param header - The header element to control
 * @param config - Optional configuration overrides
 * @returns Cleanup function to remove event listeners
 */
export function initHeaderScroll(
  header: HTMLElement,
  config: HeaderScrollConfig = {}
): () => void {
  const { threshold, hideOffset, hiddenClass, menuOpenClass } = {
    ...DEFAULT_CONFIG,
    ...config,
  };

  let lastScrollY = 0;
  let ticking = false;

  function updateVisibility(): void {
    const currentScrollY = window.scrollY;
    const isMenuOpen = header.classList.contains(menuOpenClass);

    // Don't hide if menu is open or near top of page
    if (isMenuOpen || currentScrollY < hideOffset) {
      header.classList.remove(hiddenClass);
      lastScrollY = currentScrollY;
      ticking = false;
      return;
    }

    const scrollDelta = currentScrollY - lastScrollY;

    if (scrollDelta > threshold) {
      header.classList.add(hiddenClass);
    } else if (scrollDelta < -threshold) {
      header.classList.remove(hiddenClass);
    }

    lastScrollY = currentScrollY;
    ticking = false;
  }

  function onScroll(): void {
    if (!ticking) {
      requestAnimationFrame(updateVisibility);
      ticking = true;
    }
  }

  // Respect reduced motion preference
  const prefersReducedMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)'
  ).matches;

  if (!prefersReducedMotion) {
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Return cleanup function
  return () => {
    window.removeEventListener('scroll', onScroll);
  };
}
