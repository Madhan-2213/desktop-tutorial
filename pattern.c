#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int n;
    scanf("%d", &n);
    int len=2*n-1;
    int i,j;
    int hmin=0,vmin=0;
    int min;
    for(i=0;i<n*2-1;i++)
    {
        for(j=0;j<2*n-1;j++)
        {
            vmin=i>n-1?len-1-i:i;
            hmin=j>n-1?len-1-j:j;
            min=hmin<vmin?hmin:vmin;
            printf("%d ",n-min);
        }
        printf("\n");
    }
    return 0;
}
