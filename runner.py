
from service.vigilant import service_call
from model.legacy.oracle import db



def run_server():
    service_call()
    db.call_db()


run_server()
