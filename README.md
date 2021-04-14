# WinePort

## Introduction

WinePort is a winery and winemaker booking site that facilitates the discovery and bookings of wines between local winemakers and wineries. This site lets you list new winemakers and wineries, discover them, and list wines with winemakers as a winery owner.

### Motivation

The motivation for this project is to build a prototype to test the feasibility of a social platform that will bring online the interactions and flow of information for actors of the wine industry.

## Project Dependencies
### Backend
#### main dependencies:
* **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** 
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
* **python-jose-cryptodome** for decoding JWT's

You can download and install these and all other required dependencies using `pip` as:
```
pip install -r requirements.txt
```
> **Note** - If I do not mention the specific version of a package, then the default latest stable package will be installed. 

### Frontend
Fontend consists of html, css and `Jinja2` templating

## Project Structure
#### Main files
  ```sh
  |-- main
  |   ├── static
  |   │   ├── css 
  |   │   ├── font
  |   │   ├── ico
  |   │   ├── img
  |   │   └── js
  |   └── templates
  |   |   ├── errors
  |   |   ├── forms
  |   |   ├── layouts
  |   |   └── pages
  |   └── auth.py
  |   └── error.log
  |   └── run.py *** the main app. Includes SQLALchemy models
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── db_populate.py
  ├── forms.py *** All custom forms
  ├── README.md
  ├── requirements.txt *** The dependencies to install with `pip3 install -r requirements.txt`
  └── setup.sh *** environment variables 
  ```

Overall:
* Models are located in the `MODELS` section of `main/run.py`.
* Controllers are also located in `main/run.py`.
* The web frontend is located in `main/templates/`, which builds static assets deployed to the web server at `main/static/`.
* Web forms for creating data are located in `form.py`


Highlight folders:
* `main/templates/pages` -- Defines the pages that are rendered to the site. These templates render views based on data passed into the template’s view, in the controllers defined in `run.py`. These pages successfully represent the data to the user.
* `main/templates/layouts` -- Defines the layout that a page can be contained in to define footer and header code for a given page.
* `main/templates/forms` -- Defines the forms used to create new winemakers, wines, and wineries.
* `main/run.py` -- Defines routes that match the user’s URL, and controllers which handle data and renders views to the user. 
* Models in `main/run.py` -- Defines the data models that set up the database tables.
* `config.py` -- Stores configuration variables and instructions, separate from the main application code. 

## Local Development

### Running the development server
1. Create a virtual environment
2. Install project dependencies

```
pip install -r requirements.txt 
```

### Creating the Database
3. Create a new Postgres database in CLI
```
psql createdb <database_name>
```
4. Connect the database to the project by updating DATABASE_URL variable in `setup.sh`
5. Add environment variables to bash session
```
source setup.sh
```
6. Run database migrations to create schema on psql
```
python manage.py db upgrade
```

### Populating the Database
7. Populate the database
```
python db_populate.py
```

8. Run flask
```
flask run
```

## Hosting 
App is hosted in `Heroku` at:

[https://fsnd-capstone-wineport.herokuapp.com/](https://fsnd-capstone-wineport.herokuapp.com/) 


## API behavior and RBAC controls

| | User 1 | User 2 |
| ---  | --- | --- |
| Role | WinePort Manager | Winemaker |
| Permissions | delete:winery edit:wine edit:winemaker edit:winery post:wine post:winemaker post:winery | edit:wine post:wine |

## Valid JWT tokens for Code Review
User 1 token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9`

User 2 token:
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9`
