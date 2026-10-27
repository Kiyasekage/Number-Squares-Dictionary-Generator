def generated_square(n):
    dictionary = {}
    for i in range(1,n+1):
        dictionary[i] = pow(i,2)
    return dictionary


print("Welcome to generating ascending numbers and its square values to a dictionary")
limit = int(input("Please input the limit of dictionary : "))
given_dict = generated_square(limit)
print(given_dict)
