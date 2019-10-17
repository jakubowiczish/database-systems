CREATE OR REPLACE PROCEDURE dodaj_rezerwacje(id_wycieczki_param NUMBER, id_osoby_param NUMBER)
AS
    counter INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO counter
    FROM DOSTEPNE_WYCIECZKI_VIEW v
    WHERE v.ID_WYCIECZKI = id_wycieczki_param;

    IF counter = 0 THEN
        raise_application_error(-20011, 'Nie znaleziono wycieczki o podanym id');
    END IF;

    SELECT COUNT(*)
    INTO counter
    FROM OSOBY o
    WHERE o.ID_OSOBY = id_osoby_param;

    IF counter = 0 THEN
        raise_application_error(-20012, 'Nie znaleziono osoby o podanym id');
    END IF;

    SELECT COUNT(*)
    INTO COUNTER
    FROM REZERWACJE r
    WHERE r.ID_OSOBY = id_osoby_param
      AND r.ID_WYCIECZKI = id_wycieczki_param;

    IF counter > 0 THEN
        raise_application_error(-20013, 'Rezerwacja z danym id wycieczki i id osoby już istnieje');
    END IF;

    INSERT INTO REZERWACJE (ID_WYCIECZKI, ID_OSOBY, STATUS)
    VALUES (id_wycieczki_param, id_osoby_param, 'N');
END;