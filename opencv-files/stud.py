from sklearn.metrics import SCORERS


class student:
    def __init__(self,name ,score):
        self.name = name 
        self.score = score
    def grade(self):
        if(self.score >=90):
            print(f"{self.name } got A grade")
        elif self.score >=81 and self.score <=89:
            print(f"{self.name} got B grade")
person1 = student("anyone",89)
person1.grade()