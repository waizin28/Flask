from db import db

# Tell what table and what column we will have
# it will also automatically turn into python object

# create mapping between row in table and python class
# add user_id = db.Column(required=True) later
class BudgetModel(db.Model):
    # create table call budgets
    __tablename__ = "budgets"

    # create following columns

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80), unique=True, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=False) # nullable = False -> cannot create item that doesn't have start date
    end_date = db.Column(db.Date, unique=False)
    budget_amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    amount_spent = db.Column(db.Float(precision=2), unique=False, nullable=False)
    amount_avaiable = db.Column(db.Float(precision=2), unique=False, nullable=False)

    # We can also see all of the transactions that are associated with this budget (SQL Alchemy will handle this)
    # lazy="dynamic" means transactions won't be fetch from database until we tell it to
    # cascade="all, delete"
    transactions = db.relationship(
        "TransactionModel", back_populates="budget", lazy="dynamic", cascade='all, delete'
    )