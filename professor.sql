DROP TABLE department;
DROP TABLE subject;
DROP TABLE researchfield;
DROP TABLE professor;

CREATE SEQUENCE department_id START 1;
CREATE SEQUENCE subject_id START 1;
CREATE SEQUENCE researchfield_id START 1;
CREATE SEQUENCE professor_id START 1;

CREATE TABLE department (
    id          integer PRIMARY KEY DEFAULT nextval('department_id'),
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE subject (
    id          integer PRIMARY KEY DEFAULT nextval('subject_id'),
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE researchfield (
    id          integer PRIMARY KEY DEFAULT nextval('researchfield_id'),
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE professor (
    id          integer PRIMARY KEY DEFAULT nextval('professor_id'),
    name        varchar(40),
    surname     varchar(40),
    title       varchar(40),
    eng_title   varchar(40),
    email       varchar(60),
    homepage    varchar(200),
    url         varchar(200)
);    

CREATE TABLE phone (
    profid      integer REFERENCES professor(id),
    pnumber     varchar(30)
);

CREATE TABLE doesresearch (
    idprof      integer REFERENCES professor(id),
    idfield     integer REFERENCES researchfield(id) 
);

CREATE TABLE teaching (
    idprof      integer REFERENCES professor(id),
    idfield     integer REFERENCES subject(id) 
);

CREATE TABLE deptmember (
    idprof      integer REFERENCES professor(id),
    idfield     integer REFERENCES department(id) 
);

