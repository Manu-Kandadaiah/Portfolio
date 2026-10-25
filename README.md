# Professional Flask Developer Portfolio

A production-minded, recruiter-friendly personal portfolio built with Python, Flask, Jinja2, SQLAlchemy, SQLite, HTML5, CSS3, and vanilla JavaScript.

> **Important:** The included name/contact information and sample project content are placeholders. Replace them with your own verified information. Sample project descriptions are clearly marked `PLACEHOLDER` and must not be presented as employment/client work unless they genuinely represent your work.

## Project Overview

This project is designed for a developer targeting Python, backend, Flask, data analytics, AI/ML, software development, and related IT roles. The architecture separates normal editable content, database-backed project content, templates, routes, styles, JavaScript, and configuration so you do not need to redesign the site each time you update your portfolio.

## Features

- Professional responsive home page with profile image fallback
- Editable About, skills, current-focus, and contact information
- Project categories: Python, Data Analytics, AI/ML
- SEO-friendly project URLs such as `/project/it-asset-management-system`
- Project status: `Completed`, `In Progress`, or `Coming Soon`
- Multiple project screenshots per project
- Client-side project category filtering plus normal Flask category routes
- Resume page with automatic missing-file fallback
- Contact form with CSRF, email validation, length limits, honeypot spam field, and private SQLite storage
- Blog / LinkedIn update area
- Dark/light theme remembered in `localStorage`
- Responsive mobile navigation
- Accessible labels, focus states, semantic HTML, skip link, and alt text
- Custom 404 and 500 pages
- Optional protected admin area for projects, blog/update entries, and private contact messages
- No default admin password and no secrets hard-coded into source code
- PythonAnywhere-compatible WSGI entry point
- Automated Flask tests in `tests/`

## Technologies

- Python 3.10+
- Flask 3.x
- Flask-SQLAlchemy
- Flask-WTF / WTForms
- SQLite
- Jinja2
- HTML5 / CSS3
- Vanilla JavaScript
- python-dotenv

## Folder Structure

See [`PROJECT_STRUCTURE.txt`](PROJECT_STRUCTURE.txt) for the complete tree.

```text
flask_developer_portfolio/
├── app.py
├── wsgi.py
├── config.py
├── init_db.py
├── seed.py
├── generate_admin_hash.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── .env.example
├── .gitignore
├── instance/
├── tests/
└── app/
    ├── __init__.py
    ├── content.py
    ├── extensions.py
    ├── forms.py
    ├── models.py
    ├── utils.py
    ├── routes/
    ├── templates/
    └── static/
```

# Installation

## 1. Extract or clone the project

Open PowerShell / Command Prompt in the project folder.

```powershell
cd path\to\flask_developer_portfolio
```

## 2. Create a virtual environment

