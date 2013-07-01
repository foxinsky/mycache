# Design Specification#
## Content
[DB schemas](#db-schemas)  
[Modules](#modules)  
 * [User management](#user-management)
	

## DB schemas ##

**fieldname** - primary key

*fieldname* - secondary key

**Table: users**  
Data in this table is dynamic and updates in the following cases:
 * new user registration
 * existed user changes own profile
 * existed user deletes own profile
 
Field | Type | Description
--- | --- | ---
**user_id** | bigint | autoincrement id
email | varchar() | email, filled on registration
name | varchar | nickname, filled on registration
passwd | varchar | md5 hash from password which filled on registration
*account_type* | byte | (free, premium) link to account_types table
is_active | boolean | Changes after account activation
ctime | timestamp | Unix time of account creation
mtime | timestamp |  Unix time of last account change
dbname | varchar | name for user's DB with finance information


**Table: account_types**  
Data in this table is static and filled up on DB creation procedure.  
Data can be updated only by devs in case of:
 * adding new account type
 * editing existed account type (rare operation)
 * deleting existed account type
 
Field | Type | Description
--- | --- | ---
**acctype_id** | byte | autoincrement id
acctype_str | varchar | string representation of the account (disable, free, premium, extra premium, admin, etc)
acctype_descr | text | short description of the account's feature


## Modules ##

External dependency:

 * python-mysql.connector

#### User management

**is_user_registered**(username=None, email=None):

    Check if user with <username> or <email> has already registered in the system
    you should set at least one parameter
    
    :param username:    Username for checking, default = None
    :param email:       Email address for checking, default = None

    :return 1 or 0:     Return "1" if user is already registered.     

**is_username_valid**(username)

	Check if username is valid. Valid username should be at least 5 alphabetical chars, without numbers and special symbols.

	:return 1 or 0:		Returns "1" if username is valid.



    


#### Authority

#### Charts

#### Category management

#### Bank_Accounts management
#### Buy_Places management
#### Shoping List
#### Analyzing
#### Planned_Events management
#### Bank_deposit_credit
#### Sharing
#### Monetary
#### Backups
#### Aging
#### Feedbacks
#### export_import
#### appserver
