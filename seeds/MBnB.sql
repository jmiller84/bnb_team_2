DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(6,2),
    user_id int,
    constraint fk_user foreign key (user_id)
    references users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT,
    space_id INT,
    date DATE,
    constraint fk_user foreign key (user_id)
    references users(id) ON DELETE CASCADE,
    constraint fk_space foreign key (space_id)
    references spaces(id) ON DELETE CASCADE
);

INSERT INTO users (username, password) VALUES ('topdev', 'makers456!');
INSERT INTO users (username, password) VALUES ('pikachu82', 'thunderbolt*');
INSERT INTO users (username, password) VALUES ('boardgameking', 'catan1234!');
INSERT INTO users (username, password) VALUES ('yogaguru', 'downwarddog!');

INSERT INTO spaces (name, description, price, user_id) VALUES ('Cottage', 'A nice cottage', 27.50, 4);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Villa', 'A mediterranean villa with a sea view', 70.00, 2);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Alpine lodge', 'A cosy ski lodge with wood-burning fire', 95.00, 1);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Studio Apartment', 'A cool apartment in the centre of the bustling city', 102.00, 3);
INSERT INTO spaces (name, description, price, user_id) VALUES ('Tent', 'A tent in a field of cows', 10.00, 2);

INSERT INTO bookings (user_id, space_id, date) VALUES (1, 1, '2023-10-30');
INSERT INTO bookings (user_id, space_id, date) VALUES (2, 1, '2023-09-25');
INSERT INTO bookings (user_id, space_id, date) VALUES (2, 3, '2023-10-10');
INSERT INTO bookings (user_id, space_id, date) VALUES (3, 1, '2023-09-06');
INSERT INTO bookings (user_id, space_id, date) VALUES (1, 2, '2023-10-07');
INSERT INTO bookings (user_id, space_id, date) VALUES (4, 2, '2023-09-15');

