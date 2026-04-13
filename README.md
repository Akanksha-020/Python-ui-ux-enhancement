# Workshop Booking (UI/UX Redesign)

This project is a redesigned version of the FOSSEE Workshop Booking portal with a focus on mobile-first usability, accessibility, modern visual hierarchy, and performance-conscious enhancements.

## What Changed

The core Django structure and backend flow are unchanged. The redesign focuses on the frontend shell and high-traffic pages:

1. Updated global layout and visual system in the shared base template and stylesheet.
2. Added a lightweight React enhancement (`React 18 UMD`) for a mobile quick-navigation bar.
3. Improved readability and hierarchy on login, registration, and workshop status pages.
4. Added better semantic structure and SEO metadata (`description`, proper main landmark, skip link).

## Setup Instructions

1. Clone repository:

```bash
git clone https://github.com/Akanksha-020/Python-ui-ux-enhancement
cd python-ui-ux-enhancement
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create admin account:

```bash
python manage.py createsuperuser
```

6. Start development server:

```bash
python manage.py runserver
```

7. Open in browser:

```text
http://127.0.0.1:8000/
```

8. Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Reasoning

### 1) What design principles guided your improvements?

1. Mobile-first clarity: prioritizing legible text, tappable controls, and concise layouts for students on phones.
2. Visual hierarchy: stronger headings, card containers, cleaner spacing, and consistent button/input treatments.
3. Progressive enhancement: keeping server-rendered Django pages as primary, then layering React where it adds UX value.
4. Accessibility basics: skip link, focus styles, semantic `main` landmark, and improved contrast.
5. Consistency: unified color tokens, component surfaces, and table/form behavior across pages.

### 2) How did you ensure responsiveness across devices?

1. Applied mobile-first spacing and typography in shared CSS.
2. Converted wide table behavior into horizontal scroll containers on smaller screens.
3. Added a React-powered fixed quick-action dock only on mobile breakpoints.
4. Preserved Bootstrap responsive grid usage while improving card and content wrappers.

### 3) What trade-offs did you make between design and performance?

1. Trade-off made: adding React introduces extra JS payload.
2. Mitigation: no build pipeline and no large SPA conversion; React is used only for one lightweight navigation enhancement.
3. Kept most rendering server-side to avoid hydration complexity and runtime overhead.
4. Used minimal animation and simple gradients to avoid expensive rendering.

### 4) What was the most challenging part and how did you approach it?

The most challenging part was modernizing UX while preserving legacy Django templates and route logic.

Approach used:

1. First stabilized the shared base template and global CSS tokens.
2. Enhanced only high-impact templates (login/register/status pages) to avoid risky broad rewrites.
3. Added React as an isolated component with data attributes from Django templates, avoiding backend coupling.

## Visual Showcase

Add screenshots to these paths and update as needed:

1. `docs/screenshots/before-login.png`
2. `docs/screenshots/after-login.png`
3. `docs/screenshots/before-dashboard.png`
4. `docs/screenshots/after-dashboard.png`

Example embed format:

```md
![Before Login](docs/screenshots/before-login.png)
![After Login](docs/screenshots/after-login.png)
![Before Dashboard](docs/screenshots/before-dashboard.png)
![After Dashboard](docs/screenshots/after-dashboard.png)
```

## Notes

1. Existing backend functionality is preserved.
2. Redesign focuses on UX quality, readability, and responsive behavior for student users.
3. See `docs/Getting_Started.md` for additional project-specific information.

## FAQ (Updated)

### 1) Why does Propose Workshop redirect to Django admin?

If you are logged in as superuser, this project intentionally redirects you to admin for workshop routes. Use a normal coordinator account for the proposal flow.

### 2) How can I create a normal user account?

Use either method below:

1. Register from site (recommended for coordinator flow).
2. Or create from admin:
	- Admin > Users > Add user
	- Keep superuser unchecked
	- Fill required profile fields in Admin > Profiles

### 3) Why am I not receiving activation email?

In development, activation email is printed to terminal because EMAIL_BACKEND is set to console backend in settings.

### 4) What about the "User has no profile" login error?

This has been handled in code with safer profile checks and automatic profile creation for non-superusers.
