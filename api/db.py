import mysql.connector as mysql

cnx= mysql.MySQLConnection(
	host="db-server-evergreenscastri.mysql.database.azure.com",
	port = 3306,
	user= "evergreenscastri@db-server-evergreenscastri",
	password= "cwdSGL91",
	database = "evergreen",
)