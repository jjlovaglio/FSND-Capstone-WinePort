#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import form
from forms import *
from flask_migrate import Migrate
import sys
import itertools

# Auth0 login flow imports
from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Auth0 login flow app config
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id='6FDjYXzq4EsS2t5ZVCV7arEZuC0q0HPE',
    client_secret= env.get('AUTH0_CLIENT_SECRET'),
    api_base_url='https://jjlovaglio.us.auth0.com',
    access_token_url='https://jjlovaglio.us.auth0.com/oauth/token',
    authorize_url='https://jjlovaglio.us.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


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
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120), unique=True)
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
    facebook_link = db.Column(db.String(120), nullable=True, unique=True)
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


# TODO Implement Wine and Winemaker models, and complete all model relationships and properties, as a database migration. - done

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Decorator @requires_auth
#----------------------------------------------------------------------------#

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def check_permissions(permission, payload):
    if 'permissions' not in payload:
                        raise AuthError({
                            'code': 'invalid_claims',
                            'description': 'Permissions not included in JWT.'
                        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found.'
        }, 403)
    return True


def requires_auth(permission=''):
  def requires_auth_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      if 'profile' not in session:
        # Redirect to Login page here
        return redirect('/login')

      check_permissions(permission, payload)

      return f(*args, **kwargs)
    return decorated
  return requires_auth_decorator


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

# Auth0 login flow controllers

@app.route('/login-results')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['logged_in'] = True
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    flash('You were successfully logged in.')
    return render_template('pages/home.html', userinfo=userinfo)


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://127.0.0.1:5000/login-results')


@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('index', _external=True), 'client_id': '6FDjYXzq4EsS2t5ZVCV7arEZuC0q0HPE'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


@app.route('/dashboard')
# @requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))


# End Auth0 login flow controllers

@app.route('/')
def index():
  # Stand out
  # Wine Recent Listed Winemakers and Recently Listed Wineries on the homepage, - done 
  # returning results for Winemakers and Wineries sorting by newly created. - done
  # Limit to the 10 most recently listed items. - done
  recent_wineries = Winery.query.order_by(Winery.id).limit(10).all()
  recent_winemakers = Winemaker.query.order_by(Winemaker.id).limit(10).all()

  return render_template('pages/home.html', recent_wineries = recent_wineries, recent_winemakers = recent_winemakers)

#  Wineries
#  --------------------------------------------------------------------------#

@app.route('/wineries')
def wineries():
  # TODO: replace with real wineries data. - done
  #       num_wines should be aggregated based on number of upcoming wines per winery. - done
  current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  winery_query = Winery.query.group_by(Winery.id, Winery.state, Winery.city).all()
  city_and_state = ''
  data = []
  for winery in winery_query:
      upcoming_wines = winery.wines.filter(Wine.start_time > current_time).all()
      if city_and_state == winery.city + winery.state:
          data[len(data) - 1]["wineries"].append({
            "id": winery.id,
            "name": winery.name,
            "num_upcoming_wines": len(upcoming_wines)
          })
      else:
          city_and_state = winery.city + winery.state
          data.append({
            "city": winery.city,
            "state": winery.state,
            "wineries": [{
              "id": winery.id,
              "name": winery.name,
              "num_upcoming_wines": len(upcoming_wines)
            }]
          })

  return render_template('pages/wineries.html', areas=data)

@app.route('/wineries/search', methods=['POST'])
def search_wineries():
  # TODO: implement search on wineries with partial string search. Ensure it is case-insensitive. - done
  # seach for Hop should return "The Musical Hop". - done
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee" - done
  
    # Stand out
  # TODO: Implement Search Wineries by City and State - done
  # Searching by "San Francisco, CA" should return all wineries in San Francisco, CA. - done
  
  search_term = request.form.get('search_term', '')
  q1 = Winery.query.all()
  winery_list = []

  for winery in q1:
    city_and_state = winery.city + ', ' + winery.state
    if city_and_state == search_term:
      winery_list.append(winery)  


  q2 = Winery.query.filter(Winery.name.ilike(f'%{search_term}%')).all()
  winery_list += q2
 
  response = {
    "count": len(winery_list),
    "data": []
  }
  for winery in winery_list:
    response["data"].append({
      "id": winery.id,
      "name": winery.name
    })
  return render_template('pages/search_wineries.html', results=response, search_term=search_term)

