## Phân loại hệ điều hành 
### Dưới gốc độ loại máy tính
#### Hệ điều hành dành cho: 
- MainFrame 
- Server 
- PC 
- PDA 
- Chuyên biệt (Car, TV)
- RTOS
### Dưới gốc độ hình thức xử lý
#### Hệ thống: 
- Xử lý theo chương trình:
	- Uniprogramming: 
		- Tác vụ được thi hành tuần tự
		- Bộ giám sát thương trực
		- CPU và các thao tác nhập xuất xử lý offline
		- Spooling (đồng bộ hóa các thao tác bên ngoài )
	- Multiprogramming: yêu cầu đối với hđh:
		- job **scheduling**
		- **memory** management
		- **CPU** scheduling
		- **resources** allocation
		- **protection** 
- Timesharing: yêu cầu đối với hđh
	- Job scheduling
	- Memory management
	- Process management
	- File management
	- Resource Allocation
	- Protection
- Song song (parallel, tightly coupled system)
	- [[4.9 Định thời tiểu trình#Đa xử lý bất đối xứng]]
	- [[4.9 Định thời tiểu trình#Đa xử lý đối xứng]]
- Phân tán (distributed, loosely coupled system )
	- Mỗi processor có bộ nhớ riêng, giao tiếp với nhau qua các kênh nối mạng, bus tốc độ cao
	- Người dùng chỉ nhìn thấy một hệ thống đơn nhất
	- Ưu điểm:
		- Chia sẻ tài nguyên
		- Chia sẻ sức mạnh tính toán
		- Độ tin cậy cao
		- Độ sẵn sàng cao
	- P2P
	- Client Server 
- RTOS
	- Hard realtime: yêu cầu nghiêm ngặt về mức độ realtime 
		- Sử dụng trong y tế, quân dội
	- Soft realtime: yêu cầu realtime nhưng không nghiêm ngặt
		- Sử dụng trong multi media, virtual reality
