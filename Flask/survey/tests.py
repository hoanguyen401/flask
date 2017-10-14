import unittest
from bs4 import BeautifulSoup
import requests
from survey import app,db
from survey.models import Question

class TestApp(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()
        
    def defaultTest(self):
        q = Question("abcacb")
        db.session.add(q)
        db.session.commit()
        self.assertEqual(q.nu_maybe, 0)
        self.assertEqual(q.nu_no,0)
        self.assertEqual(q.nu_yes,0)
        
    def test_title(self):
        title = "Flask example - survey" 
        response = requests.get('http://1270.0.0.1:5000')
        soup = BeautifulSoup(response.text)
        self.assertEqual(soup.title.getText(), title)
        