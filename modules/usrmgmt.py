import pprint
import config
import re
import mysql.connector
#from mysql.connector import errorcode

dbconfig  = {
  'user': config.dbuser,
  'password': config.dbpasswd,
  'host': config.dbhost,
  'database': config.dbname,
}

def is_user_registered(username=None, email=None):
    """
    Check if user with <username> or <email> has already registered in the system
    you should set at least one parameter
    
    :param username:    Username for checking, default = None
    :param email:       Email address for checking, default = None
    
    """

    try:
        cnx = mysql.connector.connect(**dbconfig)
    except mysql.connector.Error as err:
        print(err)
        
    cursor = cnx.cursor()
    if username is not None:
        query = ("SELECT name FROM users WHERE name = %s")
        cursor.execute(query, (username,))
    elif email is not None:
        query = ("SELECT email FROM users WHERE email = %s")
        cursor.execute(query, (email,))
    else:
        return 0
            
    rez = cursor.fetchall()
    cursor.close()
    cnx.close()
    
    if len(rez) > 0:
        retcode = 1
    else: 
        retcode = 0
        
    return retcode


def is_username_valid(username):
    
    rez = re.match(r'^[A-z][A-z|\.|\s]+$',username) != None
    retcode = 0
    return rez

def is_email_valid(email):

    rez = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*(\+[_a-z0-9-]+)@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None
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
      
    :param username:    Nickname, name of user
    :param passwd:  Password in plain-text format
    :param email:       Email address of the new user
    :param account_type:    Define type of user account - admin, free, premium, etc
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
