numbers=[]

while True:
    x=input()
    if x=="Done":
        break
    else:
        numbers.append(float(x))
print(len(numbers))
print(sum(numbers)/len(numbers))
print(min(numbers))
print(max(numbers))