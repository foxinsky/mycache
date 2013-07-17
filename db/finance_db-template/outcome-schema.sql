CREATE  TABLE IF NOT EXISTS `finance_db-template`.`outcome` (
  `idoutcome` BIGINT NOT NULL AUTO_INCREMENT ,
  `out_acc` INT NOT NULL ,
  `out_summ` INT NOT NULL ,
  `out_currency` INT NOT NULL ,
  `out_cat` INT NOT NULL ,
  `out_comment` VARCHAR(45) NULL ,
  `out_place` INT NOT NULL DEFAULT 1 ,
  PRIMARY KEY (`idoutcome`) ,
  INDEX `fk_outcome_1` (`out_acc` ASC) ,
  INDEX `fk_outcome_2` (`out_currency` ASC) ,
  INDEX `fk_outcome_3` (`out_cat` ASC) ,
  INDEX `fk_outcome_4` (`out_place` ASC) ,
  CONSTRAINT `fk_outcome_1`
    FOREIGN KEY (`out_acc` )
    REFERENCES `finance_db-template`.`fin_acc` (`idfinacc` )
    ON DELETE SET NULL
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_outcome_2`
    FOREIGN KEY (`out_currency` )
    REFERENCES `finance_db-template`.`currency` (`idcurrency` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_outcome_3`
    FOREIGN KEY (`out_cat` )
    REFERENCES `finance_db-template`.`category` (`idcategory` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_outcome_4`
    FOREIGN KEY (`out_place` )
    REFERENCES `finance_db-template`.`place` (`idplace` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Table for outcome money tracking'
