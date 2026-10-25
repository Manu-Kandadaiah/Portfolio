from flask import Blueprint, flash, redirect, render_template, url_for

from ..extensions import db
from ..forms import ContactForm
from ..models import ContactMessage

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        if form.website.data:
            flash("Unable to process the request.", "error")
            return redirect(url_for("contact.contact"))

        message = ContactMessage(
            name=form.name.data.strip(),
            email=form.email.data.strip().lower(),
            subject=form.subject.data.strip(),
            message=form.message.data.strip(),
        )
        db.session.add(message)
        db.session.commit()
        flash("Your message has been sent successfully.", "success")
        return redirect(url_for("contact.contact"))

    if form.is_submitted() and form.errors:
        flash("Please correct the highlighted fields and try again.", "error")
    return render_template("contact.html", form=form)
