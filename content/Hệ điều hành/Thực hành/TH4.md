## Scheduling algorithm revising 
[[4.2 First-Come, First-served]]
[[4.5 Round Robin]]
[[4.3 Shortest Job First]]

---
## First Come First Serve 
```C
#include<stdio.h

void main(){
	int pn[10];
	int arr[10], bur[10], star[10], finish[10], tat[10], wt[10], i, n;
	int totwt=0, totat=0;

	printf("Enter the number of processes: ");
	scanf("%d", &n);

	for(i=0; i<n; i++){
		printf{"Enter the Process Name, Arrival Time and Burst Time: ";
		scanf("%d%d%d", &pn[i], &arr[i], &bur[i]);
		}
	for (i=0; i<n; i++){
		if(i==0){
			star[i]=arr[i];
			wt[i] = star[i] - arrr[i];
			finish[i] = start[i] + bur[i];
			tat[i] = finish[i] - arr[i];
		}else{
			star[i] = finish[i-1];
			wt[i] = star[i] - arr[i];
			finish[i] = star[i] + bur[i];
			tat[i] = finish[i] - arr[i];
			}
	}
	printf("\Pname\tArrtime\tBurtime\tStart\tTAT\t Finish\n);
for (i = 0; i<n;i++){
	printf("%d\t%6d\t%6d\t%6d\t%6d\t%6d\n", pn[i], arr[i], bur[i], star[i], tat[i], finish[i]);
	totwt += wt[i];
	tottat += tat[i];
}
}
```
Bug: chương trình đang sắp xếp theo tên tiến trình, tiến trình nhập đầu tiên 
![[Pasted image 20250429141526.png]]
![[Pasted image 20250429155903.png]]
![[Pasted image 20250429155916.png]]
![[Pasted image 20250429155925.png]]
## SJF

![[23520825-vo-anh-kiet-lab04.pdf]]