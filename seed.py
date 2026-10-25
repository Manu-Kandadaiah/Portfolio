from app import create_app
from app.extensions import db
from app.models import BlogPost, Project, ProjectImage

app = create_app()

PROJECTS = [{'title': 'IT Help Management System',
  'slug': 'it-help-management-system',
  'category': 'python',
  'short_description': 'Flask-based IT support ticket management with assignment, priorities, status '
                       'tracking and REST APIs.',
  'full_description': 'Backend-focused IT support application described in the supplied resume. It manages '
                      'tickets, users, and support workflows with database-backed CRUD operations.',
  'technologies': 'Python, Flask, REST APIs, MySQL/SQLite, HTML, CSS',
  'features': 'Ticket creation and assignment\n'
              'Priority and category management\n'
              'Status tracking and CRUD operations\n'
              'Search, filtering, dashboard and reporting\n'
              'Database-backed REST API endpoints',
  'problem': 'IT support requests need consistent tracking, ownership and status visibility.',
  'solution': 'Ticket workflows, user records, and database-backed APIs for support operations.',
  'learning': 'Implementation details and technical challenges require source repository review; not '
              'independently verified.',
  'future_improvements': 'Add verified screenshots and architecture notes\n'
                         'Document tests and deployment\n'
                         'Measure support workflow outcomes',
  'status': 'Completed',
  'featured': True,
  'image': 'images/projects/showcase/it-help-management-system.svg'},
 {'title': 'IT Asset Management System',
  'slug': 'it-asset-management-system',
  'category': 'python',
  'short_description': 'Track IT inventory, employee allocations, returns and asset status with Flask and '
                       'SQL.',
  'full_description': 'An IT asset workflow application described in the supplied resume, covering '
                      'employees, inventory and assignments.',
  'technologies': 'Python, Flask, REST APIs, MySQL/SQLite, HTML, CSS',
  'features': 'Employee and asset management\n'
              'Inventory and allocation tracking\n'
              'Asset return processing\n'
              'Status tracking and CRUD\n'
              'Search, filters, dashboard and basic reporting',
  'problem': 'IT assets and employee allocations require organized, searchable records.',
  'solution': 'A database-backed asset management workflow with REST endpoints and a web interface.',
  'learning': 'Specific implementation challenges and results have not been independently verified.',
  'future_improvements': 'Add actual application screenshots\n'
                         'Document deployment and test coverage\n'
                         'Confirm asset audit workflows',
  'status': 'Completed',
  'featured': True,
  'image': 'images/projects/showcase/it-asset-management-system.svg'},
 {'title': 'E-Commerce Website / Backend',
  'slug': 'e-commerce-website-backend',
  'category': 'python',
  'short_description': 'E-commerce backend with authentication, products, categories, cart and order '
                       'processing.',
  'full_description': 'A Flask and SQL e-commerce application described in the supplied resume, including '
                      'user, product, cart and order workflows.',
  'technologies': 'Python, Flask, REST APIs, MySQL/SQLite, HTML, CSS',
  'features': 'User registration and login\n'
              'Product and category management\n'
              'Product search and shopping cart\n'
              'Order processing\n'
              'CRUD endpoints and database integration',
  'problem': 'An online store needs coordinated product, user, cart and order management.',
  'solution': 'Backend business logic and REST APIs for common store operations.',
  'learning': 'The uploaded portfolio does not contain this application source, so challenges and test '
              'results remain unverified.',
  'future_improvements': 'Add real UI screenshots and API examples\n'
                         'Document validation and tests\n'
                         'Confirm deployment readiness',
  'status': 'Completed',
  'featured': True,
  'image': 'images/projects/showcase/e-commerce-website-backend.svg'}]

POSTS = [
    {
        "title": "Portfolio Launch Notes",
        "slug": "portfolio-launch-notes",
        "summary": "PLACEHOLDER — Use this section for genuine project updates, learning notes, or external LinkedIn articles.",
        "category": "Portfolio Update",
        "external_url": None,
        "published": True,
    }
]


with app.app_context():
    db.create_all()
    if Project.query.count() == 0:
        for raw_data in PROJECTS:
            data = raw_data.copy()
            image = data.pop("image")
            project = Project(**data)
            project.images.append(ProjectImage(image_path=image, alt_text=f"{project.title} conceptual illustration (not a screenshot)", sort_order=0))
            db.session.add(project)
        db.session.commit()
        print("Seeded resume-supported project entries.")
    else:
        print("Projects already exist; seed skipped.")

    if BlogPost.query.count() == 0:
        db.session.add_all(BlogPost(**post) for post in POSTS)
        db.session.commit()
        print("Seeded sample blog/update entries.")
    else:
        print("Blog posts already exist; seed skipped.")
