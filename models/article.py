from database.connection import get_db_connection

class Article:
    def __init__(self, id=None, title=None, content=None, author=None, magazine=None):
        self._id = id
        self._title = title
        self._content = content
        self._author = author
        self._magazine = magazine

    def create_article(self, title, content, author, magazine):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (title, content, author.id, magazine.id))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    def read_article(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE id = ?', (self._id,))
        article = cursor.fetchone()
        conn.close()
        return article

    def update_article(self, new_title, new_content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE articles SET title = ?, content = ? WHERE id = ?', (new_title, new_content, self._id))
        conn.commit()
        conn.close()
        self._title = new_title
        self._content = new_content

    def delete_article(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE id = ?', (self._id,))
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
     return self._title

    @title.setter
    def title(self, value):
     if hasattr(self, '_title'):  # Title should not change after initialization
        raise AttributeError("Title cannot be changed after the article is created.")
     if len(value) < 5 or len(value) > 50:
        raise ValueError("Title must be between 5 and 50 characters.")
     self._title = value


    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def _repr_(self):
        return f'<Article {self._title}, Author: {self._author.name}, Magazine: {self._magazine.name}>'
