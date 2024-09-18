class Company(object):
    def __init__(self,name,name_rep,Bio,Cell_Number,TypeofMemo):
        self.__name=name
        self.__bio=Bio
        self.__namerep=name_rep
        self.__cell=Cell_Number
        self.__memo=TypeofMemo
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n
        return self.__name
    @property
    def namerep(self):
        return self.__namerep
    @namerep.setter
    def namerep(self,Nr):
        self.namerep=Nr
        return self.__namerep
    @property
    def bio(self):
        return self.__bio
    @bio.setter
    def bio(self,b):
        self.__bio=b
        return self.__bio    
    @property
    def cell(self):
        return self.__cell
    @cell.setter
    def cell(self,c):
        self.__cell=c
        return self.__cell
    @property
    def memo(self):
        return self.__memo
    @memo.setter
    def memo(self,Mem):
        self.__memo=Mem
        return self.__memo
    def __str__(self):
        string=f'{self.__name.upper()} \n'
        string+=f'{self.__namerep.upper()} \n'
        string+=f'{self.__bio} \n'
        string+=f'Cell No: {self.__cell} \n'
        string+=f'{self.__memo.upper()}MEMO'
        return string 
    
    
    