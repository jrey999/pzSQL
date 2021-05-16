# PZSQL

### A half finished wrapper around psycopg2 that makes it a bit more elegant to use

```from pzSQL.connect import DB


db = Db(db_name, user, password, host=host)```
&nbsp;

```data = db.select("SELECT * FROM table")```
