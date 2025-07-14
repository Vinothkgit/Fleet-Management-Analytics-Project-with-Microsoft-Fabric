# Fleet-Management-Analytics-Project-with-Microsoft-Fabric
A complete real-time **Fleet Monitoring Solution** using **Microsoft Fabric**, open APIs, enriched telemetry, Delta Lakehouse architecture, and **Power BI** dashboards. Designed with scalability, alerting, and business intelligence in mind.

## 📌 Project Overview

This project demonstrates how to build a modern data platform from API to dashboard using **Microsoft Fabric (Trial)**. It simulates a real-world use case of monitoring vehicles using enriched data (e.g., fuel level, engine temp, location congestion) and generating insights via the **Lakehouse** architecture.

---

## 🔧 Tech Stack

- **Microsoft Fabric**: Lakehouse, Notebooks, Eventstream (planned), Pipelines  
- **Power BI**: Dashboard, KPI Cards
- **Python**: Data ingestion + enrichment  
- **PySpark**: Silver layer transformation  
- **Delta Table**: Bronze → Silver → Gold  
- **APIs**: MBTA Open Transit Feed

---

## 🗂️ Lakehouse Structure

| Layer | Table Name | Description |
|-------|------------|-------------|
| Bronze | `bronze_fleet_data` | Raw enriched API data |
| Silver | `silver_fleet_data` | Cleaned, typed, and normalized |
| Gold | `gold_vehicle_summary` | KPIs per vehicle |
|       | `gold_driver_summary` | Driver efficiency and incidents |
|       | `gold_location_congestion` | Location-based congestion metrics |
|       | `gold_daily_health_summary` | Day-wise trends of fleet health |
|       | `gold_fleet_status_snapshot` | Current location + telemetry for all vehicles |


---

## 🚀 How It Works

1. **Ingest API Data**: Python script fetches MBTA vehicle data and adds fake telemetry (fuel, temp, etc.)
2. **Bronze Layer**: Enriched data saved as a Delta table
3. **Silver Layer**: PySpark transformations (data typing, cleaning)
4. **Gold Layer**: Aggregated + derived tables for reporting
5. **Power BI**: Connected directly to Lakehouse for reporting
6. *(Optional)*: Stream into Eventstream + Activator for alert automation
---

## 🧠 Future Enhancements

- Azure Event Hub Integration  
- Fabric Activator for real-time alerting  
- Predictive maintenance (ML integration)  
- Email/SMS alerting for critical flags  
- Driver behavior analysis over time

---

## 🙌 Credits

Built using **public APIs**, simulated telemetry, and **Microsoft Fabric** capabilities.

📬 Feel free to fork, explore, or contribute!

---

## 🔗 Let's Connect

💼 [LinkedIn] - https://www.linkedin.com/in/vino-r-mt/ 
💻 [More Projects] - https://github.com/Vinothkgit/water-quality-monitoring-End-to-End-Microsoft-Fabric-Data-Engineering-Project-

---

#fabric #powerbi #dataengineering #iot #analytics #openapi #fleetmanagement #microsoftfabric



