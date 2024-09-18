from Batsman import batsman
def main():
    list_of_Batsmans=[]
    Batsman1=batsman(10)
    Batsman2=batsman(8)
    Batsman3=batsman(12)
    list_of_Batsmans.append(Batsman1)
    list_of_Batsmans.append(Batsman2)
    list_of_Batsmans.append(Batsman3)
    for batsmans in range (len(list_of_Batsmans)):
        print(f'Batsman No.{batsmans+1}')
        list_of_Batsmans[batsmans].show()
        print('\n')
if __name__ == "__main__":
    main()
