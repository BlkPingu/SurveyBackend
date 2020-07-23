from app import User
from app import db





def create_new_database(db):
    db.create_all()
    admin = User(username='admin', email='contact@tobiaskolb.dev')
    db.session.add(admin)
    db.session.commit()


create_new_database(db)

User.query.all()
