## 2025-09-11 - [Admin Portal Modal Accessibility & Escape Key Dismissal]
**Learning:** Admin modal overlays in single-page HTML interfaces often lack accessible labels on icon-only close buttons and keyboard dismissibility (`Escape` key), creating barriers for screen reader and keyboard-only users.
**Action:** Always verify icon-only modal close buttons have descriptive `aria-label` attributes and ensure a global keydown handler for `Escape` is bound to close open modals.
