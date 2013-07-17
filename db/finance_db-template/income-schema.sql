CREATE  TABLE IF NOT EXISTS `finance_db-template`.`income` (
  `idincome` BIGINT NOT NULL AUTO_INCREMENT ,
  `in_acc` INT NOT NULL ,
  `in_summ` INT NOT NULL ,
  `in_currency` INT NOT NULL ,
  `in_cat` INT NOT NULL ,
  `in_comment` VARCHAR(45) NULL ,
  PRIMARY KEY (`idincome`) ,
  INDEX `fk_income_acc` (`in_acc` ASC) ,
  INDEX `fk_income_1` (`in_currency` ASC) ,
  INDEX `fk_income_2` (`in_cat` ASC) ,
  CONSTRAINT `fk_income_acc`
    FOREIGN KEY (`in_acc` )
    REFERENCES `finance_db-template`.`fin_acc` (`idfinacc` )
    ON DELETE SET NULL
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_income_1`
    FOREIGN KEY (`in_currency` )
    REFERENCES `finance_db-template`.`currency` (`idcurrency` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_income_2`
    FOREIGN KEY (`in_cat` )
    REFERENCES `finance_db-template`.`category` (`idcategory` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Table for incomming money tracking'