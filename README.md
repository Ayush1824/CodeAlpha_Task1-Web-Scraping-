# CodeAlpha Internship - Task 1: Web Scraping with Octoparse

## 📌 Project Overview
This project is part of my CodeAlpha internship.  
For Task 1, I used **Octoparse** (a no-code web scraping tool) to extract the IMDb Top 250 Movies list and saved it into a CSV file.

## 🛠️ Tools Used
- **Octoparse** – For building and running the scraping workflow
- **CSV** – For storing the scraped data

## 📂 Files in Repository
- `imdb_top_250.csv` → Output CSV containing movie data scraped from IMDb
- `README.md` → Project documentation

## 📊 Data Extracted
The scraper collects:
- 🎬 Movie Title  
- 📅 Release Year  
- ⭐ IMDb Rating  

## 🚀 How I Did It
1. Opened Octoparse and created a **new task** for IMDb Top 250.
2. Configured the workflow to:
   - Load the IMDb Top 250 page.
   - Extract movie title, year, and rating.
   - Loop through all pages (if applicable).
3. Ran the workflow and exported the results to a CSV file.

## 📌 Output
The scraper generated:
