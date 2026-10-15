## 2025-05-18 - Accessible Food Card Carousel Items
**Learning:** Dynamically rendered food cards were non-semantic `div` elements with `onclick` handlers, making them inaccessible to screen readers and keyboard users.
**Action:** Always render interactive card/modal triggers as `<button type="button">` with descriptive `aria-label` attributes and visible keyboard focus states (`focus-visible:ring-2`).
