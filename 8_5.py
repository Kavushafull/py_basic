class Warehouse:
    in_stock = {}
    @classmethod
    def to_unit(cls, printer = 0, scaner = 0, xerox = 0):
        cls.in_stock["Принтер"] = cls.in_stock["Принтер"] - printer
        cls.in_stock["Сканер"] = cls.in_stock["Сканер"] - scaner
        cls.in_stock["Ксерокс"] = cls.in_stock["Ксерокс"] - xerox
        return f'{printer} принтеров, {scaner}, сканеров и {xerox} ксероксов передано в подразделение'


    def __str__(self):
        return f'На складе: {self.in_stock.get("Принтер")} принтеров, {self.in_stock.get("Сканер")} сканеров, {self.in_stock.get("Ксерокс")} ксероксов'


class OfficeEquipment:
    printers_count = 0
    scanners_count = 0
    xeroxs_count = 0
    @classmethod
    def to_warehouse(cls):
        active_equipment = dict(zip(['Принтер', 'Сканер', 'Ксерокс'], [cls.printers_count, cls.scanners_count, cls.xeroxs_count]))
        return Warehouse.in_stock.update(active_equipment)

    def __str__(self):
        return f'В активе: {self.printers_count} принтеров, {self.scanners_count} сканеров, {self.xeroxs_count} ксероксов'


class Printer(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.printers_count = OfficeEquipment.printers_count + count

    def __str__(self):
        return f'Поступило {self.count} принтеров'


class Scaner(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.scanners_count = OfficeEquipment.scanners_count + count

    def __str__(self):
        return f'Поступило {self.count} сканеров'


class Xerox(OfficeEquipment):
    def __init__(self, count):
        self.count = count
        OfficeEquipment.xeroxs_count = OfficeEquipment.xeroxs_count + count

    def __str__(self):
        return f'Поступило {self.count} ксераксов'


a = Printer(4)
print(a)
b = Printer(6)
c = Scaner(5)
d = Xerox(7)
print(OfficeEquipment())
OfficeEquipment.to_warehouse()
print(Warehouse())
print(Warehouse.to_unit(1, 2))
print(Warehouse())
