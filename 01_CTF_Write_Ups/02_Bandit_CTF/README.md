# BANDIT CTF (overthewire.org)
## Level 0
**Level Goal:**
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the [Level 1](https://overthewire.org/wargames/bandit/bandit1.html) page to find out how to beat Level 1.
**SOLUTION**:

    ssh bandit.labs.overthewire.org -p2220 -l bandit0

put bandit0 as the password twice because it doesnt work the first time
*no flag this level*

## Level 1
**Level Goal**
The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

**SOLUTION:**

    cat readme

*FLAG:* boJ9jbbUNNfktd78OOpsqOltutMc3MY1

## Level 2
**Level Goal**
The password for the next level is stored in a file called **-** located in the home directory

**SOLUTION:**
we need to leave that first session 

    bandit0@bandit:~$ exit
    logout
    Connection to bandit.labs.overthewire.org closed.
 now log into the "bandit1" server using the flag from level 1 as the password
  

      frost@Laptop:~$ ssh bandit.labs.overthewire.org -p2220 -l bandit1
      bandit1@bandit.labs.overthewire.org's password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
  we need to do this for every level progression so going forward it is implied i do this before each solution.
  

    ls
i can see the - file but cant cat it normally like before however if i use 

    bandit1@bandit:~$ cat < -
	CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
*Flag:* CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


## Level 3
**Level Goal**
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

**SOLUTION:**

    bandit2@bandit:~$ cat spaces\ in\ this\ filename 
    UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
*Flag:* UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

## Level 4 
**Level Goal**
The password for the next level is stored in a hidden file in the **inhere** directory.

**SOLUTION:**

    bandit3@bandit:~$ ls
    inhere
    bandit3@bandit:~$ cd inhere/
    bandit3@bandit:~/inhere$ ls -a 
    .  ..  .hidden
    bandit3@bandit:~/inhere$ cat .hidden 
    pIwrPrtPN36QITSp3EQaw936yaFoFgAB
*Flag:* pIwrPrtPN36QITSp3EQaw936yaFoFgAB

## Level 5
**Level Goal**
The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

**SOLUTION:**

    bandit4@bandit:~$ cd inhere/
    bandit4@bandit:~/inhere$ ls
    -file00  -file02  -file04  -file06  -file08
    -file01  -file03  -file05  -file07  -file09
 we need to use ./ before the file name because the - indicates a flag
i tested all these file and found it in -file07

    bandit4@bandit:~/inhere$ cat ./-file07
    koReBOKuIDDepwhWk7jZC0RTdopnAYKh
*Flag:* koReBOKuIDDepwhWk7jZC0RTdopnAYKh

## Level 6
**Level Goal**
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:
-   human-readable
-   1033 bytes in size
-   not executable


**SOLUTION:**

    bandit5@bandit:~$ cd inhere/
    bandit5@bandit:~/inhere$ ls
    maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
    maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
    maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
    maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
    
   using find i found the right file

    bandit5@bandit:~/inhere$ find . -type f -size 1033c
    ./maybehere07/.file2
    bandit5@bandit:~/inhere$ cat maybehere07/.file2
    DXjZPULLxYr17uwoI01bNLQbtFemEgo7
   *Flag:* DXjZPULLxYr17uwoI01bNLQbtFemEgo7

## Level 7
**Level Goal**
The password for the next level is stored **somewhere on the server** and has all of the following properties:
-   owned by user bandit7
-   owned by group bandit6
-   33 bytes in size

**SOLUTION:**
after lots of trial and error and many Google searchers i found the followinf to give me the right result

    bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -exec cat {} \;
    HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

*Flag:* HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

## Level 8
**Level Goal**
The password for the next level is stored in the file **data.txt** next to the word **millionth**

**SOLUTION:**

    bandit7@bandit:~$ grep millionth data.txt
    millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
*Flag:* cvX2JJa4CFALtqS87jk27qwqGhBM9plV

## Level 9
**Level Goal**
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

**SOLUTION:**
Knowing i cant just look at the filw and find it i need a way to get unique lines. i found that uniq -u qill do this and i needed to sort it first then pipe it into the uniq for it to work

    bandit8@bandit:~$ sort data.txt | uniq -u
    UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

*Flag:* UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

## Level 10
**Level Goal**
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

**SOLUTION:**

    bandit9@bandit:~$ grep -a == data.txt

at the end of the long grep it give the flag
*Flag:* truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

## Level 11
**Level Goal**
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

**SOLUTION:**

    bandit10@bandit:~$ ls
    data.txt
    bandit10@bandit:~$ cat data.txt
    VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
going to the website https://www.base64decode.org/
after decoding the message i got the output:
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

*Flag:* IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

## Level 12
**Level Goal**
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

**SOLUTION:**

    bandit11@bandit:~$ cat data.txt 
    Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh

using the website https://cryptii.com/pipes/rot13-decoder i got the message:
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
*Flag:* 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

## Level 13
**Level Goal**
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

**SOLUTION:**

    bandit12@bandit:~$ mkdir /tmp/frost
    bandit12@bandit:~$ cp data.txt /tmp/frost
    bandit12@bandit:~$ cd /tmp/frost
    bandit12@bandit:/tmp/frost$ ls
    data.txt
    bandit12@bandit:/tmp/frost$ xxd -r data.txt > data_xxd_reverse
    bandit12@bandit:/tmp/frost$ file data_xxd_reverse
    data_xxd_reverse: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
    bandit12@bandit:/tmp/frost$ zcat data_xxd_reverse > data_zcat
    bandit12@bandit:/tmp/frost$ file data_zcat
    data_zcat: bzip2 compressed data, block size = 900k
    bandit12@bandit:/tmp/frost$ bzip2 -d data_zcat
    bzip2: Can't guess original name for data_zcat -- using data_zcat.out
    bandit12@bandit:/tmp/frost$ file data_zcat.out
    data_zcat.out: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
    bandit12@bandit:/tmp/frost$ zcat data_zcat.out > data_zcat_2
    bandit12@bandit:/tmp/frost$ file data_zcat_2
    data_zcat_2: POSIX tar archive (GNU)
    bandit12@bandit:/tmp/frost$ tar xvf data_zcat_2
    data5.bin
    bandit12@bandit:/tmp/frost$ file data_zcat_2
    data_zcat_2: POSIX tar archive (GNU)
    bandit12@bandit:/tmp/frost$ file data5.bin
    data5.bin: POSIX tar archive (GNU)
    bandit12@bandit:/tmp/frost$ tar xvf data5.bin
    data6.bin
    bandit12@bandit:/tmp/frost$ file data6.bin
    data6.bin: bzip2 compressed data, block size = 900k
    bandit12@bandit:/tmp/frost$ bzip2 -d data6.bin
    bzip2: Can't guess original name for data6.bin -- using data6.bin.out
    bandit12@bandit:/tmp/frost$ file data6.bin.out
    data6.bin.out: POSIX tar archive (GNU)
    bandit12@bandit:/tmp/frost$ tar xvf data6.bin.out
    data8.bin
    bandit12@bandit:/tmp/frost$ file data8.bin
    data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
    bandit12@bandit:/tmp/frost$ zcat data8.bin > data8_zcat
    bandit12@bandit:/tmp/frost$ file data8_zcat
    data8_zcat: ASCII text
    bandit12@bandit:/tmp/frost$ cat data8_zcat 
    The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

*Flag:* 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

## Level 14
**Level Goal**
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

**SOLUTION:**

    bandit13@bandit:~$ cat sshkey.private

gives private key too big to paste here, takes up too much space. 

    bandit13@bandit:~$ ssh bandit14@localhost -i sshkey.private 
gives us access to bandit14 machine

    cat /etc/bandit_pass/bandit14
    4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

cat the file that the level goal told us to

*Flag:* 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
