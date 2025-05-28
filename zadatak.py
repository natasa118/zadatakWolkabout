import os
import psutil
import datetime
import subprocess

def danas():
    return datetime.datetime.now().strftime("%Y-%m-%d %X")

def cpuUsage(limit):
    procenat = psutil.cpu_percent(interval = 1)
    #print(procenat)

    usage = "PASS" if procenat < limit else "FAIL"
    
    return usage, procenat

def memoryUsage(limit):
    memorija = psutil.virtual_memory()
    slobodno = memorija.available/(1024*1024)
    #print(slobodno)
    usage = "PASS" if slobodno > limit else "FAIL"
    slobodno = round(slobodno/1024,1)
    return usage, slobodno

def diskSpace(limit):
    memorija = psutil.disk_usage('/').percent
   # print(memorija)
    usage =  "PASS" if memorija < limit else "FAIL"
    return usage, memorija

def runningServices():
    radi = subprocess.run(
    ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager", "--no-legend"],
    stdout=subprocess.PIPE,
    text=True)

    #print (radi)
    services = []
    
    for red in radi.stdout.strip().split('\n'):
        if red:
            delovi = red.split()
            services.append(delovi[0])

    #print(services)
    return services

def noviFajl():
    with open("dijagnostika.txt", "w") as fajl:
        fajl.write("Today is: ")

def main():
    os.chdir("/home/natasa/Desktop/python/")
    
    noviFajl()
    fajl = open("dijagnostika.txt", "a")

    #print(danas())
    #cpuUsage(10.0)
    #memoryUsage(500)
    #diskSpace(80)
    #runningServices()
    
    fajl.write(danas()+"\n")
    cpuPass, cpuProc = cpuUsage(10.0)
    memPass, memFree = memoryUsage(500)
    diskPass, diskProc =diskSpace(80)
    servisi = runningServices()

    
    fajl.write("CPU check: "+cpuPass+" ("+str(cpuProc)+"%)\n")
    fajl.write("Memory check: "+memPass+" ("+str(memFree)+"GB free)\n")
    fajl.write("Disk check: "+diskPass+" (/ partition at "+str(diskProc)+"%)\n")
    fajl.write("Running services: \n")
    for stavka in servisi:
        fajl.write("- "+ stavka + "\n")


    fajl.close()


main()
