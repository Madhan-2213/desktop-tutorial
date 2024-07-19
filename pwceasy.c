#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
char ch;
scanf("%c", &ch)   ;
printf("%c\n", ch);

char str[59];
scanf("%s", &str)   ;
printf("%s\n", str);

char s[1000];
scanf(" %[^\n]%*c", s);
printf("%s", s);
return 0;
}
