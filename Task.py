class NUMBERS:
    def __init__(self):
        self.odd_numbers = []
        self.even_numbers = []
        self.current_index = 0
    def add_number(self, num):
        if isinstance(num, (int, float)):
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)
    def delete_number(self, num):
        if num in self.odd_numbers:
            self.odd_numbers.remove(num)
        elif num in self.even_numbers:
            self.even_numbers.remove(num)
    def alter_number(self, old_num, new_num):
        self.delete_number(old_num)
        self.add_number(new_num)
    def search_number(self, num):
        combined_list=self.odd_numbers+self.even_numbers
        if num in combined_list:
            return f"{num}, The Number Exists!"
        else:
            return f"{num}, The Number Doesn't Exists!"
    def print_numbers(self):
        numbers_list = []
        min_len = min(len(self.odd_numbers), len(self.even_numbers))
        for i in range(min_len):
            numbers_list.append(self.odd_numbers[i])
            numbers_list.append(self.even_numbers[i])
        numbers_list += self.odd_numbers[min_len:] + self.even_numbers[min_len:] 
        print(numbers_list)
    def __iter__(self):
        self.current_index = 0
        return self
    def __next__(self):
        combined_list = self.odd_numbers + self.even_numbers
        if self.current_index < len(combined_list):
            result = combined_list[self.current_index]
            self.current_index += 1
            return result
        else:
            return f'Iteration Stopped'
    def __getitem__(self, index):
        min_len = min(len(self.odd_numbers), len(self.even_numbers))
        if index < min_len * 2:
            if index % 2 == 0:
                return self.odd_numbers[index // 2]  
            else:
                return self.even_numbers[index // 2]
        else:
            return f'Index is out of range !'
    def __setitem__(self,index, value):
        min_len = min(len(self.odd_numbers),len(self.even_numbers))
        if index<min_len * 2:
            if index % 2 == 0:
                self.odd_numbers[index // 2] = value
            else:
                self.even_numbers[index // 2] = value
        else:
            return f'Index is out of range !'
def main():
    numbers = NUMBERS()
    numbers.add_number(3)
    numbers.add_number(8)
    numbers.add_number(5)
    numbers.add_number(12)
    numbers.add_number(7)
    print("Original List:")
    numbers.print_numbers()
    value = numbers[2]
    print("Value at index 2:", value)
    numbers[2] = 10
    print("After Changing 5 to 10 using index operator:")
    numbers.print_numbers()
main()

