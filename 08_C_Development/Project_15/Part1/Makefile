squeue_client: squeue.o squeue_client.o
	gcc -std=c99 -Wall -o squeue squeue_client.o squeue.o

squeue.o: squeue.h squeue.c
		gcc -std=c99 -Wall -c squeue.h squeue.c

squeue_client.o: squeue_client.c
	gcc -std=c99 -Wall -c squeue_client.c

clean:
	rm -f *.o squeue_client *.gch
