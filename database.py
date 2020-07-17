class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), primary_key=True)
    time_created = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer(3), unique=False, nullable=False)
    token = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<Session %r>' % self.session

def create_new_database(db):
    db.create_all()
    admin = User(username='admin', email='contact@tobiaskolb.dev')
    db.session.add(admin)
    db.session.commit()

def new_metadata(db, data):
    pass



