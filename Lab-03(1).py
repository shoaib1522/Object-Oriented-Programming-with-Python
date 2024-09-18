class Time_span:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
        self.total=(hours*60)+minutes
    def show(self):
        print(f'{self.hours} hours and {self.minutes} minutes')
    def add_hours(self,hrs):
        self.hours=self.hours+hrs  
    def add_minutes(self,mins):
        self.hours=(self.total+mins)//60
        self.minutes=(self.total+mins)%60
    def change(self,ts):
        abs_diff=abs(self.total-ts.total)
        return abs_diff
def main():
    Data_member=Time_span(3,40)
    Data_member.show()
    #After addition of 3 hours in 3 hours and 40 minutes
    Data_member.add_hours(3)
    Data_member.show()
    # after addition of 40 minutes in 3 hours and 40 minutes
    Data_member.add_minutes(40)
    Data_member.show()
    # CHANGE DATA-MEMBER
    ts=Time_span(7,50)
    ts.show()
    print(f'After Absolute difference: {Data_member.change(ts)}')
main()