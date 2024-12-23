num = 45+45

def mean(list1):
    return sum(list1) / len(list1)

list2 = []
def even_num(list1):
    return [i for i in list1 if i % 2 == 0]

#this code of block will execute if it is executed directly instead of importing the file as a module
def main():
    print("Testing mean function")
    n_list = list(range(1,21))
    correct_mean = 10.5
    assert(mean(n_list) == correct_mean)  # Assert that the mean is correct

    print("Getting all even")
    correct_list = [2,4,6,8,10,12,14,16,18,20]
    assert(even_num(n_list) == correct_list)  # Assert that add_five works correctly

    print("All tests passed!")

if __name__ == '__main__':
    main() 