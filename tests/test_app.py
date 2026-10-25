from app import create_app
from app.extensions import db
from app.models import BlogPost, ContactMessage, Project
from config import TestConfig


def make_app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        db.session.add(
            Project(
                title="Test Project",
                slug="test-project",
                category="python",
                short_description="A test project.",
                full_description="Full test project description.",
                technologies="Python, Flask",
                features="Feature one\nFeature two",
                status="Completed",
                featured=True,
            )
        )
        db.session.add(
            BlogPost(
                title="Test Post",
                slug="test-post",
                summary="A test update.",
                category="Testing",
                published=True,
            )
        )
        db.session.commit()
    return app


def test_public_routes():
    app = make_app()
    client = app.test_client()
    for path in ["/", "/home", "/projects", "/projects/python", "/project/test-project", "/resume", "/blog", "/contact"]:
        response = client.get(path)
        assert response.status_code == 200, path


def test_404_page():
    app = make_app()
    response = app.test_client().get("/this-page-does-not-exist")
    assert response.status_code == 404
    assert b"Page Not Found" in response.data


def test_contact_form_stores_private_message():
    app = make_app()
    client = app.test_client()
    response = client.post(
        "/contact",
        data={
            "name": "Recruiter Test",
            "email": "recruiter@example.com",
            "subject": "Opportunity",
            "message": "This is a valid test contact message.",
            "website": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"sent successfully" in response.data
    with app.app_context():
        message = ContactMessage.query.filter_by(email="recruiter@example.com").first()
        assert message is not None
        assert message.status == "New"


def test_honeypot_rejects_bot_submission():
    app = make_app()
    client = app.test_client()
    client.post(
        "/contact",
        data={
            "name": "Bot Test",
            "email": "bot@example.com",
            "subject": "Spam",
            "message": "This should not be stored in the database.",
            "website": "https://spam.invalid",
        },
    )
    with app.app_context():
        assert ContactMessage.query.filter_by(email="bot@example.com").first() is None


def test_admin_disabled_without_password_hash():
    app = make_app()
    response = app.test_client().get("/admin/login")
    assert response.status_code == 503
    assert b"Admin access is disabled" in response.data
