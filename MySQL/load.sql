DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS org;
DROP TABLE IF EXISTS award;
DROP TABLE IF EXISTS affiliations;

create table person (id int, gname_person varchar(100), fname_person varchar(100), gender varchar(20), dob date, city varchar(100), country varchar(100), primary key(id));
create table org ( id int, name_org varchar(100), dof date, city varchar(100), country varchar(100) , primary key(id));
create table award ( id int, awardYear int, category varchar(100), sortorder int, primary key(id,awardYear,category));
CREATE TABLE affiliations(
    id INT,
    name_aff VARCHAR(100),
    city VARCHAR(50),
    PRIMARY KEY(id, name_aff, city),
    country VARCHAR(50)
);

LOAD DATA LOCAL INFILE './org.del' INTO TABLE org FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"' ;
LOAD DATA LOCAL INFILE './person.del' INTO TABLE person FIELDS TERMINATED BY ','OPTIONALLY ENCLOSED BY '"'  ;
LOAD DATA LOCAL INFILE './award.del' INTO TABLE award FIELDS TERMINATED BY ','OPTIONALLY ENCLOSED BY '"'  ;
LOAD DATA LOCAL INFILE './affiliations.del' INTO TABLE affiliations FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'  ;