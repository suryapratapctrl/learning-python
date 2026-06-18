# we multithreading to perform multiple tasks at same time
import threading
import time

def walk_dog(firstname,lastname):
  time.sleep(8)
  print(f'you finish walking {firstname}{lastname}')

def take_out_trash():
  time.sleep(2)
  print('you take out the trash')

def get_mail():
  time.sleep(4)
  print("you get the mail")

chore1=threading.Thread(target=walk_dog,args=("max","the husky"))
chore1.start()
chore2=threading.Thread(target=take_out_trash)
chore2.start()
chore3=threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print('all chores are done')