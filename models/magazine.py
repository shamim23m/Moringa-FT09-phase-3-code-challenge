from database.connection import get_db_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self._id = id
        self._name = name
        self._category = category

    def create_magazine(self, name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    def read_magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (self._id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine

    def update_magazine(self, new_name, new_category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE magazines SET name = ?, category = ? WHERE id = ?', (new_name, new_category, self._id))
        conn.commit()
        conn.close()
        self._name = new_name
        self._category = new_category

    def delete_magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM magazines WHERE id = ?', (self._id,))
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
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def _repr_(self):
        return f'<Magazine {self._name}, Category: {self._category}>'