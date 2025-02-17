from models.transaction import Transaction

class TransactionController:
    @staticmethod
    def add_transaction(date, amount, category, description, department):
        Transaction.add_transaction(date, amount, category, description, department)

    @staticmethod
    def update_transaction(id, date, amount, category, description, department):
        Transaction.update_transaction(id, date, amount, category, description, department)

    @staticmethod
    def delete_transaction(id):
        Transaction.delete_transaction(id)

    @staticmethod
    def get_all_transactions(start_date=None, end_date=None, category=None, department=None):
        return Transaction.get_all_transactions(start_date, end_date, category, department)

    @staticmethod
    def get_transaction(id):
        return Transaction.get_transaction(id)
