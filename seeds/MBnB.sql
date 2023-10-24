DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(6,2)
);

INSERT INTO spaces (name, description, price) VALUES ('Cottage', 'A nice cottage', 27.50);
INSERT INTO spaces (name, description, price) VALUES ('Villa', 'A mediterranean villa with a sea view', 70.00);
INSERT INTO spaces (name, description, price) VALUES ('Alpine lodge', 'A cosy ski lodge with wood-burning fire', 95.00);