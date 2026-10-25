from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, render_template
from dotenv import load_dotenv

from config import Config
from .content import SITE_CONTENT, SKILLS, RESUME_CONTENT
from .extensions import csrf, db
from .utils import static_file_exists


def create_app(config_object=Config) -> Flask:
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    db.init_app(app)
    csrf.init_app(app)

    from .routes.main import main_bp
    from .routes.projects import projects_bp
    from .routes.contact import contact_bp
    from .routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_globals():
        profile_path = SITE_CONTENT["profile_image"]
        resume_path = f"files/{app.config.get('RESUME_FILENAME', SITE_CONTENT['resume_filename'])}"
        return {
            "site": SITE_CONTENT,
            "skills": SKILLS,
            "resume_content": RESUME_CONTENT,
            "current_year": datetime.now(timezone.utc).year,
            "profile_image_available": static_file_exists(profile_path),
            "resume_available": static_file_exists(resume_path),
            "resume_static_path": resume_path,
        }

    @app.after_request
    def security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; style-src 'self' https://cdnjs.cloudflare.com; "
            "font-src 'self' https://cdnjs.cloudflare.com; script-src 'self'; img-src 'self' data:; "
            "form-action 'self'; frame-ancestors 'self'"
        )
        return response

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(_error):
        db.session.rollback()
        return render_template("500.html"), 500

    if app.config.get("AUTO_CREATE_DB", True):
        with app.app_context():
            db.create_all()

    return app
