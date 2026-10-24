## 2025-02-24 - Dynamic ARIA State Management for Mobile Navigation
**Learning:** Collapsible navigation drawers on mobile viewports require explicit `aria-expanded` state tracking and `aria-controls` target linkage to ensure screen readers accurately communicate whether the drawer is open or closed when the user interacts with the toggle button.
**Action:** When creating or updating toggle controls for collapsible UI containers (drawers, accordions, disclosures), ensure `aria-expanded` and `aria-controls` are declared in HTML and dynamically updated in JavaScript state handlers.
