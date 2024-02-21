#print multiplication program using for loop
num=int(input("Enter the number for multiplication table:-"))
print("The multiplication table of:-",num)
for i in range(1,11):
    print(num,'*',i,'=',num*i)
#----------------------------------
#print 1 to 10 multuplication table
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end='')
        print()
#---------------------------------
#to display vowel and consonant
d=['a','d','b','c','t','h','f']
v=[]
c=[]
for ci in d:
    if ci in 'aeiou':
        v.append(ci)
    else :
        c.append(ci)
print(v)
print(c)
#----------------------------
#To display average of each given number
a=[5,10,15,20,25]
total=0
for b in a:
    total += b
    avg=total/len(a)
    print('Avrg',avg)
#-----------------------------
#to display square of given number
for i in range(1,5):
    print(i,i**2)



