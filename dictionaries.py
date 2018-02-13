#Lists are generally used to store similar objects and we can access the elements by the index.
#We can store the items in a list and process them in order

#Dictionaries are unordered and contain key value pair. They are not addressed by an index but are indexed by a key

fruit = {"orange": "a sweet organge citrux fruit",
         "apple": "good for making cider",
         "grape": "a small sweet fruit",
         "lime": "a sour green citrus fruit"}

print(fruit)
print(fruit["apple"])

bike = {"make": "Honda", "model": "250 dream", "color":"red", "engine_size": 250}
print(bike["engine_size"])
print(bike["color"])

#keys can also be different types of object. the only restriction is that they must be immutable. However we can use tuples
#as we discovered out they are immutable

fruit["pear"] = "a good peachy fruit"
print(fruit)
#if you assign value to a key you will endup replacing the previous value rather than creating a new value
#if you redefine a key the value you define later will become the value of the key. To be more precise it just updated the alue

del fruit["lime"]
#accidently you delete the entire dictionary so take care


print(fruit)
#This will retain the dictionary but clear the values
# fruit.clear()

#accessing keys that are not present in the dictionary is going to give an error. So may want to avoid such situations

# while True:
#     dictKey = input("Please enter a fruit \n")
#     if(dictKey=="quit"):
#         break
#     description = fruit.get(dictKey, "We don't have a "+ dictKey)
#     print(description)
    #has_key method is a Python2 method has been deprecated in Python3. So you might avoid using that
    # if(dictKey in fruit):
    #     description=fruit.get(dictKey)
    #     print(description)
    # else:
    #     print("We don't have a {}".format(dictKey))

for snack in fruit:
    print(snack)

#there is no guarantee the order remains the same in the dictionary. So the key is hashed. It is a one way function.
#hash functions are used a lot in cryptography and checksums

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("=="*50)

#you usually don't; do ordering while making the dictionary but rather have the keys in a list and sort and use them to print

orderedKeys = list(fruit.keys())
orderedKeys.sort()
for f in orderedKeys:
    print(f + " is " + fruit[f])

# .values method is less efficient as compared to keys() method on dictionaries

fruit_keys  = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with icecream"
print(fruit_keys)
#it did include the tomato key, meaning that it must be pointing to a reference of the keys


#there is one more important method that we need to have a look at
print(fruit.items())
#gives me a list of tuples

f_tuple = fruit.items()
#pretty useful converting tuples back to a dictionary. can be used i guess in a lot of places
#let's continue with what we were learning
print(dict(f_tuple))

