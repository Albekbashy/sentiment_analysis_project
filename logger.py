import psycopg2
import os
from datetime import datetime

def log_sentiment(text: str, sentiment: str):
    """
    Log sentiment prediction to PostgreSQL database.
    
    Args:
        text: Input text that was analyzed
        sentiment: Predicted sentiment (positive/negative)
    """
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "logs-db"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            user=os.getenv("POSTGRES_USER", "sentiment_user"),
            password=os.getenv("POSTGRES_PASSWORD", "sentiment_pass"),
            database=os.getenv("POSTGRES_DB", "sentiment_logs")
        )
        
        cursor = conn.cursor()
        
        # Insert prediction into database
        cursor.execute(
            "INSERT INTO sentiment_logs (text, sentiment, timestamp) VALUES (%s, %s, %s)",
            (text, sentiment, datetime.now())
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("# Log the result to PostgreSQL")
        
    except Exception as e:
        print(f"Warning: Could not log to database: {e}")
