#!/usr/bin/env python3

##Program created by Leon Marco M. Ebarle
##Created on March 2019

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scrollbar, Listbox

from business import Vendor
import vendorDB

class mainWindow(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "10 10 10 10")
        self.parent = parent
        self.pack()
        
        self.initMainWindowButtons()

    def initMainWindowButtons(self):
        ttk.Label(self, text="Select from below").grid(row=0, column=0)
        ttk.Button(self, text="Add Vendor", command=self.addVendorWindow).grid(row=1,
                                                                    column=0,
                                                                    padx=0)
        ttk.Button(self, text="Delete Vendor", command=self.delVendorWindow).grid(row=1,
                                                                                  column=1,
                                                                                  padx=20)
        ttk.Button(self, text="View All Vendors", command=self.viewAll).grid(row=1,
                                                                             column=2,
                                                                             padx=1)

    def viewAll(self):
        self.viewAllWindow = tk.Toplevel(self.parent)
        viewAllVendors(self.viewAllWindow)

        
    def addVendorWindow(self):
        self.addWindow = tk.Toplevel(self.parent)
        self.addWindow.title("Add Vendor")
        addVendor(self.addWindow)

    def delVendorWindow(self):
        self.delWindow = tk.Toplevel(self.parent)
        self.delWindow.title("Delete Vendor")
        delVendor(self.delWindow)

