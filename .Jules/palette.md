## 2025-05-18 - Mobile Menu ARIA Expanded State
**Learning:** Mobile navigation toggles require explicit `aria-expanded` and `aria-controls` attributes so screen readers can properly announce expanded/collapsed states.
**Action:** Always ensure disclosure buttons (toggles, accordions, mobile menus) maintain `aria-expanded` attribute dynamically updated via JS.
