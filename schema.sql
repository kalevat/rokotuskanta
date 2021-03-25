CREATE TABLE place (
	id SERIAL PRIMARY KEY,
	placename TEXT
);
INSERT INTO place (placename) VALUES ('Helsinki'),('Turku'),('Vantaa');
CREATE TABLE vaccination (
	id SERIAL PRIMARY KEY,
	vacc INT,
	date TIMESTAMP,
	place_id INTEGER REFERENCES place
);
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	rights INT,
	vaccination_id INTEGER REFERENCES vaccination
);
