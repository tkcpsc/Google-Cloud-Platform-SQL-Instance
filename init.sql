-- Create the database:

    -- CREATE DATABASE FSE_EngStore;


-- DDL:

    CREATE TABLE Suppliers (
        SupplierID INT AUTO_INCREMENT PRIMARY KEY,
        SupplierName VARCHAR(255) NOT NULL,
        ContactName VARCHAR(255),
        Address VARCHAR(255),
        City VARCHAR(100),
        PostalCode VARCHAR(20),
        Country VARCHAR(100),
        Phone VARCHAR(20)
    );

    CREATE TABLE Products (
        ProductID INT AUTO_INCREMENT PRIMARY KEY,
        ProductName VARCHAR(255) NOT NULL,
        SupplierID INT,
        Category VARCHAR(100),
        UnitPrice DECIMAL(10, 2),
        UnitsInStock INT,
        FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
    );

    CREATE TABLE Customers (
        CustomerID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerName VARCHAR(255) NOT NULL,
        ContactName VARCHAR(255),
        Address VARCHAR(255),
        City VARCHAR(100),
        PostalCode VARCHAR(20),
        Country VARCHAR(100)
    );

    CREATE TABLE Orders (
        OrderID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        OrderDate DATE,
        ShipDate DATE,
        ShipAddress VARCHAR(255),
        ShipCity VARCHAR(100),
        ShipPostalCode VARCHAR(20),
        ShipCountry VARCHAR(100),
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    );

    CREATE TABLE OrderDetails (
        OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
        OrderID INT,
        ProductID INT,
        Quantity INT,
        UnitPrice DECIMAL(10, 2),
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );


-- DML:

    -- Inserting data into Suppliers
    INSERT INTO Suppliers (SupplierName, ContactName, Address, City, PostalCode,
    Country, Phone) VALUES
    ('EcoFriendly Ltd', 'John Doe', '123 Green Road', 'EcoCity', 'EC123', 'Ecoland', '123-456-7890'),
    ('NatureGoods Inc', 'Jane Smith', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('Organic Goodness', 'John Bith', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('NatureGoods Inc', 'Dave Smith', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-544-3210'),
    ('Pure Deisl Truck LLC', 'Babe Ruth', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '800-654-3210'),
    ('KING suspension', 'Obama Glizat', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('BOCSH', 'Disney Man', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('VP RACING', 'Ben Dover', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('Hello Fresh', 'Imb Ored', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210'),
    ('Hydra', 'Will Smith', '456 Natural Way', 'GreenVille', 'GV456', 'Greenland', '987-654-3210');

    -- Inserting data into Products
    INSERT INTO Products (ProductName, SupplierID, Category, UnitPrice, UnitsInStock)
    VALUES
    ('Bamboo Toothbrush', 1, 'Personal Care', 2.99, 100),
    ('Reusable Water Bottle', 1, 'Outdoor', 10.50, 200),
    ('Organic Cotton T-shirt', 2, 'Clothing', 15.99, 150),
    ('Organic Cotton Pants', 3, 'Clothing', 17.99, 300),
    ('Tesla Model 3', 2, 'Automotive', 36500.00, 5),
    ('Rivian RT1', 2, 'Automotive', 57724.99, 1),
    ('Titanium Surf Board', 2, 'Outdoor', 3299.99, 15),
    ('Organic Synthetic Gassoline', 2, 'Automotive', 4.99, 1050),
    ('Organic Premium Motor Oil', 2, 'Automotive', 9.99, 1500),
    ('E85', 2, 'Automotive', 3.75, 2000);

    -- Inserting data into Customers
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) 
    VALUES
    ('Eco Shopper', 'Alice Johnson', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry'),
    ('Green Buyer', 'Bob Brown', '321 Green St', 'EcoVille', 'EV321', 'EcoLand'),
    ('Big Buyer', 'Elon Musk', '321 Red St', 'Bakersfield', 'BK312', 'USA'),
    ('Big Buyer', 'The Zucc', '534521 Brown St', 'Saccramento', 'SA321', 'USA'),
    ('Big Buyer', 'Billy Bezzos', '3453231 Yellow St', 'LA', 'LA321', 'USA'),
    ('Random Buyer', 'Fooghy Bargli', '321 White St', 'Orange', 'OR321', 'Aladeah'),
    ('Little Buyer', 'Shen Ming', '54321 Gray St', 'Ecotown', 'EC321', 'Kasakstan'),
    ('Eco Buyer', 'Juan Verde', '343221 Azul St', 'nowheres', 'NW321', 'Afganastan'),
    ('Not Eco Buyer', 'Arnold S', '3321 Wallstreet St', 'longtown', 'LT321', 'Nigeria'),
    ('Cheap Buyer', 'Gavin Neal', '323421 Long St', 'SyntheticOilField', 'SO321', 'Dubai');

    --  Inserting data into Orders
    INSERT INTO Orders (CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry) 
    VALUES
    (1, '2023-11-01', '2023-11-01', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry'),
    (2, '2023-10-04', '2023-10-04', '321 Green St', 'EcoVille', 'EV321', 'EcoLand'),
    (3, '2023-11-11', '2023-11-11', '321 Red St', 'Bakersfield', 'BK312', 'USA'),
    (6, '2022-12-03', '2022-12-03', '321 White St', 'Orange', 'OR321', 'Aladeah'),
    (2, '2022-07-03', '2022-07-03', '321 Green St', 'EcoVille', 'EV321', 'EcoLand'),
    (8, '2020-11-04', '2020-11-04', '343221 Azul St', 'nowheres', 'NW321', 'Afganastan'),
    (9, '2021-12-02', '2021-12-02', '3321 Wallstreet St', 'longtown', 'LT321', 'Nigeria'),
    (1, '2021-11-04', '2021-11-04', '789 Eco Ave', 'EcoTown', 'ET789', 'EcoCountry'),
    (7, '2021-11-06', '2021-11-06', '54321 Gray St', 'Ecotown', 'EC321', 'Kasakstan'),
    (4, '2019-11-07', '2019-11-07', '534521 Brown St', 'Saccramento', 'SA321', 'USA');

    --  Inserting data into OrderDetails
    INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) VALUES
    (1, 1, 2, 2.99),
    (1, 3, 1, 15.99),
    (2, 10, 10, 3.75),
    (2, 9, 1, 9.99),
    (3, 1, 4, 2.99),
    (4, 4, 3, 17.99),
    (5, 5, 1, 36500.00),
    (6, 6, 2, 57724.99),
    (7, 7, 2, 3299.99),
    (7, 8, 1, 4.99);
