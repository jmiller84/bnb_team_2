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
    area VARCHAR(255),
    country VARCHAR(255),
    description VARCHAR(255),
    price int,
    host_id int,
    constraint fk_user foreign key (host_id)
    references users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT,
    space_id INT,
    date DATE,
    confirmed BOOLEAN,
    constraint fk_user foreign key (user_id)
    references users(id) ON DELETE CASCADE,
    constraint fk_space foreign key (space_id)
    references spaces(id) ON DELETE CASCADE
);

INSERT INTO users (username, password) VALUES ('topdev', 'makers456!');
INSERT INTO users (username, password) VALUES ('pikachu82', 'thunderbolt*');
INSERT INTO users (username, password) VALUES ('boardgameking', 'catan1234!');
INSERT INTO users (username, password) VALUES ('yogaguru', 'downwarddog!');

INSERT INTO spaces (name, area, country, description, price, host_id) VALUES ('Cottage', 'Wimborne', 'UK', 'A nice cottage', 27, 4);
INSERT INTO spaces (name, area, country, description, price, host_id) VALUES ('Villa', 'Nice', 'France', 'A mediterranean villa with a sea view', 70, 2);
INSERT INTO spaces (name, area, country, description, price, host_id) VALUES ('Alpine lodge', 'Brig-Glis', 'Switzerland', 'A cosy ski lodge with wood-burning fire', 95, 1);
INSERT INTO spaces (name, area, country, description, price, host_id) VALUES ('Studio Apartment', 'New York', 'USA', 'A cool apartment in the centre of the bustling city', 102, 3);
INSERT INTO spaces (name, area, country, description, price, host_id) VALUES ('Tent', 'Tenby', 'UK', 'A tent in a field of cows', 10, 2);

INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (1, 1, '2023-10-30', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (2, 1, '2023-10-25', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (2, 3, '2023-10-10', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (3, 1, '2023-10-06', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (1, 2, '2023-10-07', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (4, 2, '2023-10-15', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (4, 3, '2023-10-12', False);

