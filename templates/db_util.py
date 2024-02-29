import mysql.connector

class AddTask:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host='MYSQL_HOST',
            user='MYSQL_USER',
            password='MYSQL_PASSWORD',
            database='MYSQL_DB'
        )

    def add_task(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        self.db_connection.commit()
        cursor.close()

    def view_task(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        tasks = cursor.fetchall()
        cursor.close()
        return tasks

    def delete_task(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        self.db_connection.commit()
        cursor.close()

    def update_task(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        self.db_connection.commit()
        cursor.close()

