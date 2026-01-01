![[Pasted image 20250408184333.png]]
- Dưới góc độ hình thức xử lý 
	- Hệ thống xử lý theo chương trình
		- Hệ thống đơn chương (uniprogramming OS)
		- Hệ thống đa chương (multiprogramming OS)
	- Hệ thống chia sẻ thời gian (Timesharing OS)
	- Hệ thống song song (parallel system)
	- Hệ thống phân tán (distributed system)
	- Hệ thống nhúng thời gian thực (RTOS)
## Hệ thống xử lý theo chương trình
### Đơn chương
	- Chỉ một công việc/chương trình được nạp vào bộ nhớ tại một thời điểm 

- Công việc/chương trình được thi hành tuần tự
	- Bộ giám sát thường trực
	- CPU và các thao tác nhập xuất:
		- Xử lý offline 
		- Đồng bộ hóa các thao tác bên ngoài – Spooling (Simultaneous Peripheral Operation On Line)
![[Pasted image 20250408184832.png]]
- Người dùng muốn chạy nhiều hơn một chương trình tại một thời điểm --> hệ thống đa chương
### Đa chương 
- Đa chương tổ chức các công việc, bao gồm mã và dữ liệu, sao cho CPU luôn có thể chọn một để thực thi
	- **Nhiều công việc được nạp đồng thời vào bộ nhớ** 
	- Một công việc được chọn và chạy bởi bộ định thời công việc (job scheduling)
	- Khi một công việc phải chờ (vd: IO), hệ điều hành chuyển sang thực thi công việc khác
- Trong hệ thông đa chương, một công việc đang thực thi được gọi là một tiến trình (process)
- Đa chương giúp tận dụng thời gian rảnh, tăng hiệu suất sử dụng CPU
- Layout bộ nhớ của một hệ thông đa chương:
![[Pasted image 20250407165618.png]]
![[Pasted image 20250408185036.png]]
## Hệ thống chia sẻ thời gian
- Là sự mở rộng của hệ thống đa chương 
- Mỗi chương trình có một lượng tử thời gian nhất định
- Phải tạo cho người dùng cảm giác liên tục, không luân phiên
- Tuy nhiên, nếu máy tính sử dụng 1 CPU thì khó xử lý được 
- Khó khăn: Phải giải quyết được thuật toán điều phối 
	- Pseudo-parallelism: cho người dùng cảm giác nhiều tác vụ giải quyết cùng một lúc
![[Pasted image 20250408185425.png]]
## Hệ điều hành song song
parallel, multiprocessor, hay tightlycoupled system
- Hầu hết chạy trên hệ thống đa bộ xử lý với shared memory (ref: [[3 - Kiến trúc hệ thống máy tính]])
- Chia chương trình thành nhiều jobs để có thể thực thi đồng thời trên nhiều CPUs
- ![[Pasted image 20250408190341.png]]
- **Ưu điểm**
	- Nhanh
	- Tin cậy khi một processor hỏng thì công việc của nó được chia sẻ giữa các processor còn lại
- **Nhược điểm**
	- Yêu cầu phần cứng cao
	- Thuật toán khó
![[Pasted image 20250408190524.png]]
[[4.9 Định thời tiểu trình#Định thời đa bộ xử lý]] 
## Hệ thống nhúng xử lý thời gian thực
- Nhiệm vụ phải thực thi đúng trong khoảng thời gian yêu cầu
- Phân loại 
	- Hard-realtime system: phải xử lý trong khoảng thời gian yêu cầu
		- Sử dụng trong quân đội, hàng không, giao thông, công nghiệp
	- Soft realtime system:
		- Chấp nhận thỉnh thoảng delay
		- Sử dụng trong hệ thống truyền thông đpt
--> Đắt, giới hạn, phức tạp
## Hệ thống phân tán
distributed system, looselycoupled systemƯU
	Mỗi processor có bộ nhớ riêng, giao tiếp với nhau qua các kênh nối như mạng, bus tốc độ cao
	Người dùng chỉ thấy một hệ thống đơn nhất
**Ưu điểm**
- resource sharing
- computational sharing
- high reliabilitiy
- high availability
### Client Server
- Server: cung cấp dịch vụ
- Client: sử dụng dịch vụ
![[Pasted image 20250408190813.png]]
### P2P 
- Các máy tính ngang hàng nhau
- Không có csdl tập trung
- VD: Gnuttella
- ![[Pasted image 20250408190203.png]]
