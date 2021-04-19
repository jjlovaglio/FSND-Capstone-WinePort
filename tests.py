from os import environ as env
import unittest
import json
from models import setup_db
from run import app, generate_auth_url
from flask_sqlalchemy import SQLAlchemy

class WinePortTestCase(unittest.TestCase):
    """This class represents the WinePort test case.
       in order to run it, the psql testing database, environment
       variables and db_populate.py (database seeding) 
       need to be setup correctly as per README.md 
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.token1 = env["USER_1_TOKEN"]

        self.app = app
        self.client = self.app.test_client
        self.database_name = "wineport_test_db"
        self.database_path = "postgresql://{}/{}".format('localhost', self.database_name)
        setup_db(self.app, self.database_path)
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    # begin RBAC tests
    def test_Winemaker_Role_has_all_permissions(self):
        """ If token 1 is current, assert success 200
        """
        headers = {
            "Authorization": self.token1
        }
        res = self.client().get('/')
    
    def test_Manager_Role_has_all_permissions(self):
        pass

    # end RBAC tests
    def test_index_success_200(self):
        """Test index endpoint for success"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_index_failure_error_405(self):
        """ Test index for failure by sending a post request"""
        res = self.client().post('/')
        self.assertEqual(res.status_code,405)

    def test_wineries_success_200(self):
        res = self.client().get('/wineries')
        self.assertIn(b'Tupungato, Mendoza', res.data)

    def test_wineries_failure_405(self):
        res = self.client().post('/wineries')
        self.assertEqual(res.status_code, 405)

    def test_search_wineries_success_200(self):
        res = self.client().post('/wineries/search')
        self.assertIn(b'Vaglio Wines', res.data)

    def test_search_wineries_failure_405(self):
        res = self.client().get('/wineries/search')
        self.assertEqual(res.status_code, 405)

    def test_show_winery_success_200(self):
        res = self.client().get('/wineries/1')
        self.assertEqual(res.status_code, 200)

    def test_show_winery_failure_405(self):
        res = self.client().post('/wineries/1')
        self.assertEqual(res.status_code,405)

    def test_create_winery_success_200(self):
        headers = {
            "Authorization": self.token1
        }
        res = self.client().get('/wineries/create', headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_create_winery_submission_success_200(self):
        pass

    def test_create_winery_submission_failure(self):
        pass

    def test_delete_winery_success_200(self):
        pass

    def test_delete_winery_failure(self):
        pass

    def test_winemakers_success_200(self):
        pass

    def test_winemakers_failure_405(self):
        pass

    def test_search_winemakers_success_200(self):
        pass

    def test_search_winemakers_failure_405(self):
        pass

    def test_show_winemaker_success_200(self):
        pass

    def test_show_winemaker_failure_405(self):
        pass

    def test_create_winemaker_form_success_200(self):
        pass

    def test_create_winemaker_form_failure(self):
        pass

    def test_create_winemaker_submission_success_200(self):
        pass

    def test_create_winemaker_submission_failure(self):
        pass

    def test_wines_success_200(self):
        pass

    def test_wines_failure(self):
        pass

    def test_create_wines_success_200(self):
        pass

    def test_create_wines_failure(self):
        pass

    def test_create_show_submission_success_200(self):
        pass

    def test_crate_show_submission_failure(self):
        pass

    def edit_winemaker_success_200(self):
        pass

    def edit_winemaker_failure(self):
        pass

    def edit_winemaker_submission_success_200(self):
        pass

    def edit_winemaker_submission_failure(self):
        pass

    def edit_winery_success_200(self):
        pass

    def edit_winery_failure(self):
        pass

    def edit_winery_submission_success(self):
        pass

    def edit_winery_submission_failure(self):
        pass

    # 38 tests!

# make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()