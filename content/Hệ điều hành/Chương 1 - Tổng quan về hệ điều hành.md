---
share_link: https://share.note.sx/ticlgnq0#+yz2gbbWxaJlGmQqrw2kHlArNJ3eQvOvRUwtzXLiqTo
share_updated: 2025-04-24T11:47:28+07:00
---
# Tổng quan về hệ điều hành
## Hệ điều hành là gì 
	Chương trình trung gian giữa phần cứng máy tính và người dùng, có chức năng điều khiển và phối hợp việc sử dụng phần cứng và cung cấp cacs dịch vụ cơ bản cho các ứng dụng
## Mục tiêu
	- Giúp người dùng dễ dàng sử dụng hệ thống
	- Quản lý và cấp phát tài nguyên hệ thống một cách hiệu quả
## Cấu trúc hệ thống máy tính 
![[Pasted image 20250407162304.png]]
- Phần cứng: bao gồm các tài nguyên cơ bản của máy tính như CPU, bộ nhớ, các thiết bị I/O
- Hệ điều hành: Phân phối tài nguyên, điều khiển và phối hợp các hoạt động của các chương trình trong hệ thống 
- Chương trình ứng dụng: Sưr dụng hệ thống tài nguyên để giải quyêt smoojt bài toán tính toán nào đó của người dùng. Ví dụ: Compilersr, database system, video games, business programs
- Users (people, machines, others computers)
# Hoạt động bên trong máy tính 
## Bên trong hệ điều hành 
- Chương trình duy nhất luôn chạy tại tất cả các thời điểm máy tính hoạt động là nhân (kernal)
- Đi kèm với nhân còn có hai loại chương tình: 
	- Chương trình hệ thống: được đóng gói cùng với hệ điều hành nhưng không phải một phần của nhân 
	- Chương trình ứng dụng: tất cả các chương trình không có liên kết (associate) với hoạt động của hệ thống
-  Ngày nay, một số hệ điều hành còn chứa [middleware] - một tập hợp các khung/nền tảng phần mềm (sofware framework) cung cấp các dịch vụ bổ sung hỗ trợ cho nhà phát triển ứng dụng như cơ sở dữ liệu, đa phương tiện, đồ hòa
## Hoạt động bên trong may tính
- CPU (một hoặc nhiều) và các trình điều khiển thiết bị (device controller) kết nối với nhau thông qua bus để truy xuất bộ nhớ chia sẻ (shared memory)
![[Pasted image 20250407162924.png]]
- Các thiết bị IO và CPU có thể thực thi đồng thời (concurently)
- Mỗi trình điều khiển chịu trách nhiệm một loại thiết bị cụ thể
- Mỗi trình điều khiển thiết bị có một bộ đêm (buffer) cục bộ
- Môi loại trình điều khiển thiết bị có một device drvier tương ứng của hệ điều hành để quản lý nó 
- CPU di chuyển dữ liệu giữa bộ nhớ chính và các bộ đệm cục bộ 
- Khi trình điều khiển thiết bị hoàn tất các thao tác, nó báo hiệu cho CPU bằng cách phát sinh một ngắt 
## Ngắt
- Đặc điểm cơ bản của ngắt: 
	- Ngắt chuyển điều khiển đến interupt service routine thông qua interupt vecotr (chứa địa chỉ của tất  cả các service  routine ) --> like a function
	- Kiến trúc ngắt phải lưu dịa chỉ của lệnh phát sinh ngắt --> Để qua lại vị trí sau khi thực hiện xong hàm 
	- Ngắt được tạo ra bởi phần mềm do lỗi hoặc do yêu cầu của người dùng, được gọi là trap hoặc exception
	- Hệ điều hành hoạt động định hướng theo ngắt
- Quá trình phát sinh của ngắt: 
![[Pasted image 20250407163410.png]]
## Cấu trúc lưu trữ 
- Hệ thống lưu trữ được tổ chức phân cấp dựa trên: 
	- Tốc độ truy xuất
	- Chi phí 
	- Khả năng lưu trữ dữ liệu khi không có nguồn điện
- Phân cấp lưu trữ
![[Pasted image 20250407163520.png]]
- Main memory - thiết bị lưu trữ dung lượng lớn duy nhất CPU truy xuất trực tiếp 
	- Random access
	- Mất dữ liệu khi không có nguồn điẹn
	- Được xây dựng dựa trên công nghệ bán dẫn Dynamic random access Memory 
- Secondary storage: mở rộng cho bộ nhớ chính để cung cấp khả năng lưu trữ khi không có nguồn điện dung lượng lớn
## Hoạt động của máy tính hiện đại
Kiến trúc  Voneuman
![[Pasted image 20250407163734.png]]
Phân biệt các khái niệm về bộ xử lý:
- CPU - thành phần phần cứng thực thi các lệnh
- Processor - một con chip chứa một hoặc nhiều CPU 
- Core - đơn vị tính toán cơ bản của cpu
- Multicore - Nhiều lõi tính toán trên cùng một CPU
- Multiprocessor - Nhiều bộ xử lý 

