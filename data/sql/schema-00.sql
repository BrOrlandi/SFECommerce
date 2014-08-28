CREATE TABLE sfec_user(
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL UNIQUE,
    password text NOT NULL,
    birth_date date,
    register_date date NOT NULL,
    type int
);

CREATE TABLE scef_address(
    state text NOT NULL,
    city text NOT NULL,
    address text NOT NULL,
    zip text NOT NULL,
    user_id bigint NOT NULL REFERENCES sfec_user(id)
);

CREATE TABLE sfec_customer(
    id bigint NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

CREATE TABLE sfec_vendor(
    id bigint NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

CREATE TABLE sfec_admin(
    id bigint NOT NULL REFERENCES sfec_user(id) PRIMARY KEY
);

CREATE TABLE sfec_category(
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    description text
);

CREATE TABLE sfec_product(
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    stock int NOT NULL,
    description text NOT NULL,
    price float NOT NULL,
    is_available boolean,
    category_id bigint NOT NULL REFERENCES sfec_category(id)
);
