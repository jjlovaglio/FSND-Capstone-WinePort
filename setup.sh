
# Database Paths
export DATABASE_URL="postgres://localhost/wineport_dev_db"
echo "DATABASE_URL: "$DATABASE_URL
export TEST_DATABASE_URL="postgresql://localhost/wineport_test_db"
echo "TEST_DATABASE_URL: "$TEST_DATABASE_URL

# Auth0 JWT for user 1 and 2 used in tests.py
export USER_1_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9.eyJpc3MiOiJodHRwczovL2pqbG92YWdsaW8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMmE3YzQxNWVhZTg2MDA2OGU0MjUwMSIsImF1ZCI6IndpbmVwb3J0IiwiaWF0IjoxNjE4OTYwOTgwLCJleHAiOjE2MTkwNDczODAsImF6cCI6IjZGRGpZWHpxNEVzUzJ0NVpWQ1Y3YXJFWnVDMHEwSFBFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6d2luZXJ5IiwiZWRpdDp3aW5lIiwiZWRpdDp3aW5lbWFrZXIiLCJlZGl0OndpbmVyeSIsInBvc3Q6d2luZSIsInBvc3Q6d2luZW1ha2VyIiwicG9zdDp3aW5lcnkiXX0.NdzD3aK0es3OT-_2vyFneJ0HeJsJi8Icx1xP8rAL2C4bGFYJBZuh0rgYKQt726yHGGhYNp7tssp_c8wBITUxxxVU3ZzhzADrwDcWU0a8xnhUzNHwOIjtPSSm6j9hDRvcAn3s0BONwsY6ent7LUgd1LCbd_FNtXmKWEFJcvuXQ1bsmxy2-pZi-GT4VkqZf8TFdNlQyVbTsYkQZlWXIv2wqXKIDGZaIK_eYZtkrEraeXabzpnueQIS5UxiFJJWPpTbyRcbYQmjAbN1KCRtskHHAcvNFBlWtHQHyn_wKJGqLzD-jm9pXm0UhTGYartz-flw91YQdpuIzQDZcgl7uHmB-g"
echo "USER_1_TOKEN: "$USER_1_TOKEN
export USER_2_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExcTh6NHhFay1zSjJ0WnpXa3A2aSJ9.eyJpc3MiOiJodHRwczovL2pqbG92YWdsaW8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMmE3YzZhNWVhZTg2MDA2OGU0MjUwYyIsImF1ZCI6IndpbmVwb3J0IiwiaWF0IjoxNjE4OTYyMDk5LCJleHAiOjE2MTkwNDg0OTksImF6cCI6IjZGRGpZWHpxNEVzUzJ0NVpWQ1Y3YXJFWnVDMHEwSFBFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJlZGl0OndpbmUiLCJwb3N0OndpbmUiXX0.aOf1gSc7qU8uu9hu4OyuhiG8HkKK2Hb_CTZp86xMVVokfsQJjJXZO3ebR4BGPL6FeZ5Uk8Ixqk7yDSn8jq3t0vvWzYm1Q7wQlBJv0kN353wYhkROE2vHsSf_zxpVKdg5GfVPSvYR-t9IY8hLoJwAdnfYJc0ET-6QGeC5i9vUSmaYr76-yWOimAqL2hg-CvaLiku-mubo-Oh4UWX8J4W_pRwc1GBYxQ2VG9CIC2FKutQNtAgDvDkoh7TnN-gNa5MEP_-n60-V67oFrla0e9kVPwQ2oUUIVRNYrId5i4ROj-XLASY3gQwhf63wYbk17ZXzwOOQRZwfsOCQFCsJ-hPmCg"
echo "USER_2_TOKEN: "$USER_2_TOKEN
# set env to Development
export APP_SETTINGS="config.ProductionConfig"
# export APP_SETTINGS="config.TestingConfig"
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