CREATE OR REPLACE FUNCTION dostepne_wycieczki_function2(kraj_param VARCHAR2, data_od DATE, data_do DATE)
    RETURN wycieczki_table AS
    result_table wycieczki_table;
BEGIN
    IF data_do < data_od THEN
        raise_application_error(-20020,
                                'Niepoprawny przedzial czasu - data z parametru data_do jest wczesniej niz data_od');
    END IF;

    SELECT wycieczki_type(w.ID_WYCIECZKI, w.NAZWA, w.KRAJ, w.OPIS, w.LICZBA_MIEJSC, w.DATA)
        BULK COLLECT
    INTO result_table
    FROM WYCIECZKI w
    WHERE w.KRAJ = kraj_param
      AND w.DATA >= data_od
      AND w.DATA <= data_do
      AND w.LICZBA_WOLNYCH_MIEJSC > 0;

    RETURN result_table;
END;