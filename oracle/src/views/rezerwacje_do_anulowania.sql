CREATE OR REPLACE VIEW REZERWACJE_DO_ANULOWANIA AS
SELECT r.NR_REZERWACJI,
       r.ID_WYCIECZKI,
       r.ID_OSOBY,
       r.STATUS
FROM REZERWACJE r
         JOIN WYCIECZKI w ON r.ID_WYCIECZKI = w.ID_WYCIECZKI
WHERE w.DATA - CURRENT_DATE <= 7
  AND r.STATUS = 'N';