```powershell
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you may use Command Prompt instead or adjust the current-user execution policy according to your organization's security policy.

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

For development tests:

```bash
pip install -r requirements-dev.txt
```

## 5. Create `.env`

Copy `.env.example` to `.env`.

Windows:

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Generate a strong secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Put the generated value in `.env`:

```env
SECRET_KEY=your-generated-random-value
DATABASE_URL=sqlite:///portfolio.db
AUTO_CREATE_DB=1
RESUME_FILENAME=resume.pdf
ADMIN_PASSWORD_HASH=
```

`portfolio.db` is stored inside Flask's instance folder when you use the relative SQLite URI shown above.

## 6. Initialize the database

The application creates tables automatically when `AUTO_CREATE_DB=1`, but you can initialize explicitly:

```bash
python init_db.py
```

## 7. Seed demonstration projects

```bash
python seed.py
```

This inserts clearly labeled sample/placeholder project entries. It does not invent GitHub URLs, clients, employers, or certifications.

## 8. Run locally

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

# Main Routes

| Route | Purpose |
|---|---|
| `/` or `/home` | Home page |
| `/projects` | All projects |
| `/projects/python` | Python projects |
| `/projects/data-analytics` | Data analytics projects |
| `/projects/ai-ml` | AI/ML projects |
| `/project/<slug>` | Project detail page |
| `/resume` | Resume page |
| `/blog` | Blog / LinkedIn updates |
| `/contact` | Contact details and secure contact form |
| `/admin/login` | Optional protected admin area |

# How to Customize My Portfolio

## Change name, title, about, contact details, LinkedIn, GitHub, and skills

Edit:

```text
app/content.py
```

The primary values are inside:

- `SITE_CONTENT`
- `SKILLS`
- `RESUME_CONTENT`

You do not need to edit route functions for normal content changes.

## Change profile photo

Add your photograph as:

```text
app/static/images/profile.jpg
```

The home page detects this file automatically. If it is missing, the included professional SVG placeholder is shown instead.

Recommended:

- Square or near-square image
- JPG or optimized WebP/JPG under approximately 500 KB
- Professional head-and-shoulders photograph

## Change resume

Add your real public resume PDF as:

```text
app/static/files/resume.pdf
```

The Resume page automatically enables **Download Resume** and **View Resume** when the file exists.

If you want another filename, set:

```env
RESUME_FILENAME=Your_Name_Resume.pdf
```

Then place that exact file in `app/static/files/`.

## Add or edit projects through the admin area

The optional admin interface is the easiest way to manage project database records.

### Enable admin securely

There is **no default password**.

Generate a password hash:

```bash
python generate_admin_hash.py
```

Enter a strong password of at least 12 characters. Copy the generated hash into `.env`:

```env
ADMIN_PASSWORD_HASH=your-generated-hash
```

Restart the Flask app and visit:

```text
http://127.0.0.1:5000/admin/login
```

The admin area lets you:

- Add/edit/delete projects
- Set project category/status/featured state
- Add screenshot paths
- Add/edit/delete blog/update cards
- Read/delete private contact messages

If `ADMIN_PASSWORD_HASH` is empty, admin login is disabled by design.

## Add a Python project

1. Put screenshots in:

```text
app/static/images/projects/python/
```

2. Open `/admin/login`.
3. Click **Add project**.
4. Choose category **Python Developer**.
5. Use a slug such as `employee-management-system`.
6. Enter screenshot paths relative to `app/static/`, for example:

```text
images/projects/python/employee-management-1.png
images/projects/python/employee-management-2.png
```

7. Add a GitHub URL only when the repository actually exists and is appropriate to share.

## Add a Data Analyst project

Store screenshots in:

```text
app/static/images/projects/data-analytics/
```

Choose **Data Analytics** in the admin form. Include the dataset context, tools used, analyses performed, and genuine business insights in the description fields.

## Add an AI/ML project

Store screenshots in:

```text
app/static/images/projects/ai-ml/
```

Use status:

- `Coming Soon` when only planned
- `In Progress` while actively being built
- `Completed` only after it is actually completed

This prevents the portfolio from making false completion claims.

## Add project screenshots manually in Python

If you prefer not to use the admin panel, edit `seed.py` before the first seed or insert records using SQLAlchemy. Project screenshot paths are stored in the `ProjectImage` table.

## Add GitHub links

For your general GitHub profile, edit:

```python
SITE_CONTENT["github_url"]
```

in `app/content.py`.

For individual projects, use the admin project form. The GitHub button is hidden automatically when `github_url` is empty.

## Change LinkedIn

Edit:

```python
SITE_CONTENT["linkedin_url"]
```

in `app/content.py`.

## Change contact information

Edit these fields in `app/content.py`:

```python
"email"
"phone"
"location"
"linkedin_url"
"github_url"
```

# Database Design

## `Project`

Stores title, slug, category, descriptions, technologies, features, problem, solution, learning, future improvements, GitHub/live URL, status, featured flag, and creation time.

## `ProjectImage`

Stores one-to-many project screenshot paths and alt text.

## `ContactMessage`

Stores recruiter/contact form submissions privately in SQLite. Messages are **not exposed publicly**.

## `BlogPost`

Supports current external/LinkedIn update cards and provides a foundation for future on-site blog posts.

# Contact Form Security

The contact form includes:

- Flask-WTF CSRF protection
- Server-side validation
- Email validation
- Name, subject, and message length limits
- Hidden honeypot field for basic bot filtering
- Jinja auto-escaping for displayed content
- Private storage in SQLite
- No password collection
- No public message listing

For a high-traffic public site, consider adding rate limiting and/or an external transactional email service later.

# Admin Security

- No default admin password
- Password hash only, stored in environment configuration
- Session-protected admin routes
- CSRF protection for forms and delete actions
- Admin can be completely disabled by leaving `ADMIN_PASSWORD_HASH` empty
- `.env` is ignored by Git

Do not place your plain-text admin password in source code or GitHub.

# Dark / Light Mode

Theme behavior is implemented in:

```text
app/static/js/main.js
```

The browser stores the selected theme in:

```text
localStorage['portfolio-theme']
```

Colors are centralized as CSS variables in:

```text
app/static/css/style.css
```

Change the visual identity by editing the values near the top of that file.

# Testing

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run:

```bash
pytest -q
```

The tests cover public routes, project detail routing, 404 behavior, contact-message persistence, honeypot rejection, and the safe disabled-admin state.

# Git / GitHub Setup

Before publishing, confirm that `.env`, the SQLite database, and private files are not being tracked.

```bash
git init
git add .
git commit -m "Initial portfolio website"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY
git push -u origin main
```

Do not replace `YOUR_GITHUB_REPOSITORY` with anything until you create your actual repository.

# Deploying to PythonAnywhere

The project includes `wsgi.py` and is designed to work with a standard PythonAnywhere Flask deployment.

## 1. Create your PythonAnywhere account

Create an account and note your actual username. The instructions below use the placeholder `YOUR_USERNAME`.

## 2. Upload or clone your repository

From a PythonAnywhere Bash console:

```bash
cd ~
git clone YOUR_GITHUB_REPOSITORY portfolio
cd portfolio
```

Or upload the project using the Files interface.

## 3. Create a virtual environment

Use a Python version supported by your PythonAnywhere account, for example:

```bash
python3 -m venv /home/YOUR_USERNAME/.virtualenvs/portfolio-env
source /home/YOUR_USERNAME/.virtualenvs/portfolio-env/bin/activate
```

## 4. Install requirements

```bash
pip install -r requirements.txt
```

## 5. Create a web application

In the **Web** tab:

1. Click **Add a new web app**.
2. Choose **Manual configuration** or Flask as appropriate for your account.
3. Choose the Python version matching your virtual environment.
4. Set the virtualenv path to:

```text
/home/YOUR_USERNAME/.virtualenvs/portfolio-env
```

## 6. Configure environment variables

PythonAnywhere does not require committing a `.env` file. You may create a private `.env` in the project folder or set environment values through the WSGI file / platform-supported configuration.

At minimum set a strong production `SECRET_KEY`.

To enable admin, set a generated `ADMIN_PASSWORD_HASH` rather than a plain password.

## 7. Configure WSGI

Open the WSGI configuration file from the PythonAnywhere **Web** tab and use a configuration based on:

```python
import os
import sys

