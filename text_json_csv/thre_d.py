#multi threading= used to perform mutiple task concurrently
#thread= a single sequence of execution in a program    


import threading
import time

def animal():
    time.sleep(8)
    print("you finish walking the dog")

def trash():
    time.sleep(3)
    print("you finish taking out the trash")
def mail():
    time.sleep(5)
    print("you finish receiving the mail")


chore1=threading.Thread(target=animal)
chore1.start()
chore2=threading.Thread(target=trash)
chore2.start()
chore3=threading.Thread(target=mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("all chores are started")