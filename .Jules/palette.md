# Palette's Journal - UX & Accessibility Learnings

## 2026-03-30 - Admin Portal Modal Keyboard Dismissal & ARIA Consistency
**Learning:** Admin/staff management interfaces often miss keyboard accessibility features like Escape key modal dismissal and explicit `aria-label`s on icon-only close/delete buttons, creating a disparity in accessibility compared to the main visitor-facing site.
**Action:** When auditing or implementing staff modals and administrative action buttons, ensure keyboard event listeners (`Escape` key) and `aria-label` attributes are consistently applied alongside public-facing UI components.
