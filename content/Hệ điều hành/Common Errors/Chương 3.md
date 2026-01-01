## Một tiến trình bao gồm 
- Text section (program code)
- Data section (global variables)
- Program Counters, processor registers
- Heap section (bộ nhớ cấp phát động)
- Stack section (chứa dữ liệu tạm thời):
	- Function parameters 
	- Local variables 
	- Return Addresses 
## Các bước khởi tạo một tiến trình 
- Khởi tạo PID 
- Cấp phát không gian nhớ để nạp tiến trình
- Khởi tạo khối PCB
- Thiết lập các mối liên hệ cần thiết (VD: sắp PCB vào hàng đợi định thời )
## PCB gồm: 
- Trạng thái tiến trình 
- Bộ đếm chương trình 
- Các thanh ghi
- Thông tin CPU Schedule
- Thông tin quản lý bộ nhớ
- Thông tin: lượng CPU, thời gian sử dụng
- Thông tin trạng thái IO 
## Yêu cầu của hệ điều hành về quản lý tiến trình 
- Hỗ trợ sự thực thi luân phiên giữa nhiều tiến trình 
	- Hiệu suất sử dụng CPU 
	- Thời gian đáp ứng 
- Phân phối tài nguyên hệ thống hợp lý 
- Trành deadlock 
- Cung cấp cơ chế giao tiếp, đồng bộ giữa các tiến trình 
- Cung cấp cơ chế hỗ trợ user tạo/kết thúc tiến trình 