# Kiến trúc hệ thống máy tính
## Hệ thống đơn bộ xử lý: 
- Chỉ có một bộ xử lý đa dụng (general-purpose processor) với một lõi duy nhất: thực thi  các tập lệnh đa dụng (bao gồm các lệnh trong các tiến trình)
- Có thể kèm theo các bộ xử lý riêng biệt: chỉ có thể thực thi các tập lệnh hạn chế và không thể chạy tiến trình
## Hệ thống đa bộ xử lý
- Tên gọi khác: prallel systems, tightly-coupled systems
- Ưu điểm: 
	- Tăng cương năng suất hệ thống (system throughput): càng nhiều bộ xử lý thì càng nhanh xong việc
	- Kinh tế: ít tốn kém vì có thể dùng chung tài nguyên
	- Độ tin cậy cao: Khi một bột xử lý hỏng thì công việc của nó được chia sẻ giữa các bộ xử lý còn lại
- Phân loại: 
	- Đa xử lý bất đối xứng - mỗi bộ xử lý thực thi công việc khác nhau 
	- Đa xử lý đối xứng - mỗi bộ xử cùng thực hiện tất cả công việc

**Kiến trúc đa xử lý đối xứng**

![[Pasted image 20250407164823.png]]

**Thiết kế nhân kép**

![[Pasted image 20250407164849.png]]

**Hệ thống NUMA**

![[Pasted image 20250407164931.png]]

## Hệ thống gom cụm
- Là một dạng hệ thống đa bộ xử lý, nhưng nhiều hệ thống làm việc với nhau 
	- Thường chia sẻ không gian lưu trữ qua mạng lưu trữ khu vực (storage-area network - SAN)
	- Cung cấp các dịch vụ có độ sẵn sàng cao (high-availability): dịch vụ được cung cấp liên tục cho dùng một phần cứng bị hỏng
	- Có thể theo cấu trúc đối xứng hoặc bất đối xứng
		- Gôm cụng bất đối xứng: một máy ở chế độ hot-standby, các máy còn lại chạy ứng dụng 
		- Gom cụng đối xứng: Nhiều nút chạy ứng dụng và giám sát các nút còn lại
- Cấu trúc của một hệ thống gom cụm

![[Pasted image 20250407165225.png]]

# Các thao tác trong hệ điều hành 
## Đơn chương
- Đơn chương: 
	- Chỉ một công việc/chương trình được nạp vào bộ nhớ tại một thời điềm 
	- Công việc/chương trình được thi hành tuần tự
- Người dùng muốn chạy nheieuf hơn một chương trình tại một thời điểm --> hệ thống đa chương
## Đa chương
- Đa chương tổ chức các công việc, boa gồm mã và dữ liệu, sao cho CPU luôn có thể chọn một để thực thi
	- Nhiều công việ được nạp đồng thời vào bộ nhớ 
	- Một công việc được chọn và chạy bởi bộ định thời công việc (job scheduling)
	- Khi một công việc phải chờ (vd: IO), hệ điều hành chuyển sang thực thi công việc khác
- Trong hệ thông đa chương, một công việc đang thực thi được gọi là một tiến trình (process)
- Đa chương giúp tận dụng thời gian rảnh, tăng hiệu suất sử dụng CPU
![[Pasted image 20250407165618.png]]
- Layout bộ nhớ của một hệ thông đa chương
## Đa nhiệm:
- Đa nhiệm là một sự mở rộng của đa chương - CPU chuyển các công việc thường xuyên hơn để người dugnf có thể tương tác với từng công việc khi nó chạy
# Các thao tác trong hệ điều hành
## Các chế độ hoạt động
- Việc có nhiều chế độ hoạt động cho phép hệ điều hanhf bảo vệ chính nó và các thành phần khác của hệ thống
	- Hai chế độ cơ bản: user mode, kernal mode
	- Có thể mở rộng nhiều hơn hai chế độ
- Bit chế độ được thêm vào phần cứng
	- Dùng đề phân biệt khi nào thì hệ thống đang thực thi mã người dùng hay mã hạt nhân 
	- Khi một ứng dụng của ngời dùng thực thi --> Bit chế độ người dùng (1)
	- Khi mã trong hạt nhân thực thi -> bit chế độ hạt nhân (0)
- Một số lệnh được thiết kế riêng như đặc quyền, các lệnh này chỉ thực thi ở chế độ hạt hân
- Ví dụ chuyển từ chế độ người dùng sang chế độ hạt nhân

![[Pasted image 20250407165952.png]]