# set env to Development
# export APP_SETTINGS="config.DevelopmentConfig"
export APP_SETTINGS="config.TestingConfig"
echo "APP_SETTINGS set to: "$APP_SETTINGS
# The Auth0 callback url
export AUTH0_CALLBACK_URL="http://127.0.0.1:5000/callback-url"
echo "Auth0 callback url set to: "$AUTH0_CALLBACK_URL
# The Auth0 JWT api audience
export AUTH0_JWT_API_AUDIENCE="wineport"
echo "Auth0 jwt api audience set to: "$AUTH0_JWT_API_AUDIENCE
# The Auth0 Domain Name
export AUTH0_DOMAIN="jjlovaglio.us.auth0.com"
echo "Auth0 domain set to: "$AUTH0_DOMAIN
# The Auth0 clent ID
export AUTH0_CLIENT_ID="6FDjYXzq4EsS2t5ZVCV7arEZuC0q0HPE"
echo "Auth0 client ID set to: "$AUTH0_CLIENT_ID
# local database used
# export DATABASE_URL="postgresql://localhost/fsndcapstoneherokutest"
export DATABASE_URL="postgresql://localhost/db_populate_v1"
echo "Local Database URL set to:"$DATABASE_URL
export FLASK_APP="run.py"
echo "Flask app set to: "$FLASK_APP
export FLASK_ENV=development
echo "Environment mode set to: "$FLASK_ENV

# run with $ source setup.sh