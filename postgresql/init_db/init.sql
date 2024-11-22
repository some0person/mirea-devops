CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR NOT NULL,
    product_price REAL NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP NOT NULL);