import os
import psutil
import datetime
import subprocess

def danas():

    return datetime.datetime.now().strftime("%Y-%m-%d %X")

def cpuUsage(limit):
    procenat = psutil.cpu_percent(interval = 1)
    usage = "PASS" if procenat < limit else "FAIL"

    return usage, procenat

def memoryUsage(limit):
    memorija = psutil.virtual_memory()
    slobodno = memorija.available/(1024*1024)
    usage = "PASS" if slobodno > limit else "FAIL"
    slobodno = round(slobodno/1024,1)

    return usage, slobodno

def diskSpace(limit):
    memorija = psutil.disk_usage('/').percent
    usage =  "PASS" if memorija < limit else "FAIL"

    return usage, memorija

def runningServices():
    radi = subprocess.run(
    ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager", "--no-legend"],
    stdout=subprocess.PIPE,
    text=True)

    services = []
    for red in radi.stdout.strip().split('\n'):
        if red:
            delovi = red.split()
            services.append(delovi[0])

    return services

def noviFajl():
    with open("dijagnostika.txt", "w") as fajl:
        fajl.write("Today is: ")

def main():

    noviFajl()
    fajl = open("dijagnostika.txt", "a")
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
