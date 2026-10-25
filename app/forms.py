from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional, URL


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=254)])
    subject = StringField("Subject", validators=[DataRequired(), Length(min=3, max=180)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10, max=3000)])
    website = StringField("Website", validators=[Optional(), Length(max=200)])  # honeypot
    submit = SubmitField("Send Message")


class AdminLoginForm(FlaskForm):
    password = PasswordField("Admin password", validators=[DataRequired(), Length(min=8, max=200)])
    submit = SubmitField("Sign in")


class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=160)])
    slug = StringField("Slug", validators=[DataRequired(), Length(max=180)])
    category = SelectField(
        "Category",
        choices=[
            ("python", "Python Developer"),
            ("data-analytics", "Data Analytics"),
            ("ai-ml", "AI & Machine Learning"),
        ],
        validators=[DataRequired()],
    )
    short_description = TextAreaField("Short description", validators=[DataRequired(), Length(max=320)])
    full_description = TextAreaField("Full description", validators=[DataRequired(), Length(max=8000)])
    technologies = StringField("Technologies (comma separated)", validators=[DataRequired(), Length(max=500)])
    features = TextAreaField("Key features (one per line)", validators=[Optional(), Length(max=4000)])
    problem = TextAreaField("Problem statement", validators=[Optional(), Length(max=5000)])
    solution = TextAreaField("Solution", validators=[Optional(), Length(max=5000)])
    learning = TextAreaField("What I learned", validators=[Optional(), Length(max=5000)])
    future_improvements = TextAreaField("Future improvements (one per line)", validators=[Optional(), Length(max=4000)])
    github_url = StringField("GitHub URL", validators=[Optional(), URL(), Length(max=500)])
    live_url = StringField("Live URL", validators=[Optional(), URL(), Length(max=500)])
    status = SelectField(
        "Status",
        choices=[("Completed", "Completed"), ("In Progress", "In Progress"), ("Coming Soon", "Coming Soon")],
        validators=[DataRequired()],
    )
    featured = BooleanField("Featured")
    image_paths = TextAreaField(
        "Screenshot paths (one relative static path per line)",
        validators=[Optional(), Length(max=4000)],
    )
    submit = SubmitField("Save project")


class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=180)])
    slug = StringField("Slug", validators=[DataRequired(), Length(max=200)])
    summary = TextAreaField("Summary", validators=[DataRequired(), Length(max=420)])
    category = StringField("Category", validators=[DataRequired(), Length(max=80)])
    external_url = StringField("External / LinkedIn URL", validators=[Optional(), URL(), Length(max=500)])
    published = BooleanField("Published")
    submit = SubmitField("Save post")
