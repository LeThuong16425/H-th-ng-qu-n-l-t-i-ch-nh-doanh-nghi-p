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
    def get_all_transactions():
        return Transaction.get_all_transactions()

    @staticmethod
    def get_transaction(id):
        return Transaction.get_transaction(id)
