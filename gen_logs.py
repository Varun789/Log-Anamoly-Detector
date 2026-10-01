import csv
import random
from datetime import datetime, timedelta

def generate_synthetic_logs(filename="server_logs.csv", num_records=1000):
    endpoints = ["/home", "/login", "/api/data", "/checkout"]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "endpoint", "status_code", "response_time_ms"])
        
        start_time = datetime.now()
        
        for i in range(num_records):
            timestamp = (start_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
            endpoint = random.choice(endpoints)
            
            # Injecting anomalies roughly 3% of the time
            if random.random() < 0.03:
                status_code = random.choice([500, 502, 503])
                response_time_ms = random.randint(1500, 5000) # High latency anomaly
            else:
                status_code = random.choice([200, 201, 301])
                response_time_ms = random.randint(20, 250)    # Normal latency
                
            writer.writerow([timestamp, endpoint, status_code, response_time_ms])
            
    print(f"[*] Generated {num_records} log entries in {filename}")

if __name__ == "__main__":
    generate_synthetic_logs()