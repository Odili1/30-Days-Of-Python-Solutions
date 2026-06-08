# ----- CLASSES AND OBJECTS
class Person:
    def __init__(self, firstname, lastname, age, city, country) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city
        self.country = country
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, *skill):
        self.skills.append(skill)


print(Person)

p = Person('Odili', 'diligwe', 12, 'lagos', 'Nigeria')
print(p.person_info())
p.add_skill('Spring Boot', 'Django', 'Express')
print(p.skills)

class Student(Person):
    def __init__(self, firstname, lastname, age, city, country) -> None:
        super().__init__(firstname, lastname, age, city, country)
    pass

s1 = Student('Emerie', 'Madu', 24, 'Osogbo', 'Nigera')
# print(s1)
# print(s1.age)


# ----- EXERCISE -----
# ----- LEVEL 1 -----
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self, data) -> None:
        self.data = data

    # Extra Methods
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def sort(self):
        return sorted(ages)
    
    # Measure of Central Tendency
    def mean(self):
        length = self.count()
        add = self.sum()
        return (add/length).__ceil__()
    def median(self):
        sorted_ages = self.sort()
        index = self.count() // 2
        return sorted_ages[index - 1]
    def mode(self):
        most = 0
        num = 0
        unique = list(set(self.data))
        i = 0
        while (i < len(unique)):
            freq = len(list(filter(lambda x: x == unique[i], self.data)))
            if (most < freq):
                most = freq
                num = unique[i]
            else:
                pass
            i += 1
        return f'mode: {num}, count: {most}'
    
    # Measure Variability
    def range(self):
        minimum = self.min()
        maximum = self.max()
        return maximum - minimum
    def variance(self):
        avg = self.mean()
        summation = 0
        for num in self.data:
            num -= avg
            summation += num **2
        return summation / (self.count() - 1)
    def std(self):
        from math import sqrt
        return sqrt(self.variance())
    def freq_dist(self):
        arr = []
        unique = set(self.data)
        for i in sorted(list(unique), reverse=True):
            freq = self.data.count(i)
            arr.append(tuple([float(freq*4), i]))
        return sorted(arr, key=lambda x: x[0], reverse=True)
    
    def describe(self):
        return (f'''
            Count: {self.count()}
            Sum: {self.sum()}
            Min: {self.min()}
            Max: {self.max()}
            Range: {self.range()}
            Mean: {self.mean()}
            Median: {self.median()}
            Mode: {self.mode()}
            Standard Deviation: {self.std()}
            Variance: {self.variance()}
            Frequency Distribution: {self.freq_dist()}
''')



data = Statistics(ages)
print("Count: ", data.count())
print("Sum: ", data.sum())
print("Min: ", data.min())
print("Max: ", data.max())
print("Range: ", data.range())
print("Mean: ", data.mean())
print("Median: ", data.median())
print("Mode: ", data.mode())
print("Standard Deviation: ", data.std())
print("Variance: ", data.variance())
print("Frequency Distribution: ", data.freq_dist())

print("Describe:", data.describe())



# ----- Level 2 -----
class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        pass
    def total_expenses(self):
        pass
    def account_info(self):
        pass
    def add_income(Self):
        pass
    def add_expenses(self):
        pass
    def account_balance(self):
        pass


# ---------- DONE ----------