@app.route('/wineries/<int:winery_id>')
def show_winery(winery_id):
  # wines the winery page with the given winery_id - done
  # TODO: replace with real winery data from the wineries table, using winery_id - done 
  current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  winery_query = Winery.query.get(winery_id)
  past_wines_query = winery_query.wines.filter(Wine.start_time < current_time).all()
  past_wines = []
  for wine in past_wines_query:
      past_wines.append({
        "winemaker_id":wine.winemaker_id,
        "winemaker_name":wine.winemaker.name,
        "winemaker_image_link":wine.winemaker.image_link,
        "start_time":str(wine.start_time),
      })

  upcoming_wines_query = winery_query.wines.filter(Wine.start_time > current_time).all()
  upcoming_wines = []
  for wine in upcoming_wines_query:
      upcoming_wines.append({
        "winemaker_id":wine.winemaker_id,
        "winemaker_name":wine.winemaker.name,
        "winemaker_image_link":wine.winemaker.image_link,
        "start_time":str(wine.start_time),
      })


  data = {
    "id": winery_query.id,
    "name": winery_query.name,
    "genres": winery_query.genres,
    "address": winery_query.address,
    "city": winery_query.city,
    "state": winery_query.state,
    "phone": winery_query.phone,
    "website": winery_query.website,
    "facebook_link": winery_query.facebook_link,
    "seeking_talent": winery_query.seeking_talent,
    "seeking_description": winery_query.seeking_description,
    "image_link": winery_query.image_link,
    "past_wines": past_wines,
    "upcoming_wines": upcoming_wines,
    
  }
  
  # data1={
  #   "id": 1,
  #   "name": "The Musical Hop",
  #   "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"], # missing in winery
  #   "address": "1015 Folsom Street",
  #   "city": "San Francisco",
  #   "state": "CA",
  #   "phone": "123-123-1234",
  #   "website": "https://www.themusicalhop.com", 
  #   "facebook_link": "https://www.facebook.com/TheMusicalHop",
  #   "seeking_talent": True,
  #   "seeking_description": "We are on the lookout for a local winemaker to play every two weeks. Please call us.", # missing in winery
  #   "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
  #   "past_wines": [{
  #     "winemaker_id": 4,
  #     "winemaker_name": "Guns N Petals",
  #     "winemaker_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #     "start_time": "2019-05-21T21:30:00.000Z"
  #   }], # missing in winery
  #   "upcoming_wines": [], # missing in winery
  #   "past_wines_count": 1, # missing in winery
  #   "upcoming_wines_count": 0, # missing in winery
  # }
  # data2={
  #   "id": 2,
  #   "name": "The Dueling Pianos Bar",
  #   "genres": ["Classical", "R&B", "Hip-Hop"],
  #   "address": "335 Delancey Street",
  #   "city": "New York",
  #   "state": "NY",
  #   "phone": "914-003-1132",
  #   "website": "https://www.theduelingpianos.com",
  #   "facebook_link": "https://www.facebook.com/theduelingpianos",
  #   "seeking_talent": False,
  #   "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
  #   "past_wines": [],
  #   "upcoming_wines": [],
  #   "past_wines_count": 0,
  #   "upcoming_wines_count": 0,
  # }
  # data3={
  #   "id": 3,
  #   "name": "Park Square Live Music & Coffee",
  #   "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
  #   "address": "34 Whiskey Moore Ave",
  #   "city": "San Francisco",
  #   "state": "CA",
  #   "phone": "415-000-1234",
  #   "website": "https://www.parksquarelivemusicandcoffee.com",
  #   "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
  #   "seeking_talent": False,
  #   "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #   "past_wines": [{
  #     "winemaker_id": 5,
  #     "winemaker_name": "Matt Quevedo",
  #     "winemaker_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #     "start_time": "2019-06-15T23:00:00.000Z"
  #   }],
  #   "upcoming_wines": [{
  #     "winemaker_id": 6,
  #     "winemaker_name": "The Wild Sax Band",
  #     "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-01T20:00:00.000Z"
  #   }, {
  #     "winemaker_id": 6,
  #     "winemaker_name": "The Wild Sax Band",
  #     "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-08T20:00:00.000Z"
  #   }, {
  #     "winemaker_id": 6,
  #     "winemaker_name": "The Wild Sax Band",
  #     "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-15T20:00:00.000Z"
  #   }],
  #   "past_wines_count": 1,
  #   "upcoming_wines_count": 1,
  # }
  # old_data = list(filter(lambda d: d['id'] == winery_id, [data1, data2, data3]))[0]

  return render_template('pages/show_winery.html', winery=data)