class viewAllVendors(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()

        self.vendorList = vendorDB.retrieveAllVendors()
        self.tree = ttk.Treeview(self, columns=("E-mail", "Address Line 1",
                            "Address Line 2", "City", "State", "Zip Code", "Phone",
                            "Mobile", "Payment Period", "Website"))
        
        self.tree.heading("#0", text="Vendor Name")
        self.tree.heading("#1", text="E-mail")
        self.tree.heading("#2", text="Address Line 1")
        self.tree.heading("#3", text="Address Line 2")
        self.tree.heading("#4", text="City")
        self.tree.heading("#5", text="State")
        self.tree.heading("#6", text="Zip Code")
        self.tree.heading("#7", text="Phone")
        self.tree.heading("#8", text="Mobile")
        self.tree.heading("#9", text="Payment Period")
        self.tree.heading("#10", text="Website")

        self.tree.column("#0", stretch=tk.YES, width=150)
        self.tree.column("#1", stretch=tk.YES, width=150)
        self.tree.column("#2", stretch=tk.YES, width=150)
        self.tree.column("#3", stretch=tk.YES, width=150)
        self.tree.column("#4", stretch=tk.YES, width=150)
        self.tree.column("#5", stretch=tk.YES, width=150)
        self.tree.column("#6", stretch=tk.YES, width=150)
        self.tree.column("#7", stretch=tk.YES, width=150)
        self.tree.column("#8", stretch=tk.YES, width=150)
        self.tree.column("#9", stretch=tk.YES, width=150)
        self.tree.column("#10", stretch=tk.YES, width=150)

        self.tree.grid(row=1, columnspan=10, sticky="nsew")

        for vendor in self.vendorList:
            self.tree.insert("", "end", text=vendor[0], values=(vendor[1],
                vendor[2], vendor[3], vendor[4], vendor[5], vendor[6],
                vendor[7], vendor[8], vendor[9], vendor[10]))
    
class delVendor(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.pack()

        self.vendorName = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        ttk.Label(self, text="Input Vendor Name to delete: ").grid(row=0, column=0, stick=tk.E)
        ttk.Entry(self, width=25, textvariable=self.vendorName).grid(row=0, column=1)
        ttk.Button(self, text="Delete", command=self.deleteRow).grid(row=1, column=0)

    def deleteRow(self):
        vendorString = self.vendorName.get()

        vendorList = vendorDB.retrieveVendors(vendorString)
        if len(vendorList) >= 1:
            vendorDB.deleteVendor(vendorString)
            messagebox.showinfo("Success!", "Vendor has been deleted")
        else:
            messagebox.showinfo("Error", "Vendor does not exist")
                
class addVendor(ttk.Frame):
    def __init__(self, parent):
        #initialization 
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.vendor = Vendor(vendorName="default", email="default@default.com")
        self.pack()
        
        #define StringVar components
        self.vendorName = tk.StringVar()
        self.email = tk.StringVar()
        self.addressLine1 = tk.StringVar()
        self.addressLine2 = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.zipCode = tk.StringVar()
        self.phone = tk.StringVar()
        self.mobile = tk.StringVar()
        self.paymentPeriod = tk.StringVar()
        self.paymentChoices = ["Net 30 days", "Net 7 days", "Immediate Payment"]
        self.paymentPeriod.set(self.paymentChoices[0])
        self.website = tk.StringVar()

        self.initComponents()

    def initComponents(self):

        paymentPopUp = tk.OptionMenu(self, self.paymentPeriod, *self.paymentChoices)
        
        ttk.Label(self, text="Vendor Name: ").grid(row=0, column=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.vendorName).grid(row=0, column=1)
        ttk.Label(self, text="E-mail: ").grid(row=1, column=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.email).grid(row=1, column=1)
        ttk.Label(self, text="Address Line 1: ").grid(row=2, column=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.addressLine1).grid(row=2, column=1)
        ttk.Label(self, text="Address Line 2: ").grid(row=3, column=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.addressLine2).grid(row=3, column=1)
        ttk.Label(self, text="City: ").grid(row=4, column=0, sticky=tk.E)
        ttk.Entry(self, width=10, textvariable=self.city).grid(row=4, column=1, sticky=tk.W)
        ttk.Label(self, text="State: ").grid(row=5, column=0, sticky=tk.E)
        ttk.Entry(self, width=5, textvariable=self.state).grid(row=5, column=1, sticky=tk.W)
        ttk.Label(self, text="Zip: ").grid(row=6, column=0, sticky=tk.E)
        ttk.Entry(self, width=5, textvariable=self.zipCode).grid(row=6, column=1, sticky=tk.W)
        ttk.Label(self, text="Phone: ").grid(row=7, column=0, sticky=tk.E)
        ttk.Entry(self, width=15, textvariable=self.phone).grid(row=7, column=1, sticky=tk.W)
        ttk.Label(self, text="Mobile: ").grid(row=8, column=0, sticky=tk.E)
        ttk.Entry(self, width=15, textvariable=self.mobile).grid(row=8, column=1, pady=5, sticky=tk.W)
        ttk.Label(self, text="Payment Period: ").grid(row=9, column=0, sticky=tk.E)
        paymentPopUp.grid(row=9, column=1, sticky=tk.W)
        ttk.Label(self, text="Website: ").grid(row=10, column=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.website).grid(row=10, column=1, pady=5, sticky=tk.W)

        ttk.Button(self, text="Add Vendor", command=self.insertRow).grid(row=12, column=0)

    def insertRow(self):
        error_switch = False

        if not self.vendorName.get().strip():
            messagebox.showinfo("Error", "Vendor Name can't be blank")
            error_switch = True
        else:
            self.vendor.vendorName = self.vendorName.get()
        if not self.email.get().strip():
            messagebox.showinfo("Error", "Invalid Email")
            error_switch = True
        else:
            self.vendor.email = self.email.get()
        if not error_switch:
            self.vendor.addressLine1 = self.addressLine1.get()
            self.vendor.addressLIne2 = self.addressLine2.get()
            self.vendor.city = self.city.get()
            self.vendor.state = self.state.get()
            self.vendor.zipCode = self.zipCode.get()
            self.vendor.phone = self.phone.get()
            self.vendor.mobile = self.mobile.get()
            self.vendor.paymentPeriod = self.paymentPeriod.get()
            self.vendor.website = self.website.get()

            sqlcode = vendorDB.insertVendor(self.vendor)
            if sqlcode == 0:
                messagebox.showinfo("Success", "Vendor has been added")
            elif sqlcode == 803:
                messagebox.showinfo("Error", "Duplicate vendor found in database")

        
if __name__ == "__main__":
    vendorDB.connect()
    root = tk.Tk()
    root.title("Vendor database")
    mainWindow(root)
    root.mainloop()
    vendorDB.closeConnection()
