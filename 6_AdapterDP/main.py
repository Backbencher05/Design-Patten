# from Banks.IciciBank import IciciBank
# from Banks.YesBank import YesBank


# if __name__ == '__main__':
#     # b = IciciBank().bal()
#     # print(b)

#     # let now i have to use YesBank , now i ahev to change my code 
#     # because YesBank don't have bal() method 

#     b = YesBank().balance()
#     print(b)

# so her ethe issue is that i am changing my code accoding to the Bank not recomended
# so we will create one middle ware / (Adapter)/ Connector 
# let's create Adapter who will intracy with the Banks


from Adapters.IciciBankAdapter import IciciBankAdapter
from Adapters.YesBankAdapter import YesBankAdapter
from PhonePay import PhonePay
# Now, 
if __name__ == '__main__':
#   let i want to use  IciciBank , so i will use IciciBank Adapter here 
    # b = IciciBankAdapter() 
    b = YesBankAdapter()
    p = PhonePay(b)
    print(p.checkBalance())
    
# it's simple like we are linking the account to phonepay 



# so the flow is:

# we have phonePay class which is only dependent on Abstract class of Bank Adpater