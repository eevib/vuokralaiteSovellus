CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER, 
    visible INTEGER
);

