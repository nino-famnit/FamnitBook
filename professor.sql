CREATE TABLE phone (
    profid      integer REFERENCES professor(id),
    pnumber     varchar(30),
);

CREATE TABLE department (
    id          integer PRIMARY KEY,
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE subject (
    id          integer PRIMARY KEY,
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE researchfield (
    id          integer PRIMARY KEY,
    name        varchar(200),
    eng_name    varchar(200)
);

CREATE TABLE professor (
    id          integer PRIMARY KEY,
    name        varchar(40),
    surname     varchar(40),
    title       varchar(40),
    eng_title   varchar(40),
    email       varchar(60),
    homepage    varchar(200),
    url         varchar(200),
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

