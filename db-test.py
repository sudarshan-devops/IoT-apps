import MySQLdb
table="test1"
db=MySQLdb.connect("localhost","root","12345","testdb")
cursor = db.cursor()
cursor.execute("drop table if exists "+table)
sql="create table " +table+ "(DateTime varchar(10),temperature varchar(5),humidity varchar(5))"
cursor.execute(sql)
db.close()
