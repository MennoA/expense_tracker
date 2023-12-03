from flask import g
from expense_tracker.auth import login_required
from expense_tracker.db import get_db


@login_required
def get_categories():
    db = get_db()
    user_id = g.user['id']
    return db.execute(
        'SELECT * FROM categories c '
        'JOIN user u ON u.id = c.user '
        'WHERE u.id = ?', (user_id,)
    ).fetchall()


@login_required
def get_tags():
    db = get_db()
    user_id = g.user['id']
    return db.execute(
        'SELECT * FROM tag t '
        'JOIN user u ON u.id = t.user '
        'WHERE u.id = ?', (user_id,)
    ).fetchall()

def get_currencies():
    db = get_db()
    return db.execute(
        'SELECT * from currency'
    ).fetchall()
    

