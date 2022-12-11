import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_index(self):
        response = requests.get("http://127.0.0.1:5000/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h1>The Lightweight Task-Tracking Software!</h1>' in response.text, True)

    def test_notes(self):
        response = requests.get("http://127.0.0.1:5000/notes")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        #self.assertEqual('Date' in response.text, True)
       
    def test_note(self):
        response = requests.get("http://127.0.0.1:5000/notes/2")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        #self.assertEqual('Comment' in response.text, True)

    def test_new(self):
        response = requests.get("http://127.0.0.1:5000/notes/new")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        #self.assertEqual('<form action="new" method="post">' in response.text, True)

    def test_delete(self):
        response = requests.get('http://127.0.0.1:5000/notes/delete')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_users(self):
        response = requests.get('http://127.0.0.1:5000/users')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_profile(self):
        response = requests.get('http://127.0.0.1:5000/profile')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_bugreport(self):
        response = requests.get('http://127.0.0.1:5000/form')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        

if __name__ == "__main__":
    unittest.main()
