## 2026-03-31 - [Keyboard Navigation & ARIA Focus for Carousel Food Cards]
**Learning:** Interactive items inside carousels or image galleries rendered as non-semantic `<div>`s with `onclick` handlers are invisible/unreachable to keyboard tab navigation and screen readers.
**Action:** Always render interactive card items using semantic `<button type="button">` elements with explicit `aria-label` attributes, text-alignment (`text-left`), and `focus-visible:ring-2` styling.
