from app import User
from app import db
from app import create_new_database

create_new_database(db)

User.query.all()