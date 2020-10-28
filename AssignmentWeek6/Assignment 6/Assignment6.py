# Open original file
path = r"test.txt"

# Destination file
new_file = open(r"new.txt","w")

# Function to number each line and write on the destination file
def num_of_line(the_path):
    n=0
    file = open(the_path)
    for lines in file.readlines():
        n += 1
        new_file.write("Line "+str(n)+"------>"+lines)
        
num_of_line(path)
print("The new file has been return.")