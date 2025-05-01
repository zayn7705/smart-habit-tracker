from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from ..models.habit import Habit, HabitCompletion
from .. import db
from datetime import datetime, date

habits = Blueprint('habits', __name__)

@habits.route('/')
@habits.route('/dashboard')
@login_required
def dashboard():
    user_habits = Habit.query.filter_by(user_id=current_user.id).all()
    return render_template('habits/dashboard.html', habits=user_habits)

@habits.route('/habit/new', methods=['GET', 'POST'])
@login_required
def new_habit():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        habit = Habit(name=name, description=description, user_id=current_user.id)
        db.session.add(habit)
        db.session.commit()
        
        return redirect(url_for('habits.dashboard'))
        
    return render_template('habits/new.html')

@habits.route('/habit/<int:habit_id>/complete', methods=['POST'])
@login_required
def complete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
        
    completion_date = date.today()
    existing_completion = HabitCompletion.query.filter_by(
        habit_id=habit_id, 
        date=completion_date
    ).first()
    
    if existing_completion:
        db.session.delete(existing_completion)
        message = 'Habit completion removed'
    else:
        completion = HabitCompletion(habit_id=habit_id, date=completion_date)
        db.session.add(completion)
        message = 'Habit completed'
        
    db.session.commit()
    return jsonify({
        'message': message,
        'streak': habit.get_streak()
    }) 