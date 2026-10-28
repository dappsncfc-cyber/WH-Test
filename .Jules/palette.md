## 2025-02-28 - Icon-Only Action Buttons ARIA Labels in Admin Portal
**Learning:** Modal close buttons (`.fas.fa-times`) and dynamic list item delete buttons (`.fas.fa-trash`) in `admin.html` relied only on visual icons or title attributes without explicit `aria-label` attributes, rendering them non-descriptive for screen readers.
**Action:** Ensure all icon-only action and close buttons across both main site and admin portal specify explicit, descriptive `aria-label` attributes matching their action target.
