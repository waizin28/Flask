from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import TransactionModel
from schemas import TransactionSchema

blp = Blueprint("Transactions", "transactions", description="Operations on transactions")

@blp.route("/transaction/<string:transaction_id>")
class Transaction(MethodView):
    @blp.response(200, TransactionSchema)
    def get(self, transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        return transaction

    def delete(self, transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        db.session.delete(transaction)
        db.session.commit()
        return {"message": "Transaction deleted"}, 200

@blp.route("/transaction")
class TransactionList(MethodView):
    @blp.response(200, TransactionSchema(many=True))
    def get(self):
        # will return all of the transactions
        return TransactionModel.query.all()

    @blp.arguments(TransactionSchema)
    @blp.response(201, TransactionSchema)
    def post(self, transaction_data):
        transaction = TransactionModel(**transaction_data)
        try:
            db.session.add(transaction)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the transaction.")

        return transaction
