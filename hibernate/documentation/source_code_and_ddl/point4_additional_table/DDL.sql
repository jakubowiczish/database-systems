create schema APP;

create table PRODUCTS
(
	PRODUCTID INTEGER not null
		primary key,
	PRODUCTNAME VARCHAR(255),
	UNITSONSTOCK INTEGER not null
);

create table SUPPLIERS
(
	SUPPLIERID INTEGER not null
		primary key,
	CITY VARCHAR(255),
	COMPANYNAME VARCHAR(255),
	STREET VARCHAR(255)
);

create table SUPPLIERS_PRODUCTS
(
	SUPPLIER_SUPPLIERID INTEGER not null
		constraint FK1LCEBGBKYY9X3G5OVUJTBFLFA
			references SUPPLIERS,
	PRODUCTS_PRODUCTID INTEGER not null
		unique
		constraint FKFKUOWRIMPXYNTIT2EBU11K0JF
			references PRODUCTS,
	primary key (SUPPLIER_SUPPLIERID, PRODUCTS_PRODUCTID)
);

