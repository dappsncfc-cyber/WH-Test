## 2025-05-19 - Admin Portal Icon Button Accessibility Gap
**Learning:** While public pages in `index.html` were thoroughly audited for `aria-label` attributes on icon-only close/action buttons, internal staff modals and dynamic list actions in `admin.html` lacked accessibility labels on icon-only buttons (`fa-times` and `fa-trash`).
**Action:** Always audit both public-facing and admin portal interfaces for icon-only button labels when conducting accessibility sweeps across multi-page applications.
