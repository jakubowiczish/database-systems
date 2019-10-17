CREATE OR REPLACE PROCEDURE zmien_liczbe_miejsc(id_wycieczki_param NUMBER, liczba_nowych_miejsc_param NUMBER)
AS
    counter INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO counter
    FROM WYCIECZKI w
    WHERE w.ID_WYCIECZKI = id_wycieczki_param;

    IF counter = 0 THEN
        raise_application_error(-20011, 'Nie znaleziono wycieczki o podanym id');
    END IF;

    SELECT wm.LICZBA_MIEJSC - wm.LICZBA_WOLNYCH_MIEJSC
    INTO counter
    FROM WYCIECZKI_MIEJSCA wm
    WHERE wm.ID_WYCIECZKI = id_wycieczki_param;

    IF liczba_nowych_miejsc_param < counter OR liczba_nowych_miejsc_param < 0 THEN
        raise_application_error(-20030, 'Podana liczba nowych miejsc ma zbyt małą wartość');
    END IF;

    UPDATE WYCIECZKI
    SET LICZBA_MIEJSC = liczba_nowych_miejsc_param
    WHERE ID_WYCIECZKI = id_wycieczki_param;
END;