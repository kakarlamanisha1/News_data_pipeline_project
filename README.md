# News Data Pipeline Project

A complete ETL (Extract, Transform, Load) data pipeline for collecting news articles from NewsAPI, processing them, and storing in AWS S3 and Snowflake using Apache Airflow orchestration.

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Installation & Setup](#installation--setup)
7. [Configuration](#configuration)
8. [Running the Pipeline](#running-the-pipeline)
9. [Docker Commands](#docker-commands)
10. [Airflow UI](#airflow-ui)
11. [Pipeline Details](#pipeline-details)
12. [Troubleshooting](#troubleshooting)
13. [Contributing](#contributing)
14. [License](#license)

---

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

### Step 3: Verify .env File

```bash
# View the .env file content
cat .env

# Ensure all variables are set (Linux/Mac)
source .env
echo $NEWS_API_KEY
```

### Step 4: Install Python Dependencies (Optional)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# View installed packages
pip list
```

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

---

## ⚙️ Configuration

### Update API Keys in Scripts

If not using environment variables, update the scripts directly:

**For extract_news.py:**
```bash
# Edit extract_news.py
nano scripts/extract_news.py

# Update:
API_KEY = "your_actual_newsapi_key"
```

**For load_snowflake.py:**
```bash
# Edit load_snowflake.py
nano scripts/load_snowflake.py

# Update:
AWS_ACCESS_KEY = "your_actual_aws_access_key"
AWS_SECRET_KEY = "your_actual_aws_secret_key"
BUCKET_NAME = "your_bucket_name"
```

### Airflow Configuration

The `docker-compose.yaml` file contains Airflow settings. Key configurations:

```yaml
# Timezone
AIRFLOW__CORE__DEFAULT_TIMEZONE: Asia/Kolkata

# Executor
AIRFLOW__CORE__EXECUTOR: LocalExecutor

# Database
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
```

To modify these, edit `docker-compose.yaml` and restart containers:

```bash
docker-compose down
docker-compose up -d
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

### Method 2: Trigger via Command Line

```bash
# Trigger the DAG using airflow CLI
docker exec airflow-scheduler airflow dags trigger news_pipeline

# View DAG status
docker exec airflow-scheduler airflow dags list

# View DAG runs
docker exec airflow-scheduler airflow dags list-runs -d news_pipeline

# View task status
docker exec airflow-scheduler airflow tasks list news_pipeline
```

### Method 3: Automatic Daily Scheduling

The pipeline is set to run automatically every day at midnight UTC. No action needed - just ensure containers are running.

```bash
# Check if scheduler is running
docker-compose ps | grep scheduler

# View scheduler logs to confirm scheduling
docker-compose logs airflow-scheduler | tail -20
```

### Monitor Pipeline Execution

```bash
# View real-time logs
docker-compose logs -f airflow-scheduler

# Check specific task logs
docker exec airflow-scheduler airflow tasks logs news_pipeline extract

# List all DAG runs
docker exec airflow-scheduler airflow dags list-runs -d news_pipeline --limit 10
```

---

## 🐳 Docker Commands

### Container Management

```bash
# Start all containers
docker-compose up -d

# Stop all containers
docker-compose down

# Stop containers and remove volumes
docker-compose down -v

# Restart all containers
docker-compose restart

# Restart specific container
docker-compose restart airflow-webserver

# Restart scheduler
docker-compose restart airflow-scheduler

# Restart database
docker-compose restart postgres
```

### View Logs

```bash
# View all logs
docker-compose logs

# View logs for specific service
docker-compose logs airflow-webserver
docker-compose logs airflow-scheduler
docker-compose logs postgres

# View last 50 lines
docker-compose logs --tail 50

# Follow logs in real-time (Ctrl+C to exit)
docker-compose logs -f

# View logs since specific time
docker-compose logs --since 10m
```

### Container Status

```bash
# List running containers
docker-compose ps

# List all containers (running and stopped)
docker-compose ps -a

# View container resource usage
docker stats

# Check container logs
docker-compose logs container_name
```

### Execute Commands in Container

```bash
# Access Airflow CLI
docker exec airflow-scheduler airflow version

# List all DAGs
docker exec airflow-scheduler airflow dags list

# Validate DAG
docker exec airflow-scheduler airflow dags validate dags/news_pipeline.py

# Access PostgreSQL
docker exec -it postgres psql -U airflow -d airflow

# Execute Python in container
docker exec airflow-scheduler python -c "import airflow; print(airflow.__version__)"
```

### Cleanup

```bash
# Remove containers and networks
docker-compose down

# Remove containers, networks, and volumes
docker-compose down -v

# Remove all stopped containers
docker container prune

# Remove unused volumes
docker volume prune

# Clean everything
docker system prune -a
```

---

## 🌐 Airflow UI

### Access Airflow Dashboard

```
URL: http://localhost:8080
Username: admin
Password: admin
```

### Dashboard Features

**DAG View:**
- View all DAGs (Directed Acyclic Graphs)
- Enable/disable DAGs
- Trigger manual runs
- View task dependencies

**Task View:**
- Monitor individual tasks
- Check task status (Success, Failed, Running)
- View task logs
- Retry failed tasks

**Monitoring:**
- View execution history
- Check task durations
- Monitor resource usage
- Alert configuration

### Common Airflow UI Tasks

```bash
# View DAG details
# Navigate to: Dags → news_pipeline

# Trigger pipeline
# Click: Trigger DAG button (top right)

# View logs
# Click: Task → Logs

# Mark task as success
# Right-click Task → Mark Success

# Clear task state
# Right-click Task → Clear
```

---

## 📊 Pipeline Details

### Task 1: Extract (`extract_news.py`)

**Purpose:** Fetch news data from NewsAPI

**Command to run manually:**
```bash
docker exec airflow-scheduler python /opt/airflow/scripts/extract_news.py
```

**What it does:**
- Calls NewsAPI endpoint for US top headlines
- Retrieves article data (source, title, author, description, etc.)
- Saves raw JSON response to `/opt/airflow/scripts/news.json`

**Output:**
- File: `news.json`
- Format: JSON with articles array
- Location: `/opt/airflow/scripts/news.json`

**Example output structure:**
```json
{
  "status": "ok",
  "totalResults": 50,
  "articles": [
    {
      "source": {"id": null, "name": "CNN"},
      "author": "John Doe",
      "title": "Breaking News...",
      "url": "https://...",
      "urlToImage": "https://...",
      "publishedAt": "2026-04-28T12:00:00Z",
      "content": "..."
    }
  ]
}
```

### Task 2: Transform (`transform_news.py`)

**Purpose:** Convert JSON to structured CSV format

**Command to run manually:**
```bash
docker exec airflow-scheduler python /opt/airflow/scripts/transform_news.py
```

**What it does:**
- Reads `news.json` file
- Extracts fields: source name, title, author
- Creates pandas DataFrame
- Exports to CSV format
- Saves to `/opt/airflow/scripts/news.csv`

**Output:**
- File: `news.csv`
- Format: CSV with columns (source, title, author)
- Location: `/opt/airflow/scripts/news.csv`

**Example output:**
```csv
source,title,author
CNN,Breaking News Title,John Doe
BBC,International News,Jane Smith
Reuters,Market Update,
```

### Task 3: Load (`load_snowflake.py`)

**Purpose:** Upload processed data to AWS S3

**Command to run manually:**
```bash
docker exec airflow-scheduler python /opt/airflow/scripts/load_snowflake.py
```

**What it does:**
- Reads `news.csv` from local storage
- Connects to AWS S3 using boto3
- Uploads file to S3 bucket
- Path: `s3://news-data-raw-bucket-manisha/processed/news.csv`
- Future: Load to Snowflake data warehouse

**Output:**
- Location: AWS S3 bucket
- Path: `processed/news.csv`
- Accessible via AWS Console

**Verify upload:**
```bash
# List files in S3 bucket (requires AWS CLI)
aws s3 ls s3://news-data-raw-bucket-manisha/processed/

# Download from S3
aws s3 cp s3://news-data-raw-bucket-manisha/processed/news.csv ./
```

---

## 🔧 Troubleshooting

### Issue 1: Airflow UI Not Accessible

**Problem:** Cannot access http://localhost:8080

**Solutions:**
```bash
# Check if containers are running
docker-compose ps

# View webserver logs
docker-compose logs airflow-webserver

# Check if port 8080 is in use
lsof -i :8080  # Linux/Mac
netstat -ano | findstr :8080  # Windows

# Restart webserver
docker-compose restart airflow-webserver

# Wait for container to start (30 seconds) then refresh browser
sleep 30
```

### Issue 2: DAG Not Appearing in Airflow

**Problem:** news_pipeline DAG not visible in UI

**Solutions:**
```bash
# Check DAG file syntax
docker exec airflow-scheduler airflow dags validate dags/news_pipeline.py

# List all DAGs
docker exec airflow-scheduler airflow dags list

# View DAG parse errors
docker-compose logs airflow-scheduler | grep "Error"

# Restart scheduler
docker-compose restart airflow-scheduler

# Force DAG refresh (sometimes needed)
docker exec airflow-scheduler rm -rf /opt/airflow/.airflow/
docker-compose restart airflow-scheduler
```

### Issue 3: Pipeline Task Fails

**Problem:** Tasks showing as "Failed" in Airflow

**Solutions:**
```bash
# View task logs
docker exec airflow-scheduler airflow tasks logs news_pipeline extract

# Check specific task error
docker-compose logs airflow-scheduler | grep "extract"

# Manually run task to debug
docker exec airflow-scheduler python /opt/airflow/scripts/extract_news.py

# Check environment variables
docker exec airflow-scheduler printenv | grep NEWS_API_KEY

# Verify .env file
cat .env
```

### Issue 4: API Key Not Working

**Problem:** NewsAPI authentication fails

**Solutions:**
```bash
# Verify API key in .env
grep NEWS_API_KEY .env

# Test API key manually
curl "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_KEY"

# Update API key in .env
ano .env

# Restart containers to reload env
docker-compose down
docker-compose up -d
```

### Issue 5: S3 Upload Fails

**Problem:** AWS S3 upload returns error

**Solutions:**
```bash
# Verify AWS credentials in .env
grep AWS .env

# Check AWS permissions (requires AWS CLI)
aws s3 ls s3://news-data-raw-bucket-manisha/

# Test S3 connectivity
aws s3api head-bucket --bucket news-data-raw-bucket-manisha

# Check bucket exists
aws s3 ls | grep news-data

# Verify IAM user has s3:PutObject permission
```

### Issue 6: PostgreSQL Connection Error

**Problem:** Cannot connect to PostgreSQL database

**Solutions:**
```bash
# Wait for PostgreSQL to initialize (30 seconds)
sleep 30
docker-compose restart airflow-scheduler

# Check PostgreSQL container
docker-compose ps postgres

# Access PostgreSQL directly
docker exec -it postgres psql -U airflow -d airflow

# View PostgreSQL logs
docker-compose logs postgres

# Reset database
docker-compose down -v
docker-compose up -d
```

### Issue 7: Out of Disk Space

**Problem:** Docker containers fail due to disk space

**Solutions:**
```bash
# Check disk space
df -h

# Clean unused Docker resources
docker system prune -a

# Remove old logs
docker-compose logs --tail 100 > /dev/null
docker volume prune -f

# Remove volumes
docker-compose down -v
```

### Debug Mode

**Enable detailed logging:**
```bash
# View full scheduler logs
docker-compose logs -f airflow-scheduler

# Enable Airflow debug mode
export AIRFLOW__LOGGING__LOGGING_LEVEL=DEBUG
docker-compose restart

# Check configuration
docker exec airflow-scheduler airflow config list
```

---

## 📝 Common Commands Reference

```bash
# Start pipeline
docker-compose up -d

# Stop pipeline
docker-compose down

# View logs
docker-compose logs -f

# Trigger DAG
docker exec airflow-scheduler airflow dags trigger news_pipeline

# Check DAG status
docker exec airflow-scheduler airflow dags list

# View task logs
docker exec airflow-scheduler airflow tasks logs news_pipeline extract

# Restart services
docker-compose restart

# Check containers
docker-compose ps

# Access PostgreSQL
docker exec -it postgres psql -U airflow -d airflow

# Clean up
docker system prune -a
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact & Support

- **Author:** Manisha Kakarla
- **GitHub:** [@kakarlamanisha1](https://github.com/kakarlamanisha1)
- **Email:** manisha@example.com

For issues or questions, please open an issue on GitHub.

---

**Last Updated:** April 2026  
**Status:** Active Development  
**Version:** 1.0.0