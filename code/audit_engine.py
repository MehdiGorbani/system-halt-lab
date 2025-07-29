import pandas as pd
import json
import os

class AuditEngine:
    def __init__(self, csv_path="data/integrity_audit_events.csv", json_path="data/integrity_audit_events.json"):
        self.csv_path = csv_path
        self.json_path = json_path
        self.data = None

    def load_csv(self):
        """Load audit events from CSV."""
        if os.path.exists(self.csv_path):
            self.data = pd.read_csv(self.csv_path)
            print("Loaded CSV data successfully.")
        else:
            print(f"Error: {self.csv_path} not found.")
            self.data = pd.DataFrame()

    def load_json(self):
        """Load audit events from JSON."""
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as f:
                self.data = pd.DataFrame(json.load(f))
                print("Loaded JSON data successfully.")
        else:
            print(f"Error: {self.json_path} not found.")
            self.data = pd.DataFrame()

    def analyze_events(self):
        """Analyze audit events (e.g., count events by type)."""
        if self.data.empty:
            print("No data to analyze.")
            return
        event_counts = self.data['event_type'].value_counts()
        print("Event Type Counts:\n", event_counts)

    def save_report(self, output_path="audit_report.txt"):
        """Save a simple analysis report."""
        with open(output_path, 'w') as f:
            f.write("Audit Engine Report\n")
            f.write("==================\n")
            if not self.data.empty:
                f.write(str(self.data.describe()))
            else:
                f.write("No data available.")

if __name__ == "__main__":
    engine = AuditEngine()
    engine.load_csv()  # Or load_json() for JSON data
    engine.analyze_events()
    engine.save_report()
