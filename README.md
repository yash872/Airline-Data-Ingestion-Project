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
![S3](https://github.com/yash872/Airline-Data-Ingestion-Project/blob/main/Images/S3.jpg)

