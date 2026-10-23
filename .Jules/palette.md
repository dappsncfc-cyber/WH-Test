## 2026-10-23 - Staff Admin Modal Accessibility and Keyboard Dismissal
**Learning:** Modals in `admin.html` were missing WAI-ARIA dialog attributes (`role="dialog"`, `aria-modal="true"`, `aria-labelledby`), explicit close button labels, and Escape key / backdrop overlay dismiss handling.
**Action:** Always ensure modal overlays implement complete WAI-ARIA dialog markup, labelled close buttons, backdrop click listeners, and document-level Escape key event listeners for keyboard navigation consistency across both public and admin interfaces.
