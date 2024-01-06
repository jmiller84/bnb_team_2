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
    image_url VARCHAR(255),
    max_guests int,
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

INSERT INTO users (username, password) VALUES ('WillPat', 'makers456!');
INSERT INTO users (username, password) VALUES ('KatyP82', 'thunderbolt*');
INSERT INTO users (username, password) VALUES ('TomR', 'catan1234!');
INSERT INTO users (username, password) VALUES ('BusyLizzie', 'downwarddog!');

INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES ('Cottage', 'Wimborne', 'UK', 'This chocolate box 16th Century Grade II listed cottage is Full of the character you would expect from such an old property yet with just the right degree of up-dating to give you a comfortable stay: the perfect country retreat', 27, 4, 'images/cottage.jpeg', 6);
INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES ('Villa', 'Nice', 'France', 'In the heart of local life, this charming villa has superb panoramic views of the sea. You have the beach within easy reach, but are not too far away from the city to enjoy all the amenities Nice has to offer.', 70, 2, 'images/mediterraneanVilla.jpeg', 5);
INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES ('Alpine lodge', 'Brig-Glis', 'Switzerland', 'Welcome to our lovely cosy chalet. We are located in a quiet car free village, only reachable by cablecar. Enjoy an incredible view of stunning mountains from your bedroom. Perfect for hiking, skiing and relaxing.', 95, 1, 'images/snowyCabin.jpeg', 6);
INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES ('Studio Apartment', 'New York', 'USA', 'Luxury 1 Bedroom in the heart of NYC! Central to all shopping, restaurants, and attractions. Highrise Apartment with Floor to Ceiling windows provide a breathtaking view of the River and Skyline', 102, 2, 'images/studioApartment.jpeg', 2);
INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES ('Tent', 'Tenby', 'UK', 'A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants.', 50, 2, 'images/tent.jpeg', 4);

INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (1, 1, '2024-01-30', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (2, 1, '2024-01-25', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (2, 3, '2024-01-10', True);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (3, 1, '2024-01-06', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (1, 2, '2024-01-07', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (4, 2, '2024-01-15', False);
INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (4, 3, '2024-01-12', False);