#Help quick_sort method to organize the every elements from "start" to "end"
def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high

def quick_sort(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    #Kinda some recursives
    #sorting numbers smaller than pivot
    quick_sort(arr, start, p-1)
    #sorting number bigger than pivot
    quick_sort(arr, p+1, end)


def quick_sort_by_id(products):
    id_list = []
    for i in range (len(products)):
        id_list.append(products[i].pro_id)

    quick_sort(id_list, 0, len(id_list) - 1)

    index = 1
    print("Sorted by: ID")
    print("%-4s %-4s  %-50s    %10s    %9s %20s    %1s" % ("No.", "ID", "Name", "Type", "Price", "Date import", "Status"))
    for pro_id in id_list:
        for i in range (len(products)):
            if pro_id == products[i].pro_id:
                print("%-5d" % (index), end='')
                index += 1
                print(products[i].get_info())
                break

def quick_sort_by_name(products):
    name_list = []
    for i in range (len(products)):
        name_list.append(products[i].name)

    quick_sort(name_list, 0, len(name_list) - 1)

    index = 1
    print("Sorted by: NAME")
    print("%-4s %-4s %-50s    %10s    %9s %20s    %1s" % ("No.", "ID", "Name", "Type", "Price", "Date import", "Status"))
    for name in name_list:
        for i in range (len(products)):
            if name == products[i].name:
                print("%-5d" % (index), end='')
                index += 1
                print(products[i].get_info())
                break

def quick_sort_by_price(products):
    price_list = []
    for i in range (len(products)):
        price_list.append(products[i].price)
    quick_sort(price_list, 0, len(price_list) - 1)

    index = 1
    print("Sorted by: PRICE")
    print("%-4s %-4s %-50s    %10s    %9s %20s    %1s" % ("No.", "ID", "Name", "Type", "Price", "Date import", "Status"))
    for price in price_list:
        for i in range (len(products)):
            if price == products[i].price:
                print("%-5d" % (index), end='')
                index += 1
                print(products[i].get_info())
                break

def searching(products, item_name):
    index = 1
    print(f"Finding: {item_name}")
    print("%-4s %-4s %-50s    %10s    %9s %20s    %1s" % ("No.", "ID", "Name", "Type", "Price", "Date import", "Status"))
    for i in range (len(products)):
        if item_name in products[i].name:
            print("%-5d" % (index), end='')
            index += 1
            print(products[i].get_info())

