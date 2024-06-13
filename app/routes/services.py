from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from ..models import WasteCollectionSchedule
from .. import db

bp = Blueprint('services', __name__)

@bp.route('/services')
@login_required
def services_dashboard():
    schedules = WasteCollectionSchedule.query.all()
    return render_template('services_dashboard.html', schedules=schedules)

@bp.route('/services/schedule', methods=['GET', 'POST'])
@login_required
def manage_schedule():
    if request.method == 'POST':
        # Manage schedule logic here
        pass
    return render_template('manage_schedule.html')
