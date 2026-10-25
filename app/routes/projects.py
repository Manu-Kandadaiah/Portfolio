from flask import Blueprint, abort, render_template

from ..models import Project

projects_bp = Blueprint("projects", __name__)

CATEGORY_LABELS = {
    "python": "Python Developer Projects",
    "data-analytics": "Data Analyst Projects",
    "ai-ml": "AI & Machine Learning Projects",
}
CATEGORY_DESCRIPTIONS = {
    "python": "Backend and full-stack applications built around Python, Flask, databases, APIs, and practical workflows.",
    "data-analytics": "Data cleaning, SQL, Python analytics, Excel reporting, visualization, and business insight projects.",
    "ai-ml": "Machine-learning and AI projects, with unfinished work clearly labeled In Progress or Coming Soon.",
}


def _project_page_context(selected_category: str):
    items = Project.query.order_by(Project.featured.desc(), Project.created_at.desc()).all()
    counts = {key: sum(1 for item in items if item.category == key) for key in CATEGORY_LABELS}
    return {
        "projects": items,
        "selected_category": selected_category,
        "category_labels": CATEGORY_LABELS,
        "category_descriptions": CATEGORY_DESCRIPTIONS,
        "category_counts": counts,
    }


@projects_bp.route("/projects")
def projects():
    return render_template("projects.html", **_project_page_context("all"))


@projects_bp.route("/projects/<category>")
def category(category):
    if category not in CATEGORY_LABELS:
        abort(404)
    return render_template("projects.html", **_project_page_context(category))


@projects_bp.route("/project/<slug>")
def detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    return render_template("project_detail.html", project=project, category_labels=CATEGORY_LABELS)
