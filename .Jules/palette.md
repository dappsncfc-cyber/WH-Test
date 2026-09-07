# Palette's Journal - Critical Learnings

## 2026-09-07 - Admin Modal Accessibility and Keyboard Trapping
**Learning:** Icon-only modal close buttons and lack of `Escape` key dismissal in administrative interface modals create barriers for screen reader and keyboard-only users.
**Action:** Always ensure icon-only buttons include descriptive `aria-label` attributes and implement global `Escape` key handlers for interactive overlays/modals across all application portals.
