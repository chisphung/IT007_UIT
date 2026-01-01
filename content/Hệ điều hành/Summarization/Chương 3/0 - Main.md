	Tiến trình là một chương trình đang thực thi
	Bản thân hệ điều hành cũng là một tiến trình
	Hệ điều hành phải là tiến trình được nạp vào đầu tiên

![[Pasted image 20250408203556.png]]
Process memory layout contains:  
	- Text section (program code)
	- Data section (global variables)
	- Program counter, processor registers
	- Heap section (chứa bộ nhớ cấp phát động)
	- Stack section (chứa dữ liệu tạm thời)
		- Function parameters 
		- Return address
		- Local variables 
![[Pasted image 20250408201623.png]]
![[Pasted image 20250408201654.png]]
**Các bước nạp chương trình vào bộ nhớ**
	Từ những file riêng lẻ, bao gồm header, c,... **thông qua compiler/assembler**
	--> thành những file obj, **thông qua Linker**
	--> thành những load module, **thông qua Loader**
	--> thành những **process image** --> được nạp vào bộ nhớ chính 

![[Pasted image 20250407230638.png]]
-  #IMP Các bước khởi tạo tiến trình: 
	- Cấp phát một định danh duy nhất cho tiến trình 
	- Cấp phát không gian nhớ để nạp tiến trình 
	- Khởi tạo khối dữ liệu PCB cho tiến trình 
	- Thiết lập các mối liên hệ cần thiết (VD: sắp xếp PCB vào hàng đợi định thời)
## [[1 - Trạng thái tiến trình]]
## Process control block
	Là một kiểu dữ liệu chứa thông tin của tiến trình bao gồm PID, state, PC, register, scheduling info, mem manament info, accounting info, io status info

![[Pasted image 20250408204137.png]]

## Context switching 
![[Pasted image 20250408204410.png]]
Khi chuyển tiến trình, lưu trạng thái hiện tại 
Khi quay trở lại, reload trạng thái của tiến trình 
## #IMP==Định thời tiến trình (process scheduling)==
### Yêu cầu đối với hệ điều hành về quản lý tiến trình 
Hiệu suất CPU - Tối đa
Thời gian đáp ứng (response time) - Tối thiểu 
Phân phối tài nguyên hợp lý 
Trách deadlock
Cung cấp cơ chê giao tiếp và đồng bộ các tiến trình 
Cung cấp cơ chế hỗ trợ user tạo/kết thúc tiến trình
### Tại sao định thời 
	- Đa chương: Vài tiến trình chạy tại các thời điểm -> cần định thời để tận dụng tối đa cpu
	- Chia thời (timesharing) User tương tác với mỗi ctrinh đang thực thi --> định thời để giảm tối thiểu thời gian đáp ứng (response time)
Định nghĩa: [[4 - Phân loại hệ điều hành]]
### Các hàng đợi định thời
	- Job queue
	- Ready queue
	- Device queue
### #IMP==Bộ định thời== 
Ref ở chương 4 viết rõ hơn

![[Pasted image 20250409180733.png]]
- **Bộ định thời công việc (bộ định thời dài): New -> Ready.**  
	It runs infrequently, ( such as when one process ends selecting one more to be loaded in from disk in its place ), and can afford to take the time to implement intelligent and advanced scheduling algorithms.
- **Bộ định thời CPU (Bộ định thời ngắn): Ready -> Running**
	The **short-term scheduler**, or CPU Scheduler, runs very frequently, on the order of 100 milliseconds, and must very quickly swap one process out of the CPU and swap in another one.
- **Bộ định thời vừa: điều chỉnh mức độ đa chương của hệ thống.** 
	When system loads get high, this scheduler will swap one or more processes out of the ready queue system for a few seconds, in order to allow smaller faster jobs to finish up quickly and clear the system. See the differences in Figures 3.7 and 3.8 below.
![[Pasted image 20250408212609.png]]
ref: [[2 - Các loại định thời]]
### Phân loại tiến trình
- Tiến trình hướng IO 
- Tiến trình hướng CPU 
## #IMP [[2 - Tạo tiến trình]]
## #IMP - [[3 - Giao tiếp giữa các tiến trình]]
## #IMP - [[4 - Tiểu trình]]
	Thực thi đồng thời: tạo cảm giác các công việc được thực thi song song nhưng thực thế chỉ có 1 công việc tại 1 thời điểm
	Thực thi song song: các công việc thực thi song song với nhau bằng cách sử dụng nhiều lõi xử lý 

![[Pasted image 20250408214218.png]]

### References
- Full text - [[Chương 3 - Tiến trình]]
- [CSUIC](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/3_Processes.html)
- 