#  Create Winery
#  ----------------------------------------------------------------

@app.route('/wineries/create', methods=['GET'])
@requires_auth('post:winery')
def create_winery_form():
  form = WineryForm()
  return render_template('forms/new_winery.html', form=form)

@app.route('/wineries/create', methods=['POST'])
# @requires_auth('post:winery')
def create_winery_submission():
  # TODO: insert form data as a new Winery record in the db, instead - done
  # TODO: modify data to be the data object returned from db insertion - done
  form = WineryForm(request.form, meta={'csrf': False})
  if form.validate():
    try:
      # winery = Winery(
      #   name = form.name.data,
      #   city = form.city.data,
      #   state = form.state.data,
      #   address = form.address.data,
      #   phone = form.phone.data,
      #   genres = form.genres.data,
      #   facebook_link = form.facebook_link.data 
      # )
      winery = Winery()
      form.populate_obj(winery)
      db.session.add(winery)
      db.session.commit()
      # on successful db insert, flash success
      flash('Winery: ' + request.form['name'] + ' was successfully listed!')
    except:
      # TODO: on unsuccessful db insert, flash an error instead. - done
      # e.g., flash('An error occurred. Winery ' + data.name + ' could not be listed.')
      # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
      error = True
      db.session.rollback()
      flash('An error occurred. Winery ' + form.name.data + ' could not be listed.')
      flash(f'{sys.exc_info()}')
    finally:
      db.session.close()
  else:
    messages = []
    for field, errors in form.errors.items():
      for error in errors:
        messages.append(field + ' : ' + error + '\n')
    flash('The Winery data is not valid. Please try again.')
    for message in messages:
      flash(message)
  return render_template('pages/home.html')

@app.route('/wineries/<winery_id>/delete', methods=['DELETE', 'POST'])
# @requires_auth('delete:winery')
def delete_winery(winery_id):
  # TODO: Complete this endpoint for taking a winery_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  error = False
  try:
    winery = Winery.query.get(winery_id)
    db.session.delete(winery)
    db.session.commit()
    flash(f'Winery: {winery.name} was successfully deleted!')
  except:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
  if error:
    abort(500)
  else:
    return redirect(url_for('index'))

  # BONUS CHALLENGE: Implement a button to delete a Winery on a Winery Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage - done


#  Winemakers
#  ----------------------------------------------------------------
@app.route('/winemakers')
def winemakers():
  # TODO: replace with real data returned from querying the database - done
  winemaker_query = Winemaker.query.order_by(Winemaker.name).all()
  # data=[{
  #   "id": 4,
  #   "name": "Guns N Petals",
  # }, {
  #   "id": 5,
  #   "name": "Matt Quevedo",
  # }, {
  #   "id": 6,
  #   "name": "The Wild Sax Band",
  # }]
  return render_template('pages/winemakers.html', winemakers=winemaker_query)



@app.route('/winemakers/search', methods=['POST'])
def search_winemakers():
  # TODO: implement search on winemakers with partial string search. Ensure it is case-insensitive. - done
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band". - done
  # search for "band" should return "The Wild Sax Band". - done

  # Stand out
  # TODO: Implement Search Winemakers by City and State, and Search Wineries by City and State. - done
  # Searching by "San Francisco, CA" should return all winemakers or wineries in San Francisco, CA. - done

  search_term = request.form.get('search_term', '')
  q1 = Winemaker.query.all()
  winemaker_list = []

  for winemaker in q1:
    city_and_state = winemaker.city + ', ' + winemaker.state
    if city_and_state == search_term:
      winemaker_list.append(winemaker)

  q2 = Winemaker.query.filter(Winemaker.name.ilike(f'%{search_term}%')).all()
  winemaker_list += q2


  response = {
    "count": len(winemaker_list),
    "data": []
  }

  for winemaker in winemaker_list:
    response["data"].append({
      "id": winemaker.id,
      "name": winemaker.name
    })

  return render_template('pages/search_winemakers.html', results=response, search_term=search_term)

