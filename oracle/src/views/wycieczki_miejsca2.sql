CREATE OR REPLACE VIEW WYCIECZKI_MIEJSCA2
AS
SELECT w.ID_WYCIECZKI,
       w.kraj,
       w.data,
       w.nazwa,
       w.liczba_miejsc,
       w.LICZBA_WOLNYCH_MIEJSC
FROM wycieczki w;
