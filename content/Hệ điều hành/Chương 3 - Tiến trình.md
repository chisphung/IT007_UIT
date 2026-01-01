# Khái niệm cơ bản 
	Một hệ điều hành thực thi chương trình như là một tiến trình 
	Tiến trình là một chương trình đang thực thi 
	Chương trình là thực thể bị động lưu trên ổ đĩa (tập tin thực thi - executable file); tiến trình là thực thể chủ động 
	Chương trình trở thành tiến trình khi một tập tin thực thi được nạp vào bộ nhớ 
- Một tiến trình bao gồm: 
	- Text section (program code)
	- Data section (global variables)
	- Program counter, processor registers
	- Heap section (chứa bộ nhớ cấp phát động)
	- Stack section (chứa dữ liệu tạm thời)
		- Function parameters 
		- Return address
		- Local variables 

![[Pasted image 20250407230551.png]]

**Layout bộ nhớ của một chương trình C**

![[Pasted image 20250407230613.png]]

**Các bước nạp chương trình vào bộ nhớ**

![[Pasted image 20250407230638.png]]

- Các bước khởi tạo tiến trình: 
	- Cấp phát một định danh duy nhất cho tiến trình 
	- Cấp phát không gian nhớ để nạp tiến trình 
	- Khởi tạo khối dữ liệu PCB cho tiến trình 
	- Thiết lập các mối liên hệ cần thiết (VD: sắp xếp PCB vào hàng đợi định thời)
# Trạng thái tiến trình
- new: tiến trình vừa được tạo 
- ready: tiến trình đã có đủ tài nguyên, chỉ cần CPU 
- running: các lệnh của tiến trình đang được thực thi
- waiting (hay blocked): tiến trình đợi IO hoàn tất hoặc đợi tín hiệu 
- terminated: tiến trình đã kết thúc

![[Pasted image 20250407230903.png]]

Cho đoạn code như sau: 

![[Pasted image 20250407233440.png]]

- Biên dịch chương trình trong Linux: gcc test.c -o test 
- Thực thi chương trình: ./test
- Trong hệ thống sẽ có một tiến trình test được tạo ra, thực thi và kết thúc 
- Chuỗi trạng thái của tiến trình test như sau (trường hợp tốt nhất): 
	- new 
	- ready
	- running
	- waiting (do chờ IO khi gọi printf)
	- ready 
	- running 
	- tẻminated
**Cho đoạn chương trình sau**

![[Pasted image 20250407233642.png]]
![[Pasted image 20250407233655.png]]

# Process control block
- Mỗi tiến trình trong hệ thống đều được cấp phát một PCV
	- PCB là một trong các cấu trúc dữ liệu quan trọng nhất của hệ điều hành
- PCB gồm:
	- Trạng thái tiến trình: new, ready, running
	- Bộ đếm chương trình
	- Các thanh ghi 
	- Thông tin lập thời biểu CPU: độ ưu tiên
	- Thông tin quản lý bộ nhớ 
	- Thông tin: lượng CPU, thời gian sử dụng 
	- Thông tin trạng thái IO

![[Pasted image 20250407234024.png]]

# Định thời tiến trình
**Yêu cầu đối với hệ điều hành về quản lý tiến trình**
- Hỗ trợ sử thực thi luân phiên giữa nhiều tiến trình: 
	- Hiệu suất sử dụng CPU
	- Thời gian đáp ứng 
- Phân phối tài nguyên hệ thống lý 
- Tránh deadlock, trì hoãn vô hạn định
- Cung cấp cơ chế giao tiếp và đồng bộ hoạt động các tiến trình
- Cung cấp cơ chế hỗ trợ user tạo/kết thúc tiến trình

- Tại sao phải định thời?
	- Đa chương: 
		- Có vài tiến trình chạy tại các thời điểm
		- Mục tiêu: Tận dụng tối đa CPU
	- Chia thời:
		- User tương tác với mỗi chương trình đang thực thi 
		- Mục tiêu: giảm tối thiểu thời gian đáp ứng
