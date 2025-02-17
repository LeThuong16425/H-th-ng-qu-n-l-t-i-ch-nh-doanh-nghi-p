from flask import Flask, render_template, request, redirect, url_for
from models.transaction import Transaction
from controllers.transaction_controller import TransactionController

app = Flask(__name__)

@app.before_request
def initialize_database():
    Transaction.create_table()

@app.route('/')
def index():
    transactions = TransactionController.get_all_transactions()
    return render_template('transaction_list.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        department = request.form['department']
        TransactionController.add_transaction(date, amount, category, description, department)
        return redirect(url_for('index'))
    return render_template('transaction_form.html', transaction=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        department = request.form['department']
        TransactionController.update_transaction(id, date, amount, category, description, department)
        return redirect(url_for('index'))
    transaction = TransactionController.get_transaction(id)
    return render_template('transaction_form.html', transaction=transaction)

@app.route('/delete/<int:id>')
def delete_transaction(id):
    TransactionController.delete_transaction(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
