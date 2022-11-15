---Task 1
create sequence my_seq
start with 1
increment by 1;
--------------------------------------------------------------------------------------------------------------------------------
--Task 2 Create tables
-- Create Customer Table
create table CUSTOMER (
    cust_id number(9),
    username varchar2(20) not null,
    passwd varchar2(10) not null,
    first_name varchar2(30) not null,
    last_name varchar2(30) not null,
    credit_type varchar2(20) not null,
    phone varchar2(15)
    );

-- Add named constraints for  table CUSTOMER
alter table CUSTOMER
add constraint customer_id_pk primary key (cust_id)
add constraint customer_username_uq unique(username)
add constraint customer_credit_type_ck check (credit_type in ('high','low','average'));
--------------------------------------------------------------------------------------------------------------------------
-- Create Customer Order Table
create table CUST_ORDER(
    ord_id number(9),
    cust_id number(9) not null,
    order_date date default sysdate not null
    );

-- Add named constraints for  table CUST_ORDER
alter table CUST_ORDER
add constraint cust_order_ord_id_pk primary key (ord_id)
add constraint cust_order_cust_id_fk foreign key (cust_id) references customer(cust_id)
-------------------------------------------------------------------------------------------------------------------------
--Create cart table
create table CART(
    row_id number(9),
    ord_id number(9) not null,
    prod_id number(9) not null,
    quantity number(9) not null
);
-- Add named constraints for cart
alter table CART
add constraint cart_row_id_pk primary key (row_id)
add constraint cart_ord_id_fk foreign key (ord_id) references cust_order(ord_id)
add constraint cart_prod_id_fk foreign key (prod_id) references product(prod_id);
-------------------------------------------------------------------------------------------------------------------------
--Create product table
create table PRODUCT(
    prod_id number(9),
    group_id number(9) not null,
    prod_name varchar(255) not null,
    price number(9,2) not null
);

-- add names constraints
alter table PRODUCT
add constraint product_prod_id_pk primary key (prod_id)
add constraint product_group_id_fk foreign key (group_id) references prod_group(group_id);
--------------------------------------------------------------------------------------------------------------------------------
-- Create product pic table
create table PROD_PICT(
    pict_id number(9),
    prod_id number(9) not null,
    file_type varchar(255) not null,
    width number(9) not null,
    height number(9) not null,
    path varchar(255) not null
);
-- add named constraints 
alter table PROD_PICT 
add constraint prod_pict_pict_id_pk primary key (pict_id)
add constraint prod_pict_prod_id_fk foreign key (prod_id) references PRODUCT(prod_id)
add constraint prod_pict_file_type check (file_type in ('gif', 'jpg'));
--------------------------------------------------------------------------------------------------------------------------------
-- Create product group table
create table PROD_GROUP(
    group_id number(9),
    group_name varchar(255) not null
);

--Add table constraints
alter table PROD_GROUP
add constraint prod_group_group_id_pk primary key (group_id)
--------------------------------------------------------------------------------------------------------------------------------