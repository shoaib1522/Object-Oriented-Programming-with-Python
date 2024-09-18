import random
class batsman:
    def __new__(cls,no_of_matches=None):
        obj=super().__new__(cls)
        return obj
    def __init__(self,no_of_matches=None):
        self.__no_of_matches=no_of_matches
        self.__name=None
        self.__country=None
        self.__score=[]
        if self.__no_of_matches==None:
            self.__no_of_matches=random.randint(1,95)
            self.__randomscore(self.__no_of_matches)
        else:
            self.__randomscore(no_of_matches)           
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,Name):
        self.__name=Name
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self,country_name):
        self.__country=country_name
    @property
    def no_of_matches(self):
        return self.__no_of_matches 
    @no_of_matches.setter
    def no_of_matches(self,number):
        self.__no_of_matches=number
        return
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score_upd):
        self.__score=score_upd
        return
    def __randomscore(self,no_of_matches):
        for i in range(self.__no_of_matches):
            random_number=random.randint(1,10)
            if random_number<=8:
                self.__score.append(random.randint(0,180))
            else:
                self.__score.append(random.randint(350,500))
        return
    def calctotal(self):
        calc_total=0
        for num in self.__score:
            calc_total+=num
        return calc_total
    def calcAverage(self):
        calc_Average=(self.calctotal())/(len(self.__score))
        return calc_Average
    def Maxscore(self):
        maximum_score=0
        for num in self.__score:
            if maximum_score<num:
                maximum_score=num
        return maximum_score
    def count50s(self):
        count_50s=0
        for num in self.__score:
            if num<100 and num>=50:
                count_50s+=1
        return count_50s
    def count100s(self):
        count_100s=0
        for num in self.__score:
            if num>=100 and num>50:
                count_100s+=1
        return count_100s
    def show(self):
        print('No of Matches: ',self.__no_of_matches)
        print('Score:',end=" ")
        for num in self.__score:
            print(num,end=' ')
        print()
        print('Total Score: ',self.calctotal())
        print('Average of Batsman: ',self.calcAverage())
        print('Maximum Score Of the Batsman: ',self.Maxscore())
        print('Total Number Of 50s: ', self.count50s())
        print('Total Number Of 100s: ', self.count100s())