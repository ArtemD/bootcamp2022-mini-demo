from .schema import Tax
from . import Session

def start():
    # Create a session
    session = Session()
    return session

def insert(company, tax_paid, session):
    # Insert a new tax
    session.add(Tax(company=company, tax_paid=string2float(tax_paid)))

def stop(session):
    session.commit()
    session.close()

def string2float(string):
    return float(string.replace(',', '.'))

def get_taxes():
    session = Session()
    # Get all taxes (limited to 1000)
    taxes = session.query(Tax).order_by(Tax.tax_paid.desc()).limit(1000).all()
    return taxes