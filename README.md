**Fleet Management Analytics Platform – Microsoft Fabric Lakehouse**

A scalable Lakehouse-based fleet analytics platform built using Microsoft Fabric, Delta Lake, PySpark, and Power BI.
This project simulates real-time fleet monitoring by ingesting public transit data and enriching it with operational telemetry for analytics and KPI reporting.

📌 **Architecture Overview**

This solution demonstrates how to design a modern cloud data platform from API ingestion to business-ready analytics using Medallion Architecture (Bronze → Silver → Gold).

The system processes vehicle data, applies transformation logic, and produces analytics-ready tables optimized for reporting and decision-making.

<img width="1024" height="1536" alt="Fleet Management Analytics_diagram" src="https://github.com/user-attachments/assets/c5905a6e-9de4-4532-897f-3cf7d64f43c1" />


🛠 **Tech Stack**

Microsoft Fabric (Lakehouse, Notebooks)

Delta Lake (Medallion Architecture)

PySpark (Data Transformation)

Spark SQL

Python (API ingestion & enrichment)

Power BI (Analytics Dashboard)

MBTA Open Transit API (Data Source)

🗂 Lakehouse Design
Bronze Layer – Raw Ingestion

Table: bronze_fleet_data

Ingests vehicle location data from MBTA API

Enriched with simulated telemetry:

Fuel level

Engine temperature

Driver ID

Congestion indicator

Stored as Delta table

Minimal transformation applied

Silver Layer – Clean & Structured

Table: silver_fleet_data

Data typing and schema enforcement

Null handling and field normalization

Standardized timestamp formats

Data quality checks implemented

Transformation logic applied using PySpark

Gold Layer – Analytics & KPI Modeling

Optimized, business-ready tables created for reporting:

gold_vehicle_summary – KPIs per vehicle

gold_driver_summary – Driver performance & incident tracking

gold_location_congestion – Congestion metrics by area

gold_daily_health_summary – Daily fleet operational trends

gold_fleet_status_snapshot – Current telemetry snapshot

These tables are structured for analytical workloads and Power BI consumption.

🚀 End-to-End Workflow

Python script ingests vehicle data from public API

Data enriched with operational telemetry fields

Stored in Bronze Delta table

PySpark transformations produce Silver layer

Aggregations and KPI modeling create Gold layer

Power BI connects directly to Lakehouse for analytics

📊 Analytics Layer

Power BI dashboard provides:

Vehicle performance metrics

Fleet health indicators

Congestion heat mapping

Driver efficiency analysis

Daily operational trends

Designed for near real-time monitoring and decision support.

🧠 Engineering Concepts Demonstrated

Medallion Architecture (Bronze → Silver → Gold)

Delta Lake data modeling

API ingestion with Python

Schema validation and normalization

Incremental processing concepts

Data quality validation

KPI-driven aggregation modeling

Lakehouse-based analytics integration

🔮 Future Enhancements

Real-time streaming ingestion

Event-driven alerting

Predictive maintenance modeling

Partition optimization

ML-based driver behavior scoring

📌 Key Takeaways

This project demonstrates hands-on implementation of a scalable Lakehouse data platform using Microsoft Fabric and modern data engineering practices.

It highlights practical experience in:

ETL design

Data transformation using PySpark

Analytics modeling

Cloud-based data architecture
