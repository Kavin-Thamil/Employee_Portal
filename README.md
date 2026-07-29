# ☁️ Smart Employee Portal

> A cloud-native employee management platform built with Python (Flask) and deployed on AWS infrastructure.

Smart Employee Portal is a secure, cloud-hosted web application designed for employee document management and administrative workflows. Built with Flask and deployed across a custom AWS architecture, it emphasizes cloud security, role-based access control (RBAC), and high availability.

---

## ✨ Key Features

### 🔐 Secure Employee & Document Workflows
- Employee authentication and session handling for secure portal access
- Document upload, retrieval, and management with role-based permissions
- CRUD operations for administrative oversight of employee records

### ☁️ AWS Cloud Infrastructure & Networking
- **Amazon EC2 & VPC:** Deployed on Linux EC2 instances inside a custom Virtual Private Cloud (VPC) with structured public/private subnets and Security Groups
- **Application Load Balancer (ALB):** Routes incoming HTTP/HTTPS traffic to ensure high availability and load distribution
- **Amazon S3 & IAM:** Secure document storage using IAM role-based access—zero hardcoded AWS credentials in the codebase
- **Amazon RDS (MySQL):** Managed relational database instance isolated within private subnets for enhanced data security

### 📊 Automated Monitoring & Alerting
- **Amazon CloudWatch:** Real-time logging and metric tracking for server health and application performance
- **Amazon SNS:** Automated notification alerts triggered by system load anomalies or infrastructure events

---

## 🛠 Tech Stack

### Application Layer
- Python 3.x
- Flask & Gunicorn
- HTML5, CSS3, Bootstrap 5

### Cloud & DevOps (AWS)
- Amazon EC2, VPC, ALB
- Amazon S3, IAM Roles
- Amazon CloudWatch & SNS
- Linux (Amazon Linux / Ubuntu)

### Database
- Amazon RDS (MySQL)

---

## 📐 Cloud Architecture Overview

```
[ Client / Browser ]
        │
        ▼
[ Application Load Balancer (ALB) ]
        │
        ├──► [ Public Subnet: EC2 Instance (Flask + Gunicorn) ] ──► [ Amazon S3 Document Storage ]
        │                                                      ──► [ Amazon CloudWatch / SNS ]
        │
        └──► [ Private Subnet: Amazon RDS MySQL Database ]
```

---

## 🚀 Local Development Setup

### Prerequisites
- Python 3.10+
- MySQL Server
- AWS Account (for S3/RDS integration if testing cloud features locally)
- Git

### Installation

1. **Clone the repository:**
   ```
   git clone [https://github.com/Kavin-Thamil/Smart-Employee-Portal.git](https://github.com/Kavin-Thamil/Smart-Employee-Portal.git)
   cd Smart-Employee-Portal
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   ```
   - **Windows:** `venv\Scripts\activate`
   - **macOS / Linux:** `source venv/bin/activate`

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=your_secret_key
   FLASK_ENV=development
   DB_HOST=127.0.0.1
   DB_USER=root
   DB_PASSWORD=your_local_db_password
   DB_NAME=employee_portal_db
   AWS_REGION=ap-south-1
   S3_BUCKET_NAME=your-s3-bucket
   ```

5. **Run the local development server:**
   ```
   python app.py
   ```
   Open `http://127.0.0.1:5000/` in your browser.

---

## 📖 Key Engineering Learnings

Building and deploying Smart Employee Portal provided practical experience with:

- **Cloud Security Engineering:** Implemented least-privilege IAM roles and isolated database layers in private VPC subnets to protect application data.
- **Production Deployment:** Managed Linux server configuration, environment variable isolation, and web server routing for a live Flask application.
- **Observability:** Configured CloudWatch alarms and SNS notification pipelines to proactively monitor cloud infrastructure health.

---

## 👤 Author

**Kavin Thamil A**  
- **LinkedIn:** [linkedin.com/in/kavinthamil](https://linkedin.com/in/kavinthamil)  
- **GitHub:** [@Kavin-Thamil](https://github.com/Kavin-Thamil)  
- **Email:** kavinthamil01@gmail.com
