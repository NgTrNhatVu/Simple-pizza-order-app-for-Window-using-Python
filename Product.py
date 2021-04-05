# Object represents a product
class Product:
    __pro_id = 0
    __name = ""
    __pro_type = ""
    __s = ""
    __m = ""
    __l = ""
    __date_import = ""
    __status = ""

    def __init__(self, pro_id, name, pro_type, s, m, l, date_import, status):
        self.pro_id = pro_id
        self.name = name
        self.pro_type = pro_type
        self.s = s
        self.m = m
        self.l = l
        self.date_import = date_import
        self.status = status

    def get_pro_id(self):
        return self.pro_id

    def get_name(self):
        return self.name

    def get_pro_type(self):
        return self.pro_type

    def get_s(self):
        return self.s

    def get_m(self):
        return self.m

    def get_l(self):
        return self.l

    def get_date_import(self):
        return self.date_import

    def get_status(self):
        return self.status

    def get_info(self):
        print(f"%-10s    %10s    %9s %9s %9s %20s    %1s" % (self.name, self.pro_type, self.s, self.m. self.l, self.date_import, self.status), end='')
        return ''
