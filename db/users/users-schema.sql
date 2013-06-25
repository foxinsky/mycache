CREATE TABLE users (
	user_id	bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(20) NOT NULL UNIQUE, 
	name varchar(20) NOT NULL UNIQUE,
	passwd binary(20) NOT NULL,
	account_type int NOT NULL,
	is_active boolean default 0,
	dbname varchar(20) NOT NULL,
	ctime timestamp DEFAULT CURRENT_TIMESTAMP(),
	mtime timestamp On update current_timestamp(),
	PRIMARY KEY (user_id),	
)	ENGINE=InnoDB DEFAULT CHARSET=utf8;
