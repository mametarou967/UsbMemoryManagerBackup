from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User id:{0} username{1}>'.format(self.id,self.username)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<Loan id:{0} user_id:{1} valid:{2} time:{3}>'.format(self.id,self.user_id,self.valid,self.timestamp)
    

class UsbMemory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usb_number = db.Column(db.Integer)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'))

    def __repr__(self):
        return '<UsbMemory id:{0} usb_number:{1} loan_id:{2}>'.format(self.id,self.usb_number,self.loan_id)

class Rireki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    rireki_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Rireki id:{0} loan_id:{1} timestamp:{2} rireki_id:{3}>'.format(self.id,self.loan_id,self.timestamp,self.rireki_id)

