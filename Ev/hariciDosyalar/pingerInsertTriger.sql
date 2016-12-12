CREATE TRIGGER PingerIserted
	AFTER INSERT
	ON pinger FOR EACH ROW
BEGIN

	Update pinger
		SET tarih=sysdate
		WHERE makineAdi=new.makineAdi
END;