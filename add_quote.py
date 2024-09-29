import redis

def add_quote(quote, author):
    # Connect to the Redis database
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # Format the quote with the author
    formatted_quote = f"{quote} - {author}"

    # Store the quote in Redis
    r.rpush("quotes", formatted_quote)
    print("Quote added to the database.")

if __name__ == "__main__":
    new_quote = input("Enter the quote: ")
    author_name = input("Enter the author's name: ")
    add_quote(new_quote, author_name)

