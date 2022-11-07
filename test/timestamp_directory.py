# create a new directory with timestamp as name 
import os, datetime

mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d'))
os.makedirs(mydir)