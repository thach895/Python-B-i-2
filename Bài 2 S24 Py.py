class MemberCard:

    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if not isinstance(value, int):
            raise TypeError("Điểm phải là số nguyên")

        if value < 0:
            raise ValueError("Điểm không được âm")

        self.__points = value

    def add_points(self, amount):
        if amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000