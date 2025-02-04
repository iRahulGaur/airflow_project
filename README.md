# Weather Data Pipeline using Apache Airflow & AWS

## Overview
This project implements an automated weather data pipeline using **Apache Airflow**, **AWS EC2**, **AWS S3**, and **Python**. The pipeline fetches Sydney's weather data daily and stores it as a CSV file in an **S3 bucket**.

## Technologies Used
- **Apache Airflow** - Workflow orchestration
- **AWS EC2** - Compute instance for running Airflow
- **AWS S3** - Cloud storage for weather data
- **Python** - Data extraction and processing

## Features
- Automatically fetches Sydney's weather data daily
- Stores the data as a CSV file in an **AWS S3 bucket**
- Uses **Apache Airflow DAG** for scheduling and execution
- Logs and monitors workflow execution

## Project Structure
```
/airflow_project
│── dags/
│   ├── weather_pipeline.py  # Airflow DAG for data extraction
│── scripts/
│   ├── fetch_weather.py     # Python script to fetch weather data
│── requirements.txt         # Required Python packages
│── README.md                # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **Apache Airflow**
- **AWS CLI** (configured with proper IAM permissions)
- **Boto3** for AWS interactions

### Steps to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/iRahulGaur/airflow_project.git
   cd airflow_project
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Start Airflow Services**
   ```sh
   airflow db init
   airflow webserver --port 8080 &
   airflow scheduler &
   ```
4. **Trigger DAG Execution**
   - Open the Airflow UI at [http://localhost:8080](http://localhost:8080)
   - Enable and trigger the DAG manually (it also runs automatically daily)

## AWS Configuration
1. **Create an S3 Bucket**
   ```sh
   aws s3 mb s3://your-weather-data-bucket
   ```
2. **Set Up IAM Roles & Policies**
   Ensure your EC2 instance has an IAM role with the necessary **S3 read/write** permissions.

## Airflow DAG Breakdown
- The DAG **`weather_pipeline.py`** runs daily to:
  1. Fetch weather data from an API
  2. Save it as a CSV file
  3. Upload the CSV file to **AWS S3**

## Future Enhancements
- Implement **data transformation** using Pandas
- Store data in **AWS RDS or DynamoDB** for better querying
- Set up **email or Slack alerts** for failures
- Add **unit tests** for improved reliability

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---
Feel free to contribute or raise issues if you have any suggestions!
