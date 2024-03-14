#tuple ,set and dictionary
#tuple is immutable,ordered collection of objects.It's a collection that cannot be changed
#after it is created.
#diffrence between list and tuple
#list is changable but list is not both are odered and allow duplicate value
#set is unordered and doesnot allow the duplicate element
#dictionary is also unordered collection of key:value pair.It's not ordered and 
#decleration - list is decalred with [] but tuples are declared with ()
tup=("apple","banana","cherry")
print(tup)
tup2=("rose","dandellions ", "lotus" ,"sunflower "," lily","daliya")
print(tup2)
#remove duplicates from list using set() method in python
#accessing elemets in tuples
print(tup2[-1])
print(tup[2])
print(tup2[3])
#for certain range
print(tup2[2:])

#check if rows is present in tuple
print("rose" in tup)
#count no of times rose is present in tuple
print("rose".count("rose"))

if "apple" in tup :
    print("yes there is apple in the list")

print("lily".count in tup)

#once tuple is creted you cannot change its value 
#but you can convert the tuple in list and change the list and convert the list backa in tuple
x = ("apple"," banana","mango")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#convert the tuple into list , add "orange " and convert it back into tuple
m = ("apple"," banana","mango")
n=list(m)
y.append("kiwi")
m=tuple(y)
print(x)
y.remove("apple")
del m
print("tuple deleted")

#unpacking a tuple
#apple="green"
#banana="yellow"
#cherry="red"
#using astrisk will apply it universally
fruits =("apple","banana" ,"cherry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#using for loop
thistuple=("apple","banana","cherry")
for i in thistuple :
    print(i)

#to join two or more tuples
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3 =tuple1+tuple2
print(tuple3)

# to print tuple n no of times just multiply it 
multuple=tuple1*2
print(multuple)

#to count the element is tuple
tuple4=(2,3,4,5,6,5)
x=tuple4.count(5)
print(x)

#sets 
s={"apple", "banana", "cherry"} #set is unordered collection of
#a setr is a unodered unchangable and unindexed  collection of unique elements
print(s)

#if there is any duplicate value it will ignore it there will not be a ny error
s1={"apple", "banana", "cherry","cherry"} 
s2={"apple","banana",True ,2}
print(s1)
print(s2)
#to find the length of set
print(len(s))

s3={"saitama","goku","naruto"}
s4={1,3,6}
s5={True,False,True}
print(s3)
print(s4)
print(s5)

#to find data types of set
print(type(s3))

#to add elemets from s3 to s4 we use update
s4.update(s3)
print(s4)

#remove
s5.remove(False)
print(s5)

#discard
s5.discard("True")

#clear
s3.clear()

#union
set1={"a","b","c",2}
set2={1,2,3}
set1.union(set2)
set1.update(set2)
print(set1)

#intersection
set1.intersection_update(set2)
print(set1)

#keep the items that are not present in both the sets
x={"apple","bannaa","kiwi"}
y={"apple","orange","mango"}
z=x.symmetric_difference(y)
print(z)

#dictionaries are written with curly brackets and have keys and values
thisdict ={
    "brand":"Marcedes-Benz",
    "model":"EQS",
    "year": 2024
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

#dictionaries with multiple data types