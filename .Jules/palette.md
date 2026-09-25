## 2026-09-25 - Modal Dismissal Parity Across Public and Admin Interfaces
**Learning:** Admin portal modals previously required users to click explicit "Close" or "Cancel" buttons, whereas main site modals allowed dismissal via `Escape` key and backdrop clicking. Consistent modal behavior reduces user friction and provides keyboard accessibility across the entire web application.
**Action:** Whenever adding modal dialogs to secondary or admin interfaces, ensure global `Escape` key listeners and backdrop overlay click handlers are included alongside close buttons.
