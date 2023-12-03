from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db
from expense_tracker.utils import get_categories

bp = Blueprint('categories', __name__)

# init
@bp.route('/init')
@login_required
def init():
    db = get_db()

    user_id = session.get('user_id')

    categories = get_categories()

    return render_template('categories/main.html', categories=categories)

# select category

# create category

# edit category

# delete category