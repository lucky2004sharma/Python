class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def code(self):
        print("Developer is writing Python code")


developer1 = Developer()

developer1.work()
developer1.code()