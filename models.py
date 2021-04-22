
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
setup_db(app) used in tests.py
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    db.app = app
    db.init_app(app)
    db.create_all()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Winery(db.Model):
    __tablename__ = 'winery'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(300))
    wines = db.relationship('Wine', backref='winery', lazy='dynamic')

    def __repr__(self):
      return f'''< winery 
                        id: {self.id},
                      name: {self.name},
                      city: {self.city},
                     state: {self.state} >'''

    # TODO: implement any missing fields, as a database migration using Flask-Migrate - done

class Winemaker(db.Model):
    __tablename__ = 'winemaker'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120))
    seeking_winery = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(300))
    wines = db.relationship('Wine', backref='winemaker', lazy='dynamic')

    def __repr__(self):
      return f'''< winemaker 
               id: {self.id},
             name: {self.name},
             city: {self.city},
            state: {self.state}>'''

    # TODO: implement any missing fields, as a database migration using Flask-Migrate - done

class Wine(db.Model):
    __tablename__ = 'wines'
    id = db.Column(db.Integer, primary_key=True)
    winery_id = db.Column(db.Integer, db.ForeignKey(
        'winery.id'), nullable=False)
    winemaker_id = db.Column(db.Integer, db.ForeignKey(
        'winemaker.id'), nullable=False)
    start_time = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
      return f'''\n
            Wine: {self.id} 
           Winery: {self.winery.name} 
          Winemaker: {self.winemaker.name}
      start_time: {self.start_time} '''


