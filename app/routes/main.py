from pathlib import Path

from flask import Blueprint, current_app, render_template

from ..content import SITE_CONTENT
from ..models import BlogPost, Project

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@main_bp.route("/home")
def home():
    featured = Project.query.filter_by(featured=True).order_by(Project.created_at.desc()).limit(6).all()
    return render_template("index.html", featured_projects=featured)


@main_bp.route("/resume")
def resume():
    resume_file = Path(current_app.static_folder) / "files" / current_app.config["RESUME_FILENAME"]
    return render_template("resume.html", resume_exists=resume_file.is_file())


@main_bp.route("/blog")
def blog():
    posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.created_at.desc()).all()
    return render_template("blog.html", posts=posts, linkedin_url=SITE_CONTENT["linkedin_url"])
