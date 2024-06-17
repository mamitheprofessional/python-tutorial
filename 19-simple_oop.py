

class Employee:
    def __init__(self,name,base_pay,experience):
        self.name = name
        self.base_pay = base_pay
        self.experience = experience

    def get_pay(self):
        return self.base_pay
    
    def get_experience(self):
        return self.experience



class Doctor(Employee):
    def __init__(self,name,base_pay,experience,on_call_allowance):
        super().__init__(name,base_pay,experience)
        self.on_call_allowance=on_call_allowance

    def get_pay(self):
        return self.base_pay + self.on_call_allowance


class Nurse(Employee):
    def __init__(self,name,base_pay,experience,hourly_pay):
        super().__init__(name,base_pay,experience)
        self.hourly_pay=hourly_pay

    def get_pay(self):
        return self.base_pay*160 + self.hourly_pay

if __name__=="__main__":
    doc=Doctor("Millicent",12000,3000,7)
    print(doc.get_pay())
    print(doc.get_experience())
    emp = Employee("Tarnished", 9500, 4)
    print(emp.get_pay())
    print(emp.get_experience())
    nurse = Nurse("Malenia blade of Miquella", 8500, 85, 6)
    print(nurse.get_pay())