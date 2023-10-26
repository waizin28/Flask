from db import db

# user_id and category_id as foreign key
class TransactionModel(db.Model):
    # create table call budgets
    __tablename__ = "transactions"

    # create following columns
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(80), unique=False, nullable=False)
    
    isSubscription =  db.Column(db.Boolean, unique=False, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False)
   
    budget_id = db.Column(
        db.Integer, db.ForeignKey("budgets.id"), unique=False, nullable=False
    )
    budget = db.relationship("BudgetModel", back_populates="transactions")

    
