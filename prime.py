def prime(a):
    if a > 1:
        for i in range(2,a):
            if a%i == 0:
                break

        else:
            return a

list1 = [prime(val) for val in range(0,100) if prime(val) != None ]
print(list1)

# list1 = []
# for val in range(0,100):
#     a = prime(val)
#     if a != None:
#         list1.append(a)

a = 754
list2 = [q for q in list1 if a%q==0]
print(list2)

print("Largest prime factor of number:",max(list2))

# list2=[]
# a = 754
# for q in list1:
#     if a%q == 0:
#         list2.append(q)
# print(list2)








