## 2026-03-30 - Reservation Modal Tab Switcher Accessibility
**Learning:** Modal tab switchers require proper ARIA roles (`role="tablist"`, `role="tab"`, `role="tabpanel"`) and synchronized state attributes (`aria-selected`, `aria-controls`, `aria-labelledby`) to ensure screen readers accurately convey active tab panels and tab state changes.
**Action:** Always include ARIA tab attributes on modal tab navigation elements and dynamically update `aria-selected` within tab switching JavaScript handlers.
