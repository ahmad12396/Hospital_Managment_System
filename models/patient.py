CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    age INTEGER,
    gender TEXT,
    blood_group TEXT
);

print("hello")