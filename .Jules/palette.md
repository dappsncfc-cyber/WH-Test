## 2025-05-18 - Accessible Icon-Only Buttons in Admin Modals and Lists
**Learning:** Icon-only action buttons (such as modal close icons `fa-times` and item delete icons `fa-trash`) lack accessible names if `aria-label` is omitted, making them unannounced or obscure to screen readers.
**Action:** Always inspect icon-only interactive controls and ensure an explicit, context-specific `aria-label` attribute is added alongside visual icons.
