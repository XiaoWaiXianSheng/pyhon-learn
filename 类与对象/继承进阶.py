class Phone:
    IMEI = None  # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_5g(self):
        print("父类5g通话")


"""复写父类"""
"""调用父类成员及方法"""
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        '''方式1'''
        print(f"父类的厂商是{Phone.producer}")
        Phone.call_by_5g(self)
        print("子类5g")

    def call_by_5g01(self):
        """方式2"""
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

