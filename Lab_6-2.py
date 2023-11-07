#Create a Python file named lab_6-2.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a variable my_row and set it equal to a list that contains the names of 2 people in your row.
my_row = ["sean","lowell"]
#Using slices, add your name to the end of the list.
my_row[2:2] = ["dylan"]
#Create another variable my_row2 and set it equal to my_row.
my_row2 = my_row
#Add a statement that prints my_row2
print(my_row)
#Add a statement that removes the value at index 1 from my_row
del my_row[1]
#Add a statement that prints my_row. What do you notice happens and why?
print(my_row)
    #the word lowell is removed becuse the index starts at 0 and lowell is in the seccond slot

