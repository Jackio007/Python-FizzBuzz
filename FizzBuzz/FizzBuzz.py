import timeit

code = """

def FizzBuzz(i):

    list = {
        "0":"FizzBuzz",
        "1":"Fizz",
        "2":"Buzz",
        "3":i
    }
    
    val = 0

    if i%3==0 and i%5==0:
        val = 0
    elif i%3 == 0:
        val = 1
    elif i%5 == 0:
        val = 2
    else:
        val = 3

    x = list.get(str(val))
    print(x)

i = 1

while i < 100000:
    FizzBuzz(i)

    i = i+1
"""


execution_time = timeit.timeit(code, number=1)

print("\n")
print(execution_time)
