CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN DEFAULT TRUE, 
    visible INTEGER DEFAULT 1
);
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    device_type TEXT NOT NULL,
    model TEXT NOT NULL,
    description TEXT,
    visible INTEGER DEFAULT 1
);
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    visible INTEGER DEFAULT 1
);
CREATE TABLE rents (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers NOT NULL,
    device_id INTEGER REFERENCES devices NOT NULL,
    start_day DATE NOT NULL,
    end_day DATE NOT NULL,
    visible INTEGER DEFAULT 1
);
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices NOT NULL,
    service_date DATE NOT NULL,
    description TEXT,
    visible INTEGER DEFAULT 1
); 
