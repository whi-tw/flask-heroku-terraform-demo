from myapp import app
import unittest

class appTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello_world(self):
        rv = self.app.get("/")
        assert b"Hello, World!" in rv.data
    
    def test_test(self):
        rv = self.app.get("/test")
        assert b"This is a test" in rv.data
    
    def test_name(self):
        rv = self.app.get("/hello/potato")
        assert b"Hello, potato!" in rv.data

if __name__ == '__main__':
    unittest.main()
