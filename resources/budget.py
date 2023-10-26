from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import BudgetModel
from schemas import BudgetSchema, UpdateBudgetSchema
from datetime import timedelta

blp = Blueprint("Budgets", "budgets", description="Operation on budgets")

# group together function with same route
@blp.route("/budget/<string:budget_id>")
class Budget(MethodView):
    @blp.response(200, BudgetSchema)
    def get(self, budget_id):
        budget = BudgetModel.query.get_or_404(budget_id)
        return budget

    def delete(self, budget_id):
        budget = BudgetModel.query.get_or_404(budget_id)
        db.session.delete(budget)
        db.session.commit()
        return {"message": "Budget deleted."}

    @blp.arguments(UpdateBudgetSchema)
    @blp.response(200, BudgetSchema)
    def put(self, budget_data, budget_id):
        budget = BudgetModel.query.get(budget_id)

        # check if budget exist
        if budget:
            # if exist, will update 
            budget.start_date = budget_data["start_date"]
            budget.end_date = budget_data["start_date"] + timedelta(days=30)
            budget.total_amount = budget_data["total_amount"]
            budget.category_name = budget_data["category_name"]
            budget.budget_amount = budget_data["budget_amount"]
            budget.amount_spent = budget_data["amount_spent"]
        else:
            # if doesn't exist, will create a new budget
            budget = BudgetModel(id=budget_id, end_date=budget_data["start_date"] + timedelta(days=30), **budget_data)
        db.session.add(budget)
        db.session.commit()

        return budget


@blp.route("/budget")
class BudgetList(MethodView):
    @blp.response(200, BudgetSchema(many=True))
    def get(self):
        # will return all of the budgets
        return BudgetModel.query.all()

    @blp.arguments(UpdateBudgetSchema)
    @blp.response(201, BudgetSchema)
    def post(self, budget_data):
        budget = BudgetModel(end_date=budget_data["start_date"] + timedelta(days=30), **budget_data)
        try:
            db.session.add(budget)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A category with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the budget.")

        return budget

