from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db
from expense_tracker.utils import get_categories

bp = Blueprint('categories', __name__, url_prefix='/categories')

# init
@bp.route('/main')
@login_required
def main():
    db = get_db()
    return render_template('categories/main.html', categories=get_categories())

# create category
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        subcat = request.form['subcat']
        parent = request.form['parent']
        description = request.form['description']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO categories (name, subcat, parent, description, user)'
                ' VALUES (?, ?, ?, ?, ?)',
                (name, subcat, parent, description, g.user['id'])
            )
            db.commit()
            return redirect(url_for('categories.main'))

    return render_template('categories/create.html')

# edit category
@bp.route('/edit', methods=('GET', 'POST'))
@login_required
def edit():
    db = get_db()
    return render_template('categories/edit.html', categories=get_categories())


# delete category
#@bp.route('/delete')
#@login_required
#def delete(int id):
#    return redirect(url_for('main'))
