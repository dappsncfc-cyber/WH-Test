## 2026-03-30 - Modal Dialog Accessibility with WAI-ARIA
**Learning:** Screen readers require `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` attributes matching header title IDs on modal containers to announce dialog contents and titles when opened.
**Action:** When creating modal overlays, always add `role="dialog"`, `aria-modal="true"`, and associate `aria-labelledby` with a unique ID on the modal's primary heading element.
