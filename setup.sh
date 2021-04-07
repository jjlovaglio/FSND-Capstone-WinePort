export DATABASE_URL="postgresql://localhost/fsndcapstoneherokutest"
export FLASK_APP=run
export FLASK_ENV=development
echo "Database URL set to:"$DATABASE_URL
echo "Flask app set to: "$FLASK_APP
echo "Environment mode set to: "$FLASK_ENV

# run with $ source setup.sh