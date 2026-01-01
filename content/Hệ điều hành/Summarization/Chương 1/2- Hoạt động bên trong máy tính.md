## Bên trong hệ điều hành
- Chương trình duy nhất luôn chạy tại tất cả các thời điểm máy tính hoạt động là nhân (kernel)
- Đi kèm với nhân còn có hai loại chương trình: 
	- Chương trình hệ thống: được đóng gói cùng với hệ điều hành nhưng không phải một phần của nhân 
	- Chương trình ứng dụng: tất cả các chương trình không có liên kết (associate) với hoạt động của hệ thống
-  Ngày nay, một số hệ điều hành còn chứa [middleware] - một tập hợp các khung/nền tảng phần mềm (sofware framework) cung cấp các dịch vụ bổ sung hỗ trợ cho nhà phát triển ứng dụng như cơ sở dữ liệu, đa phương tiện, đồ hòa
## Hoạt động bên máy tính
- CPU (một hoặc nhiều) và các trình điều khiển thiết bị (device controller) kết nối với nhau thông qua bus để truy xuất bộ nhớ chia sẻ (shared memory)
![[Pasted image 20250407162924.png]]
- Các thiết bị IO và CPU có thể thực thi đồng thời (concurently) 
	- --> Vừa in vừa nhập bàn phím được 
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
- ![[Pasted image 20250407163410.png]]
## Cấu trúc lưu trữ 
- Hệ thống lưu trữ được tổ chức phân cấp dựa trên: 
	- Tốc độ truy xuất
	- Chi phí 
	- Khả năng lưu trữ dữ liệu khi không có nguồn điện
- Phân cấp lưu trữ![[Pasted image 20250407163520.png]]
- Main memory - thiết bị lưu trữ dung lượng lớn duy nhất CPU truy xuất trực tiếp 
	- Random access: can access any memory cell directly in any order, with the same speed
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
