#!/usr/bin/python3

'''
Docstring goes here

'''


class MyList(list):
    ''' class MyList '''
    def print_sorted(self):
        ''' print_sorted fn '''
        arr = self[:]
        done = False
        while not done:
            done = True
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    done = False
        print(arr)


if __name__ == '__main__':
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
