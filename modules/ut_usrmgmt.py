import usrmgmt

print
print "User Management unit tests"
print

# db_open
cnx = usrmgmt.db_open()
if cnx is not None:
    rez = " *** PASSED"
else:
    rez = " !!! FAILED"
print " db_open"+rez    

# db_close
usrmgmt.db_close(cnx)
print " db_close ???"
print

#is_user_registered
##  existed username
rez=usrmgmt.is_user_registered("user1")
if rez:
    print " is_user_registered(\"user1\") == "+str(rez)+" *** PASSED"
else:
    print " is_user_registered(\"user1\") == "+str(rez)+" !!! FAILED"
##  existed email
rez = usrmgmt.is_user_registered(email="email1")
if rez:
    print " is_user_registered(email=\"email1\") == "+str(rez)+" *** PASSED"
else:
    print " is_user_registered(email=\"email1\") == "+str(rez)+" !!! FAILED"
##  existed username and email
rez = usrmgmt.is_user_registered("user1", "email1")
if rez:
    print " is_user_registered(\"user1\", \"email1\") == "+str(rez)+" *** PASSED"
else:
    print " is_user_registered(\"user1\", \"email1\") == "+str(rez)+" !!! FAILED"
##  NOT-existed username
rez = usrmgmt.is_user_registered("user159")
if rez:
    print " is_user_registered(\"user159\") == "+str(rez)+" !!! FAILED"
else:
    print " is_user_registered(\"user159\") == "+str(rez)+" *** PASSED"
##  NOT-existed email
rez = usrmgmt.is_user_registered(email="email159")
if rez:
    print " is_user_registered(email=\"email159\")  == "+str(rez)+" !!! FAILED"
else:
    print " is_user_registered(email=\"email159\")  == "+str(rez)+" *** PASSED"
print

#is_username_valid
rez = usrmgmt.is_username_valid('John')
if rez:
    print " is_username_valid('John') == "+str(rez)+" *** PASSED"
else:
    print " is_username_valid('John') == "+str(rez)+" !!! FAILED"
       
rez = usrmgmt.is_username_valid('John1')
if rez:
    print " is_username_valid('John1') == "+str(rez)+" !!! FAILED"
else:
    print " is_username_valid('John1') == "+str(rez)+" *** PASSED"
    
rez = usrmgmt.is_username_valid('John!')
if rez:
    print " is_username_valid('John!') == "+str(rez)+" !!! FAILED"
else:
    print " is_username_valid('John!') == "+str(rez)+" *** PASSED"
print

#is_email_valid
rez = usrmgmt.is_email_valid('user.name+somepart@server.com')
if rez:
    print " is_email_valid('user.name+somepart@server.com') == "+str(rez)+" *** PASSED"
else:
    print " is_email_valid('user.name+somepart@server.com') == "+str(rez)+" !!! FAILED"

rez = usrmgmt.is_email_valid('user.name@somepart@server.com')
if rez:
    print " is_email_valid('user.name@somepart@server.com') == "+str(rez)+" !!! FAILED"
else:
    print " is_email_valid('user.name@somepart@server.com') == "+str(rez)+" *** PASSED"
print