@app.route('/winemaker/<int:winemaker_id>')
def show_winemaker(winemaker_id):
  # wines the winery page with the given winery_id
  # TODO: replace with real winery data from the wineries table, using winery_id - done
  current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  winemaker_query = Winemaker.query.get(winemaker_id)
  past_wines_query = winemaker_query.wines.filter(Wine.start_time < current_time).all()
  past_wines = []
  for wine in past_wines_query:
      past_wines.append({
        "winery_id":wine.winery_id,
        "winery_name":wine.winery.name,
        "winery_image_link":wine.winery.image_link,
        "start_time":str(wine.start_time),
      })

  upcoming_wines_query = winemaker_query.wines.filter(Wine.start_time > current_time).all()
  upcoming_wines = []
  for wine in upcoming_wines_query:
      upcoming_wines.append({
        "winery_id":wine.winery_id,
        "winery_name":wine.winery.name,
        "winery_image_link":wine.winery.image_link,
        "start_time":str(wine.start_time),
      })

  data = {
    "id": winemaker_query.id,
    "name": winemaker_query.name,
    "genres": winemaker_query.genres,
    "address": winemaker_query.address,
    "city": winemaker_query.city,
    "state": winemaker_query.state,
    "phone": winemaker_query.phone,
    "website": winemaker_query.website,
    "facebook_link": winemaker_query.facebook_link,
    "seeking_winery": winemaker_query.seeking_winery,
    "seeking_description": winemaker_query.seeking_description,
    "image_link": winemaker_query.image_link,
    "past_wines": past_wines,
    "upcoming_wines": upcoming_wines,
    
  }

  # data1={
  #   "id": 4,
  #   "name": "Guns N Petals",
  #   "genres": ["Rock n Roll"],
  #   "city": "San Francisco",
  #   "state": "CA",
  #   "phone": "326-123-5000",
  #   "website": "https://www.gunsnpetalsband.com",
  #   "facebook_link": "https://www.facebook.com/GunsNPetals",
  #   "seeking_winery": True,
  #   "seeking_description": "Looking for wines to perform at in the San Francisco Bay Area!",
  #   "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #   "past_wines": [{
  #     "winery_id": 1,
  #     "winery_name": "The Musical Hop",
  #     "winery_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
  #     "start_time": "2019-05-21T21:30:00.000Z"
  #   }],
  #   "upcoming_wines": [],
  #   "past_wines_count": 1,
  #   "upcoming_wines_count": 0,
  # }
  # data2={
  #   "id": 5,
  #   "name": "Matt Quevedo",
  #   "genres": ["Jazz"],
  #   "city": "New York",
  #   "state": "NY",
  #   "phone": "300-400-5000",
  #   "facebook_link": "https://www.facebook.com/mattquevedo923251523",
  #   "seeking_winery": False,
  #   "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #   "past_wines": [{
  #     "winery_id": 3,
  #     "winery_name": "Park Square Live Music & Coffee",
  #     "winery_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2019-06-15T23:00:00.000Z"
  #   }],
  #   "upcoming_wines": [],
  #   "past_wines_count": 1,
  #   "upcoming_wines_count": 0,
  # }
  # data3={
  #   "id": 6,
  #   "name": "The Wild Sax Band",
  #   "genres": ["Jazz", "Classical"],
  #   "city": "San Francisco",
  #   "state": "CA",
  #   "phone": "432-325-5432",
  #   "seeking_winery": False,
  #   "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "past_wines": [],
  #   "upcoming_wines": [{
  #     "winery_id": 3,
  #     "winery_name": "Park Square Live Music & Coffee",
  #     "winery_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-01T20:00:00.000Z"
  #   }, {
  #     "winery_id": 3,
  #     "winery_name": "Park Square Live Music & Coffee",
  #     "winery_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-08T20:00:00.000Z"
  #   }, {
  #     "winery_id": 3,
  #     "winery_name": "Park Square Live Music & Coffee",
  #     "winery_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-15T20:00:00.000Z"
  #   }],
  #   "past_wines_count": 0,
  #   "upcoming_wines_count": 3,
  # }
  # old_data = list(filter(lambda d: d['id'] == winemaker_id, [data1, data2, data3]))[0]
  return render_template('pages/show_winemaker.html', winemaker=data)

