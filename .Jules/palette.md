## 2025-05-18 - Icon-Only Buttons Accessibility in Admin Portal
**Learning:** In dynamically updated admin portals with icon-only controls (e.g. close modal buttons, delete buttons with trash icons), screen readers require explicit `aria-label` attributes to correctly describe button intent without relying on visual title tooltips or icon classes.
**Action:** Always include specific `aria-label` attributes (e.g. `aria-label="Delete Dish"`, `aria-label="Close diagnostics modal"`) on icon-only buttons during template rendering or HTML authoring.
