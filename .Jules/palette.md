## 2025-05-18 - Booking Modal Tab Pattern & Floating FAB Accessibility
**Learning:** Embedded modal tab switchers and floating action buttons (FABs) require explicit WAI-ARIA roles (`tablist`, `tab`, `tabpanel`, `aria-controls`, `aria-labelledby`, `aria-selected`) and `aria-label` tags so assistive technology can accurately communicate active tab state transitions and action targets.
**Action:** Always complement tab button class changes with dynamic updates to `aria-selected` attributes in JavaScript tab switcher handlers.
