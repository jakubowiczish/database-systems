CREATE OR REPLACE TRIGGER usun_rezerwacje
    BEFORE DELETE
    ON REZERWACJE
    FOR EACH ROW
BEGIN
    raise_application_error(-20045, 'Usuniecie rezerwacji jest niemozliwe.');
end;
