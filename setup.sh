
# Auth0 JWT for user 1 and 2 used in tests.py
export USER_1_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9.eyJpc3MiOiJodHRwczovL2pqbG92YWdsaW8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMmE3YzQxNWVhZTg2MDA2OGU0MjUwMSIsImF1ZCI6IndpbmVwb3J0IiwiaWF0IjoxNjE4ODU1Njk1LCJleHAiOjE2MTg5NDIwOTUsImF6cCI6IjZGRGpZWHpxNEVzUzJ0NVpWQ1Y3YXJFWnVDMHEwSFBFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6d2luZXJ5IiwiZWRpdDp3aW5lIiwiZWRpdDp3aW5lbWFrZXIiLCJlZGl0OndpbmVyeSIsInBvc3Q6d2luZSIsInBvc3Q6d2luZW1ha2VyIiwicG9zdDp3aW5lcnkiXX0.l_GNQzxejvt1wYPOtkatHOwBdINpqt9fCnnP_9nJAHQ6YY9joxOOJGrNnQ6c15ktspEa6ARFDquDQcK0xUVCLFlFO6OPDUOPtMO3p9Lsvu5vksB053zHX5RyeiM3TGeJqF5Cigzun3q-87VD-OqqaFi4eF6_HL99MKLwA5xakBmW2InAOK8AWM8rs3XdLYo7fLDiKSw38HNwxd44S3tbyXQ6zuFg934vjAho4GfhslHCZsDWxeycFvRHY8XfxTH0RTw-guRUonB6Hvsx0Mm7s7t4WfkJ1Ii1IRgYe_PMV2RyNQ1-WgyvS5pgyhlfkgJ1j_OTyrqMxM9CQWcxAPmVvA"
echo "USER_1_TOKEN: "$USER_1_TOKEN
export USER_2_TOKEN=""
echo "USER_2_TOKEN: "$USER_2_TOKEN
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

export FLASK_APP="run.py"
echo "Flask app set to: "$FLASK_APP


# The JWT code signing secret
export AUTH0_CLIENT_SECRET="ciSUBukBySmpp-D_HuJW3JXSIRG-hJfdJsweOGXn-HMVFVlH7lBhopIA8K9BYXZx"
echo "Auth0 secret set to: "$AUTH0_CLIENT_SECRET

# run with $ source setup.sh