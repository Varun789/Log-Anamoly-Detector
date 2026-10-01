import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(log_file="server_logs.csv", output_file="anomalies.csv"):
    print(f"[*] Loading logs from {log_file}...")
    try:
        df = pd.read_csv(log_file)
    except FileNotFoundError:
        print("[!] Log file not found. Run generate_logs.py first.")
        return

    features = df[['response_time_ms']]

    print("[*] Training Isolation Forest model...")

    model = IsolationForest(contamination=0.05, random_state=42) 
    

    df['anomaly_score'] = model.fit_predict(features)

    anomalies = df[df['anomaly_score'] == -1]

    print(f"[*] Analysis complete. Found {len(anomalies)} anomalies out of {len(df)} logs.")
    
    if not anomalies.empty:
        anomalies.to_csv(output_file, index=False)
        print(f"[*] Anomalies saved to {output_file} for SRE review.")
        print("\nSample Anomalies Detected:")
        print(anomalies[['timestamp', 'endpoint', 'status_code', 'response_time_ms']].head())
    else:
        print("[*] No anomalies detected. System is healthy.")

if __name__ == "__main__":
    detect_anomalies()