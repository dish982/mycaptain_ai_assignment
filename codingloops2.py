def positive_num(list1):
    return[num for num in list1  if num>0]
a=input("Enter a list of numbers")
list1=[int(num.strip()) for num in a.split(", ")]
print("Positive numbers are:", positive_num(list1))