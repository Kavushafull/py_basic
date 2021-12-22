class Warehouse:
    in_stock = {}


class OfficeEquipment:
    printers_count = 0
    scanners_count = 0
    xeroxs_count = 0

    def __str__(self):
        return f'На складе {self.printers_count} принтеров, {self.scanners_count} сканеров, {self.xeroxs_count} ксероксов'


class Printer(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.printers_count = OfficeEquipment.printers_count + count

    def __str__(self):
        return f'На склад поступило {self.count} принтеров'


class Scaner(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.scanners_count = OfficeEquipment.scanners_count + count

    def __str__(self):
        return f'На склад поступило {self.count} сканеров'


class Xerox(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.xeroxs_count = OfficeEquipment.xeroxs_count + count

    def __str__(self):
        return f'На склад поступило {self.count} ксераксов'


a = Printer(4)
print(a)
b = Printer(6)
c = Scaner(5)
d = Xerox(7)
print(OfficeEquipment())