#  Create Winemaker
#  ----------------------------------------------------------------

@app.route('/winemakers/create', methods=['GET'])
# @requires_auth('post:winemaker')
def create_winemaker_form():
  form = WinemakerForm()
  return render_template('forms/new_winemaker.html', form=form)

@app.route('/winemakers/create', methods=['POST'])
# @requires_auth('post:winemaker')
def create_winemaker_submission():
  # called upon submitting the new winemaker listing form
  # TODO: insert form data as a new Winemaker record in the db, instead - done
  # TODO: modify data to be the data object returned from db insertion - done
  form = WinemakerForm(request.form, meta={'csrf': False})
  if form.validate():
      try:
        # alternative way to populate fields from line 603:
        # winemaker = Winemaker(
        #   name = form.name.data,
        #   city = form.city.data,
        #   state = form.state.data,
        #   phone = form.phone.data,
        #   genres = form.genres.data,
        #   facebook_link = form.facebook_link.data 
        # )
        
        winemaker = Winemaker()
        form.populate_obj(winemaker)
        db.session.add(winemaker)
        db.session.commit()
        # on successful db insert, flash success
        flash('Winemaker: ' + request.form['name'] + ' was successfully listed!')
      except:
        # TODO: on unsuccessful db insert, flash an error instead. - done
        # e.g., flash('An error occurred. Winemaker ' + data.name + ' could not be listed.')
        # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
        error = True
        db.session.rollback()
        flash('An error occurred. Winemaker ' + form.name.data + ' could not be listed.')
        flash(f'{sys.exc_info()}')
      finally:
        db.session.close()
  else:
    messages = []
    for field, errors in form.errors.items():
      for error in errors:
        messages.append(field + ' : ' + error + '\n')
    flash('The Winemaker data is not valid. Please try again.')
    for message in messages:
      flash(message)

  # on successful db insert, flash success - done
  # TODO: on unsuccessful db insert, flash an error instead. - done
  # e.g., flash('An error occurred. Winemaker ' + data.name + ' could not be listed.') - done
  return render_template('pages/home.html')


#  Wines
#  ----------------------------------------------------------------

@app.route('/wines')
def wines():
  # displays list of wines at /wines
  # TODO: replace with real wineries data. - done
  #       num_wines should be aggregated based on number of upcoming wines per winery. - done
  wines_query = Wine.query.all()
  data = []
  for query in wines_query:
    data.append({
      "winery_id": query.winery_id,
      "winery_name": query.winery.name,
      "winemaker_id": query.winemaker_id,
      "winemaker_name": query.winemaker.name,
      "winemaker_image_link": query.winemaker.image_link,
      "start_time": str(query.start_time)
    })
  # old_data=[{
  #   "winery_id": 1,
  #   "winery_name": "The Musical Hop",
  #   "winemaker_id": 4,
  #   "winemaker_name": "Guns N Petals",
  #   "winemaker_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #   "start_time": "2019-05-21T21:30:00.000Z"
  # }, {
  #   "winery_id": 3,
  #   "winery_name": "Park Square Live Music & Coffee",
  #   "winemaker_id": 5,
  #   "winemaker_name": "Matt Quevedo",
  #   "winemaker_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #   "start_time": "2019-06-15T23:00:00.000Z"
  # }, {
  #   "winery_id": 3,
  #   "winery_name": "Park Square Live Music & Coffee",
  #   "winemaker_id": 6,
  #   "winemaker_name": "The Wild Sax Band",
  #   "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-01T20:00:00.000Z"
  # }, {
  #   "winery_id": 3,
  #   "winery_name": "Park Square Live Music & Coffee",
  #   "winemaker_id": 6,
  #   "winemaker_name": "The Wild Sax Band",
  #   "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-08T20:00:00.000Z"
  # }, {
  #   "winery_id": 3,
  #   "winery_name": "Park Square Live Music & Coffee",
  #   "winemaker_id": 6,
  #   "winemaker_name": "The Wild Sax Band",
  #   "winemaker_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": "2035-04-15T20:00:00.000Z"
  # }]
  return render_template('pages/wines.html', wines=data)

