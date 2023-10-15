with open("lol.txt",'w') as file:
    file.write('haha'*1000)


# modes for opening files
# r - erad a file(no writing) - this is the default
# w - write to a file(previous contents removed)
# a - append to a file(previous contents not removed) - but always adds to the end.
# r+ - read and write to a file(writing based on a cursor) - overwrites from beginning

# with open("story.txt",'a') as file:
#     file.seek(0,2)
#     file.write(":)\n")
    
# a and w creates new files if not already exisitng
# r and + only works with existing files
with open("story.txt",'r+') as file:
    file.write("added using r+")
    file.seek(20)
    file.write("added using r+")
    
