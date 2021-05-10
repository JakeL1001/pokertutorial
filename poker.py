from pokerapp import pokerpack, db
from pokerapp.models import User, Results

@pokerpack.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Results": Results}