@app.route('/wines/create')
# @requires_auth('post:wine')
def create_wines():
  # renders form. do not touch.
  form = WineForm()
  return render_template('forms/new_wine.html', form=form)

@app.route('/wines/create', methods=['POST'])
# @requires_auth('post:wine')
def create_show_submission():
  # called to create new wines in the db, upon submitting new wine listing form - done
  # TODO: insert form data as a new Wine record in the db, instead - done
  form = WineForm(request.form, meta={'csrf': False})
  if form.validate():
    try:
      wine = Wine(
        winemaker_id = form.winemaker_id.data,
        winery_id = form.winery_id.data,
        start_time = form.start_time.data
      )
      db.session.add(wine)
      db.session.commit()
      # on successful db insert, flash success - done
      flash('Wine of date: ' + request.form['start_time'] + ' was successfully listed!')
    except:
      # TODO: on unsuccessful db insert, flash an error instead. - done
      # e.g., flash('An error occurred. Wine ' + data.name + ' could not be listed.')
      # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
      error = True
      db.session.rollback()
      flash('An error occurred. Wine of date: ' + str(form.start_time.data) + ' could not be listed.')
      flash(f'{sys.exc_info()}')
    finally:
      db.session.close()
  else:
    messages = []
    for field, errors in form.errors.items():
      for error in errors:
        messages.append(field + ' : ' + error + '\n')
    flash('The Wine data is not valid. Please try again.')
    for message in messages:
      flash(message)
  return render_template('pages/home.html')


#  Update Wineries & Winemakers
#  ----------------------------------------------------------------
@app.route('/winemaker/<int:winemaker_id>/edit', methods=['GET'])
# @requires_auth('edit:winemaker')
def edit_winemaker(winemaker_id):
  winemaker = Winemaker.query.get(winemaker_id)
  form = WinemakerForm(obj=winemaker)

  # Alternative loading of data from line 735:
  # form.name.data = winemaker.name
  # form.state.data = winemaker.state
  # form.city.data = winemaker.city
  # form.phone.data = winemaker.phone
  # form.genres.data = winemaker.genres
  # form.facebook_link.data = winemaker.facebook_link

  winemaker={
    "id": winemaker.id,
    "name": winemaker.name,
    "genres": winemaker.genres,
    "city": winemaker.city,
    "state": winemaker.state,
    "phone": winemaker.phone,
    "website": winemaker.website,
    "facebook_link": winemaker.facebook_link,
    "seeking_winery": winemaker.seeking_winery,
    "seeking_description": winemaker.seeking_description,
    "image_link": winemaker.image_link
  }
  # TODO: populate form with fields from winemaker with ID <winemaker_id> - done
  return render_template('forms/edit_winemaker.html', form=form, winemaker=winemaker)

@app.route('/winemaker/<int:winemaker_id>/edit', methods=['POST', 'PATCH'])
# @requires_auth('edit:winemaker')
def edit_winemaker_submission(winemaker_id):
  # TODO: take values from the form submitted, and update existing
  # winemaker record with ID <winemaker_id> using the new attributes - done
  form_winemaker = WinemakerForm(request.form)
  db_winemaker = Winemaker.query.get(winemaker_id)
  error = False
  try:
    db_winemaker.name = form_winemaker.name.data
    db_winemaker.city = form_winemaker.city.data
    db_winemaker.state = form_winemaker.state.data
    db_winemaker.phone = form_winemaker.phone.data
    db_winemaker.genres = form_winemaker.genres.data
    db_winemaker.facebook_link = form_winemaker.facebook_link.data
    db.session.add(db_winemaker)
    db.session.commit()
  except ValueError as e:
    print(e)
    error = True
    db.session.rollback()
  finally:
    if not error:
      flash(f'Winemaker: {db_winemaker.name} was successfully updated!')
    else:
      flash('An error occurred. Winemaker could not be updated.')
    db.session.close()

  return redirect(url_for('show_winemaker', winemaker_id=winemaker_id))

