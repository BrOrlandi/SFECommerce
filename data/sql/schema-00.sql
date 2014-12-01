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

DROP TABLE IF EXISTS sfec_address;
CREATE TABLE sfec_address(
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
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS sfec_product;
CREATE TABLE sfec_product(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER NOT NULL,
    description TEXT NOT NULL,
    price TEXT NOT NULL,
    is_available INTEGER
);

DROP TABLE IF EXISTS sfec_category_product;
CREATE TABLE sfec_category_product(
    category_id INTEGER,
    product_id INTEGER,
    PRIMARY KEY (category_id,product_id)
);

DROP VIEW IF EXISTS sfec_admin_view;
CREATE VIEW sfec_admin_view AS
SELECT * FROM sfec_admin a
JOIN sfec_user u ON a.id = u.id;

DROP VIEW IF EXISTS sfec_vendor_view;
CREATE VIEW sfec_vendor_view AS
SELECT * FROM sfec_vendor v
JOIN sfec_user u ON v.id = u.id;

DROP VIEW IF EXISTS sfec_customer_view;
CREATE VIEW sfec_customer_view AS
SELECT * FROM sfec_customer c
JOIN sfec_user u ON c.id = u.id;

DROP TABLE IF EXISTS sfec_customer_service;
CREATE TABLE sfec_customer_service(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES sfec_order(id),
    customer_id INTEGER NOT NULL REFERENCES sfec_customer(id),
    vendor_id INTEGER NOT NULL REFERENCES sfec_vendor(id)
);

DROP TABLE IF EXISTS sfec_cart;
CREATE TABLE sfec_cart(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES sfec_order(id),
    user_id INTEGER NOT NULL REFERENCES sfec_user(id),
    UNIQUE(user_id)
);

DROP TABLE IF EXISTS sfec_order;
CREATE TABLE sfec_order(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES sfec_user(id),
    status TEXT NOT NULL
);

DROP TABLE IF EXISTS sfec_order_product;
CREATE TABLE sfec_order_product(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    quantity INTEGER NOT NULL,
    order_id INTEGER NOT NULL REFERENCES sfec_order(id),
    product_id INTEGER NOT NULL REFERENCES sfec_product(id),
    UNIQUE(order_id, product_id) ON CONFLICT REPLACE -- Previnir que um produto seja adicionado mais de uma vez a um mesmo pedido.
);
