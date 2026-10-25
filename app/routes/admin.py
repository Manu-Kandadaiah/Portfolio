from __future__ import annotations

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from ..extensions import db
from ..forms import AdminLoginForm, BlogPostForm, ProjectForm
from ..models import BlogPost, ContactMessage, Project, ProjectImage
from ..utils import admin_required, safe_lines, slug_is_valid

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def _admin_enabled() -> bool:
    return bool(current_app.config.get("ADMIN_PASSWORD_HASH"))


def _populate_project(project: Project, form: ProjectForm) -> None:
    project.title = form.title.data.strip()
    project.slug = form.slug.data.strip().lower()
    project.category = form.category.data
    project.short_description = form.short_description.data.strip()
    project.full_description = form.full_description.data.strip()
    project.technologies = form.technologies.data.strip()
    project.features = (form.features.data or "").strip()
    project.problem = (form.problem.data or "").strip()
    project.solution = (form.solution.data or "").strip()
    project.learning = (form.learning.data or "").strip()
    project.future_improvements = (form.future_improvements.data or "").strip()
    project.github_url = (form.github_url.data or "").strip() or None
    project.live_url = (form.live_url.data or "").strip() or None
    project.status = form.status.data
    project.featured = bool(form.featured.data)

    project.images.clear()
    for index, image_path in enumerate(safe_lines(form.image_paths.data or "")):
        project.images.append(
            ProjectImage(
                image_path=image_path,
                alt_text=f"{project.title} screenshot {index + 1}",
                sort_order=index,
            )
        )


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if not _admin_enabled():
        return render_template("admin/login.html", form=None, admin_disabled=True), 503

    form = AdminLoginForm()
    if form.validate_on_submit():
        password_hash = current_app.config["ADMIN_PASSWORD_HASH"]
        try:
            valid = check_password_hash(password_hash, form.password.data)
        except ValueError:
            valid = False
        if valid:
            session.clear()
            session["admin_authenticated"] = True
            flash("Admin sign-in successful.", "success")
            return redirect(url_for("admin.dashboard"))
        flash("Invalid admin password.", "error")
    return render_template("admin/login.html", form=form, admin_disabled=False)


@admin_bp.route("/logout", methods=["POST"])
@admin_required
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("main.home"))


@admin_bp.route("/")
@admin_required
def dashboard():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(50).all()
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template("admin/dashboard.html", projects=projects, messages=messages, posts=posts)


@admin_bp.route("/projects/new", methods=["GET", "POST"])
@admin_required
def project_new():
    form = ProjectForm()
    if form.validate_on_submit():
        slug = form.slug.data.strip().lower()
        if not slug_is_valid(slug):
            form.slug.errors.append("Use lowercase letters, numbers, and hyphens only.")
        elif Project.query.filter_by(slug=slug).first():
            form.slug.errors.append("That slug already exists.")
        else:
            project = Project()
            _populate_project(project, form)
            db.session.add(project)
            db.session.commit()
            flash("Project created.", "success")
            return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", form=form, heading="Add project")


@admin_bp.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
@admin_required
def project_edit(project_id):
    project = db.get_or_404(Project, project_id)
    form = ProjectForm(obj=project)
    if request.method == "GET":
        form.image_paths.data = "\n".join(image.image_path for image in project.images)
    if form.validate_on_submit():
        slug = form.slug.data.strip().lower()
        duplicate = Project.query.filter(Project.slug == slug, Project.id != project.id).first()
        if not slug_is_valid(slug):
            form.slug.errors.append("Use lowercase letters, numbers, and hyphens only.")
        elif duplicate:
            form.slug.errors.append("That slug already exists.")
        else:
            _populate_project(project, form)
            db.session.commit()
            flash("Project updated.", "success")
            return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", form=form, heading="Edit project")


@admin_bp.route("/projects/<int:project_id>/delete", methods=["POST"])
@admin_required
def project_delete(project_id):
    project = db.get_or_404(Project, project_id)
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted.", "success")
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/blog/new", methods=["GET", "POST"])
@admin_required
def blog_new():
    form = BlogPostForm()
    if form.validate_on_submit():
        slug = form.slug.data.strip().lower()
        if not slug_is_valid(slug):
            form.slug.errors.append("Use lowercase letters, numbers, and hyphens only.")
        elif BlogPost.query.filter_by(slug=slug).first():
            form.slug.errors.append("That slug already exists.")
        else:
            post = BlogPost(
                title=form.title.data.strip(),
                slug=slug,
                summary=form.summary.data.strip(),
                category=form.category.data.strip(),
                external_url=(form.external_url.data or "").strip() or None,
                published=bool(form.published.data),
            )
            db.session.add(post)
            db.session.commit()
            flash("Blog/update entry created.", "success")
            return redirect(url_for("admin.dashboard"))
    return render_template("admin/blog_form.html", form=form, heading="Add blog/update")


@admin_bp.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
@admin_required
def blog_edit(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = BlogPostForm(obj=post)
    if form.validate_on_submit():
        slug = form.slug.data.strip().lower()
        duplicate = BlogPost.query.filter(BlogPost.slug == slug, BlogPost.id != post.id).first()
        if not slug_is_valid(slug):
            form.slug.errors.append("Use lowercase letters, numbers, and hyphens only.")
        elif duplicate:
            form.slug.errors.append("That slug already exists.")
        else:
            post.title = form.title.data.strip()
            post.slug = slug
            post.summary = form.summary.data.strip()
            post.category = form.category.data.strip()
            post.external_url = (form.external_url.data or "").strip() or None
            post.published = bool(form.published.data)
            db.session.commit()
            flash("Blog/update entry updated.", "success")
            return redirect(url_for("admin.dashboard"))
    return render_template("admin/blog_form.html", form=form, heading="Edit blog/update")


@admin_bp.route("/blog/<int:post_id>/delete", methods=["POST"])
@admin_required
def blog_delete(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Blog/update entry deleted.", "success")
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/messages/<int:message_id>")
@admin_required
def message_detail(message_id):
    message = db.get_or_404(ContactMessage, message_id)
    if message.status == "New":
        message.status = "Read"
        db.session.commit()
    return render_template("admin/message_detail.html", message=message)


@admin_bp.route("/messages/<int:message_id>/delete", methods=["POST"])
@admin_required
def message_delete(message_id):
    message = db.get_or_404(ContactMessage, message_id)
    db.session.delete(message)
    db.session.commit()
    flash("Message deleted.", "success")
    return redirect(url_for("admin.dashboard"))
