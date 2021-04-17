import unittest
import json
from models import setup_db
from run import app


class ResourceTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "wineport_test_db"
        self.database_path = "postgresql://{}/{}".format('localhost', self.database_name)
        setup_db(self.app, self.database_path)
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)



# make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()