CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER, 
    visible INTEGER
);
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    device_type TEXT,
    model TEXT,
    desription TEXT
    visible INTEGER
);
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
    visible INTEGER
);
CREATE TABLE rents (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers,
    device_id INTEGER REFERENCES devices,
    start_day DATE,
    end_day DATE
    visible INTEGER
);
