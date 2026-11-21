import os
import secrets
import sqlite3
from pathlib import Path

from flask import Flask, redirect, render_template_string, request, session, url_for

DEMO_USER = "leen"
DEMO_PASSWORD = "demo-student"

PAGE = """
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Course Registration</title>
<h1>University Course Registration System</h1>
{% if login %}
  <h2>Demo student sign-in</h2>
  {% if error %}<p role="alert">{{ error }}</p>{% endif %}
  <form method="post">
    <label>Username <input name="username" required></label>
    <label>Password <input name="password" type="password" required></label>
    <button type="submit">Sign in</button>
  </form>
{% else %}
  <h2>Course catalog</h2>
  <form method="get">
    <label>Course name or code <input name="q" value="{{ query }}"></label>
    <button type="submit">Search</button>
  </form>
  {% if sections %}
    <table>
      <thead><tr><th>Code</th><th>Course</th><th>Section</th>
      <th>Meeting time</th><th>Available seats</th></tr></thead>
      <tbody>
      {% for section in sections %}
        <tr><td>{{ section.code }}</td><td>{{ section.name }}</td>
        <td>{{ section.number }}</td><td>{{ section.meetings }}</td>
        <td>{{ section.seats }}</td></tr>
      {% endfor %}
      </tbody>
    </table>
  {% else %}<p>No matching courses.</p>{% endif %}
{% endif %}
</html>
"""

SCHEMA = """
CREATE TABLE IF NOT EXISTS course (code TEXT PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS section (
    id INTEGER PRIMARY KEY, code TEXT NOT NULL REFERENCES course(code),
    number TEXT NOT NULL, capacity INTEGER NOT NULL, sample_enrolled INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS meeting_time (
    id INTEGER PRIMARY KEY, section_id INTEGER NOT NULL REFERENCES section(id),
    day TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL
);
INSERT OR IGNORE INTO course VALUES
    ('CS201', 'Data Structures'), ('CS101', 'Programming I');
INSERT OR IGNORE INTO section VALUES
    (1, 'CS201', '01', 30, 22), (2, 'CS201', '02', 30, 30),
    (3, 'CS101', '01', 25, 15);
INSERT OR IGNORE INTO meeting_time VALUES
    (1, 1, 'Sunday', '10:00', '11:15'),
    (2, 1, 'Tuesday', '10:00', '11:15'),
    (3, 2, 'Monday', '12:00', '13:15'),
    (4, 3, 'Wednesday', '09:00', '10:15');
"""

SEARCH = """
SELECT c.code, c.name, s.number,
       GROUP_CONCAT(m.day || ' ' || m.start_time || '-' || m.end_time, ', ') AS meetings,
       s.capacity - s.sample_enrolled AS seats
FROM course AS c
JOIN section AS s ON s.code = c.code
JOIN meeting_time AS m ON m.section_id = s.id
WHERE INSTR(LOWER(c.name), LOWER(?)) > 0
   OR INSTR(LOWER(c.code), LOWER(?)) > 0
GROUP BY c.code, c.name, s.id, s.number, s.capacity, s.sample_enrolled
ORDER BY c.code, s.number
"""


def create_app(database=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("COURSE_APP_SECRET") or secrets.token_hex(32)
    if database is None:
        Path(app.instance_path).mkdir(parents=True, exist_ok=True)
        database = Path(app.instance_path) / "catalog.sqlite3"

    with sqlite3.connect(database) as connection:
        connection.executescript(SCHEMA)

    @app.route("/", methods=["GET", "POST"])
    def sign_in():
        error = None
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            if username == DEMO_USER and password == DEMO_PASSWORD:
                session.clear()
                session["student"] = DEMO_USER
                return redirect(url_for("catalog"))
            error = "Incorrect username or password. Try again."
        return render_template_string(PAGE, login=True, error=error)

    @app.get("/catalog")
    def catalog():
        if session.get("student") != DEMO_USER:
            return redirect(url_for("sign_in"))
        query = request.args.get("q", "").strip()
        with sqlite3.connect(database) as connection:
            connection.row_factory = sqlite3.Row
            sections = connection.execute(SEARCH, (query, query)).fetchall()
        return render_template_string(PAGE, login=False, query=query, sections=sections)

    return app
