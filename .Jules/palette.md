## 2026-10-12 - Explicit Form Label Association and Modal ARIA Labels in Admin Portal
**Learning:** Glassmorphism modal form fields without `for` attributes on labels fail WCAG accessibility compliance and make touch targets harder to hit for mobile/screen-reader users.
**Action:** Always link form `<label>` elements to `<input>`, `<select>`, and `<textarea>` IDs using `for="..."` attributes and ensure all icon-only close buttons specify `aria-label="Close modal"`.
