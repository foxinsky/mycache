CREATE  TABLE IF NOT EXISTS `finance_db-template`.`category` (
  `idcategory` INT NOT NULL AUTO_INCREMENT ,
  `cat_name` VARCHAR(45) NOT NULL ,
  `cat_type` ENUM('in', 'out') NOT NULL ,
  PRIMARY KEY (`idcategory`) )
ENGINE = InnoDB