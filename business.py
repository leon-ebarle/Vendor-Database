#!/usr/bin/env python3

##Program created by Leon Marco M. Ebarle
##Created on March 2019

class Vendor:
    def __init__(self, vendorName, email, addressLine1="",
                 addressLine2="", city="", state="", zipCode="",
                 phone="", mobile="", paymentPeriod="net 30 days",website=""):
        self.vendorName = vendorName
        self.email = email
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phone
        self.mobile = mobile
        self.paymentPeriod = paymentPeriod
        self.website = website

##Vendor Name
    @property
    def vendorName(self):
        return self.__vendorName

    @vendorName.setter
    def vendorName(self, vendorName):
        if not vendorName.strip() or vendorName is None:
            raise ValueError("Vendor Name can't be blank")
        else:
            self.__vendorName = vendorName

    
##Email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not email.strip() or email is None:
            raise ValueError("E-mail can't be blank")
        elif "@" not in email or "." not in email:
            raise ValueError("Invalid e-mail")
        else:
            self.__email = email


##Address Line 1
    @property
    def addressLine1(self):
        return self.__addressLine1
    
    @addressLine1.setter
    def addressLine1(self, addressLine1):
        self.__addressLine1 = addressLine1

##Address Line 2
    @property
    def addressLine2(self):
        return self.__addressLine2
    
    @addressLine2.setter
    def addressLine2(self, addressLine2):
        self.__addressLine2 = addressLine2

##City
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, city):
        self.__city = city

##State
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state

##Zip Code
    @property
    def zipCode(self):
        return self.__zipCode
    
    @zipCode.setter
    def zipCode(self, zipCode):
        self.__zipCode = zipCode

##Phone
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

##mobile
    @property
    def mobile(self):
        return self.__mobile

    @phone.setter
    def mobile(self, mobile):
        self.__mobile = mobile

##Payment Period
    @property
    def paymentPeriod(self):
        return self.__paymentPeriod

    @paymentPeriod.setter
    def paymentPeriod(self, paymentPeriod):
        self.__paymentPeriod = paymentPeriod

        
def main():
    test = Vendor(vendorName="Boat Vendor", email="boat@gmail.com")
    print("Vendor Name: ", test.vendorName)
    print("Email: ", test.email)
    print("Address Line 1: ", test.addressLine1)
    print("Address Line 2: ", test.addressLine2)
    print("City: ", test.city)
    print("State: ", test.state)
    print("zip Code: ", test.zipCode)
    print("Landline: ", test.phone)
    print("Mobile: ", test.mobile)
    print("Payment Period: ", test.paymentPeriod)
    print("Website: ", test.website)


if __name__ == "__main__":
    main()
