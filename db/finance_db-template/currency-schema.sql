CREATE  TABLE IF NOT EXISTS `finance_db-template`.`currency` (
  `idcurrency` INT NOT NULL AUTO_INCREMENT ,
  `currency_name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idcurrency`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Table for currency info'
