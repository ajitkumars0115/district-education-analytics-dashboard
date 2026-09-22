# District Education Analytics Dashboard

An end-to-end data analytics project that cleans, analyzes, and visualizes 
school-level data for a district, using Python, SQL Server, and Power BI.

## Overview
This project takes raw school infrastructure data, cleans and anonymizes it 
for privacy, loads it into SQL Server for analysis, and presents the 
findings through an interactive Power BI dashboard.

## Tools & Technologies
- **Python (pandas)** — data cleaning and anonymization
- **SQL Server** — data storage and analysis queries
- **Power BI** — interactive dashboard and visualization

## Project Workflow
1. **Data Cleaning** — Removed sensitive/personal columns (names, phone 
   numbers, emails) and anonymized school names using Python (pandas).
2. **SQL Analysis** — Loaded the cleaned data into SQL Server and wrote 
   queries to analyze school distribution, operational status, and more.
3. **Dashboard** — Built an interactive Power BI dashboard with KPI cards, 
   charts, and slicers for filtering by block and location type.

## Key Insights
- The district has **2,351 schools** in total.
- **93% of schools are in rural areas**, only 7% are urban.
- **PATEPUR block** has the highest number of schools (247), while 
  **DESARI block** has the lowest (56).
- 100% of schools fall under **Government (Dept. of Education)** management.
- Only **13% of schools** offer education up to Higher Secondary level — 
  the majority (87%) are limited to Primary/Upper Primary.
- **126 schools (5%)** are permanently closed, with RAGHOPUR block 
  showing the highest closure count.

## Files in this Repository
- `clean_school_data.py` — Python script for data cleaning and anonymization
- `school_analysis_queries.sql` — SQL queries used for analysis
- `screenshots/` — Power BI dashboard screenshots

## Dashboard Preview
(Screenshots added in the `screenshots` folder)

## Note on Data Privacy
The original dataset contained sensitive information (school names, 
head of school details, contact numbers, emails). All personal and 
identifying information has been removed or anonymized before being 
used in this project.
