from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..models import WasteCollectionSchedule, RecyclingTracker
from .. import db

bp = Blueprint('household', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    schedules = WasteCollectionSchedule.query.filter_by(user_id=current_user.id).all()
    recycling = RecyclingTracker.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', schedules=schedules, recycling=recycling)

@bp.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    if request.method == 'POST':
        schedule_date = request.form.get('schedule_date')
        new_schedule = WasteCollectionSchedule(user_id=current_user.id, schedule_date=schedule_date)
        db.session.add(new_schedule)
        db.session.commit()
        return redirect(url_for('household.dashboard'))
    return render_template('schedule.html')
