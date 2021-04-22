dropdb wineport_dev_db && createdb wineport_dev_db
python manage.py db upgrade
python db_populate.py