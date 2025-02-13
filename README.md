# Email Automation Script  

## Overview  
This project automates email data collection by extracting links, modifying URLs, and retrieving emails from web pages. It consists of three Python scripts that work together to streamline the data extraction process.  

### 1️⃣ Link Collection Auto (`link_collection.py`)  
- Automates the extraction of **target URLs** from specified sources.  
- Stores collected links for further processing.  

### 2️⃣ URL Modifier (`url_modifier.ipynb`)  
- Processes and refines the collected URLs to ensure correct formatting.  
- Prepares the links for the final data extraction phase.  

### 3️⃣ Main Data Auto (`main_data_auto.ipynb`)  
- Extracts **email addresses** and other relevant information from the modified URLs.  
- Handles data parsing and storage efficiently.  

## ⚙️ Installation & Setup  

### Prerequisites  
Ensure you have **Python 3.x** installed on your system.  

### Steps  
1. Clone the repository and navigate to the project directory:  
   ```bash
   git clone <repo-url>
   cd <repo-folder>

## 📋 Requirements
The script requires the following Python packages:

- pandas – Data manipulation and storage
- asyncio – Asynchronous operations
- playwright – Browser automation
- playwright-stealth – Bypassing bot detection
- nest_asyncio – Running async functions in Jupyter or nested loops
- os – File and system operations
- re – Regular expressions for data extraction
- cloudscraper
- Time
- Random

## 🚀 Usage

1. Run link_collection.py to gather target URLs

2. Execute url_modifier.py to refine and modify the collected links

3. Run main_data_auto.py to extract emails and store the final dataset

## ⚠️ Known Issues & Considerations
- Cloudflare Protection: The script currently bypasses Cloudflare protection successfully, but continued monitoring is required.
- Optimization: The script is functional but may require further tuning for efficiency.

## 👥 Contributors
Nikhil Ratnakar
Sourabh
