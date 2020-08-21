#importing 
import socket
#Enter Target Dns
print("")
hostname=str(input("Enter Dns Or Target : "))
Target_Ip=socket.gethostbyname(hostname)
print(" Host Name : {}".format(hostname))
print("Target Ip ===> {}".format(Targer_Ip))