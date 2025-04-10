PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT
);

CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    creation_timestamp INTEGER,
    completion_timestamp NTEGER,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
