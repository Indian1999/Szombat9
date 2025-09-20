#print("Hello World!")
#name = input("Add meg a neved: ")
#print("Hello " + name + "!")

#print(type(name)) #<class 'str'> komment

name = "Logi Róbert"
age = 11
weight = 42.7
is_smart = False

print(type(name))       #<class 'str'>
print(type(age))        #<class 'int'>
print(type(weight))     #<class 'float'>
print(type(is_smart))   #<class 'bool'>

print("Szia! A nevem " + name + "!")
print(str(age) + " éves vagyok!")
print("A súlyom " + str(weight) + " kg.")
if is_smart == True:
    print("Okos vagyok.")
else:
    print("Nem vagyok valami okos...")

birth_year = int(input("Add meg, hogy melyik évben születtél: "))
result = birth_year + age # type int
if result < 2025:
    print(str(result) + "-ban/-ben voltál annyi idős, mint most én!")
elif result > 2025:
    print(str(result) + "-ban/-ben leszel annyi idős, mint most én!")
else:
    print("Ugyan annyi idősek vagyunk!")

#2010 -> "2010"