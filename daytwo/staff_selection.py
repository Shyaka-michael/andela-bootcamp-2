'''opp aspects inheritence polymorpshim overinding'''

class Staff():
    def __init__(self,id_no,name,sex,):
        self.id_no = id_no
        self.name = name
        self.sex =sex
        self.salary_variation = 1550


    def pay(self ):
        """OOP overide mehod in subclass"""
        pass

class Teaching(Staff):
    """ inheretence """
    salary_variation = 2000
    """encapsulation of a class varaiable teaching staff get more money"""
    def __init__(self,id_no,name,sex, postion ):
        super().__init__(id_no,name,sex)


    def pay(self,ammount):
        """polymorphis through overriding"""
        if ammount > self.salary_varition:
            print('ammount can pay teaching staff')
            return True
        else:
            print('ammount cannot pay teaching staff')
            return False



class Non_teaching(Staff):
    def __init__(self,id_no,name,sex, postion):
        super().__init__(id_no, name, sex)

    def pay(self,ammount):
        if ammount > self.salary_varition:
            print('ammount cannot be paid to non_teaching staff')
            return False
        else:
            print('ammount can pay non_teaching staff')
            return True
