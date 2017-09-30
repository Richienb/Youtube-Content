import time 
from subprocess import call

#read
data = open("links.txt","r")
#store lines in array
links = data.readlines()

#loop through links
for link in links:
    script = "youtube-dl --no-check-certificate --format best "+link 
    call(script)
