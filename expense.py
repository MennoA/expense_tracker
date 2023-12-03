from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db
from expense_tracker.utils import get_categories, get_currencies, get_tags

bp = Blueprint('expense', __name__)


#create
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        category = request.form['category']
        subcat = request.form['subcat']
        tag = request.form['tag']
        income = request.form['income']
        amount = request.form['amount']
        account = request.form['account']
        currency = request.form['currency']
        description = request.form['description']
        error = None

        if name == None:
            error = 'name is required.'
        
        if date == None:
            error = 'date is required.'

        if amount == None:
            error = 'amount is required.'

        if error is None:
            db = get_db()
            db.execute(
                'INSERT INTO EXPENSE (name, date, amount, income, tag, category, subcat, description, account, cur) '
                'VALUES (?,?,?,?,?,?,?,?,?)',
                (name, date, amount, income, tag, category, subcat, description, account, currency)
            )
            db.commit()
            return redirect(url_for('overview.index'))
        else:
            flash(error)

    return render_template('expense/create.html', categories=get_categories(), subcategories=get_categories(), tags=get_tags(), currencies=get_currencies())


    
#delete

#edit