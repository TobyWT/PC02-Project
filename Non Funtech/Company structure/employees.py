class Employee:
    def __init__(self, pay, email, name):
        self.name = name
        self.pay = pay
        self.email = email


class Developer(Employee):
    def __init__(self, pay, email, name):
        Employee.__init__(self, pay, email, name)
        # why do we need to use self parameter???


