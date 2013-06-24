# Design Specification#
## Content
[DB schemas](#db-schemas)  
[Modules](#modules)  
 * [User management](#user-management)
	

## DB schemas ##

**Table: users**  
Data in this table is dynamic and updates in the following cases:
 * new user registration
 * existed user changes own profile
 * existed user deletes own profile
 
Field | Type | Description
--- | --- | ---
user_id | bigint | autoincrement id
email | varchar() | email, filled on registration
name | varchar | nickname, filled on registration
passwd | varchar | md5 hash from password which filled on registration
account_type | byte | (free, premium) link to account_types table
is_active | boolean | Changes after account activation, 


**Table: account_types**  
Data in this table is static and filled up on DB creation procedure.  
Data can be updated only by devs in case of:
 * adding new account type
 * editing existed account type (rare operation)
 * deleting existed account type
 
Field | Type | Description
--- | --- | ---
acctype_id | byte | autoincrement id
acctype_str | varchar | string representation of the account (disable, free, premium, extra premium, admin, etc)
acctype_descr | text | short description of the account's feature


## Modules ##

#### User management

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
