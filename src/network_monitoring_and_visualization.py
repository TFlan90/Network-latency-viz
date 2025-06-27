from pythonping import ping


def getPing(ip_or_hostname:str):
    result = ping(ip_or_hostname, count=4)
    print(result)



ip_or_hostname = input("Give an IP address or hostname\n")
getPing(ip_or_hostname)
