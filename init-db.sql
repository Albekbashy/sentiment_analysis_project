-- Database initialization script for sentiment analysis logs
-- This runs automatically when the PostgreSQL container starts

-- Create sentiment_logs table
CREATE TABLE IF NOT EXISTS sentiment_logs (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    sentiment VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster timestamp queries
CREATE INDEX IF NOT EXISTS idx_timestamp ON sentiment_logs(timestamp);

-- Create index for sentiment filtering
CREATE INDEX IF NOT EXISTS idx_sentiment ON sentiment_logs(sentiment);

-- Insert sample data for testing
INSERT INTO sentiment_logs (text, sentiment) VALUES
    ('This is a great product!', 'positive'),
    ('Terrible experience', 'negative'),
    ('Amazing work!', 'positive');

-- Display confirmation
SELECT 'Database initialized successfully!' AS status;