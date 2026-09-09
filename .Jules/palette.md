## 2026-09-09 - Accessibility and Modal Keyboard Controls in Admin Interfaces
**Learning:** Admin management interfaces often lack basic screen reader accessibility (`aria-label` on icon-only action buttons) and keyboard modal dismiss functionality (`Escape` key handling), causing accessibility barriers for keyboard/screen-reader power users.
**Action:** When working on modal or icon-heavy management pages (like `admin.html`), ensure all icon-only buttons (`aria-label`) and modal overlays (`keydown` Escape listener) have explicit keyboard accessibility attributes and listeners.
