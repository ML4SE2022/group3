from sqlalchemy import func

session.query(func.now()).all()