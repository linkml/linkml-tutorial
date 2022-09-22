

CREATE TABLE "Animal" (
	id TEXT NOT NULL, 
	name TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	species TEXT, 
	breed TEXT, 
	color TEXT, 
	weight_in_mgs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnimalCollection" (
	animals TEXT, 
	PRIMARY KEY (animals)
);

CREATE TABLE "Person" (
	name TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	primary_email TEXT, 
	vital_status VARCHAR(7) NOT NULL, 
	pets TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person_Collection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