![[Pasted image 20250407234540.png]]
## Các hàng đợi định thời
- Hàng đợi công việc - Job queue
- Hàng đợi sẵn sàng - Ready queue
- Hàng đợi thiết bị Device queue

![[Pasted image 20250407234647.png]]

**Lưu đồ hàng đợi của định thời tiến trình**

![[Pasted image 20250407234715.png]]

## Bộ định thời
### Phân loại bộ định thời 
- Bộ định thời công việc (job scheduler) hay bộ định thời dài (long-tẻm scheduler)
- Bộ định thời CPU hay bộ định thời ngắn
### Phân loại tiến trình: 
- Các tiến trình có thể mô tả như: 
	- Tiến trình hướng IO 
	- Tiến trình hướng CPU 
- Thời gian thực hiện khác nhau -> kết hợp hài hòa giữa chung
### Bộ định thời trung gian/vừa
- Đôi khi hệ điều hành (như time-sharing system) có thêm medium term scheduling để điều chỉnh mức độ đa chương của hệ thống 
- **Medium term scheduler**
	- chuyển tiến trình từ bộ nhớ sang đĩa (swap out)
	- chuyển tiến trình từ đĩa vào bộ nhớ (swap in)

![[Pasted image 20250407235049.png]]

### Chuyển ngữ cảnh 
Quá trình CPU chuyển từ tiến trình này đến tiến trình khác 

![[Pasted image 20250407235132.png]]

# Các tác vụ đối với tiến trình
- Tạo tiến trình mới: 
	- Một tiến trình có thể tạo nhiều tiến trình mới thông qua system call create-processs (vd: hàm fork trong UNIX)
		- Ví dụ:  Khi user đăng nhập hệ thống, một command interpreter (shell) sẽ được tạo ra cho user
	- Tiến trình được tạo là tiến trình con của tiến trình tạo (tiến trình cha)
		- Quan hệ cha-con định nghĩa một cây tiến trình
### Cây tiến trình trong Linux/UNIX
![[Pasted image 20250407235545.png]]
## Tạo tiến trình
- Tiến trình con nhận tài nguyên: Từ OS hoặc tiến trình cha 
- Chia sẻ tài nguyên của tiến trình cha:
	- Tiến trình cha và con chia sẻ  mọi tài nguyên 
	- Tiến trình con chia sẻ một phần tài nguyên của cha 
- Trình tự thực thi 
	- Tiến trình cha và con thực thi đồng thời (concurrently)
	- Tiến trình cha đợi đến khi các tiến trình con kết thúc
### Hàm fork()
- Tiến trình con sao chép không gian địa chỉ của tiến trình cha -> Tiến trình con: 
	- Sao chép toàn bộ source code của tiến trình cha 
	- Sao chép giá trị của các biến đã được tạo 
	- **Bắt đầu thực thi tại vị trí mà tiến trình được**
- Giá trị trả về của hàm fork sẽ thuộc 1 trong 3 trường hợp:
	- Lớn hơn 0: Cho biết đây là tiến trình cha 
	- Bằng 0: Cho biết đây là tiến trình con 
	- Nhỏ hơn 0: Hàm fork() thất bại
### Họ hàm exec()
- Nạp một tác vụ mới vào không gian địa chỉ của tiến trình gọi hàm 
	- Tác vụ mới sẽ được ghi đè vào không gian địa chỉ của tiến trình 
	- Tiến trình thực thi tác vụ mới thay vì source code ban đầu
![[Pasted image 20250408000341.png]]
### Về quan hệ cha/con
- Không gian địa chỉ :
	- Không gian địa chỉ của tiến trình con được nhân bản từ cha 
	- Không gian địa chỉ của tiến trình con được khởi tạo từ template
- Ví dụ trong Unix/Linux
	- System call fork() tạo một tiến trình mới 
	- System call exec() dùng sau fork() để nạp một chương trình mới vào không gian nhớ của tiến trình mới
