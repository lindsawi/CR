## This script is used to compare two list text documents to determine the difference between the two lists. 
# file 1 is larger
# file 2 is smaller 

with open('Spring-holds-all.txt', 'r') as file1:
    with open('already-emailed.txt', 'r') as file2:
        difference = set(file1).difference(file2)

difference.discard('\n')

with open('diff.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)
