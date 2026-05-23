# Medallion Architecture Activity

## Project Overview

This activity demonstrates the implementation of **Medallion Architecture** using:

* Bronze Layer → Raw Data
* Silver Layer → Cleaned Data
* Gold Layer → Business Report

Server Used:

```bash
20.110.145.182
```

---

# Step 1 — Connect to Server

```bash
ssh azureuser@20.110.145.182
```

---

# Step 2 — Create Project Directory

```bash
mkdir -p ~/medallion-activity
cd ~/medallion-activity
```

---

# Step 3 — Create Architecture Folders

```bash
mkdir -p bronze silver gold scripts
```

Verify:

```bash
ls
```

Expected Output:

```bash
bronze  gold  scripts  silver
```

---

# Step 4 — Install Required Packages

```bash
sudo apt update
sudo apt install python3-venv python3-pip tree -y
```

---

# Step 5 — Create Python Virtual Environment

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

# Step 6 — Install Pandas

```bash
pip install pandas
```

Verify Installation:

```bash
python -c "import pandas; print(pandas.__version__)"
```

---

# Step 7 — Create Bronze Layer Data

```bash
cat > bronze/sales_raw.csv <<'EOF'
id,name,product,amount,city
1,Rahul,Laptop,50000,Pune
2,Amit,Mouse,500,Mumbai
3,Sneha,Keyboard,1500,Pune
4,Rahul,Laptop,50000,Pune
5,Neha,Monitor,,Nashik
EOF
```

Verify File:

```bash
cat bronze/sales_raw.csv
```

---

# Step 8 — Create Bronze → Silver Script

```bash
cat > scripts/bronze_to_silver.py <<'EOF'
import pandas as pd

df = pd.read_csv("bronze/sales_raw.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["amount"] = df["amount"].fillna(0)

# Standardize city names
df["city"] = df["city"].str.upper()

# Save cleaned data
df.to_csv("silver/sales_clean.csv", index=False)

print("Bronze to Silver completed")
EOF
```

---

# Step 9 — Run Bronze → Silver Pipeline

```bash
python scripts/bronze_to_silver.py
```

Expected Output:

```bash
Bronze to Silver completed
```

---

# Step 10 — Verify Silver Layer

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

# Step 11 — Create Silver → Gold Script

```bash
cat > scripts/silver_to_gold.py <<'EOF'
import pandas as pd

df = pd.read_csv("silver/sales_clean.csv")

gold = df.groupby("city")["amount"].sum().reset_index()

gold.columns = ["city", "total_sales"]

gold.to_csv("gold/city_sales_report.csv", index=False)

print("Silver to Gold completed")
EOF
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
