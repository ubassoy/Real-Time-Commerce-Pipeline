# Real-Time Commerce Data Pipeline 🚀
A scalable data engineering pipeline that streams commerce data from a Kafka producer to a Power BI dashboard for real-time analytics.

## 🏗️ Architecture
**Infrastructure:** Dockerized environment using `jupyter/datascience-notebook`[cite: 2].
**Producer:** Python-based Kafka producer streaming CSV data.
**Streaming:** Apache Kafka cluster managed via Zookeeper.
**Consumer:** Python-based Kafka consumer for data cleaning and API integration.
**Visualization:** Real-time data push to Power BI REST API[cite: 10].

## 🛠️ Tech Stack
**Language:** Python 3.10 
**Streaming:** Apache Kafka 
**Containerization:** Docker & Docker Compose 
**Libraries:** Pandas (Data manipulation), Kafka-Python (Streaming), Requests (API integration) [cite: 10, 15]
**Big Data:** Apache Spark 3.3.0 & Java 17 [cite: 2, 3]

