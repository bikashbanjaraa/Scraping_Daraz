# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        # Create SQLite connection and cursor
        self.conn = sqlite3.connect('scrapy_items.db')
        self.cursor = self.conn.cursor()
        # Create a table for your items if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                ID integer primary key,
                url TEXT,
                image TEXT,
                name TEXT,
                rating REAL,
                price REAL,
                sold INTEGER
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        # Close SQLite connection when spider is done
        self.conn.close()

    def process_item(self, item, spider):
        # Insert item into the database
        self.cursor.execute('''
            INSERT INTO items (url, image, name, rating, price, sold)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item.get('url'),
            item.get('image'),
            item.get('name'),
            item.get('rating'),
            item.get('price'),
            item.get('sold')
        ))
        self.conn.commit()
        return item