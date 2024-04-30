from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

# Define Expense model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float)

# Function to add expense
def add_expense(description, amount):
    expense = Expense(description=description, amount=amount)
    db.session.add(expense)
    db.session.commit()

# Define route for the home page
@app.route('/')
def index():
    return 'hi'

# Define route for adding expenses
@app.route('/add_expense')
def add_expense_form():
    return render_template('add_expense.html')

# Route to add expense
@app.route('/add_expense', methods=['POST'])
def add_expense_route():
    description = request.form['description']
    amount = float(request.form['amount'])
    add_expense(description, amount)  # Call add_expense with description and amount
    return 'Expense added successfully!'

if __name__ == '__main__':
    # Create database tables
    db.create_all()
    # Run Flask application
    app.run(debug=True)
