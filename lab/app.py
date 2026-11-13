"""
JM Cyber lab — Challenge 1: "Front Door".

A deliberately-vulnerable login app. Binds to 127.0.0.1 ONLY.
Do not expose this to a network you don't fully control.
"""

import os
import sqlite3

from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lab.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

app = Flask(__name__)
# Fine for a local lab; never reuse a hardcoded key in a real app.
app.secret_key = "jm-cyber-lab-dev-key"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create the database from schema.sql on first run."""
    fresh = not os.path.exists(DB_PATH)
    if fresh:
        db = sqlite3.connect(DB_PATH)
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            db.executescript(f.read())
        db.commit()
        db.close()


@app.route("/")
def index():
    if session.get("user"):
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # VULN: user input is concatenated straight into the SQL string.
        # Entering  ' OR '1'='1' --  as the username bypasses the password
        # check and returns the first row (admin). The fix is parameterized
        # queries: db.execute("... WHERE username=? AND password=?", (u, p)).
        query = (
            "SELECT * FROM users "
            f"WHERE username = '{username}' AND password = '{password}'"
        )

        try:
            row = get_db().execute(query).fetchone()
        except sqlite3.Error as exc:
            # Leaking the DB error is itself a lesson for a later challenge.
            error = f"SQL error: {exc}"
            row = None

        if row:
            session["user"] = row["username"]
            session["role"] = row["role"]
            return redirect(url_for("dashboard"))
        if error is None:
            error = "Invalid credentials."

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if not session.get("user"):
        return redirect(url_for("login"))

    flag = None
    if session.get("role") == "admin":
        flag = get_db().execute(
            "SELECT value FROM flags WHERE name = 'front-door'"
        ).fetchone()["value"]

    return render_template(
        "dashboard.html",
        user=session.get("user"),
        role=session.get("role"),
        flag=flag,
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    # 127.0.0.1 only — this app is intentionally vulnerable.
    app.run(host="127.0.0.1", port=5000, debug=True)
