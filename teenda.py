from random import randint

class Teenda:
    @property
    def Category(self):  # 3 or 5
        return self.__cat

    @Category.setter
    def Category(self, c):
        self.__cat = c

    @property
    def Data(self):  # a list of 5 integers
        return self.__data

    @Data.setter
    def Data(self, d):
        self.__data = [0] * 5
        self.__data[0] = d[0]
        self.__data[1] = d[1]
        self.__data[2] = d[2]
        if self.Category == 5:
            self.__data[3] = d[3]
            self.__data[4] = d[4]

    @property
    def isDead(self):  # Bool
        return self.__dead

    def __kill(self):  # Bool
        self.__dead = True

    def __init__(self, c, d):
        self.Category = c
        self.Data = d
        self.__dead = False

    def __isValid(self):
        rv = False
        if (
            self.Category == 3
            and self.Data[1] > self.Data[0]
            and self.Data[1] > self.Data[2]
            and self.Data[0] > self.Data[2]
        ):
            rv = True
        elif (
            self.Category == 5
            and self.Data[2] > self.Data[0]
            and self.Data[2] > self.Data[1]
            and self.Data[2] > self.Data[3]
            and self.Data[2] > self.Data[4]
            and self.Data[1] > self.Data[0]
            and self.Data[1] > self.Data[3]
            and self.Data[1] > self.Data[4]
            and self.Data[0] > self.Data[4]
        ):
            rv = True
        return rv

    def __destroy(self):
        self.__kill()

    def __split(self):
        if self.Category == 5:
            print("spliting .... " + str(self))

            h = self.Data[2] // 2
            t1 = Teenda(3, [self.Data[0], self.Data[1], h])
            t2 = Teenda(3, [h, self.Data[3], self.Data[4], h])
            if not t1.__isValid():
                t1.__destroy()
            if not t2.__isValid():
                t2.__destroy()
            self.__destroy()
            return [t1, t2]
        else:
            return []

    def __grow(self):
        if self.Category == 3:
            print("growing .... " + str(self))
            self.Category = 5

            self.Data[4] = self.Data[2]
            self.Data[2] = self.Data[1]
            self.Data[1] = (self.Data[0] + self.Data[2]) // 2
            self.Data[3] = (self.Data[2] + self.Data[4]) // 2
            if not self.__isValid():
                self.__destroy()
                return []
            else:
                return []

    def mutate(self):
        rn = randint(2345, 9876)
        if rn % 11 == 0 or rn % 23 == 0 or rn % 67 > 55:
            return self.__split()
        elif rn % 7 == 0 or rn % 17 == 0 or rn % 83 < 13:
            return self.__grow()

    def __str__(self):
        r = ""
        r = (
            r
            + "T"
            + str(self.Category)
            + ": "
            + str(self.Data[0])
            + " "
            + str(self.Data[1])
            + " "
            + str(self.Data[2])
        )
        if self.Category == 5:
            r = r + " " + str(self.Data[3]) + " " + str(self.Data[4])
        return r


def main():
    teendas = []
    teendas.append(Teenda(3, [4, 7, 2]))
    teendas.append(Teenda(5, [23, 35, 42, 30, 20]))
    teendas.append(Teenda(3, [7, 29, 3]))
    j = 1
    while j <= 100:  # 100000000:
        print("----- iteration no. " + str(j))
        for t in teendas:
            if t.isDead == False:
                print(str(t))
        for t in teendas:
            if t.isDead == False:
                newteendas = t.mutate()
                if newteendas:
                    for nt in newteendas:
                        teendas.append(nt)
        j = j + 1


main()
