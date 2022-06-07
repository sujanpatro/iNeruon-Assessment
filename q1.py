import imp
from datetime import datetime

def log(message):
    file = open('logs.txt', 'r+')
    now = datetime.now()
    date = now.date()
    current_time = now.strftime("%H:%M:%S")
    file.write(str(date) + "/" + str(current_time) + "\t\t" + message +"\n")

def replace_func():
    file = open('example.txt', 'r')  # opening the file in read mode
    content = file.read()  # reading the contents of the file and storing in the content variable as a string
    file.close()  # closing file after reading

    content.replace('placement', 'screening')  # replacing 'placement' occurences with 'screening' in the content variable

    file = open('example.txt', 'w')  # reopening the file but in write mode
    # file is truncated this time
    file.write(content)  # writing the modified content to the file
    file.close()  # closing file after writing

replace_func()