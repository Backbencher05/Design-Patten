from SortingAlgo.BubbleSort import BubbleSort
from SortingAlgo.QuickSort import QuickSort
from SortingAlgo.MergeSort import MergeSort

class SortingFactory:

    def getSortingObj(self, algo):
        if algo == "Bubble":
            return BubbleSort()
        
        if algo == "Quick":
            return QuickSort()
        
        if algo == "Merge":
            return MergeSort()
        
# just return the object , not even sort method 
# i.e MergeSort().sort(data)