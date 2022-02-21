#created by satwika
string=str(input("enter the string:-") )
even_letters=""
for i in range(len(string)):
        if i%2==0:
            even_letters = even_letters + string[i]
print(even_letters)
