# Medallion Architecture 

## Project Overview

This activity demonstrates the implementation of **Medallion Architecture** using:

* Bronze Layer → Raw Data
* Silver Layer → Cleaned Data
* Gold Layer → Business Report

Server Used:

```bash
SERVER IP
```

---

# Step 1 — Connect to Server

```bash
ssh azureuser@SERVER_IP
```

---

# Step 2 — Clone Repository

```bash
git clone https://github.com/shubhsalunke/Flask-PostgreSQL-Dockerfile.git
```

---

# Step 3 — Navigate to Project Directory

```bash
cd 04.2.Medallion-Architecture
```

---

# Step 4 — Verify Project Files

```bash
ls
```

Expected Output:

```bash
README.md  bronze  gold  scripts  silver
```

---

# Step 5 — Install Required Packages

```bash
sudo apt update
sudo apt install python3-venv python3-pip tree git -y
```

---

# Step 6 — Create Python Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment:

```bash
source venv/bin/activate
```

Expected:

```bash
(venv)
```

---

# Step 7 — Install Pandas

```bash
pip install pandas
```

Verify Installation:

```bash
python -c "import pandas; print(pandas.__version__)"
```

---

# Step 8 — Verify Bronze Layer File

```bash
cat bronze/sales_raw.csv
```

Expected Output:

```bash
id,name,product,amount,city
1,Rahul,Laptop,50000,Pune
2,Amit,Mouse,500,Mumbai
3,Sneha,Keyboard,1500,Pune
4,Rahul,Laptop,50000,Pune
5,Neha,Monitor,,Nashik
```

---

# Step 9 — Verify Scripts

```bash
ls scripts
```

Expected Output:

```bash
bronze_to_silver.py
silver_to_gold.py
```

---

# Step 10 — Run Bronze → Silver Pipeline

```bash
python scripts/bronze_to_silver.py
```

Expected Output:

```bash
Bronze to Silver completed
```

---

# Step 11 — Verify Silver Layer

```bash
cat silver/sales_clean.csv
```

Expected Output:

```bash
id,name,product,amount,city
1,Rahul,Laptop,50000.0,PUNE
2,Amit,Mouse,500.0,MUMBAI
3,Sneha,Keyboard,1500.0,PUNE
4,Rahul,Laptop,50000.0,PUNE
5,Neha,Monitor,0.0,NASHIK
```

---

# Step 12 — Run Silver → Gold Pipeline

```bash
python scripts/silver_to_gold.py
```

Expected Output:

```bash
Silver to Gold completed
```

---

# Step 13 — Verify Gold Layer

```bash
cat gold/city_sales_report.csv
```

Expected Output:

```bash
city,total_sales
MUMBAI,500.0
NASHIK,0.0
PUNE,101500.0
```

---

# Step 14 — Install Tree Command

```bash
sudo apt update
sudo apt install tree -y
```

Verify Installation:

```bash
tree --version
```

Expected Output:

```bash
tree v2.x.x
```

---

# Step 15 — Verify Complete Architecture

```bash
tree
```

Expected Structure:

```bash
.
├── bronze
│   └── sales_raw.csv
├── gold
│   └── city_sales_report.csv
├── scripts
│   ├── bronze_to_silver.py
│   └── silver_to_gold.py
├── silver
│   └── sales_clean.csv
└── venv
```

---

# Architecture Flow

```text
Raw Data
   ↓
Bronze Layer
   ↓
Silver Layer
   ↓
Gold Layer
   ↓
Analytics / Reporting
```

---

# Technologies Used

* Python
* Pandas
* Linux
* Git
* Virtual Environment (venv)

---

# Conclusion

This project successfully demonstrates:

* Raw data ingestion
* Data cleaning and transformation
* Data aggregation
* Layer-based data processing
* Medallion Architecture implementation

Based on Medallion Architecture concepts. 
