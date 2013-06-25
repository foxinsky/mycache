CREATE TABLE account_types (
	acctype_id tinyint NOT NULL UNSIGNED,
	acctype_str varchar (20) NOT NULL,
	acctype_descr text,
	PRIMARY KEY(acctype_id)	
)	ENGINE=InnoDB DEFAULT CHARSET=utf8;
