CREATE TRIGGER TakipOda
	AFTER UPDATE
	ON odalar FOR EACH ROW
BEGIN

	INSERT INTO changed
		( isim, deger, userID )
	VALUES
		( new.isim, new.deger, new.userID );

END;