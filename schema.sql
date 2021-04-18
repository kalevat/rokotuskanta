CREATE TABLE place (
	id SERIAL PRIMARY KEY,
	placename TEXT UNIQUE
);
INSERT INTO place (placename) VALUES ('Helsinki'),('Turku'),('Vantaa');

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	rights INT
);

CREATE TABLE vaccination (
	id SERIAL PRIMARY KEY,
	vacc INT,
	date TIMESTAMP,
	vacc_id INT,
	place_id INTEGER REFERENCES place,
	user_id INTEGER REFERENCES users
);

CREATE TABLE rights (
	id SERIAL PRIMARY KEY,
	description TEXT
);

CREATE TABLE vaccine (
	id SERIAL PRIMARY KEY,
	vaccname TEXT
);

INSERT INTO vaccine (vaccname) VALUES ('Pfizer'), ('Johnson&Johnson'), ('Moderna'), ('AstraZeneca'), ('Sputnik');
