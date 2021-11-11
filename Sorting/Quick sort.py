"""defining function quick sort and accepting numbers to sort from users"""

def quick_sort(collection: list) -> list:
	
    if len(collection) < 2:
        return collection
    pivot = collection.pop()  # Use the last element as the first pivot
    greater: List[int] = []  # All elements greater than pivot.
    lesser: List[int] = []  # All elements less than or equal to pivot.
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
    
    
if __name__ == "__main__":
    # taking user input 
    user_input = input("Enter numbers separated by a comma:\n").strip()
 
    unsorted = [int(item) for item in user_input.split(",")]

    print(quick_sort(unsorted)) # defined function is called 
