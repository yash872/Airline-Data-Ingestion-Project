# Airline-Data-Ingestion-Project
***
## Project Overview
This project is an overview of an Event Driven Sales Data Projection data pipeline that Process the Orders data based on their Status and route towards DynamoDB or SQS as per the Business requirement rules.
An airline daily data ingestion project using S3, S3 Cloudtrail Notification, Event Bridge Pattern Rule, Glue Crawler, Glue Visual ETL, SNS, Redshift, and Step Function

***

## Architectural Diagram
![Event-Driven-SalesDataPipeline Architecture](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/Event-Driven-SalesDataPipeline.jpg)

***

## Key Steps
### 1. Create a S3 bucket
- we will create a S3 bucket "airline-data-input" to store the airport dimension file and daily input files.
![S3](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/S3.JPG)


### 2. Create a Schema in Redshift
- we will create a "airlines" schema in Redshift with both the Tables.
    - airport_dim
    - daily_flights_fact

- Copy the aiports data from S3 to Reshift aiport_dim table.

![Redshift](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/Redshift.JPG)


### 3. Create Glue Crawlers for Redshift Tables
- we will create glue crawlers for the Redshift tables.
![RedShift_Crawlers](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/RedShift_Crawlers.JPG)

### 4. Create Glue Crawlers for S3 Input data
- first we will create a dummy hive style folder in our S3 and upload a dummy data file to create the crawler.
- S3 Data Input File
![S3-crawler](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/S3-crawler.JPG)
- S3 Glue Crawler
![S3-flihgt-data](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/S3-flihgt-data.JPG)
- Glue Tables
![glue-tables](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/glue-tables.JPG)

### 5. Create Glue ETL Pipeline
- we will create a Glue Pipeline "flight-data-ingestion-pipeline" in which we join our daily data with the airport-dim and create a denormalized table for further analysis.
![glue-pipeline](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/glue-pipeline.JPG)

### 6. Create SNS
- we will create a SNS Topic "glue-job-notification" and subscribed by your email address to get the notification.
![SNS](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/SNS.JPG)


### 7. Create State Machine using Step Function
- we will create a State Machine using Step Function service and create a complete workflow in it. 
![StateMachine](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/StateMachine.JPG)

### 8. Create an Event Rule
- we will create an Event Rule "Airline-S3-StepFunc-EventRule" Which will triger the State Machine on a Object Creation in airline data S3 bucket.
![EventRule](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/EventRule.JPG)

### 9. Create an Event Bridge Rule
- we will create an Event Rule "Airline-S3-StepFunc-EventRule" Which will triger the State Machine on a Object Creation in airline data S3 bucket.
![EventRule](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/EventRule.JPG)

### 9. Upload the input flight data csv file 
- we will upload the input flight data csv file in the input S3 bucket which will trigger the State machine using Event Bridge Rule.
- S3 file
![fileUpload](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/fileUpload.JPG)

- Glue Job Run
![glueJobRun](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/glueJobRun.JPG)

- State Machine Run
![StateMachineSuccess](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/StateMachineSuccess.JPG)

### 9. Output Data in Redshift
- we can the output data stored in Redshift fact table.
![factData](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/factData.JPG)
