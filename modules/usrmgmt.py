import pprint
import config
import mysql.connector
#from mysql.connector import errorcode

dbconfig  = {
  'user': config.dbuser,
  'password': config.dbpasswd,
  'host': config.dbhost,
  'database': config.dbname,
}

def isUserRegistered(username, email):
	"""
	Check if user with <username> or <email> has already registered in the system
	
	:param username:	Username for checking
	:param email:		Email address for checking
	
	"""

	try:
		cnx = mysql.connector.connect(**dbconfig)
	except mysql.connector.Error as err:
		print(err)
		
	#normal flow
	cursor = cnx.cursor()
	query = ("SELECT name FROM users WHERE email = %s")
	cursor.execute(query, (email,))
	rez = cursor.fetchall()
	pprint.pprint(rez)
	cursor.close()
	cnx.close()
		
	retcode = 0
	return retcode

def isUserValid(username, email):

	retcode = 0
	return retcode



def UserAdd(username, passwd, email, account_type = 1):
	"""
	Add appropriate record about user to the database. Current workflow is the following:
	  - check if username valid 
	  - check if user has already registered using username or email  
	  - create userDB
	  - add record about new user
	  - send verification email
	  
	Parameters:
	  
	:param username:	Nickname, name of user
	:param passwd:	Password in plain-text format
	:param email:		Email address of the new user
	:param account_type:	Define type of user account - admin, free, premium, etc
						Default account type is free.
						
	  
	"""
	
	try:
		cnx = mysql.connector.connect(**dbconfig)
	except mysql.connector.Error as err:
		print(err)
	
	cursor = cnx.cursor()
	query = ("INSERT INTO users "
			 "(email, name, passwd, dbname) "
			 "VALUES (%s, %s, %s, %s)")	
	query_values = (email, username, passwd, 'testuser_db')
		 
	cursor.execute(query, query_values)	
	cnx.commit()
	
	cursor.close()
	cnx.close()	
	retcode = 0
	return retcode

def UserDel():

	retcode = 0
	return retcode



def UserInfo():
	retcode = 0
	return retcode

def UserList():
	retcode = 0
	return retcode

def UserMod():
	retcode = 0
	return retcode

def UserDBCreate():
	retcode = 0
	return retcode

def UserDBDrop():
	retcode = 0
	return retcode


def AcctypeAdd():
	retcode = 0
	return retcode

def AcctypeDel():
	retcode = 0
	return retcode

def AcctypeList():
	retcode = 0
	return retcode
