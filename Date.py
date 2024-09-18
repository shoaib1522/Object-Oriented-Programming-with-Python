class Date:
    MaxDD=31
    MaxMM=12
    def __new__(cls,DD=1,MM=1,YYYY=1):
        obj = super().__new__(cls)
        return obj
    def __init__(self,DD=1,MM=1,YYYY=1):
        self.DD=DD
        self.MM=MM
        self.YYYY=YYYY
        return
    def __str__(self):
        return 'Date: {}-{}-{}'.format(self.DD,self.MM,self.YYYY)