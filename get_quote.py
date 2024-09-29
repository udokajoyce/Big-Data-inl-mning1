import redis
import random

def get_random_quote():
    # Connect to the Redis database
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # Get all quotes
    quotes = r.lrange("quotes", 0, -1)
    
    if quotes:
        # Select a random quote
        random_quote = random.choice(quotes).decode("utf-8")
        print("Random Quote:", random_quote)
    else:
        print("No quotes found in the database.")

if __name__ == "__main__":
    get_random_quote()

