# Palette Journal - UX & Accessibility Learnings

## 2025-05-18 - Admin Portal Modal Accessibility & Keyboard Shortcuts
**Learning:** Modal dialogs in `admin.html` lacked explicit `aria-label` tags on close (`.fa-times`) and delete (`.fa-trash`) icon-only buttons, and lacked Escape key event handlers.
**Action:** Always ensure icon-only buttons receive descriptive `aria-label` attributes and all modal views bind an Escape key listener to close active overlays.
