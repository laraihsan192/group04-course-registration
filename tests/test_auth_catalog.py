import tempfile
import unittest
from pathlib import Path

from src.app import create_app


class SignInAndCatalogTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        app = create_app(Path(folder.name) / "test.sqlite3")
        self.client = app.test_client()

    def sign_in(self):
        return self.client.post(
            "/", data={"username": "leen", "password": "demo-student"}
        )

    def test_valid_sign_in(self):
        self.assertEqual(self.sign_in().location, "/catalog")

    def test_invalid_sign_in(self):
        response = self.client.post("/", data={"username": "leen", "password": "wrong"})
        self.assertIn(b"Try again", response.data)
        self.assertEqual(self.client.get("/catalog").location, "/")

    def test_catalog_requires_sign_in(self):
        self.assertEqual(self.client.get("/catalog").location, "/")

    def test_search_by_name(self):
        self.sign_in()
        response = self.client.get("/catalog", query_string={"q": "data structures"})
        self.assertIn(b"CS201", response.data)
        self.assertNotIn(b"CS101", response.data)

    def test_search_by_code_and_section_details(self):
        self.sign_in()
        response = self.client.get("/catalog", query_string={"q": "cs201"})
        for expected in (b"Data Structures", b"<td>01</td>", b"<td>02</td>",
                         b"Sunday 10:00-11:15", b"Tuesday 10:00-11:15",
                         b"<td>8</td>", b"<td>0</td>"):
            self.assertIn(expected, response.data)

    def test_no_results(self):
        self.sign_in()
        response = self.client.get("/catalog", query_string={"q": "xyz"})
        self.assertIn(b"No matching courses", response.data)
