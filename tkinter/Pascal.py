#Pascal triangle
def pascal_triangle(N): #N - number of rows
    pascal_triangle = [] #list of lists
    for i in range(0, N): #number of rows
        new_row = [1] #first element of the row
        for j in range(1, i): #number of elements in the row
            new_row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]) #sum of the two elements above
        new_row.append(1) #last element of the row
        pascal_triangle.append(new_row) #add the row to the triangle
    return pascal_triangle #return the triangle

print(pascal_triangle(6)) #print the triangle
