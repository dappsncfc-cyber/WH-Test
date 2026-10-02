## 2025-05-18 - Floating Icon-Only Collapsible Buttons
**Learning:** Floating action buttons with collapsible text spans (e.g. `max-w-0` expanding on hover) appear as icon-only controls to screen readers when collapsed if an explicit `aria-label` is not defined on the parent `<button>`.
**Action:** Always provide `aria-label` on floating action buttons that collapse text visually, ensuring screen readers clearly identify their function regardless of visual hover/expansion state.
