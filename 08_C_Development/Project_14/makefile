wordSearch2D: wordSearch2D.o puzzle2D.o
	gcc -Wall -std=c99 -o wordSearch2D wordSearch2D.o puzzle2D.o -lm 

wordSearch2D.o: wordSearch2D.c
	gcc -std=c99 -Wall -c wordSearch2D.c -lm
puzzle2D.o: puzzle2D.c puzzle2D.h
	gcc -std=c99 -Wall -c puzzle2D.c -lm

run: wordSearch2D
	./wordSearch2D -w wordlist.txt -p puzzle.txt -o myfile.txt
clean:
	rm -f wordSearch2D *.o output.txt

