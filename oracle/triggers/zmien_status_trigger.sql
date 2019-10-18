CREATE OR REPLACE TRIGGER zmien_status
    AFTER UPDATE
    ON REZERWACJE
    FOR EACH ROW
DECLARE
    difference_of_places_available int;
BEGIN
    INSERT INTO REZERWACJE_LOG (ID_REZERWACJI, DATA, STATUS)
    VALUES (:NEW.NR_REZERWACJI, CURRENT_DATE, :NEW.STATUS);

    CASE
         WHEN :OLD.STATUS <> 'A' AND :NEW.STATUS = 'A'
            THEN
                difference_of_places_available := 1;

        WHEN :OLD.STATUS = 'A' AND :NEW.STATUS <> 'A'
            THEN
                difference_of_places_available := -1;

        ELSE
            difference_of_places_available := 0;
        END CASE;

    UPDATE WYCIECZKI w
    SET LICZBA_WOLNYCH_MIEJSC = LICZBA_WOLNYCH_MIEJSC + difference_of_places_available
    WHERE w.ID_WYCIECZKI = :NEW.ID_WYCIECZKI;
end;
