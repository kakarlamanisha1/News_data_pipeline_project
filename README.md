# News Data Pipeline Project

A complete ETL (Extract, Transform, Load) data pipeline for collecting news articles from NewsAPI, processing them, and storing in AWS S3 and Snowflake using Apache Airflow orchestration.


## 🎯 Project Overview

The News Data Pipeline Project is an automated ETL system that:
- **Extracts** top headlines from NewsAPI
- **Transforms** raw JSON data into structured CSV format
- **Loads** processed data to AWS S3 and Snowflake data warehouse
- **Orchestrates** the entire workflow using Apache Airflow with daily scheduled execution

This project demonstrates modern data engineering practices including containerization, orchestration, cloud integration, and data warehousing.

---

## ✨ Features

- ✅ Automated daily news data collection
- ✅ Apache Airflow orchestration with DAG scheduling
- ✅ Docker containerization for easy deployment
- ✅ AWS S3 integration for data storage
- ✅ Snowflake data warehouse integration
- ✅ PostgreSQL metadata database
- ✅ Environment-based configuration management
- ✅ Error handling and logging
- ✅ Scalable and modular architecture

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PIPELINE WORKFLOW                         │
└─────────────────────────────────────────────────────────────┘

NewsAPI
  │
  ├─→ EXTRACT (extract_news.py)
  │   • Fetch top US headlines
  │   • Convert to JSON
  │   └─→ Output: news.json
  │
  ├─→ TRANSFORM (transform_news.py)
  │   • Parse JSON data
  │   • Extract key fields (source, title, author)
  │   • Create structured format
  │   └─→ Output: news.csv
  │
  └─→ LOAD (load_snowflake.py)
      • Upload to AWS S3
      • Push to Snowflake
      └─→ Output: Data in Cloud Storage

Orchestration: Apache Airflow (Daily Schedule)
Database: PostgreSQL (Metadata)
```

---

## 📁 Project Structure

```
News_data_pipeline_project/
├── dags/
│   └── news_pipeline.py              # Airflow DAG definition
├── scripts/
│   ├── extract_news.py               # Extract from NewsAPI
│   ├── transform_news.py             # Transform JSON to CSV
│   └── load_snowflake.py             # Load to S3/Snowflake
├── config/
│   └── config.py                     # Configuration management
├── docker-compose.yaml               # Docker Compose setup
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore file
└── README.md                         # Project documentation
```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed and accounts created:

### System Requirements
- Docker & Docker Compose (v20+)
- Python 3.8 or higher
- Git
- 2GB RAM minimum
- Internet connection

### Required API Keys & Accounts

1. **NewsAPI Key**
   - Sign up at https://newsapi.org
   - Get your API key from dashboard
   - Free tier: 100 requests per day

2. **AWS Account**
   - Create AWS account at https://aws.amazon.com
   - Generate Access Key ID and Secret Access Key
   - Create S3 bucket: `news-data-raw-bucket-manisha`
   - Ensure IAM permissions for S3 access

3. **Snowflake Account (Optional)**
   - Sign up at https://www.snowflake.com
   - Get account ID, username, password
   - Create warehouse, database, and schema

### Verify Installations

```bash
# Check Docker
docker --version
# Output: Docker version 20.x.x

# Check Docker Compose
docker-compose --version
# Output: Docker Compose version 2.x.x

# Check Python
python --version
# Output: Python 3.8+

# Check Git
git --version
# Output: git version 2.x.x
```

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/kakarlamanisha1/News_data_pipeline_project.git
cd News_data_pipeline_project
```

### Step 2: Create Environment Configuration File

Create a `.env` file in the root directory:

```bash
cat > .env << EOF
# NewsAPI Configuration
NEWS_API_KEY=your_newsapi_key_here

# AWS S3 Configuration
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
AWS_BUCKET=news-data-raw-bucket-manisha
AWS_REGION=us-east-1

# Snowflake Configuration (Optional)
SNOWFLAKE_USER=your_snowflake_user
SNOWFLAKE_PASSWORD=your_snowflake_password
SNOWFLAKE_ACCOUNT=your_snowflake_account
SNOWFLAKE_WAREHOUSE=your_warehouse_name
SNOWFLAKE_DATABASE=your_database_name
SNOWFLAKE_SCHEMA=your_schema_name
EOF
```

Or manually edit the `.env` file with your credentials.


### Step 4: Install Python Dependencies (Optional)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


### Step 5: Start Docker Containers

```bash
# Build and start containers in detached mode
docker-compose up -d

# Check container status
docker-compose ps

# View logs (all services)
docker-compose logs -f

# View specific service logs
docker-compose logs -f airflow-webserver
docker-compose logs -f airflow-scheduler
docker-compose logs -f postgres
```

----

# Update:
AWS_ACCESS_KEY = "your_actual_aws_access_key"
AWS_SECRET_KEY = "your_actual_aws_secret_key"
BUCKET_NAME = "your_bucket_name"
```


### Schedule Configuration

Edit `dags/news_pipeline.py` to change schedule:

```bash
# Edit the DAG file
nano dags/news_pipeline.py

# Change schedule parameter:
schedule="@daily"        # Daily at midnight UTC
schedule="@hourly"       # Every hour
schedule="@weekly"       # Weekly on Monday
schedule="0 9 * * *"     # Daily at 9 AM UTC (cron format)
```

---

## ▶️ Running the Pipeline

### Method 1: Access Airflow Web UI (Recommended)

```bash
# 1. Open browser and navigate to Airflow
# URL: http://localhost:8080

# 2. Login with credentials
# Username: admin
# Password: admin

# 3. Find the "news_pipeline" DAG in the list

# 4. Click on the DAG name

# 5. Click "Trigger DAG" button (top right)

# 6. Confirm the trigger
```


## 🌐 Airflow UI

### Access Airflow Dashboard

```
URL: http://localhost:8080
Username: admin
Password: admin
```

For issues or questions, please open an issue on GitHub.

---

**Last Updated:** April 2026  
**Status:** Active Development  
**Version:** 1.0.0
