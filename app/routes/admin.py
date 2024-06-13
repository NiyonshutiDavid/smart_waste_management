from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from ..models import User, WasteCollectionSchedule, RecyclingTracker
from .. import db

bp = Blueprint('admin', __name__)

@bp.route('/admin')
@login_required
def admin_dashboard():
    users = User.query.all()
    schedules = WasteCollectionSchedule.query.all()
    recycling = RecyclingTracker.query.all()
    return render_template('admin_dashboard.html', users=users, schedules=schedules, recycling=recycling)

@bp.route('/admin/manage_users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if request.method == 'POST':
        # Manage users logic here
        pass
    return render_template('manage_users.html')
