PROGRAM DESCRIPTION:
  my program starts off by going through all the flags and assigning the file names accordingly if no -o is provided it 
  defaults to output.txt
  The program then goes through the puzzle file and makes a 2D array of the puzzle lines and calls hash on that word to 
  get the solution. then it calls fgets on each line in the word list and calls all 8 functions from puzle2D.c one by one 
  until it finds the solution and prints it to the output file and moves on to the next word. if however it checks the word 
  with all 8 functions and doesn't find a solution then it will print that there is no solution to the file.
  
RUNNING PROGRAM:
  I have included a run function in my make file so if you type "make run" it will call 
  the line "./wordSearch2D -w wordlist.txt -p puzzle.txt -o myfile.txt" and save the output
  to the file myfile.txt. alternatively you could just type "./wordSearch2D -w wordlist.txt -p puzzle.txt" 
  into the terminal and it will print the solution to output.txt and that should match expected_soln.txt
  After that you can then go "make clean" to remove the executable, output.txt and any .o file 
  
