/**
 * Mobile Menu Utility
 *
 * Manages mobile navigation menu state with accessibility support.
 * Handles open/close, keyboard navigation, and responsive behavior.
 */

export interface MobileMenuElements {
  menu: HTMLElement;
  openButton: HTMLElement;
  closeButton: HTMLElement;
  header: HTMLElement;
}

export interface MobileMenuConfig {
  /** CSS class applied when menu is open (default: 'mobile-menu--open') */
  openClass?: string;
  /** CSS class applied to header when menu is open (default: 'header--menu-open') */
  headerOpenClass?: string;
  /** Breakpoint at which menu auto-closes (default: 640) */
  breakpoint?: number;
}

const DEFAULT_CONFIG: Required<MobileMenuConfig> = {
  openClass: 'mobile-menu--open',
  headerOpenClass: 'header--menu-open',
  breakpoint: 640,
};

/**
 * Initializes mobile menu functionality with full accessibility support.
 *
 * Features:
 * - Open/close with buttons
 * - Escape key to close
 * - Auto-close when clicking nav links
 * - Auto-close when resizing past breakpoint
 * - Body scroll lock when open
 * - Focus management
 *
 * @param elements - Required DOM elements
 * @param config - Optional configuration overrides
 * @returns Cleanup function to remove event listeners
 */
export function initMobileMenu(
  elements: MobileMenuElements,
  config: MobileMenuConfig = {}
): () => void {
  const { menu, openButton, closeButton, header } = elements;
  const { openClass, headerOpenClass, breakpoint } = {
    ...DEFAULT_CONFIG,
    ...config,
  };

  function isOpen(): boolean {
    return menu.classList.contains(openClass);
  }

  function open(): void {
    menu.classList.add(openClass);
    menu.setAttribute('aria-hidden', 'false');
    openButton.setAttribute('aria-expanded', 'true');
    header.classList.add(headerOpenClass);
    document.body.style.overflow = 'hidden';
    closeButton.focus();
  }

  function close(): void {
    menu.classList.remove(openClass);
    menu.setAttribute('aria-hidden', 'true');
    openButton.setAttribute('aria-expanded', 'false');
    header.classList.remove(headerOpenClass);
    document.body.style.overflow = '';
  }

  function closeAndFocusOpen(): void {
    close();
    openButton.focus();
  }

  function onKeyDown(e: KeyboardEvent): void {
    if (e.key === 'Escape' && isOpen()) {
      closeAndFocusOpen();
    }
  }

  function onMediaChange(e: MediaQueryListEvent): void {
    if (e.matches) {
      close();
    }
  }

  // Attach event listeners
  openButton.addEventListener('click', open);
  closeButton.addEventListener('click', closeAndFocusOpen);
  document.addEventListener('keydown', onKeyDown);

  // Close when clicking nav links
  const navLinks = menu.querySelectorAll('a');
  navLinks.forEach((link) => link.addEventListener('click', close));

  // Auto-close on resize past breakpoint
  const mediaQuery = window.matchMedia(`(min-width: ${breakpoint}px)`);
  mediaQuery.addEventListener('change', onMediaChange);

  // Return cleanup function
  return () => {
    openButton.removeEventListener('click', open);
    closeButton.removeEventListener('click', closeAndFocusOpen);
    document.removeEventListener('keydown', onKeyDown);
    navLinks.forEach((link) => link.removeEventListener('click', close));
    mediaQuery.removeEventListener('change', onMediaChange);
  };
}
