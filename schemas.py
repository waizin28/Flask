from marshmallow import Schema, fields

# budget schema
# amount_spent need to be calculated by amount from transactionschema
class PlainBudgetSchema(Schema):
    id = fields.Int(dump_only=True)
    category_name = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    budget_amount = fields.Float(required=True)
    amount_spent = fields.Float()
    amount_avaiable = fields.Float()

# need to add user_id 
class PlainTransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    alias = fields.Str(required=True)
    isSubscription = fields.Boolean(required=True)
    date = fields.Date(required=True)
    amount = fields.Float(required=True)
    description = fields.Str()

class UpdateBudgetSchema(Schema):
    start_date = fields.Date()
    amount_avaiable = fields.Float()
    category_name = fields.Str()
    budget_amount = fields.Float()
    amount_spent = fields.Float()

class TransactionSchema(PlainTransactionSchema):
    budget_id = fields.Int(required=True, load_only=True)
    budget =  fields.Nested(PlainBudgetSchema(), dump_only=True) # use only for returning not when receiving

# this will include schema where we can see all of related transactions
class BudgetSchema(PlainBudgetSchema):
    transactions = fields.List(fields.Nested(PlainTransactionSchema()), dump_only=True) # get the budget associated with this transaction






