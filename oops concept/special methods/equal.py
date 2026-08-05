class student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
s1 = student("nishat")
s2 = student("nishat")
s3 = student("karishma")

print(s1 == s2)
print(s1 == s3)