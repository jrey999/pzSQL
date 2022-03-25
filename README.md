# PZSQL

```bash
pip install pzSQL
```

### A half finished wrapper around psycopg2 that makes it a bit more elegant to use

```from pzSQL.pzSQL import Db```
####
####
```db = Db(db_name, user, password, host)```
####
```data = db.select("SELECT * FROM table")```

returns data without using ```fetchall()```
