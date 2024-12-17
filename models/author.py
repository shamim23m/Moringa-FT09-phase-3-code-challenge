from database.connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name

    def create_author(self, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    def read_author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (self._id,))
        author = cursor.fetchone()
        conn.close()
        return author

    def update_author(self, new_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE authors SET name = ? WHERE id = ?', (new_name, self._id))
        conn.commit()
        conn.close()
        self._name = new_name

    def delete_author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM authors WHERE id = ?', (self._id,))
        conn.commit()
        conn.close()
        
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be modified after initialization.")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT articles.* FROM articles
            JOIN authors_articles ON articles.id = authors_articles.article_id
            WHERE authors_articles.author_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT magazines.* FROM magazines
            JOIN authors_magazines ON magazines.id = authors_magazines.magazine_id
            WHERE authors_magazines.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def _repr_(self):
        return f'<Author {self._name}>'