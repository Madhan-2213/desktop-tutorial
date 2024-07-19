#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int num1,num2,i,j,sum=0;
scanf("%d",&num1);
int arr1[num1];
for(i=0;i<=num1;i++){
    scanf("%d",&arr1[i]);
}  

for(i=0;i<num1;i++){
    sum+=arr1[i];
}
printf("%d",sum);
return 0;    
    return 0;
}
