"""
私有成员的使用
"""


class Phone:

    __current_voltage = 1  # 运行电压

    def __keep__single_core(self):
        print("CPU单核模式")

    '''私有成员无法被类对象使用，但可以被 其他的成员使用'''
    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("满足5g")
        else:
            self.__keep__single_core()
            print("单核模式运行")


phone = Phone()
# phone.__keep__single_core

# print(phone.__current_voltage)

phone.call_by_5g()