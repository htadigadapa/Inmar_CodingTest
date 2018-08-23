start_range=1
end_range=100
for i in range(start_range,end_range+1):
    if (i%3 == 0) and (i%5 == 0):
        print(str(i) +" is divisible by 3,5")
        print("Fizzbuzz")
    elif i%5 == 0:
        print(str(i) +" is divisible by 5")
        print("buzz")
    elif i%3 == 0:
        print(str(i) +" is divisible by 3")
        print("Fizz")


