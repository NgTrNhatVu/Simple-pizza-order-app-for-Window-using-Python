import numpy as np
import pandas as pd

from Product import Product


class Helper:
    __excel_path = ""

    def __init__(self, excel_path):
        self.__excel_path = excel_path

    def get_list_of_product(self):
        # Reading excel input
        xls = pd.ExcelFile(self.__excel_path)
        df = xls.parse()
        # Turn the dataframe into a list of Objects(which is every products in the store)
        pro_list = [
            (Product(
                row["ID"],
                row["Name"],
                row["Type"],
                row["S"],
                row["M"],
                row["L"],
                row["Date import"],
                row["Status"]
            )
            )
            for index, row in df.iterrows()
        ]

        return pro_list
