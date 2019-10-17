CREATE OR REPLACE FUNCTION przyszle_rezerwacje_osoby(id_osoby_param NUMBER)
    RETURN osoby_wycieczki_table AS
    result_table    osoby_wycieczki_table;
    ilosc_wycieczek INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO ilosc_wycieczek
    FROM OSOBY o
    WHERE o.ID_OSOBY = id_osoby_param;

    IF ilosc_wycieczek = 0 THEN
        raise_application_error(-20001, 'Nie znaleziono osoby o podanym id');
    END IF;

    SELECT osoby_wycieczki_type(o.IMIE, o.NAZWISKO, w.NAZWA, w.DATA, w.KRAJ, r.STATUS)
        BULK COLLECT
    INTO result_table
    FROM WYCIECZKI w
             JOIN REZERWACJE r ON w.ID_WYCIECZKI = r.ID_WYCIECZKI
             JOIN OSOBY o ON r.ID_OSOBY = o.ID_OSOBY
    WHERE o.ID_OSOBY = id_osoby_param
      AND r.STATUS <> 'A'
      AND w.DATA > CURRENT_DATE;

    RETURN result_table;
END;