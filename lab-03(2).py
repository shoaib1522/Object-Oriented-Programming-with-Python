class Time_span:
    def __init__(self,minutes):
        self.minutes=minutes
    def show(self):
        hours=(self.minutes)//60
        minutes=(self.minutes)%60
        print(f'{hours} hours and {minutes} minutes')
    def add_hours(self,hrs):
        hours=(self.minutes+ (hrs*60))//60
        minutes=(self.minutes+ (hrs*60))%60  
        return f'After addition of {hrs} hours : {hours} hours and {minutes} minutes'
    def add_minutes(self,mins):
        hours=(self.minutes+mins)//60
        minutes=(self.minutes+mins)%60
        return f'After addition of {mins} minutes: {hours} hours and {minutes} minutes'
    def change(self,ts):
        abs_diff=abs(self.minutes-ts)
        return abs_diff
def main():
    Data_member=Time_span(220)
    Data_member.show()
    print(Data_member.add_hours(3))
    print(Data_member.add_minutes(40))
    print(f'After Absolute difference: {Data_member.change(470)}')
main()