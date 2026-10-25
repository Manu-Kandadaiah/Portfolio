# Portfolio redesign — setup and media guide

## Run on Windows
1. Extract the ZIP and open the `flask_developer_portfolio_complete` folder in VS Code.
2. `py -m venv .venv`
3. `.venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`; configure a unique SECRET_KEY and ADMIN_PASSWORD_HASH.
6. `python seed.py` to load verified resume projects (only for a new/empty local database; back up existing data first).
7. `python app.py`; visit http://127.0.0.1:5000

## Resume
The supplied resume is installed at `app/static/files/resume.pdf`. The existing resume page serves it.

## Project media
`app/static/images/projects/showcase/` contains explicitly labelled conceptual illustrations, **not screenshots**. Replace them with real images. ProjectImage records can store multiple relative static paths. The existing detail gallery handles multiple images. For videos, add your verified video link or embed through a reviewed template update; no video was provided.

## What was verified
The portfolio Flask source and PDF resume were reviewed. The three highlighted projects are supported by resume descriptions, but their individual source repositories were **not** supplied. Therefore detailed code contributions, challenges, measurements, GitHub links, and live demo URLs are not invented. Other legacy demo entries may still exist in your own previously populated database.

## Deployment notes
Never commit `.env`, local databases or virtual environments. Set SECRET_KEY and admin hash in environment variables; use a production WSGI server and HTTPS. Existing routes, forms and database schema are retained.
