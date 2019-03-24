##Program created by Leon Marco M. Ebarle
##Created on March 2019

import sqlite3
import sys
import os
from contextlib import closing

import business

conn = None

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "c:\\prodprog\\database\\vendor.db"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "Documents/python/python32-32/prod programs/database/vendor.db"

        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def closeConnection():
    global conn
    if conn:
        conn.close()

def retrieveAllVendors():
    query = '''SELECT  VendorName, 
                       Email,
                       AddressLine1,
                       AddressLine2,
                       City,
                       State,
                       Zip,
                       Phone,
                       Mobile,
                       PaymentPeriod,
                       Website
                 FROM  Vendor'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        vendors = c.fetchall()

    return vendors

def retrieveVendor(vendorName):
    query = '''
                SELECT  VendorName,
                        Email,
                        AddressLine1,
                        AddressLine2,
                        City,
                        State,
                        Zip,
                        Phone,
                        Mobile,
                        PaymentPeriod
                        Website
                  FROM  Vendor
                 WHERE  VendorName = ?
            '''
    with closing(conn.cursor()) as c:
        c.execute(query, (vendorName,))
        vendor = c.fetchone()

    return vendor

def retrieveVendors(vendorName):
    query = '''SELECT  VendorName, 
                       Email,
                       AddressLine1,
                       AddressLine2,
                       City,
                       State,
                       Zip,
                       Phone,
                       Mobile,
                       PaymentPeriod,
                       Website
                 FROM  Vendor
                WHERE  VendorName like ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (vendorName,))
        vendors = c.fetchall()

    return vendors

def insertVendor(vendor):

    vendors = retrieveVendors(vendor.vendorName)

    if len(vendors) == 0:
        query = '''
                    INSERT INTO
                            Vendor (VendorName, Email, AddressLine1,
                                    AddressLine2, City, State, Zip,
                                    Phone, Mobile, PaymentPeriod, Website)
                            VALUES (?,?,?, ?,?,?,?, ?,?,?,?)
                '''
        with closing(conn.cursor()) as c:
            c.execute(query, (vendor.vendorName, vendor.email, vendor.addressLine1,
                              vendor.addressLine2, vendor.city, vendor.state,
                              vendor.zipCode, vendor.phone, vendor.mobile,
                              vendor.paymentPeriod, vendor.website))
            conn.commit()

        return 0
    else:
        return 803

def deleteVendor(vendorName):

    vendors = retrieveVendors(vendorName)

    if len(vendors) >= 1:
        query = '''
                    DELETE FROM VENDOR
                     WHERE VendorName = ?
                '''
        with closing(conn.cursor()) as c:
            c.execute(query, (vendorName,))
            conn.commit()
        return 0
    else:
        return 100

def main():
    connect()
## testing database module
    print("Database connected")
    print(conn)
    vendors = retrieveVendors("Element%")
    if vendors is not None:
        for vendor in vendors:
            print("Vendor:", vendor["VendorName"])
            print("Email:", vendor["Email"])
            print("Payment Period:", vendor["PaymentPeriod"])
    else:
        print("Vendor not found")

    vendor = business.Vendor(vendorName="Mwave", email="contact@mwave.com")

    sqlcode = insertVendor(vendor)
    if sqlcode == 0:
        print("Insert operation successful")
    elif sqlcode == 803:
        print("Vendor already in database. Insert unsuccessful")
    
    vendorList = retrieveVendors("Mw%")
    if vendorList is not None:
        for row in vendorList:
            print("Vendor:", row["VendorName"])
            print("Email:", row["Email"])
            print("Payment Period:", row["PaymentPeriod"])
    else:
        print("Vendor not found")
##end of test
    closeConnection()
    print("Database closed")
    print(conn)

if __name__ == "__main__":
    main()
