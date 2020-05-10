from app import app,db
from app.models import User, Loan, UsbMemory, Rireki

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Loan': Loan, 'UsbMemory': UsbMemory, 'Rireki': Rireki}

