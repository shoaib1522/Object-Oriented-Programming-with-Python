from Date import Date
from Address import Address
class Bill(object):
    Bill_number=0
    def __init__(self,DD,MM,YYYY,Customer_Name,house,street,place,city):
        self.Date=Date(DD,MM,YYYY)
        self.customername=Customer_Name
        self.Customeraaddress=Address(house,street,place,city)
        Bill.Bill_number+=1
    def __str__(self):
        return f'No. {Bill.Bill_number} \n{str(self.Date)}\nCustomer Name: {self.customername}\n{str(self.Customeraaddress)} '
    
    