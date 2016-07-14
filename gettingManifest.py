import os
from time import *
fname = "id.txt"
count = 0
lines = open(fname).read().splitlines()
listOfbookmark = []
for line in lines:
    string = "curl 'https://chrome.google.com/webstore/ajax/detail?hl=en-US&gl=US&pv=20160613&mce=rlb%2Csvp%2Catf%2Chcn%2Cgtc%2Crtr%2Cpii%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cfcf%2Crma%2Cigb%2Cpot%2Cevt%2Crer%2Cshr%2Cesl&id={}&container=CHROME&_reqid=1512100&rt=j' -H 'accept-encoding: gzip,deflate' -H 'accept-language: en-US,en;q=0.8' --data 'login=&' --compressed | grep 'permissions' | grep 'bookmarks\\".format(line) + '\\",'+ "'"
    # print line
    a = os.popen(string).read()
    if (a):
        count = count + 1
        listOfbookmark.append(line)
print count
print listOfbookmark
