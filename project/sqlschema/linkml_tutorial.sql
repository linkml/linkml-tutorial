

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	primary_email TEXT, 
	vital_status TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person_Collection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "Animal" (
	id TEXT NOT NULL, 
	name TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	species TEXT, 
	breed TEXT, 
	color TEXT, 
	weight_in_mgs TEXT, 
	"Person_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
