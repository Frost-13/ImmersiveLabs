lab8: gcd.c language_greeting.c qsort.o quicksort.o
	gcc -Wall -std=c99 gcd.c -o gcd
	gcc -DENGLISH -Wall -std=c99 language_greeting.c -o lang
	gcc -Wall -std=c99 -o qsort qsort.o quicksort.o

qsort.o: qsort.c quicksort.h
	gcc -Wall -std=c99 -c qsort.c 
quicksort.o: quicksort.c quicksort.h
	gcc -Wall -std=c99 -c quicksort.c
clean:
	rm -f  *.o qsort lang gcd
