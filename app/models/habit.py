from .. import db
from datetime import datetime, timedelta

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completions = db.relationship('HabitCompletion', backref='habit', lazy=True)
    
    def get_streak(self):
        if not self.completions:
            return 0
            
        sorted_completions = sorted([c.date for c in self.completions])
        current_streak = 1
        max_streak = 1
        
        for i in range(1, len(sorted_completions)):
            if (sorted_completions[i] - sorted_completions[i-1]).days == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
                
        return max_streak

class HabitCompletion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    __table_args__ = (db.UniqueConstraint('habit_id', 'date'),) 