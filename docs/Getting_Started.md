# Guide To Install And Run The Website

## Quick Start

> NOTE: Use Python 3.

1. Clone the repository.

```bash
git clone https://github.com/FOSSEE/workshop_booking.git
cd workshop_booking
```

2. Create and activate virtual environment.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
```

3. Install requirements.

```bash
pip install -r requirements.txt
```

4. Run database migrations.

```bash
python manage.py migrate
```

5. Create superuser.

```bash
python manage.py createsuperuser
```

6. Start server.

```bash
python manage.py runserver
```

7. Open admin and login.

```text
http://127.0.0.1:8000/admin
```

## Role Setup

1. Create one group named instructor in Admin > Groups.
2. Assign required permissions to the instructor group.
3. For instructor users:
   - Set Profile position to instructor.
   - Add user to instructor group.
4. For coordinator users:
   - Keep Profile position as coordinator.

## Instructor Specific Flow

1. Instructor can accept or manage workshops from Workshop Status.
2. Instructor can view analytics in Statistics > Workshop Statistics.
3. Instructor can post/view comments on coordinator profile and workshop pages.

## Coordinator Specific Flow

1. Coordinator can submit workshop proposals from Workshops > Propose Workshop.

## FAQ / Troubleshooting

### 1) Why does Propose Workshop open Django admin for my account?

Because superusers are intentionally redirected to admin pages in this project flow. Use a normal coordinator account for the workshop proposal flow.

### 2) How do I create a normal user quickly?

Use admin:

1. Admin > Users > Add user.
2. Ensure superuser is unchecked.
3. Open Admin > Profiles and fill required fields for that user.
4. Set position to coordinator or instructor as needed.
5. If needed for local testing, mark is_email_verified as true.

### 3) I registered from the site but did not receive activation email.

In development mode this project uses console email backend, so activation links are printed in the runserver terminal instead of inbox.

Current setting:

- workshop_portal/settings.py uses django.core.mail.backends.console.EmailBackend.

To use real email, configure SMTP values in local_settings.py and change EMAIL_BACKEND.

### 4) How to stop the server?

Press Ctrl + C in the terminal where runserver is running.

### 5) I saw "User has no profile" error before.

The app now includes safeguards to avoid this crash during login by handling missing profiles safely and creating default profiles for non-superusers when needed.

