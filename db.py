import sqlite3

DB_PATH="wiki.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute( """
            CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE,
            title TEXT,
            summary TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                from_url TEXT,
                to_url TEXT,
                PRIMARY KEY (from_url, to_url)
            )
        """)

def insert_page(url, title, summary):
    with get_connection() as conn:
        conn.execute("INSERT OR IGNORE INTO pages(url, title, summary) VALUES (?,?,?)", (url,title,summary))

def insert_link(from_url, to_url):
    with get_connection() as conn:
        conn.execute("INSERT OR IGNORE INTO links(from_url, to_url) VALUES (?,?)", (from_url,to_url))
def get_pages():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM pages").fetchall()

def get_links():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM links").fetchall()