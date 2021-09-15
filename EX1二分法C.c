#include <stdio.h> 
int BinySerch(int *arr , int x , int lengh)
{
	int left = 0, right =lengh-1;
	int mid;
	while(left<=right)
	{
		mid = left + (right - left)/2;
		if(x<arr[mid])
		{
			right=mid-1;
		}
		else if(x>arr[mid])
		{
			left=mid+1; 
		}
		else
		{
			return mid;
		}
	}
	return -1;
}
int main()
{
	int x=0;
	int arr[11]={0,1,2,3,4,5,6,7,8,9,10};
	int lengh=sizeof(arr)/sizeof(arr[0]);
	for (int i=0; i<12; i++)
	{
		printf("%d",BinySerch(arr,i,lengh));
		printf(" ");
	}
return 0;
}
