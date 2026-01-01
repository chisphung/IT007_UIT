- Single-processor systems  (Hệ thống đơn bộ xử lý)
- Multi-processor systems (Hệ thống đa bộ xử lý)
- Clustered system (Hệ thống phân cụm)
## Hệ thống đơn bộ xử lý: 
- Chỉ có ==một bộ xử lý đa dụng== (general-purpose processor) với một lõi duy nhất: thực thi  các tập lệnh đa dụng (bao gồm các lệnh trong các tiến trình)
- Có thể kèm theo các bộ xử lý riêng biệt: chỉ có thể thực thi các tập lệnh hạn chế và không thể chạy tiến trình
## Hệ thống đa bộ xử lý
- Tên gọi khác: prallel systems, ==tightly-coupled systems==
- Ưu điểm: 
	- Tăng cương năng suất hệ thống (system throughput): càng nhiều bộ xử lý thì càng nhanh xong việc
	- Kinh tế: ít tốn kém vì có thể dùng chung tài nguyên
	- Độ tin cậy cao: Khi một bột xử lý hỏng thì công việc của nó được chia sẻ giữa các bộ xử lý còn lại
- Phân loại: 
	- Đa xử lý bất đối xứng - mỗi bộ xử lý thực thi công việc khác nhau 
		[[4.9 Định thời tiểu trình#Đa xử lý bất đối xứng]]
	- Đa xử lý đối xứng - mỗi bộ xử cùng thực hiện tất cả công việc
		[[4.9 Định thời tiểu trình#Đa xử lý đối xứng]]
		- Symmetric multiprocessing or shared-memory multiprocessing (SMP) involves a multiprocessor computer hardware and software architecture where two or more identical processors are connected to a single, shared main memory, have full access to all input and output devices, and are controlled by a single operating system
**Kiến trúc đa xử lý đối xứng**

![[Pasted image 20250407164823.png]]
**Thiết kế nhân kép**

![[Pasted image 20250407164849.png]]
**Hệ thống NUMA**

![[Pasted image 20250407164931.png]]
## Hệ thống gom cụm
ref: [[4 - Phân loại hệ điều hành]] --> Hệ thống phân tán
- Là một dạng hệ thống đa bộ xử lý, nhưng nhiều hệ thống làm việc với nhau 
	- Thường chia sẻ không gian lưu trữ qua mạng lưu trữ khu vực (storage-area network - SAN)
	- Cung cấp các dịch vụ có độ sẵn sàng cao (high-availability): dịch vụ được cung cấp liên tục cho dùng một phần cứng bị hỏng
	- Có thể theo cấu trúc đối xứng hoặc bất đối xứng
		- Gôm cụng bất đối xứng: một máy ở chế độ hot-standby, các máy còn lại chạy ứng dụng 
		- Gom cụng đối xứng: Nhiều nút chạy ứng dụng và giám sát các nút còn lại
- Cấu trúc của một hệ thống gom cụm![[Pasted image 20250407165225.png]]
