---
share_link: https://share.note.sx/sq8qfpoa#NkKSNsXIRK3aKQ6j5AI9HFPs5HLfcKcRaa8rbrYm43g
share_updated: 2025-05-05T21:21:33+07:00
---
# Revising
## Word Count command: 
	Given a folder with thousands of pictures. They contain many type of format. Count num of picture for each format 

![[Pasted image 20250426145421.png]]
### To count how many pictures 
```
ls Pictures/ | wc -l
```
### To count png pictures 
```
ls Pictures/*.png | wc - l
```
### Classify JPG and PNG 
```
#!/bin/sg 
if [ ! -d "JPG" ]; then
	mkdir JPG
fi

if [ ! -d "PNG" ]; then
	mkdir PNG
fi

for image in $(ls *.png)
do
	mv $image PNG 
done

for image in &(ls *.jpg)
do
	mv $image JPG 
done

exit(0)
```
# Main
To watch the: 
**After Preprocessing**
```
gcc - E hello.c -o hello_temp.c
```
**After Compiling (asm file)**
```
gcc -S hello.c
```
**After assembling (obj file)**
```
gcc -c hello.c
```
**Create the executable file**
```
gcc hello.o -o hello
```
## Make file 
Sau khi nhấn ':' xuống dòng thì phải bắt đầu bằng 1 dấu TAB
```
all: hello run 

hello: main.c hello.c 
		gcc main.c -o hello
run: 
		./hello
clean: 
		rm -f hello
```
Để biên dịch script trên thì dùng lệnh 
```
make all
```
Ở make file trên có 4 target là all, hello, run, clean. 
	- Ở trong all có hello và run 
		- -> khi thực thi all sẽ bao gồm thực thị hello và run 
	- Nếu chạy make không có tham số thì target đầu tiên sẽ được thực thi 
	- Các target trong Makefile thực chất là tên các tệp tin
	---> để biên dịch chính xác thì thư mục hiện tại không được chứa các tệp tin có tên all, run hay clean. 
	--> Nếu muốn tồn tại các tệp tin thêm phải thêm .PHONY: \<files> vào cuối Makefile để ép buộc make luôn thực thi \<files>
```
all: hello run 

hello: 
	gcc main.c hello.c -o hello
run: 
	./hello
clean: 
	rm -f hello
.PHONY: hello
```
![[Pasted image 20250426152036.png]]
Khi thực hiện chỉnh sửa một file, thực hiện build lại
Ngược lại, nếu không có bất cứ gì thay đổi, không compile lại 
## Debug with GDB
Given the following program: 
![[Pasted image 20250426152317.png]]
```
gcc -g factorial.c -o factorial
gdb factorial
break 16 # the breakpoint line
run 
print j # print the j variable 
```
## Process in linux 
### State: 
- Running 
- Waiting 
- Suspend 
- Zombie 
```
top #list all running process 
ps #list the running process after ps command
```
### Foreground process
Mặc định, tiến trình chạy ở foreground, có thể tương tác với người dùng, chỉ có một tiến trình 
### Background 
Có thể có nhiều tiến trình Background, thêm dấu ampersand.
```
./count.sh &
```
**Stop background process**
```
kill -STOP 3565
```
![[Pasted image 20250426153549.png]]
Nếu tiến trình background yêu cầu bất cứ đầu vào nào từ bàn phím --> Nó sẽ đợi cho đến khi được chuyển thành foreground và nhận đầu vào từ bàn phím
**Một số lệnh hữu dụng trong trường hợp này**:
- jobs: liệt kê danh sách các công việc đang chạy 
- &: chuyển tiến trình sang background 
- fg <job_number>: background --> foreground 
- Ctrl + z: foreground --> background
Thông thường, tiến trình con bị khử, tiến trình cha được thông báo qua tín hiệu SIGCHLD. 
- Sau đó, ,tiến trình cha có thể thực hiện một vài công việc khác, hoặc bắt đầu lại tiến trình con (nếu cần thiết) 
- Tuy nhiên, đôi khi tiến trình cha bị khử trước tiến trình con của nó bị khử --> Tiến trình con thành tiến trình orphan 
- Khi một tiến trình bị khử, danh sách liệt kê ps có thể vẫn chỉ tiến trình với trạng thái Z, đây là trạng thái Zoombie hoặc tiến trình không tồn tại 
#### Tóm lại:
- **Orphan process**: 
	- Parent terminates, but children still exist 
	- --> orphan process --> assigned to root process (init process trong slide của THL)
	- The parent of the process is exiting, as a result, all its children are deleted. This is called cascaded termination
- **Zoombie process**
	- A child terminates, but its PCB has not released yet 
	- --> The parent must wait for children to complete