project_home = '/home/YOUR_USERNAME/portfolio'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

from wsgi import app as application
```

Replace only `YOUR_USERNAME` and the project folder if yours is different.

## 8. Initialize the database

In a Bash console with the virtual environment active:

```bash
cd /home/YOUR_USERNAME/portfolio
python init_db.py
python seed.py
```

SQLite will create the database in the Flask instance folder unless you configure another database URL.

## 9. Upload your profile photo

Place your image at:

```text
app/static/images/profile.jpg
```

## 10. Upload your resume

Place your PDF at:

```text
app/static/files/resume.pdf
```

## 11. Reload the web app

Use the **Reload** button in the PythonAnywhere Web tab.

## 12. Test the deployed website

Check:

- Home page
- Projects and category routes
- Every project detail link
- Resume page and download
- Blog/LinkedIn link
- Contact form submission
- Mobile menu
- Dark/light theme
- 404 page
- Admin access only if enabled

# Production Notes

Before sharing the site publicly:

- Replace every `YOUR_*` placeholder
- Replace all `PLACEHOLDER` project descriptions with your real content
- Add real screenshots only for your own projects
- Add GitHub links only when repositories exist
- Upload a public-safe resume
- Generate a strong `SECRET_KEY`
- Keep `.env` private
- Keep your SQLite database out of Git
- Consider a backup strategy for the SQLite database
- Consider rate limiting and email delivery if contact traffic grows

# Testing Checklist

- [ ] Flask starts without errors
- [ ] `/` and `/home` render
- [ ] `/projects` renders
- [ ] `/projects/python` renders
- [ ] `/projects/data-analytics` renders
- [ ] `/projects/ai-ml` renders
- [ ] Project detail pages render
- [ ] CSS loads
- [ ] JavaScript loads
- [ ] Mobile menu works
- [ ] Dark/light mode works and persists
- [ ] Profile image fallback works
- [ ] Resume missing-file fallback works
- [ ] Resume download works after upload
- [ ] Contact form validates input
- [ ] Contact messages remain private
- [ ] 404 page renders
- [ ] 500 handler exists
- [ ] GitHub links open in a new tab when configured
- [ ] LinkedIn opens in a new tab
- [ ] No real secrets are committed
- [ ] Admin is disabled when no password hash is configured
- [ ] `pytest -q` passes in a fully installed environment
- [ ] PythonAnywhere deployment settings are updated with your actual username/path

# Content Editing Quick Reference

| What you want to change | File / Location |
|---|---|
| Name / title / intro | `app/content.py` → `SITE_CONTENT` |
| About text | `app/content.py` → `SITE_CONTENT['about']` |
| Skills | `app/content.py` → `SKILLS` |
| Contact details | `app/content.py` → `SITE_CONTENT` |
| LinkedIn / GitHub profile | `app/content.py` → `SITE_CONTENT` |
| Resume page text | `app/content.py` → `RESUME_CONTENT` |
| Profile image | `app/static/images/profile.jpg` |
| Resume PDF | `app/static/files/resume.pdf` |
| Project screenshots | `app/static/images/projects/...` |
| Project records | Admin area or SQLite/`seed.py` |
| Project GitHub URL | Admin project form |
| Project status | Admin project form |
| Blog/update cards | Admin area |
| Colors / layout | `app/static/css/style.css` |
| UI interactions | `app/static/js/main.js` |
| Secrets / database URI | `.env` |

## Final reminder

A strong portfolio is credible because every claim can be explained. Keep `Coming Soon` and `In Progress` labels accurate, remove sample placeholder content as you replace it, and only publish project outcomes you can demonstrate in an interview.