![[Pasted image 20250408000529.png]]
### Ví dụ tạo process với fork()
```c
#include<stdio.h>
#include<unistd.h>
int main(int argx, char *argv[]){
	int pid; //create a new process
	pid = fork();
	if (pid > 0){
	printf("This is parent process");
	wait(NULL);
	exit(0);
	}
	else if (pid == 0){
	printf("This is child process");
	exxeclp("/bin/ls", "ls", NULL);
	}
	else{
	printf('Fork error');
	exit(-1);
	}
```
![[Pasted image 20250408001145.png]]
```C
#include <stdio.h> 
#include <unistd.h>
int main (int argc, char *argv[]){ int pid; /* create a new process */ pid = fork(); 

if (pid > 0) { printf(“This is parent process”); wait(NULL); exit(0); } else if (pid == 0) {

execlp(“/bin/ls”, “ls”, NULL); printf(“This is child process”); exit(0);

} else

{ // pid < 0 printf(“Fork error\n”); exit(-1);

} }
```
## Kết thúc tiến trình 
- Tiến trình tự kết thúc 
	-  Tiến tình kết thúc khi thực hiện lệnh cuối và gọi system routine exit 
- Tiến trình kết thúc do tiến trình khác (có đủ quyền: như tiến trình cha của nó)
	- Gọi system routine abort với tham số là PID của tiến trình cần được kết thúc
- Hệ điều hành thu hồi tất cả các tài nguyên của tiến trình kết thúc (vùng nhớ, IO buffer)
# Cộng tác giữa các tiến trình 
## Giao tiếp liên tiến trình (IPC)
IPC là cơ chế cung cấp bởi hệ điều hành nhằm giúp các tiến trình: 
	- Giao tiếp với nhau 
	- Đồng bộ hoạt động 
Hai mô hình IPC: 
	- Shared memory 
	- Message passing
![[Pasted image 20250410162329.png]]
### Shared memory 
- Một vùng nhớ dùng chung giữa các tiến trình cần giao tiếp với nhau 
- Quá trình giao tiếp được thực hiện dưới sự điều khiển của các tiến trình, không phải hệ điều hành 
- Cần có cơ chế đồng bộ hoạt động của tiến trình khi chúng cùng truy xuất bộ nhớ dùng chung 
### Message passing
- Naming
	- Giao tiếp trực tiếp 
		- send(P, msg): gửi thông điệp ddeenes tiến trình P 
		- receive(Q, msg): nhận thông điệp từ Q
	- Giao tiếp gián tiếp: thông qua mailbox hay port 
		- send(A, msg): gửi msg đến mailbox A
		- receive(Q, msg): nhận msg từ mailbox B
- Đồng bộ hóa (synchronization): blocking send, non blocking send, blocking receive, non blocking receive 
# Tiểu trình
## Tổng quan về tiểu trình
- Tiểu trình là một đơn vị cơ bản sử dụng CPU gồm
	- Thread ID, PC, Registers, Stack và shared code, data resources (files)
### PCB là TCB trong mô hình multithreads
![[Pasted image 20250410162829.png]]
### Lợi ích của tiến trình đa tiểu trình:
- Đáp ứng nhanh
- Chia sẻ tài nguyên
- Kinh tế
- Khả năng mở rộng
### Thực thi đồng thời vs Thực thi song song
- Thực thi đồng thời tạo ra cảm giác thực thi song song nhưng chỉ có một công việc được thực thi tại khoảng thời gian
- Thực thi song song, nhiều công việc được thực thi song song với nhau bằng cách sử dụng nhiều lõi xử lý 
### Phân loại tiểu trình: 
- Tiểu trình người dùng: 
	- Thực thi các đoạn mã trong chương trình người dùng 
	- Được quản lý mà không cần sự hỗ trợ từ hạt nhân
- Tiểu trình hạt nhân:
	- Thực thi thông qua system call
	- Được hỗ trợ và quản lý trực tiếp bởi hệ điều hành
### Các mô hình đa tiểu trình 
- Nhiều một
- Một một 
- Nhiều nhiều 
**Không có một nhiều**