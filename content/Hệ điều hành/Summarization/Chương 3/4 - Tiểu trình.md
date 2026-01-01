	Tiểu trình là một đơn vị cơ bản sử dụng CPU gồm 
	Thread ID, PC, Registers, Stack và chia sẻ chung code, data, resourses (files)

![[Pasted image 20250408213702.png]]
## PCB và TCB trong mô hình multithread
![[Pasted image 20250408213956.png]]
### Lợi ích của tiến trình đa tiểu trình
- Đáp ứng nhanh
- Chia sẻ tài nguyên
- Tiết kiệm
- Khả năng mở rộng
### Phân biệt đồng thời và song song 
[[Hệ điều hành/Summarization/Chương 3/0 - Main|0 - Main]]
### Phân loại tiểu trình 
- Tiểu trình người dùng: Thực thi code trong user mode
- Tiểu trình hạt nhân: Thực thi thông qua systemcall, được quản lý trực tiếp bởi hệ điều hành
![[Pasted image 20250408214435.png]]
### Các mô hình đa tiểu trình: 
Để giao tiếp giữa user threads và kernal threads thì có các mô hình sau:
- Many to one 
- One to one
- Many to many
ĐÉO CÓ ONE TO MANY VÌ CÓ MỘT TIỂU TRÌNH THÌ LÀM GÌ GỌI LÀ ĐA TIỂU TRÌNH
#### Many to one
	Một tiểu trình bị blocked -> tất cả bị blocked 
	Không chạy song song được
	Ít được sử dụng
	
![[Pasted image 20250408214545.png]]
### One to one 
	Tính đồng thời tốt hơn mô hình many to one, vì không bị blocked 
	Nhược điểm: soosl uonjg tiểu trình của mỗi tiến trình có thể bị hạn chế 
Được sử dụng bởi Linux và Windows 
![[Pasted image 20250408214856.png]]
### Many to many
	Khó cài đặt

![[Pasted image 20250408214924.png]]