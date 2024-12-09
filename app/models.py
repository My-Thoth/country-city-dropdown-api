from app import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)

    # This automatically creates a 'country' relationship in City.
    cities = db.relationship('City', backref='country', lazy=True)

    def __repr__(self):
        return f"<Country {self.name}>"

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

    # No need for back_populates if using backref.
    def __repr__(self):
        return f"<City {self.name}>"
