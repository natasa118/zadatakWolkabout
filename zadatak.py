import os
import psutil
import datetime

def danas():
    return datetime.datetime.now().strftime("%Y-%m-%d %X")

def cpuUsage(limit):
    procenat = psutil.cpu_percent(interval = 1)
    #print(procenat)

    usage = True if procenat < limit else False
    
    return usage, procenat

def memoryUsage(limit):
    memorija = psutil.virtual_memory()
    slobodno = memorija.available/(1024*1024)
    #print(slobodno)
    usage = True if slobodno > limit else False
    return usage

os.chdir("/home/natasa/Desktop/python")
fajl = open("dijagnostika.txt", "w")

#print(danas())
#cpuUsage(10.0)
memoryUsage(500)

fajl.close()

