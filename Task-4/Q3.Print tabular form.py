#Created by satwika
#2D list in Python
#s is a 2d list to store all tha data
s = [ [1, 'Matangi', 96],
      [2, 'Gayatri', 82],
      [3, 'Satwika', 89]]
#Take input from user
for i in range(3):    #taking student name from user
     for j in range(1):
        s[i][j+1]=str(input("Enter the {0}Student Name  ".format( int(i+1) ) ) )
for i in range(3):    #taking student marks from user
     for j in range(1):
        s[i][j+2]=str(input("Enter the {0} Student Marks  ".format( int(i+1) ) ) )          
#Printing the Section Names
print("{:<10} {:<10} {:<10}".format('Roll no','Name','Marks') )
#for loops to output the data from the 2D list
for i in range(3):            #first row
    print(s[0][i],end=" "*10)
print()
for i in range(3):            #second row
    print(s[1][i],end=" "*10) 
print()
for i in range(3):            #third row
    print(s[2][i],end=" "*10)     
print()
print("The second row from the data is ", s[1][0] , s[1][1] , s[1][2] )
