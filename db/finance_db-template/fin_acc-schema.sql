CREATE  TABLE IF NOT EXISTS `finance_db-template`.`fin_acc` (
  `idfinacc` INT NOT NULL AUTO_INCREMENT ,
  `finacc_name` VARCHAR(45) NOT NULL ,
  `finacc_incinsummary` TINYINT(1) NOT NULL DEFAULT True ,
  PRIMARY KEY (`idfinacc`) ,
  UNIQUE INDEX `idfinacc_UNIQUE` (`idfinacc` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Table with finance accounts.'