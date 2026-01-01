Burst time là thời gian một tiến trình cần CPU trong một chu kỳ CPU - I/O
## Tiến trình hướng CPU (CPU-bound)
- Tiến trình yêu cầu thời gian thực thi trên CPU nhiều 
- Thời gian hoàn thành chương trình phụ thuộc vào tốc độ thực thi của CPU
Chương trình dưới đây là chương trình hướng CPU: 
```c
#include <stdio.h> 
int main() { 
long long start = 1, end = 1000000, total = 0; 
for (long long i = start; i <= end; i++){
total += i; } 
printf("Sum of numbers from %lld to %lld is %lld\n", start, end, total); 
return 0; }
```
## Tiến trình hướng IO 
- Tiến trình yêu cầu thời gian thực thi IO nhiều hơn 
- Thời gian hoàn thành chương trình phụ thuộc chu kỳ đợi cho các thao tác IO 
Chương trình dưới đây là chương trình hướng IO
```C
#include <stdio.h> 
int main(){ 
FILE *fp; 
char filename[] = "example.txt"; 
int total = 0, ch; 
fp = fopen(filename, "r"); 
if (fp == NULL){ 
	printf("Failed to open file %s\n", filename); 
	return 1; } 
while ((ch = fgetc(fp)) != EOF){ 
total++; 
} 
fclose(fp); 
printf("Total number of characters in file %s is %d\n", filename, total); 
return 0; }
```