DROP TABLE IF EXISTS sfec_user;
CREATE TABLE sfec_user(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    birth_date INTEGER,
    register_date INTEGER NOT NULL,
    type INTEGER
);

DROP TABLE IF EXISTS scef_address;
CREATE TABLE scef_address(
    state TEXT NOT NULL,
    city TEXT NOT NULL,
    address TEXT NOT NULL,
    zip TEXT NOT NULL,
    user_id INTEGER NOT NULL REFERENCES sfec_user(id)
);

DROP TABLE IF EXISTS sfec_customer;
CREATE TABLE sfec_customer(
    id INTEGER NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

DROP TABLE IF EXISTS sfec_vendor;
CREATE TABLE sfec_vendor(
    id INTEGER NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

DROP TABLE IF EXISTS sfec_admin;
CREATE TABLE sfec_admin(
    id INTEGER NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

DROP TABLE IF EXISTS sfec_category;
CREATE TABLE sfec_category(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

DROP TABLE IF EXISTS sfec_product;
CREATE TABLE sfec_product(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    is_available INTEGER,
    category_id INTEGER NOT NULL REFERENCES sfec_category(id)
);
