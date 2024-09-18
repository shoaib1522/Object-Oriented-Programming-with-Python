from Bill import Bill
from Company import Company
from Companyfooter import CompanyFooter
from itemline import Itemline
def main():
    Company_Upper=Company('Mobilo',"Mobile City","Deals In all Kinds Of Mobile Sets and Accessories","0321-0000000","Cash")
    print(Company_Upper)
    Bill_Mobilo=Bill(22,10,2023,"Joseph",7,14,"Dera Gujran",'Islamabad')
    print(Bill_Mobilo)
    print("Particulars              Rate    Quantity   Amount")
    selling_item1=Itemline("Vivo Y21 Ultra",50000)
    print(selling_item1.calculating_price(1))
    selling_item2=Itemline('Redmi Note 12C',25000)
    print(selling_item2.calculating_price(1))
    print('                                          Total: ',selling_item1.total([selling_item2]))
    Company_Footer=CompanyFooter("Shoaib",2,"Allahwala Plaza, Markaz # 8", "Islamabad")
    print(Company_Footer)
main()