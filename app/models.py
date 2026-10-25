from __future__ import annotations

from datetime import datetime, timezone

from .extensions import db


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    slug = db.Column(db.String(180), unique=True, nullable=False, index=True)
    category = db.Column(db.String(40), nullable=False, index=True)
    short_description = db.Column(db.String(320), nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.Text, nullable=False, default="")
    features = db.Column(db.Text, nullable=False, default="")
    problem = db.Column(db.Text, nullable=False, default="")
    solution = db.Column(db.Text, nullable=False, default="")
    learning = db.Column(db.Text, nullable=False, default="")
    future_improvements = db.Column(db.Text, nullable=False, default="")
    github_url = db.Column(db.String(500), nullable=True)
    live_url = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(30), nullable=False, default="Coming Soon")
    featured = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)

    images = db.relationship(
        "ProjectImage",
        back_populates="project",
        cascade="all, delete-orphan",
        order_by="ProjectImage.sort_order",
    )

    @property
    def technology_list(self) -> list[str]:
        return [item.strip() for item in self.technologies.split(",") if item.strip()]

    @property
    def feature_list(self) -> list[str]:
        return [item.strip() for item in self.features.splitlines() if item.strip()]

    @property
    def future_improvement_list(self) -> list[str]:
        return [item.strip() for item in self.future_improvements.splitlines() if item.strip()]

    @property
    def main_image(self) -> str | None:
        return self.images[0].image_path if self.images else None


class ProjectImage(db.Model):
    __tablename__ = "project_images"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    image_path = db.Column(db.String(300), nullable=False)
    alt_text = db.Column(db.String(220), nullable=False, default="Project screenshot")
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    project = db.relationship("Project", back_populates="images")


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    subject = db.Column(db.String(180), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, index=True)
    status = db.Column(db.String(20), nullable=False, default="New")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    summary = db.Column(db.String(420), nullable=False)
    category = db.Column(db.String(80), nullable=False, default="Update")
    external_url = db.Column(db.String(500), nullable=True)
    published = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, index=True)
