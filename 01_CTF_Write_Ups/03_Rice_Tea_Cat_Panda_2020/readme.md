
## **Encryption**

## **HOOOOOOOOOOMEEEEEE RUNNNNNNNNNNNNN!!!!!** (50 pts)

AND JAKE IS ROUNDING THE BASES  
_HE PASSES BASE 32!!!_  
**HE ROUNDS BASE 64!!!!!!!**  
**WE'RE WITNESSING A MIRACLE!!!!!!!!!!!!!**

Just one more base to go ;D

Hint: Ecbf1HZ_kd8jR5K?[";(7;aJp?[4>J?Slk3<+n'pF]W^,F>._lB/=r




_**Solution:**_ since we know he passed "base" 32 and "base" 64. That leaves us with "base 86"

look up any base 86 decoder on google. I happened to use (https://www.dcode.fr/ascii-85-encoding)

decrypting the hint will give you the flag:

rtcp{uH_JAk3_w3REn't_y0u_4t_Th3_uWust0r4g3}







## **Don't Give The GIANt a COOKie** (100 pts)

It was just a typical day in the bakery for Delphine. She was preparing her famous chocolate cake, when all of a sudden a GIANt burst through the doors of her establishment and demanded a cookie. Being the strong-willed girl she was, Delphine refused and promptly threw her rolling pin at the GIANt. Doing what any sensible being would do when faced with projectiles, the GIANt let out a shriek and ran out of the shop. Delphine smiled to herself, it was another day well done.

But oh? What's this? It seems the GIANt dropped this behind while he was screaming and scrambling out of the shop.

`69acad26c0b7fa29d2df023b4744bf07`

_**Solution:**_ This looks like a common md5 hash to me so i put it into a md5 decoder (https://www.md5online.org/md5-decrypt.html). Thankfully it didn't have a salt attatched to it and gave me the result "chocolate mmm"

i tried rtcp{chocolate_mmm}  and that was the correct flag.









##   


## **15**  (100 pts)

Lhzdwt eceowwl: Dhtnwt Pcln Eaao Qwoohvw

Okw qsyo okcln bah'i fslo cl baht Dhtnwt Pcln dhtnwt cy yazwalw'y eaao ehlnhy. Dho sy co ohtly aho, okso zcnko dw fkso bah nwo. S 4vksllwt hmqasiwi s mkaoa slalbzahyqb oa okw ycow ykafvsycln kcy ewwo cl s mqsyocv dcl ae qwoohvw, fcok okw yosowzwlo: "Okcy cy okw qwoohvw bah wso so Dhtnwt Pcln." Sizcoowiqb, kw ksi ykawy al. Dho okso'y wgwl fatyw.

Okw mayo fwlo qcgw so 11:38 MZ al Xhqb 16, sli s zwtw ofwlob zclhowy qsowt, okw Dhtnwt Pcln cl rhwyocal fsy sqwtowi oa okw tanhw wzmqabww. So qwsyo, C kamw kw'y tanhw. Kaf ici co ksmmwl? Fwqq, okw DP wzmqabww ksil'o twzagwi okw WJCE isos etaz okw hmqasiwi mkaoa, fkcvk yhnnwyowi okw vhqmtco fsy yazwfkwtw cl Zsbecwqi Kwcnkoy, Akca. Okcy fsy so 11:47. Oktww zclhowy qsowt so 11:50, okw Dhtnwt Pcln dtslvk siitwyy fsy mayowi fcok fcykwy ae ksmmb hlwzmqabzwlo. Ecgw zclhowy qsowt, okw lwfy yosocal fsy valosvowi db slaokwt 4vksllwt. Sli oktww zclhowy qsowt, so 11:58, s qclp fsy mayowi: DP'y "Owqq hy sdaho hy" alqclw eathz. Okw eaao mkaoa, aokwtfcyw plafl sy wjkcdco S, fsy soosvkwi. Vqwgwqsli Yvwlw Zsnsuclw valosvowi okw DP cl rhwyocal okw lwjo isb. Fkwl rhwyocalwi, okw dtwspesyo ykceo zslsnwt ysci "Ak, C plaf fka okso cy. Kw'y nwoocln ectwi." Zbyowtb yaqgwi, db 4vksl. Laf fw vsl sqq na dsvp oa wsocln aht esyo eaai cl mwsvw.

tovm{v4T3Ehq_f1oK_3J1e_i4O4}

_**Solution:**_ we can see that the flag is at the end. since we have such a long text i figured we could try to do a frequency analysis on this whole thing. i used this website to help me (https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html)



after just trying things out (getting the words "the, they, a, is" filling in the flag header "rtcp" and then filling in letters in words as i see them i got the decrypted text:



number fifteen: burger king foot lettuce



the last thing you'd want in your burger king burger is someone's foot fungus. but as it turns out, that might be what you get. a 4channer uploaded a photo anonymously to the site showcasing his feet in a plastic bin of lettuce, with the statement: "this is the lettuce you eat at burger king." admittedly, he had shoes on. but that's even worse.



the post went live at 11:38 pm on july 16, and a mere twenty minutes later, the burger king in question was alerted to the rogue employee. at least, i hope he's rogue. how did it happen? well, the bk employee hadn't removed the exif data from the uploaded photo, which suggested the culprit was somewhere in mayfield heights, ohio. this was at 11:47. three minutes later at 11:50, the burger king branch address was posted with wishes of happy unemployment. five minutes later, the news station was contacted by another 4channer. and three minutes later, at 11:58, a link was posted: bk's "tell us about us" online forum. the foot photo, otherwise known as exhibit a, was attached. cleveland scene magazine contacted the bk in question the next day. when questioned, the breakfast shift manager said "oh, i know who that is. he's getting fired." mystery solved, by 4chan. now we can all go back to eating our fast food in peace.



rtcp{c4r3ful_w1th_3x1f_d4t4}



using the substitution key:





##   


## **Web**

## **Robots. Yeah, I know, pretty obvious.**  (25 pts)

So, we know that Delphine is a cook. A wonderful one, at that. But did you know that GIANt used to make robots? Yeah, GIANt robots.

_**Solution**_: I went to https://riceteacatpanda.wtf/robots.txt which gave me a page with the following text:

User-agent: *
Disallow:
/robot-nurses
/flag

i then attempted https://riceteacatpanda.wtf/robot-nurses

which gave me the flag:

rtcp{r0b0t5_4r3_g01ng_t0_t4k3_0v3r_4nd_w3_4r3_s0_scr3w3d}




## No Sleep (100 pts)

Jess doesn't get enough sleep, _since he's such a gamer_ so in this challenge, you'll be staying up with him until 4:00 in the morning :D on a Monday! Let's go, gamers!

_**Solution:**_ right click + inspect. after looking around the inspect tool for a while i found this clock that was set to 2084 so i changed it to 2020 and close to my time and it gave me the flag. rtcp{w0w_d1d_u_st4y_up?}

## **General Skills**

## **Basic C4** (30 pts)

If you use that bomb, you might cause an Avalanche...  
Let's not destroy my IO, ok?

Hint: The flag starts with `c4`Submit in the format: `rtcp{90-char-flag}`

_**Solution:**_ after a bit of google searching (first i tried "C4 io", "basic C4 io" eventually came to a website http://www.cccc.io/ and it had a spot to insert a file so i thought it couldnt hurt to put it in.

it gave me the text c42CW3TbiGhvptM36RJJ9ScctgkskjvZPo6dG8JexzZRvzQR6hwovZJLDkYK5pZ6cq9e7fX1ShUiYUdM7H1Uuqj64G

this starts with c4 and looks to be about 90 chars so it was promising.

rtcp{c42CW3TbiGhvptM36RJJ9ScctgkskjvZPo6dG8JexzZRvzQR6hwovZJLDkYK5pZ6cq9e7fX1ShUiYUdM7H1Uuqj64G} was the correct key

## **Strong Password**  (1 pt)

Eat, Drink, Pet, Hug, Repeat!

flags are entered in the format rtcp{flag}

hint: Words are separated by underscores ("_")



**solution:**  rtcp{Rice_Tea_Cat_Panda}



tlyrc_o_0pnvhu}{137rmi__i_omwm

trcp{ro