@app.route('/wineries/<int:winery_id>/edit', methods=['GET'])
# @requires_auth('edit:winery')
def edit_winery(winery_id):
  winery = Winery.query.get(winery_id)
  form = WineryForm(obj=winery)
  # Alterntive loading of data from line 792:
  # form.name.data = winery.name
  # form.city.data = winery.city
  # form.state.data = winery.state
  # form.address.data = winery.address
  # form.phone.data = winery.phone
  # form.genres.data = winery.genres
  # form.facebook_link.data = winery.facebook_link
  # form.image_link.data = winery.image_link
  # form.website.data = winery.website
  # form.seeking_talent.data = winery.seeking_talent
  # form.seeking_description.data = winery.seeking_description

  winery={
    "id": winery.id,
    "name": winery.name,
    # "genres": winery.genres,
    # "city": winery.city,
    # "state": winery.state,
    # "address": winery.address,
    # "phone": winery.phone,
    # "website": winery.website,
    # "facebook_link": winery.facebook_link,
    # "seeking_talent": winery.seeking_talent,
    # "seeking_description": winery.seeking_description,
    # "image_link": winery.image_link
  }
  # TODO: populate form with values from winery with ID <winery_id> - done
  return render_template('forms/edit_winery.html', form=form, winery=winery)

@app.route('/wineries/<int:winery_id>/edit', methods=['POST', 'PATCH'])
# @requires_auth('edit:winery')
def edit_winery_submission(winery_id):
  # TODO: take values from the form submitted, and update existing - done
  # winery record with ID <winery_id> using the new attributes - done
  db_winery = Winery.query.get(winery_id)
  form_winery = WineryForm(request.form)
  error = False
  try:

    db_winery.name = form_winery.name.data
    db_winery.city = form_winery.city.data
    db_winery.state = form_winery.state.data
    db_winery.phone = form_winery.phone.data
    db_winery.genres = form_winery.genres.data
    db_winery.facebook_link = form_winery.facebook_link.data
    db_winery.image_link = form_winery.image_link.data
    db_winery.website = form_winery.website.data
    db_winery.seeking_talent = form_winery.seeking_talent.data
    db_winery.seeking_description = form_winery.seeking_description.data

    db.session.add(db_winery)
    db.session.commit()
  except ValueError as e:
    print(e)
    error = True
    db.session.rollback()
  finally:
    if not error:
      flash(f'Winery: {db_winery.name} was successfully updated!')
    else:
      flash('An error occurred. Winery could not be updated.')
    db.session.close()
  return redirect(url_for('show_winery', winery_id=winery_id))




#  Error Handlers
#  --------------------------------------------------------------- 
@app.errorhandler(400)
def bad_request_error(error):
    # optional error html display
    # return render_template('errors/400.html'), 400
    return jsonify({
      "success": False,
      "error": 400,
      "message": "Bad Request error 400"
    }), 400

@app.errorhandler(401)
def unauthorized_error(error):
    # optional error html display
    # return render_template('errors/401.html'), 401
    return jsonify({
      "success": False,
      "error": 401,
      "message": "Unauthorized error 401"
    }), 401

@app.errorhandler(403)
def forbidden_error(error):
    # optional error html display
    # return render_template('errors/403.html'), 403
    return jsonify({
      "success": False,
      "error": 403,
      "message": "Forbidden error 403"
    }), 403

@app.errorhandler(404)
def not_found_error(error):
    # optional error html display
    # return render_template('errors/404.html'), 404
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Not found error 404"
    }), 404

@app.errorhandler(500)
def internal_server_error(error):
    # optional error html display
    # return render_template('errors/500.html'), 500
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal server error 500"
    }), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
