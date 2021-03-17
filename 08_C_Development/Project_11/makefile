queue_client: queue_client.o queue.o
	gcc -Wall -std=c99 -o queue_client queue_client.o queue.o

queue_client.o: queue.h queue_client.c
	gcc -Wall -std=c99 -c queue_client.c

queue.o: queue.c
	gcc -Wall -std=c99 -c queue.c

print_error: print_error.c
	gcc -std=c99 -Wall print_error.c -o print_error
clean:
	rm -f *.o
	rm -f queue_client
	rm -f print_error
