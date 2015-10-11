
clear; clc;
A=[1 2; 3 4; 5 6]
file2=fopen('matrix.txt', 'w');
fprintf(file2, '%i %i \n' , A);
fclose(file2);
