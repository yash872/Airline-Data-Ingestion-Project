-- SCHEMA
CREATE SCHEMA airlines;

-- DIM AIRPORTS
CREATE TABLE airlines.airports_dim ( 
    airport_id BIGINT,
    city VARCHAR(100),
    state VARCHAR(100),
    name VARCHAR(200)
);

-- daily_flights_fact Table
CREATE TABLE airlines.daily_flights_fact (
    carrier VARCHAR(10),
    dep_airport VARCHAR(200),
    arr_airport VARCHAR(200),
    dep_city VARCHAR(100),
    arr_city VARCHAR(100),
    dep_state VARCHAR(100),
    arr_state VARCHAR(100),
    dep_delay BIGINT,
    arr_delay BIGINT
);

-- COPY DATA FROM S3 TO REDSHIFT
COPY airlines.airports_dim
FROM 's3://airline-data-input/airport-dim/airports.csv' 
IAM_ROLE 'arn:aws:iam::010526265053:role/service-role/AmazonRedshift-CommandsAccessRole-20240806T210859'
DELIMITER ','
IGNOREHEADER 1
REGION 'us-east-1';


-- Query
SELECT * FROM airlines.airports_dim LIMIT 5