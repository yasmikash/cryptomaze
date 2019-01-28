from datetime import datetime
from cryptomaze import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    bitcoin_address = db.Column(db.String(120), nullable=False)
    register_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    ref_balance = db.Column(db.FLOAT(precesion=15, scale=8), default=0)
    btc_balance = db.Column(db.FLOAT(precesion=15, scale=8), default=0)
    last_claim_date = db.Column(db.DateTime, default=datetime(2013, 9, 30, 7, 6, 5))
    referred_by = db.Column(db.Integer, default=0)
    withdrawals = db.relationship('Withdraw', backref='withdrawal', lazy=True)
   
    def __repr__(self):
        return "Users('{}', '{}')".format(self.id, self.btc_balance)


class Withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.FLOAT(precesion=15, scale=8), nullable=False)
    bitcoin_address = db.Column(db.String(120), nullable=False)
    withdraw_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Withdraw('{}', '{}')".format(self.amount, self.status)


