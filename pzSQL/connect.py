import psycopg2 as pgsql


class Db:

    def __init__(self, db_name, user, password, host):

        self.db_name = db_name
        self.user = user
        self.code = password
        self.host = host
        self.connection = pgsql.connect(dbname=self.db_name, user=self.user, password=self.code, host=self.host)
        self.cursor = self.connection.cursor()

    def select(self, query_string):

        self.cursor.execute(query_string)
        return self.cursor.fetchall()

    def insert(self, statement, values):

        return self.cursor.execute(statement, values)

    def close_connection(self):

        self.connection.close()

    def commit_transactions(self):

        self.connection.commit()

    def commit_and_close_connection(self):
    
        self.commit_transactions()
        self.connection.close()
    
    def restart_connection(self):
        
        self.connection.close()
        self.connection = pgsql.connect(dbname=self.name, user=self.user, password=self.code, host=self.host)

    def rollback(self):

        self.cursor.execute("ROLLBACK")
