class Phone:
    IMEI = None  # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_4g(self):
        print("4g通话")


'''单继承'''


class Phone2022(Phone):
    faceId = "100001"

    def call_by_5g(self):
        print("5g通话")


phone = Phone2022()

print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外开启")


"""多继承"""
class MyPhone(Phone, NFCReader, RemoteControl):
    """pass关键词，替代语法，不报错"""
    pass


phone01 = MyPhone()
phone01.read_card()
phone01.control()
phone01.call_by_4g()
print(phone01.producer)