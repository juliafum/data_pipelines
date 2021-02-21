## Data modeling with Spark

### Summary
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3. This project will introduce you to the core concepts of Apache Airflow. To complete the project, you will need to create your own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.
The Redshift database contains these tables:

* Staging Tables
  - staging_events
  - staging_songs
* Fact Table:
  - songplays: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
* Dimension Tables: 
  - users: user_id, first_name, last_name, gender, level
  - songs: song_id, title, artist_id, year, duration
  - artists: artist_id, name, location, latitude, longitude
  - time: start_time, hour, day, week, month, year, weekday


The project includes these files:
* dags:
 - create_tables.sql: SQL statements for creating tables in Redshift
 - udac_axample_dag.py: contains the Airflow dag
* plugins:
 - operators: 
  - stage_redshift.py: Airflow custom operator to read JSON files from S3 to Redshift
  - load_fact.py: Airflow custom operator to load the fact table in Redshift
  - load_dimension.py: Airflow custom operator to load dimension tables in Redshift
  - data_quality.py: Airflow custom operator for checking data quality
* helpers:
 - sql_queries.py: Redshift SQL queries used in the pipeline


