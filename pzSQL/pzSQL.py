import psycopg2 as pgsql


class Db:

    def __init__(self, name, user, code, host):

        self.name = name
        self.user = user
        self.code = code
        self.host = host
        self.connection = pgsql.connect(dbname=self.name, user=self.user, password=self.code, host=self.host)
        self.cursor = self.connection.cursor()

    def close_connection(self):

        self.connection.close()

    def select(self, query_string):

        self.cursor.execute(query_string)
        return self.cursor.fetchall()

    def insert(self, statement, values):

        return self.cursor.execute(statement, values)

    def commit_transactions(self):

        self.connection.commit()

    def insert_and_commit(self, statement, values):

        insert = self.insert(statement, values)
        self.commit_transactions()
        return insert

    def commit_and_close_connection(self):
    
        self.commit_transactions()
        self.connection.close()
    
    def restart_connection(self):
        
        self.connection.close()
        self.connection = pgsql.connect(dbname=self.name, user=self.user, password=self.code, host=self.host)

    def rollback(self):

        self.cursor.execute("ROLLBACK")

    def update(self, statement, values):
 
        return self.cusrsore.execute(statement, tuple(_ for _ in row[1:]) + (row[0],))

    def update_and_commit(self, statement, values):

        update = self.update(statement, values)
        self.commit_transactions()
        return update