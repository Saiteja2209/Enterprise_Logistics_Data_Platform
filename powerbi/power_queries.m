// ============================================================
// Power BI - Advanced Editor Script
// Paste this into: Home > Transform Data > Advanced Editor
// Then click "New Source" for each table, or replace all at once.
// ============================================================

// ---- DIM_CUSTOMERS ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_CUSTOMERS_Table = RAW_MART_Schema{[Name="DIM_CUSTOMERS",Kind="Table"]}[Data]
in
    DIM_CUSTOMERS_Table;

// ---- DIM_EMPLOYEES ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_EMPLOYEES_Table = RAW_MART_Schema{[Name="DIM_EMPLOYEES",Kind="Table"]}[Data]
in
    DIM_EMPLOYEES_Table;

// ---- DIM_PRODUCTS ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_PRODUCTS_Table = RAW_MART_Schema{[Name="DIM_PRODUCTS",Kind="Table"]}[Data]
in
    DIM_PRODUCTS_Table;

// ---- DIM_WAREHOUSES ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_WAREHOUSES_Table = RAW_MART_Schema{[Name="DIM_WAREHOUSES",Kind="Table"]}[Data]
in
    DIM_WAREHOUSES_Table;

// ---- DIM_DELIVERY_PARTNERS ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_DELIVERY_PARTNERS_Table = RAW_MART_Schema{[Name="DIM_DELIVERY_PARTNERS",Kind="Table"]}[Data]
in
    DIM_DELIVERY_PARTNERS_Table;

// ---- DIM_DATE ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    DIM_DATE_Table = RAW_MART_Schema{[Name="DIM_DATE",Kind="Table"]}[Data]
in
    DIM_DATE_Table;

// ---- FACT_ORDER_ITEMS ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    FACT_ORDER_ITEMS_Table = RAW_MART_Schema{[Name="FACT_ORDER_ITEMS",Kind="Table"]}[Data]
in
    FACT_ORDER_ITEMS_Table;

// ---- FACT_GPS_TRACKING ----
let
    Source = Snowflake.Databases("ZYJWLWW-BO23267.snowflakecomputing.com","LOGISTICS_WH",[Implementation="2.0"]),
    LOGISTICS_DW_Database = Source{[Name="LOGISTICS_DW",Kind="Database"]}[Data],
    RAW_MART_Schema = LOGISTICS_DW_Database{[Name="RAW_MART",Kind="Schema"]}[Data],
    FACT_GPS_TRACKING_Table = RAW_MART_Schema{[Name="FACT_GPS_TRACKING",Kind="Table"]}[Data]
in
    FACT_GPS_TRACKING_Table;
