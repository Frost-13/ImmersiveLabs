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
