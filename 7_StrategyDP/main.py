from sorterClient import Sorter


if __name__ == '__main__':
    sorting = Sorter()
    sorting.sort_data([1,3,2,4], "Quick")
    
    # let in future i have to use merge sort , in client he have to write if condition 
    # breaking OCP and SRP