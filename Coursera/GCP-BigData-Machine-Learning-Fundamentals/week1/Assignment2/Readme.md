Task 1. Source a pre-created Pub/Sub topic and create a BigQuery dataset

In this task, you create the taxirides dataset. You have two different options which you can use to create this, using the Google Cloud Shell or the Google Cloud Console.

Pub/Sub is an asynchronous global messaging service. By decoupling senders and receivers, it allows for secure and highly available communication between independently written applications. Pub/Sub delivers low-latency, durable messaging.

In Pub/Sub, publisher applications and subscriber applications connect with one another through the use of a shared string called a topic. A publisher application creates and sends messages to a topic. Subscriber applications create a subscription to a topic to receive messages from it.

Google maintains a few public Pub/Sub streaming data topics for labs like this one. We'll be using an extract of the NYC Taxi & Limousine Commission’s open dataset. The Pub/Sub topic has already been created and populated in your project environment.

BigQuery is a serverless data warehouse. Tables in BigQuery are organized into datasets. In this lab, messages published into Pub/Sub will be aggregated and stored in BigQuery.

Use one of the following options to create a new BigQuery dataset:
Option 1: The command-line tool

    In Cloud Shell (Cloud Shell icon), run the following command to create the taxirides dataset.

bq --location=us-west1 mk taxirides

    Run this command to create the taxirides.realtime table (empty schema that you will stream into later).

bq --location=us-west1 mk \ --time_partitioning_field timestamp \ --schema ride_id:string,point_idx:integer,latitude:float,longitude:float,\ timestamp:timestamp,meter_reading:float,meter_increment:float,ride_status:string,\ passenger_count:integer -t taxirides.realtime
Option 2: The BigQuery Console UI
Note: Skip these steps if you created the tables using the command line.

    In the Google Cloud console, in the Navigation menu(Navigation Menu), click BigQuery.

    If you see the Welcome dialog, click Done.

    Click on View actions (View Actions) next to your Project ID, and then click Create dataset.

    In Dataset ID, type taxirides.

    In Data location, click us-west1 (Oregon), and then click Create Dataset.

    In the Explorer pane, click expand node (Expander) to reveal the new taxirides dataset.

    Click on View actions (View Actions) next to the taxirides dataset, and then click Open.

    Click Create Table.

    In Table, type realtime

    For the schema, click Edit as text and paste in the following:

ride_id:string, point_idx:integer, latitude:float, longitude:float, timestamp:timestamp, meter_reading:float, meter_increment:float, ride_status:string, passenger_count:integer

    In Partition and cluster settings, select timestamp.

    Click Create Table.

Task 2. Create a Cloud Storage bucket

In this task, you create a Cloud Storage bucket to provide working space for your Dataflow pipeline.

Cloud Storage allows world-wide storage and retrieval of any amount of data at any time. You can use Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.

    In the Cloud console, in the Navigation menu (Navigation Menu), click Cloud Storage > Buckets.
    Click Create Bucket.
    For Name, copy and paste in your Project ID, and then click Continue.
    For Location type, click Multi-region if it is not already selected.
    Click Create.
    In the Public access will be prevented dialog box, click Confirm.

Task 3. Set up a Dataflow Pipeline

In this task, you set up a streaming data pipeline to read sensor data from Pub/Sub, compute the maximum temperature within a time window, and write this out to BigQuery.

Dataflow is a serverless way to carry out data analysis.
Restart the connection to the Dataflow API.

    In the Cloud console, in the top search bar, type Dataflow API, and then press ENTER.

    In the search results window, click Dataflow API.

    Click Manage.

    Click Disable API.

    In the Disable dialog, click Disable.

    Click Enable.

Create a new streaming pipeline:

    In the Cloud console, in the Navigation menu (Navigation Menu), click Dataflow.

    In the top menu bar, click Create Job From Template.

    Type streaming-taxi-pipeline as the Job name for your Dataflow job.

    In Regional endpoint, select us-central1 (Iowa).

    In Dataflow template, select the Pub/Sub Topic to BigQuery template.

    In Input Pub/Sub topic, select the topic that already exists in your project from the dropdown list . It will appear like the following:

    projects/<myprojectid>/topics/taxirides-realtime

    In BigQuery output table, type <myprojectid>:taxirides.realtime

Note: You must replace myprojectid with your Project ID.
Note: There is a colon : between the project and dataset name and a dot . between the dataset and table name.

    In Temporary location, click Browse.

    Click view child resources(view child resources).

    Click Create new folder(new folder), and then type the name tmp.

    Click Create, and then click Select.

    Click Optional Parameters.

    In Max workers, type 2

    In Number of workers, type 1

    Click Run Job.

A new streaming job has started! You can now see a visual representation of the data pipeline. It will take 3 to 5 minutes for data to begin moving into BigQuery.
Note: If the dataflow job fails for the first time then re-create a new job template with new job name and run the job.
Task 4. Analyze the taxi data using BigQuery

In this task, you analyze the data as it is streaming.

    In the Cloud console, in the Navigation menu (Navigation Menu), click BigQuery.

    If the Welcome dialog appears, click Done.

    In the Query Editor, type the following, and then click Run:

SELECT * FROM taxirides.realtime LIMIT 10
Note: If no records are returned, wait another minute and re-run the above query (Dataflow takes 3-5 minutes to setup the stream).

Your output will look similar to the following: Sample BigQuery output from query
Task 5. Perform aggregations on the stream for reporting

In this task, you calculate aggregations on the stream for reporting.

    In the Query Editor, clear the current query.

    Copy and paste the following query, and then click Run.

WITH streaming_data AS ( SELECT timestamp, TIMESTAMP_TRUNC(timestamp, HOUR, 'UTC') AS hour, TIMESTAMP_TRUNC(timestamp, MINUTE, 'UTC') AS minute, TIMESTAMP_TRUNC(timestamp, SECOND, 'UTC') AS second, ride_id, latitude, longitude, meter_reading, ride_status, passenger_count FROM taxirides.realtime ORDER BY timestamp DESC LIMIT 1000 ) # calculate aggregations on stream for reporting: SELECT ROW_NUMBER() OVER() AS dashboard_sort, minute, COUNT(DISTINCT ride_id) AS total_rides, SUM(meter_reading) AS total_revenue, SUM(passenger_count) AS total_passengers FROM streaming_data GROUP BY minute, timestamp
Note: Ensure Dataflow is registering data in BigQuery before proceeding to the next task.

The result shows key metrics by the minute for every taxi drop-off.

    Click Save > Save query.

    In the Save query dialog, in the Name field, type My Saved Query.

    Click Save.

Task 6. Stop the Dataflow Job

In this task, you stop the Dataflow job to free up resources for your project.

    In the Cloud console, in the Navigation menu (Navigation Menu), click Dataflow.

    Click the streaming-taxi-pipeline, or the new job name.

    Click Stop, and then select Cancel > Stop Job.
