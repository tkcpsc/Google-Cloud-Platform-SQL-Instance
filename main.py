# Author - Thomas Kudey
# Contact - Kudey@chapman.edu

'''
Supply Chain and Logistics Management Tool Utilizing Google Cloud Platform

This Python script provides a framework for a commercial supply chain and logistics application utilizing a 
convenient interface for interacting with a MySQL database hosted on Google Cloud Platform Suite. It includes 
functions to execute various queries and stored procedures, handling tasks such as listing out-of-stock products, 
finding total orders by customer, and updating stock quantities.
'''

import re
import mysql.connector
import configparser


# Connect to the Database here
def connect_to_database():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        conn = mysql.connector.connect(
            host = config['DEFAULT']['host'],
            port = config['DEFAULT']['port'],
            user = config['DEFAULT']['user'],
            password = config['DEFAULT']['password'],
            database = config['DEFAULT']['database']
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def execute_and_print_query_results(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        # Fetch the column names
        column_names = [column[0] for column in cursor.description]

        # Fetch and print the results
        query_results = cursor.fetchall()
        if query_results:
            # Print column names
            for name in column_names:
                print(name, end=' ')
            print("\n" + "-" * (len(column_names) * 12))  # Separator line

            # Iterate through each row in the results
            for row in query_results:
                for column in row:
                    print(column, end=' ')
                print()  # New line after each row
        else:
            print("No results.")

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def list_out_of_stock_products(conn):
    try:
        # Declare cursor through passed in connection.
        cursor = conn.cursor()
        query = """
                SELECT ProductName 
                FROM Products 
                WHERE UnitsInStock = 0;
                """
        # Execute and print the query
        execute_and_print_query_results(conn, query)
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def find_total_orders_by_customer(conn):
    try:
        # Declare cursor through passed in connection.
        cursor = conn.cursor()
        query = """
                SELECT CustomerName, COUNT(OrderID)
                FROM Orders
                join Customers On Orders.CustomerID = Customers.CustomerID
                GROUP BY Orders.CustomerID;
                """
        # Execute and print the query
        execute_and_print_query_results(conn, query)
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def display_most_expensive_product_per_order(conn):
    try:
        # Declare cursor through passed in connection.
        cursor = conn.cursor()
        query = """
                SELECT OrderDetails.OrderID, Products.ProductName, OrderDetails.Quantity, Products.UnitPrice
                FROM OrderDetails
                JOIN Products ON Products.ProductID = OrderDetails.ProductID
                INNER JOIN (
                    SELECT OrderDetails.OrderID, MAX(Products.UnitPrice) as MaxPrice
                    FROM OrderDetails OrderDetails
                    JOIN Products Products ON Products.ProductID = OrderDetails.ProductID
                    GROUP BY OrderDetails.OrderID
                ) as MaxPrices ON OrderDetails.OrderID = MaxPrices.OrderID AND Products.UnitPrice = MaxPrices.MaxPrice;
                """
        # Execute and print the query
        execute_and_print_query_results(conn, query)
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def retrieve_never_ordered_products(conn):
    try:
        # Declare cursor through passed in connection.
        cursor = conn.cursor()
        query = """
                SELECT ProductName
                FROM Products
                LEFT JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
                WHERE OrderDetails.ProductID IS NULL;
                """
        # Execute and print the query
        execute_and_print_query_results(conn, query)
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def show_total_revenue_by_supplier(conn):
    try:
        # Declare cursor through passed in connection.
        cursor = conn.cursor()
        query = """
                SELECT SupplierID, SUM(Products.UnitPrice*Quantity) AS "Revenue"
                FROM OrderDetails
                JOIN Products ON Products.ProductID = OrderDetails.ProductID
                GROUP BY SupplierID;
                """
        # Execute and print the query
        execute_and_print_query_results(conn, query)
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


def prompt_user_for_input(prompt_message, pattern):
    while True:
        user_input = input(prompt_message)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input, please try again.")


# Calls Procedure.
def call_new_order_procedure(conn):
    try:
        # Establish cursor to the server connection
        cursor = conn.cursor()

        # Prompt for each attribute and convert types as necessary
        p_CustomerID = int(prompt_user_for_input("Enter Customer ID (integer): ", r"^\d+$"))
        p_OrderDate = prompt_user_for_input("Enter Order Date (YYYY-MM-DD): ", r"^\d{4}-\d{2}-\d{2}$")
        p_ShipDate = prompt_user_for_input("Enter Ship Date (YYYY-MM-DD): ", r"^\d{4}-\d{2}-\d{2}$")
        p_ShipAddress = prompt_user_for_input("Enter Ship Address: ", r"^.+$")
        p_ShipCity = prompt_user_for_input("Enter Ship City: ", r"^.+$")
        p_ShipPostalCode = prompt_user_for_input("Enter Ship Postal Code: ", r"^.+$")
        p_ShipCountry = prompt_user_for_input("Enter Ship Country: ", r"^.+$")
        p_ProductID = int(prompt_user_for_input("Enter Product ID (integer): ", r"^\d+$"))
        p_Quantity = int(prompt_user_for_input("Enter Quantity (integer): ", r"^\d+$"))
        p_UnitPrice = float(prompt_user_for_input("Enter Unit Price (decimal): ", r"^\d+(\.\d{1,2})?$"))

        # Call the stored procedure
        query = "CALL new_order(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (p_CustomerID, p_OrderDate, p_ShipDate, p_ShipAddress, p_ShipCity, p_ShipPostalCode, p_ShipCountry, p_ProductID, p_Quantity, p_UnitPrice))

        conn.commit()
        print("Order created successfully. ")

    except mysql.connector.Error as e:
        print(f"Error calling stored procedure: {e}")


# Calls Procedure.
def call_update_units_in_stock_procedure(conn):
    try:
        # Establish cursor to the server connection
        cursor = conn.cursor()
        p_ProductID = int(prompt_user_for_input("Enter Product ID (integer): ", r"^\d+$"))
        p_UnitsInStock = int(prompt_user_for_input("Enter Units in Stock (integer): ", r"^\d+$"))

        # Call the stored procedure
        query = "CALL update_units_in_stock(%s, %s)"
        cursor.execute(query, (p_ProductID, p_UnitsInStock))
        conn.commit()
        print("Product units in stock updated successfully. ")
    except mysql.connector.Error as e:
        print(f"Error updating product units in stock: {e}")


def main():
    # Connect to Database.
    conn = connect_to_database()
    if conn:
        # Repeated Console Options Loop.
        while True:
            print("\nMenu:")
            print("1. List all products that are out of stock.")
            print("2. Find the total number of orders placed by each customer.")
            print("3. Display the details of the most expensive product ordered in each order.")
            print("4. Retrieve a list of products that have never been ordered.")
            print("5. Show the total revenue generated by each supplier.")
            print("6. Call the stored procedure to create a new Order along with OrderDetails.")
            print("7. Call the stored procedure to update the amount of units in stock for a specific product.")
            print("8. Quit")

            choice = input("Enter your choice (1-8): ")
            print("\n") # Just my OCD lol

            if choice == '1':
                list_out_of_stock_products(conn)
            elif choice == '2':
                find_total_orders_by_customer(conn)
            elif choice == '3':
                display_most_expensive_product_per_order(conn)
            elif choice == '4':
                retrieve_never_ordered_products(conn)
            elif choice == '5':
                show_total_revenue_by_supplier(conn)
            elif choice == '6':
                call_new_order_procedure(conn)
            elif choice == '7':
                call_update_units_in_stock_procedure(conn)
            elif choice == '8':
                print("Terminating the program.") # Needs to close the connection now.
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 8.")

        # Close the connection to the server.
        conn.close()


if __name__ == "__main__":
    main()
