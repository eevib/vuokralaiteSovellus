CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER, 
    visible INTEGER
);
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    type TEXT,
    model TEXT,
    desription TEXT
);
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);
