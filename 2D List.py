#2D List
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][1])
print(matrix[2][2])

#Number of Rows
print(len(matrix))

#Number of Columns
print(len(matrix[0]))

#leaping through 20 List
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")

#Taking Input From Matrix
rows=int(input("Enter number of rows"))
column=int(input("Enter number of columns"))

matrix=[]

for i in range(rows):
    temp=[]
    for j in range(column):
        x=int(input("Enter a Element"))
        temp.append(x)
    
    matrix.append(temp)

for i in range(rows):
    for j in range(column):
        print(matrix[i][j],end="")
    print("\n")
