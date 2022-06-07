from datetime import datetime

def log(message=None):
    f = open('logs.txt', 'a+')  # opening the log file
    
    now = datetime.now()
    date = now.date()  # get current date
    current_time = now.strftime("%H:%M:%S")  # get current time in the provide string format
    f.write(str(date) + "/" + str(current_time) + "\t\t" + message +"\n")  # appending the log message
    
    f.close()  # closing the log file

def replace_func():
    log("entered replace_func method")

    file = open('example.txt', 'r')  # opening the file in read mode
    log("opened the example.txt file in read mode")
    
    content = file.read()  # reading the contents of the file and storing in the content variable as a string
    log("extracted contents of the file to the 'content' variable")
    
    file.close()  # closing file after reading
    log("closed the example.txt file")

    content = content.replace('placement', 'screening')  # replacing 'placement' occurences with 'screening' in the content variable
    log("replaced 'placement' occurences with 'screening' in the content variable")

    file = open('example.txt', 'w')  # reopening the file but in write mode, but file is truncated this time
    log("reopened example.txt in 'w' mode, so that it truncates it while opening")
    
    file.write(content)  # writing the modified content to the file
    log("wrote modified contents to truncated example.txt")

    file.close()  # closing file after writing
    log("closed example.txt")

replace_func()
log("exited replace_func method, exiting program...")