# Apache_Airflow_Data_Pipeline
The aim of this project is to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. Since data quality plays a big part when analyses are executed on top the data warehouse, we incorporate tests against the datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

# Implemented DAG:
The begin_execution tasks simply creates the DWH tables if they do not exist.

The Stage_events and Stage_songs tables load data from S3 to Redshift. They both use the same Stage Operator with different parameters.

The Load_songplays_fact_table loads data from the staging tables to the fact table using the Fact Operator.

The Load_x_dim_table loads data to the 4 dimension (artists, users, songs, time) tables. It uses the same Dim Operator with different parameters to load the data.

The Run_data_quality_checks uses the Data Quality Operator to check the data at the end of the ETL.

The Stop_execution operator does not perform any task and simply ends the DAG execution.
