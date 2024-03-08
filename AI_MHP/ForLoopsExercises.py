
s = "your name"

print("1/PRINT all characters in 'your name' by using for loops")
for c in s:
    print(c)

print("2/PRINT all odd numbers x such that 1<=x<=10")
sum=0
for i in range(1, 11):
    if i%2==1:
        print(i)
        sum+=i

print(f"3/Computing the sum of numbers:\n    a/Compute the sum of all numbers in 2/: {sum}")
sum = 0
for i in range(1,7):
    sum+=i
print(f"    b/Compute the sum of all numbers from 1 to 6: {sum}")
mydict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
print("4/Given dict={'a': 1,'b': 2,'c': 3,'d': 4}")
print(f"    a/print all keys in dict")
for s in mydict.keys():
    print(s)
print(f"    b/print all values in dict")
for s in mydict.values():
    print(s)
print(f"    c/print all keys and values in dict")
for s in mydict:
    print(f"{s} = {mydict[s]}")

print("5/ Given courses=[131,141,142,212] and names=['Maths','Physics','Chem', 'Bio']. \nPrint a sequence of tuples, each of them contains one courses and one names")
courses = [131, 141, 142, 212]
names=["Maths","Physics", "Chem", "Bio"]
myTuples = []
myTuples = list(zip(courses, names))
# for i in range(len(courses)):
#     t = (courses[i], names[i])
#     myTuples.append(t)
print(myTuples)

print("6/ Find the number of consonants in “jabbawocky” by two ways")
str = "jabbawocky"
vowels = "ueoaiUEOAI"

count = 0
for s in str:
    if vowels.find(s) == -1:
        count+=1
print(f"    a/ Directly (i.e without using the command “continue”): {count}")
count = 0
for s in str:
    if vowels.find(s) != -1:
        count+=1
    else:
        continue
print(f"    b/ Check whether it’s characters are in vowels set and using the command “continue”: {count}")

print("7/ a is a number such that -2<=a<3. Print out all the results of 10/a using try…except. When a=0, print out “can’t divided by zero”")
for i in range(-2, 4):
    try:
        print(f"10/{i} = {10/i}")
    except Exception as Exc:
        print("Can't divided by zero")

print("8/ Given ages=[23,10,80] and names=[Hoa,Lam,Nam].\n Using lambda function to sort a list containing tuples (“age”,”name”) by increasing of the ages")
ages=[23,10,80]
names=["Hoa","Lam","Nam"]
myTuples = list(zip(ages,names))
myTuples.sort(key= lambda x : x[0])
print(myTuples)