### Create a process 
### fork()
Tạo ra một tiến trình mới, tiến trình mới là tiến trình con của tiến trình gọi hàm fork
![[Pasted image 20250426153847.png]]
### execl()
Tiến trình mới tạo ra thay thế tiến trình cha
![[Pasted image 20250426154010.png]]
### system()
Tiến trình gọi hàm system phải chờ hàm system thực thi rồi mới thực thi tiếp
This command is a combination of forking and execl() 
- Forking: creating a new process, a copy of the current one 
- Executing: using execl to replace the current process image and passes the command string to it 
![[Pasted image 20250426154318.png]]
### Kill a process 
#### Hàm exit(): 
- Dùng để kết thúc tiến trình và hoàn trả lại tài nguyên 
- Khi mộ tiến trình ocn kết thúc, ột tín hiệu gửi tới tiến trình cha và nó sẽ được đặt trong trạng thái zoombie  đặc biệt dùng để biểu diễn các tiến trình đã kết thúc cho đến khi tiến trình cha gọi hàm wait() hoặc waitpid()
#### GUI 
- **Ctrl + C:** gửi tín hiệu INT (SIGINT) đến tiến trình, ngắt ngay tiến trình 
- **Ctrl + Z:** gửi tín hiệu TSTP (SIGTSTP) đến tiến trình, dừng tiến trình (suspend). chuyển về bg
- **Ctrl + \ :** gửi tín hiệu ABRT (SIGABRT) đến tiến trình, kết thúc ngay tiến trình ABORT
**Ngoài ra, có thể sử dụng lệnh kill để kết thúc tiến trình đó**

