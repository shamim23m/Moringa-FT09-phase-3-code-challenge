from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implementation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid  # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        # Pass the fetched data as arguments to the Magazine constructor
        print(Magazine(magazine[0], magazine[1], magazine[2]))

    print("\nAuthors:")
    for author in authors:
        # Pass the fetched data as arguments to the Author constructor
        print(Author(author[0], author[1]))

    print("\nArticles:")
    for article in articles:
        # First, fetch the Author and Magazine objects using the author_id and magazine_id
        author = Author(article[3], None)  # You can fetch the author data using article[3] (author_id)
        magazine = Magazine(article[4], None, None)  # Fetch the magazine using article[4] (magazine_id)
        print(Article(article[0], article[1], article[2], author, magazine))
        
if __name__ == "__main__":
    main()
