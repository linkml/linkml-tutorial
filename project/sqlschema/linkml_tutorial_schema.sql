

CREATE TABLE "Animal" (
	id TEXT NOT NULL, 
	name TEXT, 
	species TEXT, 
	breed TEXT, 
	color TEXT, 
	weight_in_mgs INTEGER, 
	age_in_years INTEGER, 
	birth_date DATE, 
	PRIMARY KEY (id, name, species, breed, color, weight_in_mgs, age_in_years, birth_date)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	primary_email TEXT, 
	vital_status TEXT NOT NULL, 
	age_in_years INTEGER, 
	birth_date DATE, 
	pets TEXT, 
	PRIMARY KEY (id, name, primary_email, vital_status, age_in_years, birth_date, pets)
);
