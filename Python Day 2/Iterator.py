       ################### Iterator ####################
# __iter__()
# __next__()
num = [1,2,3,4]

it = iter(num)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


# EXaple
class MyNumber:
    def __init__(self,limit):
        self.num = 1
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= self.limit:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration
nums = MyNumber(3)
for i in nums:
    print(i)

