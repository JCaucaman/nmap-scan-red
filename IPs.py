import nmap
import platform
import subprocess

def myIp():
    if platform.system() == 'Windows':
        ip = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")

    else:
        ip = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")

    return ip

def ipWithMask(ip):

    ipList = ip.split(".")
    ipList[-1] = "0"
    ipStr = ".".join(ipList)
    ipMaskStr = ipStr + "/24"

    return ipMaskStr


def escanMyRed():
    ip1 = myIp()
    ipMask = ipWithMask(ip1)
    print(ipMask)

    nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
    scanner = nmap.PortScanner(nmap_search_path=nmap_path)  
    scanner.scan(hosts=ipMask, arguments='-sn')
        
    all_ip = scanner.all_hosts()

    for host in all_ip:
        print(scanner[host], end="\n")
        
escanMyRed()