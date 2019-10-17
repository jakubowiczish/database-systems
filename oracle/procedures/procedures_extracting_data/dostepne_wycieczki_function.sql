CREATE OR REPLACE FUNCTION dostepne_wycieczki_function(kraj_param varchar2, data_od date, data_do date)
    RETURN wycieczki_table AS
    result_table wycieczki_table;
BEGIN
    IF data_do < data_od THEN
        raise_application_error(-20020,
                                'Niepoprawny przedział czasu - data z parametru data_do jest wcześniej niż data_od');
    END IF;

    SELECT wycieczki_type(w.ID_WYCIECZKI, w.NAZWA, w.KRAJ, w.OPIS, w.LICZBA_MIEJSC, w.DATA)
        BULK COLLECT
    INTO result_table
    FROM WYCIECZKI w
    WHERE w.KRAJ = kraj_param
      AND w.DATA >= data_od
      AND w.DATA <= data_do
      AND w.LICZBA_MIEJSC >
          (SELECT COUNT(*) FROM REZERWACJE r where r.ID_WYCIECZKI = w.ID_WYCIECZKI AND r.STATUS <> 'A');

    RETURN result_table;
END;