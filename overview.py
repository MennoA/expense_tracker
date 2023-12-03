from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db

bp = Blueprint('overview', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()

    # display overview

    # display graph

    # limit to 10
    last_expenses = db.execute(
        'SELECT p.id, name, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('overview/index.html', expenses=last_expenses)


# go to graph

# go to account

# select account

# filter date

# go to details

# create expense/income

# go to category

# go to tag