

CREATE TABLE "NamedThing" (
	id TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id, name, description)
);

CREATE TABLE "Person" (
	id TEXT, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	birth_date TEXT, 
	age_in_years TEXT, 
	vital_status TEXT, 
	PRIMARY KEY (id, name, description, primary_email, birth_date, age_in_years, vital_status)
);

CREATE TABLE "PersonCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
