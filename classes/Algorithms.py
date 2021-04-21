#pip install unidecode
#Change any unicode charater to ascii
import unidecode


class Algorithm:

################################# SORTING ######################################
    def quick_sort_by_name(self, products):
        #Get all the name in menu into a list
        name_list = []
        for i in range(len(products)):
            name_list.append(products[i].get_name())

        #Re-arrange all name in that new list
        self.__quick_sort(name_list, 0, len(name_list) - 1)

        #Create a new menu base on alphabetical order and return it
        sorted_pro_list = []
        for name in name_list:
            for i in range(len(products)):
                if name == products[i].get_name():
                    sorted_pro_list.append(products[i])
                    
        return sorted_pro_list

    def quick_sort_by_price(self, products):
        price_list = []
        #Adding tuples that hold each product's id and price to price_list
        for i in range(len(products)):
            new_tuple = (products[i].get_pro_id(), products[i].get_s())
            price_list.append(new_tuple)
        
        #Sorting price list base on 2nd element of every tuple element,
        # which is "price" => key = 1 means price
        self.__quick_sort(price_list, 0, len(price_list) - 1, key=1)
        
        #Create a new menu with the same order as price list and return it
        sorted_pro_list = []
        for price_index in range (len(price_list)):
            for pro_index in range(len(products)):
                if price_list[price_index][0] == products[pro_index].get_pro_id():
                    sorted_pro_list.append(products[pro_index])
                
        return sorted_pro_list


    def __quick_sort(self, arr, start, end, **kwargs):
        if start >= end:
            return
        if kwargs:
            p = self.__partition(arr, start, end, key=kwargs['key'])
            # Kinda some recursives
            # sorting numbers smaller than pivot
            self.__quick_sort(arr, start, p-1, key=kwargs['key'])
            # sorting number bigger than pivot
            self.__quick_sort(arr, p+1, end, key=kwargs['key'])
        else:
            p = self.__partition(arr, start, end)
            # Kinda some recursives
            # sorting numbers smaller than pivot
            self.__quick_sort(arr, start, p-1)
            # sorting number bigger than pivot
            self.__quick_sort(arr, p+1, end)
            
  # Help __quick_sort method to organize the every elements from "start" to "end"
    def __partition(self, arr, start, end, **kwargs):
        try:
            pivot = arr[start][kwargs['key']]
        except: 
            pivot = arr[start]
        low = start + 1
        high = end

        while True:
            try:
                while low <= high and arr[high][kwargs['key']] >= pivot:
                    high -= 1
                while low <= high and arr[low][kwargs['key']] <= pivot:
                    low += 1
            except:
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
    
################################ SEARCHING  ######################################
    def searching(self, products, item_name):
        founded_list = []
        
        item_name = item_name.lower()
        #Change any unicode character to ascii
        item_name = unidecode.unidecode(item_name)
        
        for index in range (len(products)):
            #Comparing item_name with lower-case ASCII product name
            if item_name in unidecode.unidecode(products[index].get_name().lower()):
                founded_list.append(products[index])
        
        return founded_list