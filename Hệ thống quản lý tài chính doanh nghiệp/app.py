from flask import Flask, jsonify, render_template, request, redirect, url_for
from models.transaction import Transaction
from controllers.transaction_controller import TransactionController
from models.news import News
app = Flask(__name__)

@app.before_request
def initialize_database():
    Transaction.create_table()
    News.create_table()

@app.route('/')
def index():
    news = News.get_all_news()
    return render_template('news.html', news=news)

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']
        News.add_news(title, content, date)
        return redirect(url_for('index'))
    return render_template('add_news.html')

@app.route('/transaction')
def transaction_list():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    category = request.args.get('category')
    department = request.args.get('department')
    transactions = TransactionController.get_all_transactions(start_date, end_date, category, department)
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

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/monthly_revenue')
def get_monthly_revenue():
    data = Transaction.get_monthly_revenue()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
