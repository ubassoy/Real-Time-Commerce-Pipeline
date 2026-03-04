from kafka import KafkaConsumer
from json import loads
import requests
import pandas as pd
from datetime import datetime
import os
import json

API_ENDPOINT = os.getenv('POWER_BI_ENDPOINT')

topic_name = 'rta' [cite: 10]

if __name__ == "__main__": [cite: 10]
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers='localhost:9092', [cite: 10]
        value_deserializer=lambda m: json.loads(m.decode('utf-8')) [cite: 10]
    )
    
    print("Consumer started... Listening for messages.")
    
    for message in consumer: [cite: 10]
        # Accessing the message content
        content = message[6] [cite: 10]
        d = json.loads(content[1:-1]) [cite: 10]
        
        # FIXING THE ERRORS:
        # 1. item_id conversion 
        item_id = int(d['item_id']) [cite: 10]
        
        # 2. sku conversion 
        sku = str(d['sku']) [cite: 10]
        
        # 3. FIX: Changed int() to float() to handle decimals like '161.25' [cite: 9, 11]
        price = float(d['price']) 
        
        time_stamp = datetime.now().isoformat() [cite: 10]
        
        # Create DataFrame for the record 
        dt = pd.DataFrame({
            'item_id': [item_id], 
            'sku': [sku], 
            'price': [price], 
            'time': [time_stamp]
        }) [cite: 10]
        
        # Convert to JSON for the API request 
        data = dt.to_json(orient='records') [cite: 10]
        
        # Pushing data to Power BI
        if API_ENDPOINT:
            req = requests.post(API_ENDPOINT, data) [cite: 10]
            print(f"Status: {req.status_code} | Data Pushed: {sku} at ${price}") [cite: 7]
        else:
            print("Error: POWER_BI_ENDPOINT environment variable not found.")
