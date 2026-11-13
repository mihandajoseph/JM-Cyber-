-- Lab seed data. Everything here is FAKE and for local training only.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,   -- plaintext ON PURPOSE (this is a vuln lab)
    role     TEXT NOT NULL
);

-- The first row is admin; a SQL-injection login bypass returns it first.
INSERT INTO users (username, password, role) VALUES
    ('admin', 'S3cr3t-Admin-Pw!', 'admin'),
    ('alice', 'password123',      'user');

DROP TABLE IF EXISTS flags;
CREATE TABLE flags (
    name  TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

INSERT INTO flags (name, value) VALUES
    ('front-door', 'flag{sql_1nj3ct10n_0p3n3d_th3_d00r}');
