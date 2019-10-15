CREATE OR REPLACE FUNCTION uczestnicy_wycieczki(id_wycieczki_param INT)
    RETURN osoby_wycieczki_table as
    result_table    osoby_wycieczki_table;
    ilosc_wycieczek integer;
BEGIN
    SELECT COUNT(*) INTO ilosc_wycieczek FROM WYCIECZKI w WHERE w.ID_WYCIECZKI = id_wycieczki_param;

    IF ilosc_wycieczek = 0 THEN
        raise_application_error(-20006, 'Nie znaleziono wycieczki o podanym id');
    END IF;

    SELECT osoby_wycieczki_type(o.IMIE, o.NAZWISKO, w.NAZWA, w.DATA, w.KRAJ, r.STATUS)
        BULK COLLECT
    INTO result_table
    FROM WYCIECZKI w
             JOIN REZERWACJE r ON w.ID_WYCIECZKI = r.ID_WYCIECZKI
             JOIN OSOBY o ON r.ID_OSOBY = o.ID_OSOBY
    WHERE w.ID_WYCIECZKI = id_wycieczki_param
      AND r.STATUS <> 'A';

    RETURN result_table;
END;