# some client will use it to sort the data 
# and this sorter class (client) will we class by our main method / class


# from SortingAlgo.BubbleSort import BubbleSort
# from SortingAlgo.QuickSort import QuickSort
# from SortingAlgo.MergeSort import MergeSort

# class Sorter:

#     def sort_data(seft, data,algo):
#         if algo == "Bubble":
#             return BubbleSort().sort(data)
        
#         if algo == "Quick":
#             return QuickSort().sort(data)
        
#         # let i have to add another algo , i have to write another if condition
#         # we are braking OCP

#         if algo == "Merge":
#             return MergeSort().sort(data)
        
"""
So to make it more better, 
Rather my client writing if and else condition , this if-else condition should 
be managed by us(factory dp) 
client should not know which object he has to create 

here we can use Factory DP for creation of the object and write if else condtion there
"""        

# Now my client just write /say 
from Factory.SortingFactory import SortingFactory

class Sorter:
    def sort_data(self, data, algo):
        strategy = SortingFactory().getSortingObj(algo=algo)
        strategy.sort(data)

# Now my clint is not resposible :
# - to write ay if-else / create any object