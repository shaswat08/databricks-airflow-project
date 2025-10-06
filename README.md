StackExchange ETL & Dashboard Project
Overview

This project demonstrates an end-to-end data engineering pipeline using Databricks, AWS S3, Apache Spark, Airflow 3.0, Kubernetes, and CI/CD. It extracts StackExchange XML data, processes it with Spark, and visualizes insights in a dashboard.

Architecture
Part 1: Databricks

Development of ETL logic in Databricks notebooks.

Notebooks are saved as .py files in GitHub during development.
Raw data is extracted and written into AWS S3 (or Unity Catalog).
Spark clusters are triggered to process and transform the data.

Part 2: Airflow 3.0

DAGs orchestrate ETL tasks.
Tasks and operators are executed inside Kubernetes pods.
Airflow DAG repo is synced via Git to deploy changes.
Custom Airflow Docker image is used for consistent runtime environments.

Part 3: Deployment & CI/CD
Custom Docker image is pushed to AWS ECR via CI/CD pipelines.
Kubernetes cluster pulls the latest image and runs Airflow DAGs.
Automated pipeline ensures changes in notebooks or DAGs are reflected immediately.

Technologies Used

Databricks – ETL & notebook development
Apache Spark – Data transformation
AWS S3 – Storage for raw and processed data
Airflow 3.0 – Workflow orchestration
Docker – Containerization
Kubernetes (Kind) – Local cluster for running Airflow
AWS ECR – Container registry
CI/CD pipelines – Automated deployment
GitHub – Version control
