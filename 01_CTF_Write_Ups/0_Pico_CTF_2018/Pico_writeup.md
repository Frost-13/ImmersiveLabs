
picoCTF 2018



done with Linux Mint and FireFox

#### Forensics Warmup 1:

click on the "file" link.

click on "open with" and use "Archive Manager"

there is an image and when you open it has an image off the flag

picoctf{welcome_to_forensics}

#### Forensics Warmup 2

click on the "image" link

click on "save"

image wont open barbecue it's not a .png file. so we want to convert the image to a .jpg

and the image will now show and has the flag

picoctf{extensions_are_a_lie}

#### General Warmup 1

go to the website https://www.rapidtables.com/convert/number/hex-to-ascii.html

put in 0x41 an hit convert

it gives you A therefore the flag is

picoctf{A}

#### General Warmup 2

go to http://www.unitconversion.org/numbers/base-10-to-base-2-conversion.html

put 27 in the base 10 category

27(10) in base 2 is 11011 therefore our flag is

picoctf{11011}

#### General Warmup 3

go to https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=0x3D

input 0x3D in the hexadecimal section and hit convert and will give you 61

therefore our flag is

picoctf{61}

#### Resources

go to their website given (`https://picoctf.com/resources``)` and if you scroll a bit it is there is the flag

`picoCTF{xiexie_ni_lai_zheli}`

#### Reversing Warmup 1

rather than using their browser terminal I chose to use my own

I first saved the file "run" and in my Linux terminal inputted the following commands

frost@Laptop:~$ cd Downloads/

frost@Laptop:~/Downloads$ chmod +x run

frost@Laptop:~/Downloads$ ./run

picoCTF{welc0m3_t0_r3VeRs1nG}

#### Reversing Warmup 2

go to https://www.base64decode.org/

put in the given encrypted flag "`dGg0dF93NHNfczFtcEwz``" hit decode and it gives us "th4t_w4s_s1mpL3" therefore the flag is`

`picoCTF{th4t_w4s_s1mpL3}`

#### Crypto Warmup 1

by looking at the given table this is clearly a Vigenère cipher. I could do it by hand but using a converter will be much easier especially since I know how the Vigenère cipher works.

I went to the website https://planetcalc.com/2468/

set to decrypt

Set Text to _llkjmlmpadkkc_

_Set Key to thisisalilkey_

_and after hittting calculate it gives us "__secretmessage__" therefore the flag is_

`picoCTF{SECRETMESSAGE}`

#### Crypto Warmup 2

they tell us that `cvpbPGS{guvf_vf_pelcgb!}` `was encrypted using rot13`

`i went to the website https://rot13.com/ and put that message in the top and it gives us our key at the bottom which is`

`picoCTF{this_is_crypto!}`

#### grep 1

considering the challenge is called grep 1 I am assuming we need to use the grep command in the terminal. after downloading the file in the terminal I use the following command

frost@Laptop:~/Downloads$ grep "picoCTF{" file

picoCTF{grep_and_you_will_find_42783683}

I chose to use the header of the flag because we know every flag starts with picoCTF{



#### net cat

we are given the address (2018shell.picoctf.com) and port number (22847)

using net cat with the following command will give us the flag

frost@Laptop:~/Downloads$ nc 2018shell.picoctf.com 22847

That wasn't so hard was it?

picoCTF{NEtcat_iS_a_NEcESSiTy_69222dcc}



#### HEEEEEEERE'S Johnny!picoCTF 2018



done with Linux Mint and FireFox

#### Forensics Warmup 1:

click on the "file" link.

click on "open with" and use "Archive Manager"

there is an image and when you open it has an image off the flag

picoctf{welcome_to_forensics}

#### Forensics Warmup 2

click on the "image" link

click on "save"

image wont open barbecue it's not a .png file. so we want to convert the image to a .jpg

and the image will now show and has the flag

picoctf{extensions_are_a_lie}

#### General Warmup 1

go to the website https://www.rapidtables.com/convert/number/hex-to-ascii.html

put in 0x41 an hit convert

it gives you A therefore the flag is

picoctf{A}

#### General Warmup 2

go to http://www.unitconversion.org/numbers/base-10-to-base-2-conversion.html

put 27 in the base 10 category

27(10) in base 2 is 11011 therefore our flag is

picoctf{11011}

#### General Warmup 3

go to https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=0x3D

input 0x3D in the hexadecimal section and hit convert and will give you 61

therefore our flag is

picoctf{61}

#### Resources

go to their website given (`https://picoctf.com/resources``)` and if you scroll a bit it is there is the flag

`picoCTF{xiexie_ni_lai_zheli}`

#### Reversing Warmup 1

rather than using their browser terminal I chose to use my own

I first saved the file "run" and in my Linux terminal inputted the following commands

frost@Laptop:~$ cd Downloads/

frost@Laptop:~/Downloads$ chmod +x run

frost@Laptop:~/Downloads$ ./run

picoCTF{welc0m3_t0_r3VeRs1nG}

#### Reversing Warmup 2

go to https://www.base64decode.org/

put in the given encrypted flag "`dGg0dF93NHNfczFtcEwz``" hit decode and it gives us "th4t_w4s_s1mpL3" therefore the flag is`

`picoCTF{th4t_w4s_s1mpL3}`

#### Crypto Warmup 1

by looking at the given table this is clearly a Vigenère cipher. I could do it by hand but using a converter will be much easier especially since I know how the Vigenère cipher works.

I went to the website https://planetcalc.com/2468/

set to decrypt

Set Text to _llkjmlmpadkkc_

_Set Key to thisisalilkey_

_and after hittting calculate it gives us "__secretmessage__" therefore the flag is_

`picoCTF{SECRETMESSAGE}`

#### Crypto Warmup 2

they tell us that `cvpbPGS{guvf_vf_pelcgb!}` `was encrypted using rot13`

`i went to the website https://rot13.com/ and put that message in the top and it gives us our key at the bottom which is`

`picoCTF{this_is_crypto!}`

#### grep 1

considering the challenge is called grep 1 I am assuming we need to use the grep command in the terminal. after downloading the file in the terminal I use the following command

frost@Laptop:~/Downloads$ grep "picoCTF{" file

picoCTF{grep_and_you_will_find_42783683}

I chose to use the header of the flag because we know every flag starts with picoCTF{



#### net cat

we are given the address (2018shell.picoctf.com) and port number (22847)

using net cat with the following command will give us the flag

frost@Laptop:~/Downloads$ nc 2018shell.picoctf.com 22847

That wasn't so hard was it?

picoCTF{NEtcat_iS_a_NEcESSiTy_69222dcc}



#### HEEEEEEERE'S Johnny!
