# Python3 code to demonstrate working of
# Extract values of Particular Key in Nested Values
# Using list comprehension

# initializing dictionary
test = {'Tst' : {"a" : 7, "b" : 9, "c" : 12},
			'is' : {"a" : 15, "b" : 19, "c" : 20},
			'best' :{"a" : 5, "b" : 10, "c" : 2}}

# printing original dictionary
print("The original dictionary is : " + str(test))

# initializing key
temp = "b"

# using item() to extract key value pair as whole
res = [val[temp] for key, val in test.items() if temp in val]

# printing result
print("The extracted values : " + str(res))