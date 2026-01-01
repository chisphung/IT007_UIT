- Cấu trúc chung của một hệ thống [[1- Cấu trúc hệ thống]]
- Hệ điều hành là một chương trình lớn 
- Nó có nhiều dạng cấu trúc khác nhau 
	- Cấu trúc Monolithic 
	- Layered Approach
	- Microkernals 
	- Modules 
	- Hybrid systems
## Simple structure:
	Hệ điều hành không phân chia, chương trình có thể trực tiếp gọi đến phần cứng mà không thông qua systemcall
	Ví dụ MSDOS

![[Pasted image 20250408193859.png]]
## Monolithic 
	Toàn bộ những phần quan trọng nhất được gói gọn trong kernel
	Có cung cấp interface cho các chương trình ứng dụng
	Giứa kernel và phần cứng cũng có interface

![[Pasted image 20250408194205.png]]
==Linux dựa theo cấu trúc monolithic được thiết kế theo dạng mô đun== 
## Layered structure
	Chia lớp, layer trong cùng là hardware
	ngoài cùng là user interface
	Giữa người dùng và hardware phải qua nhiều tầng để truy cập đến hardware
	Mỗi tầng gọi dịch vụ tầng bên dưới 
==Ví dụ; Hệ điều hành THE==
![[Pasted image 20250408194517.png]]
## Microkernel
	Phân chia module theo microkernel (CMU Mach OS, 1980)
	Chuyển một số chức năng của OS từ kernel space sang user space --> thu gọn
	Giao tiếp qua cơ chế truyền thông điệp

[[3 - Giao tiếp giữa các tiến trình]]

![[Pasted image 20250408195049.png]]
## Module structure 
	Hệ điều hành trao đổi thông qua các dịch vụ
	Sử dụng cách tiếp cận hướng đối tượng
Ví dụ: Linux, Solaris
![[Pasted image 20250408201206.png]]
## Hybrid system
	Là cấu trúc lai giữa các cấu trúc 
Nhân Linux và Solaris theo cấu trúc kết hợp không gian địa chỉ kernel, cấu trúc monolithic và modules
Nhân Windows hầu như theo cấu trúc liền khối, cộng với cấu trúc vi nhân cho các hệ thống cá nhân khác nhau
