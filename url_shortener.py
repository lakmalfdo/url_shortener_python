import sys
import hashlib
import sqlite3
import re

class URLShortener:
    SHORT_URL_BASE = "https://short.url/"

    def __init__(self, db_name="url_shortener.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Create a table to store URL mappings if it doesn't exist
        self.cursor.execute("CREATE TABLE IF NOT EXISTS url_mappings (id INTEGER PRIMARY KEY, original_url TEXT NOT NULL, short_url TEXT NOT NULL)")
        self.conn.commit()

    def shorten_url(self, original_url):
        # Check if the URL is already in the database
        self.cursor.execute("SELECT short_url FROM url_mappings WHERE original_url=?", (original_url,))
        result = self.cursor.fetchone()
        if result:
            return result[0]

        short_url = self.SHORT_URL_BASE + hashlib.md5(original_url.encode()).hexdigest()[:8]

        # Store the URL mapping in the database
        self.cursor.execute("INSERT INTO url_mappings (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
        self.conn.commit()

        return short_url

    def expand_url(self, short_url):
        self.cursor.execute("SELECT original_url FROM url_mappings WHERE short_url=?", (short_url,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

def validate_url(url):
    # Simple URL validation using regex
    url_pattern = re.compile(r'^https?://.+')
    return bool(url_pattern.match(url))

def display_usage():
    print("Usage: python url_shortener.py -[s/e] <URL>")
    print("Use -s to shorten a URL or -e to expand a URL.")

def main():
    if len(sys.argv) != 3:
        display_usage()
        sys.exit(1)

    option = sys.argv[1]
    url = sys.argv[2]

    if not validate_url(url):
        display_usage()
        print("Error: Invalid URL. Please provide a valid URL.")
        sys.exit()

    shortener = URLShortener()

    if option == "-s":
        short_url = shortener.shorten_url(url)
        print(f"Shortened URL: {short_url}")
    elif option == "-e":
        expanded_url = shortener.expand_url(url)
        if expanded_url:
            print(f"Expanded URL: {expanded_url}")
        else:
            print("Error: The provided short URL does not exist in the database.")
    else:
        display_usage()

if __name__ == '__main__':
    main()