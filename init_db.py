import redis
import requests

def initialize_db():
    # Connect to the Redis database
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # Fetch quotes from the API
    response = requests.get("https://dummyjson.com/quotes")
    quotes = response.json()['quotes']

    # Store quotes in Redis
    for quote in quotes:
        r.rpush("quotes", f"{quote['quote']} - {quote['author']}")

    print("Database initialized with quotes.")

if __name__ == "__main__":
    initialize_db()

