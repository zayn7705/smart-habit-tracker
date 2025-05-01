# Smart Habit Tracker

A simple and effective web application to help you build and track habits with streaks, reminders, and data visualization.

## Features

- User Authentication (Register/Login)
- Create and manage habits
- Track daily habit completion
- Streak tracking for each habit
- Clean and modern UI with Tailwind CSS
- Interactive features with Alpine.js

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (Tailwind), JavaScript (Alpine.js)
- **Authentication**: Flask-Login

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zayn7705/smart-habit-tracker.git
cd smart-habit-tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Register** a new account or **Login** if you already have one
2. Create new habits from the dashboard
3. Mark habits as complete each day
4. Track your streaks and progress

## Project Structure

```
smart-habit-tracker/
├── app/
│   ├── models/
│   │   ├── user.py
│   │   └── habit.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── habits.py
│   ├── static/
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── habits/
│   │   │   ├── dashboard.html
│   │   │   └── new.html
│   │   └── base.html
│   └── __init__.py
├── instance/
├── venv/
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
