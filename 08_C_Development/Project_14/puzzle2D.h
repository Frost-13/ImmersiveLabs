#include<stdio.h>

long hash(char word[1001]);

int horizontal_forward(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int horizontal_back(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int vertical_up(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int vertical_down(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);

int diagonal_down_right(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int diagonal_down_left(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int diagonal_up_right(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);
int diagonal_up_left(char word[], char puzzle[1001][1001], int size, long solution, FILE *f);

