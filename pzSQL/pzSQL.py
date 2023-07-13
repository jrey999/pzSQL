import psycopg2 as pgsql


class Db:

    def __init__(self, name, user, code, host):

        self.name = name
        self.user = user
        self.code = code
        self.host = host
        self.cursor = self.connection.cursor()

    @property
    def connection(self):

        return pgsql.connect(dbname=self.name, user=self.user, password=self.code, host=self.host)

    def close_connection(self):
        """closes connection to database"""
        self.connection.close()

    def select(self, query_string: str) -> list[tuple]:
        """executes query and returns data"""
        self.cursor.execute(query_string)
        return self.cursor.fetchall()


    def select_json(self, query_string: str) -> list[dict]:

        """executes query and returns data as a list of dictionaries"""
        self.cursor.execute(f"SELECT json_agg(__temp_table__) FROM ({query_string}) __temp_table__;")
        return self.cursor.fetchall()

    def select_where(self, query_string: str, params: tuple) -> list[tuple]:

        self.cursor.execute(query_string, params)
        return self.cursor.fetchall()

    def select_where_json(self, query_string: str, params: tuple) -> list[dict]:

        self.cursor.execute(f"SELECT json_agg(__temp_table__) FROM ({query_string}) __temp_table__;", params)
        return self.cursor.fetchall()

    def insert(self, statement: str, values: list or tuple or dict):
        """writes query to database"""
        return self.cursor.execute(statement, tuple(values.values()) if isinstance(values, dict) else tuple(values))

    def commit_transactions(self):
        """commits transaction to database"""
        self.connection.commit()

    def commit_and_close_connection(self):
        """commits transaction and closes connection"""
        self.commit_transactions()
        self.connection.close()

    def insert_and_commit(self, statement: str, values: list or tuple or dict):
        """writes query to database and commits transaction"""
        insert = self.insert(statement, values)
        self.commit_transactions()
        return insert
    
    def restart_connection(self):
        """closes connection and starts new one"""
        self.connection.close()
        self.connection

    def rollback(self):
        """rollsback statements"""
        self.cursor.execute("ROLLBACK")

    #def update(self, statement, values):
     #   """updates row(s) in database"""
     #   return self.cusrsore.execute(statement, tuple(_ for _ in row[1:]) + (row[0],))

    #def update_and_commit(self, statement, values):
     #   """updates row(s) in database and commits transactions"""
      #  update = self.update(statement, values)
       # self.commit_transactions()
        #return update

    def switch_database(self, database):

        self.name = database
        return self.connection