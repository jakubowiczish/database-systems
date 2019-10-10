CREATE OR REPLACE VIEW WYCIECZKI_MIEJSCA AS
SELECT w.NAZWA,
       w.KRAJ,
       w.DATA,
       w.LICZBA_MIEJSC,
       w.LICZBA_MIEJSC
           - (SELECT count(*)
              FROM REZERWACJE
              WHERE REZERWACJE.ID_WYCIECZKI = w.ID_WYCIECZKI
                AND status <> 'A') AS liczba_wolnych_miejsc
FROM WYCIECZKI w;
