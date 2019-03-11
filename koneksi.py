import paramiko 
import time
import os
from progress.bar import Bar


print  ("\n") 
print  ("MMM      MMM       KKK                          TTTTTTTTTTT      KKK")
print  ("MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK")
print  ("MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK KKK")
print  ("MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK")
print  ("MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK")
print  ("MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK")
print ("")
print ("===========================================================================")
print ("================Otomatisasi Mikrotik Dengan Python=========================")
print ("===========================================================================")

print ("")
ip_list  = input("Masukan Alamat Ip Router: ")
print ("")
username = input("Masukan Username Router : ")
print ("")
password = input("Masukan Password Router : ")

os.system("clear")
try:

	print("")

	bar = Bar('Check Koneksi Ke Router', max=9)
	for i in range(9):
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		ssh_client.connect(hostname=ip_list,username=username,password=password)
		bar.next()
	bar.finish()
	

	print("Koneksi Ke Router [ OKE ]")
	print("")
	input("Tekan ENTER untuk mengirim config")


	config_list = ["interface ethernet set ether1 name=Remote",
	"interface ethernet set ether3 name=WAN",
	"interface ethernet set ether2 name=Local",
	"ip address add address=192.168.2.1/24 interface=Local",
	"ip address add address=192.168.1.19/24 interface=WAN",
	"ip route add gateway=192.168.1.1",
	"ip firewall nat add chain=srcnat out-interface=WAN action=masquerade",
	"ip dns set servers=8.8.8.8 allow-remote-requests=yes",
	"ip service disable www",
	"ip service disable ftp",
	"ip service disable telnet"]


	cnfg_bar = Bar('Mengirim Konfigurasi',max=8)
	for config,x in enumerate(config_list):
		time.sleep(1)
		ssh_client.exec_command(x)
		cnfg_bar.next()
	cnfg_bar.finish()	
	ssh_client.close()

except paramiko.AuthenticationException:
        print ("Authentication failed, please verify your credentials: %s")
except paramiko.BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
except KeyboardInterrupt:
	print ("\n")
	pass
except Exception as e:
        print (e.args)
