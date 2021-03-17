#name: Kyle Chatterley / ID: 1528573 / CCID: chatterl / lecture section: B1 / instructor: Sarah Nadi / lab section:H01/ TA: Fernando Lopez/
bucketstack_client:	bucketstack.o bucketstack_client.o
	gcc -std=c99 -Wall -o bucketstack bucketstack.o bucketstack_client.o 

bucketstack.o: bucketstack.h bucketstack.c
	gcc -std=c99 -Wall bucketstack.c -c bucketstack.h

bucketstack_client.o: bucketstack_client.c bucketstack.h
	gcc -std=c99 -Wall bucketstack_client.c -c bucketstack.h

clean:
	rm -f *.o bucketstack_client *.gch
