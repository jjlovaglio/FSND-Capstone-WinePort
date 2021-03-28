# flask-postgres-heroku-deploy-template
from Udacity's Full Stack Nano Degree deployment section

This is a working example of deployment of a Flask app + Postgres db with [heroku](https://dashboard.heroku.com)

## Installation

`$ brew install heroku <name-of-heroku-app>`

## Configure environment variables in [heroku](https://dashboard.heroku.com) dashboard

1. go to project settings 
2. click `Reveal Config Vars`
3. define variables as contained in *setup.sh* file

## Add git remote for Heroku to your local repository
`$ git remote add heroku <heroku-git-url>`

## Add postgresql add-on to your Heroku app
`$ heroku addons:create heroku-postgresql:hobby-dev --app <name-of-your-application>`

Run `heroku config --app name_of_your_application` in order to check your configuration variables in Heroku.  
You will see DATABASE_URL and the URL of the database you just created

## Push local project to Heroku
`git push heroku master`
if the previous command outputs an error, try `git push heroku HEAD:master`

## Run Migrations
Once your app is deployed, run migrations by running:  
`heroku run python manage.py db upgrade --app <name-of-your-application>`

### url of deployed app can be found on settings section of app in the [heroku](https://dashboard.heroku.com) dashboard
