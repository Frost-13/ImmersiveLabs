## Lab 1: *Ports*

**Q:** What name is given to the port numbers ranging from 0 to 1023?

**A:** Well-known ports


**Q:** How many bits are used to specify a port number? Express your answer as a numerical figure

**A:** 16

**Q:** Which service usually runs on port 443?

**A:** HTTPS

**Q:** Which of the following options would you enter into your web browser to connect to port 3000 at the specified IP address?

**A:** 127.0.0.1:3000

**Q:** What name is given to the process of attempting to connect to a range of ports in sequence on a single computer?

**A:** Port scanning

**Q:** How many ports are available per IP address? Express your answer as a numerical figure

**A:** 65535


## Lab 2:  *Internet Protocol V4*

**Q:** How many octets make up an IPv4 address? Express your answer in numerical form

**A:** 4

**Q:** The private address 172.16.21.2 falls into which class?

**A:** Class B

**Q:** What is the IPv4 address of the eth1 interface?

use `ifconfig`

**A:** 10.58.75.21

**Q:** What is the subnet mask, as 4 octets, for eth1?

use `ifconfig`

**A:** 255.255.255.224

**Q:** What class does the IPv4 address for eth1 fall under?

use `ifconfig`

**A:** Class A


## Lab 3: **Domain Names**
just some random MC questions with a timer. can't do a write up

## Lab 4: **TCP (Transmission Control Protocol)**
just some random MC questions with a timer. can't do a write up

## Lab 5: **HTTP Status Codes**
just some random MC questions with a timer. can't do a write up

## Lab 6 **FTP (File Transfer Protocol)**
**Q:** In the FTP protocol, what port is referred to as the data port?

**A:**  20

**Q:** What does the status code 332 mean?

**A:** Need account for login

**Q:** Analysing the PCAP, what is the IP address of the FTP server?

**A:** 172.17.0.5

**Q:** Analysing the PCAP, what is the username used to successfully log into the FTP server on the destination host?

**A:** jimmy

**Q:** What is the password used to successfully log into the FTP server?

**A:** batman

**Q:** The PORT command creates a secondary connection for data on a dynamic port. What is the dynamic port used in this PCAP to transfer a file using an RETR request?

**A:** 152

**Q:** Identify the file name that was retrieved from the destination host to the source host.

**A:** token.txt

**Q:** What are the contents of the file that was transferred from the FTP Server to the client?

**A:** 2f7b1f21

**Q:** Anonymous FTP logins always need a username and password. True or false?

**A:** false


## Lab 7: **Arp (Address Resolution Protocol)**
**Q:** Which MAC address is associated with the IP address ‘10.0.2.3’? Please enter your answer in the following format xx:xx:xx:xx:xx:xx

**A:** 52:54:00:12:35:03

**Q:** What is the opcode of an ARP reply?

**A:** 2

**Q:** What hexadecimal value is used to denote the protocol type IPv4?

**A:** 0800

**Q:** Which MAC address is used as the destination when broadcasting an ARP request to an entire LAN? Please enter your answer in the following format xx:xx:xx:xx:xx:xx

**A:** FF:FF:FF:FF:FF:FF

**Q:** Which type of attack can be undertaken by manipulating the information stored in the ARP cache?

**A:** Man in the middle

## Lab 8: **Protocols – LDAP**
**Q:** What does LDAP stand for?

**A:** Lightweight Directory Access Protocol

**Q:** Analysing the PCAP, a query was made to the LDAP server, listing all the entries and attributes. Can you note how many Organisational Units are found?

**A:** 2

**Q:** What port is the LDAP service normally running on for unencrypted communication

**A:** 389

**Q:** What organisational unit is Jimmy Raymond a part of?

**A:** finance

**Q:** Using Wireshark, in packet 40, what is the home directory of Sarah Gohner?

**A:** /home/users/sgohner
