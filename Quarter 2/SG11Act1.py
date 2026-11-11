class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # --- name property ---
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print("Error, name must be a string(text)")
            return
        self.__name = name

    # --- bill_amount property ---
    @property
    def bill_amount(self):
        return self.__bill_amount

    @bill_amount.setter
    def bill_amount(self, bill_amount):
        try:
            self.__bill_amount = float(bill_amount)
        except (ValueError, TypeError):
            print("Error, bill amount must be a float")

    # --- business logic ---
    def calculate_bill(self):
        # base class: bill unchanged
        pass

    def display_patient_type(self):
        return "Regular Patient"


class SeniorPatient(Patient):
    def calculate_bill(self):
        # 20% discount
        self.bill_amount = self.bill_amount * 0.80

    def display_patient_type(self):
        return "Senior Citizen"


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        # 15% discount
        self.bill_amount = self.bill_amount * 0.85

    def display_patient_type(self):
        return "PhilHealth Member"


p1 = Patient("Juan de la Cruz", 15000)
print(f"Patient Name: {p1.name}")
print(f"Patient Type: {p1.display_patient_type()}")
print(f"Original Bill: {p1.bill_amount:.2f}")
p1.calculate_bill()   
print(f"New Bill: {p1.bill_amount:.2f}")

p2 = SeniorPatient("Maria Santos", 15000)
print(f"Patient Name: {p2.name}")
print(f"Patient Type: {p2.display_patient_type()}")
print(f"Original Bill: {p2.bill_amount:.2f}")
p2.calculate_bill()
print(f"New Bill: {p2.bill_amount:.2f}")
          
p3 = PhilHealthPatient("Pedro Reyes", 15000)
print(f"Patient Name: {p3.name}")
print(f"Patient Type: {p3.display_patient_type()}")
print(f"Original Bill: {p3.bill_amount:.2f}")
p3.calculate_bill()
print(f"New Bill: {p3.bill_amount:.2f}")

