from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from expense_tracker.auth import login_required
from expense_tracker.db import get_db

bp = Blueprint('account', __name__)

# init

# select account

# create account

# edit account

# delete account