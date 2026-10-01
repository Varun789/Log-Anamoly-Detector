# Log Anomaly Detector 

Basic project which automatically detect anomalous behavior in server logs, eliminating the need for hardcoded monitoring thresholds.

## Overview
 

This project demonstrates how to apply an **Isolation Forest** (an unsupervised machine learning algorithm) to operational data to automatically flag unusual spikes in latency and error rates.

## Tech Stack
* **Python 3.9**: Core logic and scripting.
* **Scikit-Learn**: Machine learning (Isolation Forest).
* **Pandas**: Data manipulation and feature extraction.
* **Docker**: Containerization for reproducible environments.

## How the AI Works ?
The `detector.py` script uses an **Isolation Forest**. 
1. It looks at the `response_time_ms` feature of our server logs.
2. It builds a forest of random decision trees to isolate individual data points.
3. Because anomalies (like a 4000ms response time on a usually 100ms endpoint) are sparse and different, they get isolated faster (closer to the root of the tree).
4. Data points with short average path lengths are flagged as `-1` (Anomaly).

##  Getting Started

### Option 1: Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Varun789/Log-Detector.git
   cd Log-Detector
   
   
   ```
   Create virtual environment and activate it and then execute

   ```
pip install -r requirements.txt
python gen_logs.py
python detector.py
   ```

2. Run container
```
docker build -t log-detector .
docker run --rm log-detector
```
