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