## Interprocess Communication 
Các tiến trình cần cộng tác với nhau thì phải đươc chia sẻ dữ liệu. Hai mô hình giao tiếp liên tiến trình cơ bản: 
- [[#Shared memory]]
- Message passing
### Shared memory
Để cài đặt shared memory: 
**Bước 1: Khởi tạo**
```c 
fd = shm_open(name, O_CREAT | O_RDWR, 0666)
```
- name: định danh của shared memory
- O_CREATE | O_RDWR: 
	- CREATE
	- RD: READ, WR: WRITE
	- 0666: chế độ trên shared memory
		- 6: rw
		- 7: rwx
**Bước 2: Cài đặt độ lớn của shared memory**
```c
ftruncate(fd, 4096)
```
- fd: đối tượng vùng nhớ chia sẻ 
- 4096: độ lớn của vùng nhớ 
**Bước 3: khởi tạo file ánh xạ bộ nhớ có chứa đối tượng shared memory**
```C
mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0)
```
- 0: địa chỉ vùng nhớ bắt đầu ánh xạ 
- SIZE: kích thước vùng nhớ (trong code trên là 4096)
- PROT_READ | PROT_WRITE: chế độ bảo vệ cho phép đọc và ghi 
- MAP_SHARED: chế độ chia sẻ những thay đổi trên bộ nhớ với tiến trình khác
- fd: đối tượng vùng nhớ chia sẻ 
- 0: offset trên file, chỉ vị trí nhớ bắt đầu ánh xạ
**Bước 4: thu hồi bộ nhớ**
```C
munmap(ptr, SIZE);
close(fd);
shm_unlink(name);
```

### Ví dụ về bộ nhớ chia sẻ: 
Cho 2 Process A và Process B thực hiện như sau: 
-  Process A khởi tạo shared memory, ghi vào "Hello Process B", sau đó chờ bộ nhớ được cập nhật bởi Process B
- Process B truy cập shared memory, đọc dữ liệu do Process A ghi vào, sau đó, cập nhật bộ nhớ với chuỗi "Hello Process A"

### Tiểu trình trong Linux 
	Trong linux, tiểu trình thực hiện như tiến trình 
#### Tạo tiểu trình 
```c
int pthread_create(pthread_t( thread, pthread_attr_t * attr, void * (start_routine)(void *), void * arg);
```
**Trong đó:**
- pthread là biến tham chiếu kiểu pthread_t được dùng như PID 
- attr là biến tham chiếu kiểu pthread_attr thể hiện attribute của thread (dùng NULL nếu đặt thuộc tính là mặc định)
- \*start_routine là một con trỏ hàm kiểu void đến chức năng mong muốn tiểu trình thực thi 
- \*arg là con trỏ đối số cho hàm kiểu void 
Nếu tiểu trình được tao thành công, hàm pthread_create() sẽ trả về số nguyên 0, ngược lại sẽ là một số khác 0 

**Ví dụ**
```c
#include<pthread.h>
#include<stdio.h>
#con trỏ hàm
void *thread_print(void* message){
	while(1){
		print("Hello, How are you  \n);
		}
}
int main(){
	pthread_t idthread; //định danh cho tiểu trình tạo ra
	pthread_create( &idthread,
					 NULL, //0 thuộc tính
					&thread_print,//con trỏ hàm 
					NULL //đối số truyền vào hàm
					);
	while(1) printf("Im fine, n u\n");
	return 0;
}
```
**Biên dịch**
Khi biên dịch phải truyền vào cờ pthread
```
gcc -pthreead example_thread -o example.thread 
```
Khi execute thì sẽ có hai tác vụ song song với nhau: 
- Tác vụ của con trỏ hàm thread_print
- Tác vụ trong main ('iam fine and u')
- ![[Pasted image 20250428221855.png]]
### Dừng tiểu trình:
Có thể dùng hàm pthread_exit() để dừng tiểu trình:
- Đặt trong hàm để hàm tự gọi khi kết thúc 
- Gọi ở hàm main() để kết thúc hàm
**Ví dụ: Hàm tự gọi exit, main cũng gọi**
```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_THREADS 2
void *thread_print(void* threadid){
	long tid;
	tid = long(threadid);
	printf("Hello IT007!, Im thread #%ld\n", tid );
	pthread_exit(NULL);
}
int main(){
	pthread_t threads[NUM_THREADS];
	int check;
	long tID;
	for(tID = 0; tID < NUM_THREADS; tID++){
	printf(" Created thread %ld\n", tID);
	check = pthread_create(
		&threads[tID],
		NULL,
		thread_print,
		(void*)tID);
		if (check != 0){
			printf("ERROR");
			exit(-1;)
			
		}
	}
	sleep(100);
	pthread_exit(NULL);
	return 0;
}
```
**Output:**

![[Pasted image 20250428223649.png]]
**Kiểm tra:**
```
pidof example_thread_selfexit #tên ctrinh
15312
top - H -p 15312
```
![[Pasted image 20250428223820.png]]
**Hàm main gọi exit, hàm sleep**
```C 
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_THREADS 2
void *thread)print(void* threadid){
	long tid;
	tid = long(threadid);
	printf("Hello IT007!, Im thread #%ld\n", tid );
	sleep(100);
}
int main(){
	pthread_t threads[NUM_THREADS];
	int check;
	long tID;
	for(tID = 0; tID < NUM_THREADS; tID++){
	printf(" Created thread %ld\n", tID);
	check = pthread_create(
		&threads[tID],
		NULL,
		thread_print,
		(void*)tID);
		if (check != 0){
			printf("ERROR");
			exit(-1;)
			
		}
	}
	pthread_exit(NULL);
	return 0;
}
```
Khi sử dụng lệnh top: 
![[Pasted image 20250428224031.png]]
Tiểu trình main: ở trạng thái zoombie 
Hai tiểu trình còn lại ở trạng thái sleep 
Tiến tình main đợi hai tiến trình còn lại hoàn thành xong rồi mới kết thúc 
### Hợp và gỡ tiểu trình 
**Hợp tiểu trình**:
```
pthread_join(threadid, statis)
```
pthread_join sẽ ngưng pthread đang gọi tới threadid kết thúc (giống hàm system)
Khi thread kết thúc phthread_join() sẽ trả về giá trị - 
Để tháo gỡ các pthread, có thể sử dụng hàm 
```
pthread_detach(threadid)
```
**Ví dụ**
Ở vòng lặp for, sau khi tạo ra một tiểu trình sẽ gọi hàm pthread_join
```C
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_THREADS 2
void *thread)print(void* threadid){
	long tid;
	tid = long(threadid);
	printf("Hello IT007!, Im thread #%ld\n", tid );
	sleep(100);
	pthread_exit(NULL);
}
int main(){
	pthread_t threads[NUM_THREADS];
	int check;
	long tID;
	for(tID = 0; tID < NUM_THREADS; tID++){
	printf(" Created thread %ld\n", tID);
	check = pthread_create(
		&threads[tID],
		NULL,
		thread_print,
		(void*)tID);
		if (check != 0){
			printf("ERROR");
			exit(-1;)
			
		}
		pthread)join(threads[tID], NULL);
	}
	
	return 0;
}
```
**Kết quả**
Sau khi thread được tạo ra, do có hàm pthread_join, nên chương trình phải đợi cho hàm được gọi trong tiểu trình thực hiện xong 
Sau đó, chương trình thực hiện tiếp 
![[Pasted image 20250428224935.png]]
### Truyền dữ liệu cho tiểu trình 
Đối số cuối cùng của hàm pthread_create() là một con trỏ đối số cho để truyền vào 
```C
#include <pthread.h>
#include <stdio.h>
#define NUM_THREADS 2
struct strct_print_params{
	char character;
	int count;
};
void* char_print(void* args){
	struct strct_print_params* p = (struct struct_print_params*) args; // ep kieu
	int i;
	for (i = 0; i < p->count; i++)
		printf("%c\n", p->character);
	return NULL;
}
int main(){
	pthread_t tid;
	struct struct_print_params th_args;
	th_args.chracter = 'X';
	th_args.count = 5;
	pthread_create(&tid, NULL, &char_print, &th_args); //truyen vao doi so
	pthread_join(tid, NULL)
	return 0;
}
```
**Output:**
Truyền vào con trỏ hàm char_print, vào struct th_args, nhận được đầu ra là 5 chữ X như mong đợi 
![[Pasted image 20250428225856.png]]
## Truyền thông giữa các tiến trình 
### Signal 
	Là tín hiệu mà hệ điều hành gguiwr cho tiến trình

![[Pasted image 20250428230228.png]]
**Ví dụ:**
```C
#include<stdio.h>
#include<signal.h>
int loop_forever = 1;

void on_signal(){
	printf("\nCtrl+C is pressed");
	loop_forever = 0;
}
int main(){
	loop_forever = 1;
	signal(SIGINT, on_sinal); //Nếu bắt được tín hiệu SIGINT thì gọi hàm signal
	while(loop_forever){}
	return 0;
}
```
