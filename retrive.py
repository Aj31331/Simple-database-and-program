import sqlite3

def main():

    db = sqlite3.connect('movies.db')
    cursor = db.cursor()

    for row in cursor.execute('SELECT * from movies'):
      print(row)


if __name__ == '__main__':
    main()
