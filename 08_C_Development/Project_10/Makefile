find_last_node: linked_list.o find_last_node.o
	gcc -Wall -std=c99 -o find_last_node find_last_node.o linked_list.o

find_last_node.o: linked_list.h find_last_node.c
	gcc -Wall -std=c99 -c -o find_last_node.o find_last_node.c

linked_list.o: linked_list.h linked_list.c
	gcc -Wall -std=c99 -c -o linked_list.o linked_list.c

student: student_class.c
	gcc -std=c99 -Wall student_class.c -o student_class
clean:
	rm -f *.o
	rm -f find_last_node
	rm -f student_class
