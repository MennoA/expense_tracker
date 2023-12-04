from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db
from expense_tracker.utils import get_tags

bp = Blueprint('tag', __name__, url_prefix='/tags')

# init
@bp.route('/main')
@login_required
def main():
    db = get_db()
    return render_template('tag/main.html', tags=get_tags())

# create tag
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        description = request.form['description']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tags (name, color, user, description)'
                ' VALUES (?, ?, ?, ?)',
                (name, color, g.user['id'], description)
            )
            db.commit()
            return redirect(url_for('tags.main'))

    return render_template('tags/create.html')


# edit tag

# delete tag