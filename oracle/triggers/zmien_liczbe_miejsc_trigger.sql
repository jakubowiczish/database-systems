CREATE OR REPLACE TRIGGER zmien_liczbe_miejsc
    BEFORE UPDATE OF LICZBA_MIEJSC
    ON WYCIECZKI
    FOR EACH ROW
BEGIN
    SELECT :OLD.LICZBA_WOLNYCH_MIEJSC + (:NEW.LICZBA_MIEJSC - :OLD.LICZBA_MIEJSC)
    INTO :NEW.LICZBA_WOLNYCH_MIEJSC
    FROM dual;
END;

