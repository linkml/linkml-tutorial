

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
	entries TEXT, 
	animals TEXT, 
	PRIMARY KEY (entries, animals)
);

CREATE TABLE "Collection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	primary_email TEXT, 
	vital_status TEXT NOT NULL, 
	pets TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PersonCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
