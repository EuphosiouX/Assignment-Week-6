# Open the file
f=open(r"Confessions of a Tradesman by Frank Thomas Bullen Book Cover  Download This eBook.txt",'r')

# Variables
new_list = []
iter = 0

# Iterate through each word
for word in f:
    new_list += word.split()

# Iterate through each letter
for n in new_list:
    iter += len(n)

# Count the average
print("Average: {}".format(iter/len(new_list)))