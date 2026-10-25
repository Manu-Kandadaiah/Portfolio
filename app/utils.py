from __future__ import annotations

import re
from functools import wraps
from pathlib import Path

from flask import current_app, flash, redirect, session, url_for


def static_file_exists(relative_path: str) -> bool:
    static_root = Path(current_app.static_folder or "")
    return (static_root / relative_path).is_file()


def slug_is_valid(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value or ""))


def safe_lines(value: str) -> list[str]:
    return [line.strip() for line in (value or "").splitlines() if line.strip()]


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin_authenticated"):
            flash("Please sign in to access the admin area.", "warning")
            return redirect(url_for("admin.login"))
        return view(*args, **kwargs)

    return wrapped
