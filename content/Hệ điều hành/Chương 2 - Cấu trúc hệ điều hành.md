# Các thành phần của hệ điều hành
- [[#Quản lý tiến trình]]
- [[#Quản lý bộ nhớ chính]]
- [[#Quản lý file]]
- [[#Quản lý hệ thống IO]]
- [[#Quản lý hệ thống lưu trữ thứ cấp]]
- [[#Hệ thống bảo vệ]]
- [[#Hệ thống thông dịch lệnh]]
## Quản lý tiến trình
Để hoàn thành công việc, một tiến trình cần: 
- CPU 
- Bộ nhớ 
- File 
- Thiết bị IO
Các nhiệm vụ chính: 
- Tạo và hủy tiến trình
- Tạm dùng/thực thi tiếp tiến trình
- Cung cấp các cơ chế
	- Đồng bộ hoạt động của các tiến trình
	- Giao tiếp giữa các tiến trình
	- Khống chế tắc nghẽn
## Quản lý bộ nhớ chính
- Bộ nhớ chính là trung tâm các thao tác, xử lý 
- Để nâng cao hiệu suất ử dụng CPU, hệ điều hành cần quản lý bộ nhớ thích hợp
- Các nhiệm vụ chính
	- Theo dõi, quản lý các vùng nhớ đã cấp phát 
	- Quyết định sẽ nạp chương trình nào khi có vùng nhớ trống
	- Cấp phát và thu hồi các vùng nhớ khi cần thiết
## Quản lý file
- Hệ thống file
	- File
	- Thư mục
- Các dịch vụ chính
	- Tạo xáo file/thư mục
	- Các thao tác xử lý file/thư mục như copy paste
	- Ánh xạ file/thư mục vào thiết bị thứ cấp tương ứng
	- Sao lưu và phục hồi dữ liệu

## Quản lý hệ thống IO
![[Pasted image 20250407173439.png]]
- Che dấu sự khác biệt của các thiết bị IO trước người dùng 
- Có chức nagnw 
	- Cơ chế: buffering, caching, spooling
	- Cung cấp giao diện chung đến các tiến trình điều khiển thiết bị 
	- Bộ điều khiển các thiết bị phần cứng
## Quản lý hệ thống lưu trữ thứ cấp
![[Pasted image 20250407173552.png]]
- Bộ nhớ chính: kích thước nhỏ, là môi trường chứa thông tin không bền vứng --> cần hệ thống lưu trữ thứ cấp để lưu trữ các dữ liệu bền vững
- Phương tiện lưu trữ thông dụng là HDD SSD
- Nhiệm vụ của hệ điều hành trong quản lý đĩa
	- Free space management 
	- Storage allocation
	- Disk scheduling
--> Sử dụng thường xuyên --> ảnh hưởng đến tốc độ của hệ thống --> cần quản lý hiệu quả
# Các thành phần của hệ điều hành 
## Hệ thống bảo vệ
![[Pasted image 20250407173813.png]]
- Trong hệ thống cho phép nhiều users hay nhiều process diễn ra đồng thời: 
	- Kiểm soát tiến trình người dùng login/logout và sử dụng hệ thống 
	- Kiểm soát việc truy cập các tài nguyên trong hệ thống
	- Bảo đảm những user/process chỉ được phép sử dụng các tài nguyên dành cho nó 
	- Các nhiệm vụ của hệ thống bảo vệ 
		- Cung cấp cơ chế kiểm soát đăng nhập/xuất
		- Phân định được sự truy cập tài nguyên authorized và unauthorized
		- Phương tiện thi hành các chính sác (enforcement of policies) --> bảo vệ dữ liệu của ai đối với ai
## Hệ thống thông dịch lệnh
![[Pasted image 20250407174101.png]]
- Là giao diện chủ yếu giữa người dùng và OS 
	-  Ví dụ: shell, mouse-based window and menu
- Khi user login 
	- Command line interpreter chạy, chờ nhận lệnh từ người dùng, thực thi lệnh và trả về kết quả
	- Lệnh -> bộ điều khiển lệnh -> hệ điều hành
	- Các lệnh chủ yếu: 
		- Tạo hủy và quản lý tiến trình, hệ thống 
		- Kiểm soát IO 
		- Quản lý bộ lưu trữ thứ cấp
		- QUản lý bô nhớ chính
		- Truy cập hệ thông file và cơ chế bảo mật
# Các dịch vụ hệ điều hành cung cấp
![[Pasted image 20250407174311.png]]
![[Pasted image 20250407174325.png]]
- Thực thi chương trình
- Thực hiện các thao tác IO theo yêu cầu của chương trình 
- Các thao tác trên hệ thống file 
- Trao đổi thông tin giữa các tiến trình qua hai các 
	- Shared memory 
	- Message passing
- Phát hiện lỗi 
	- Trong CPU, Bộ nhớ, trên thiết bị IO 
	- Do chương trình: chia cho 0, truy cập đến địa chỉ bộ nhớ không cho phép
- Cấp phát tài nguyên
	- Tài nguyên: CPU, bộ nhớ chính, ổ đĩa
	- Ó có các routine tương ứng
- Accounting
	- Nhằm lưu vết user để tính phí hoặc đơn giản để thống kê
- Bảo vệ và an ninh
	- Hai tiến trình khác nhau không được ảnh hướng nhau 
	- Kiểm soát được các truy xuất tài nguyên của hệ thống
	- Chỉ các user được phép sử dụng hệ thống mới truy cập tài nguyên của hệ thống (vd: thông qua user name và password)
- Giao diện người dùng 
	- Hầu hết các hệ điều này hiện này đều có giao diện người dùng 
	- Giai diện CLI 
	- GUI 
	- Touchscreen

# Systemcall
- Dùng để giao tiếp giữa tiến trình và hệ điều hành, hay nói các khác là cung cấp giao diện giữa tiến trình và hệ điều hành bằng cách gọi đến các dịch vụ mà hệ điều hành cung cấp 
	- Ví dụ: open, read, write file
- Thông thường được viết bằng ngôn ngữ cấp cao và hầu hết được truy cập thông qua các API
- Có 3 APIs thông dụng là Win32 API cho Windows, POSIX API cho POSIX-based systems (bao gồm tất cả các phiên bản của UNIX, LInux, và MACOS X) và Java API cho các máy ảo Java (JVM)
- Ba phương pháp trueyenf tham số khi sử dụng system call:
	- Qua thanh ghi
	- Quan một vùng nhớ, địa chỉ của vùng nhớ dduocj wguiwr đến hệ điều hành qua thanh ghi 
	- Qua stack
![[Pasted image 20250407175046.png]]
![[Pasted image 20250407175056.png]]
# Các chương trình hệ thống
- Chương trình hệ thống gồm: 
	- Quản lý hệ thống file: create, delte, rename, list
	- Thông tin trạng thái: date, time, dung lượng bộ nhớ trống
	- Soạn thảo file: file editor
	- Hỗ trợ ngôn ngữ lập trình: compiler, assembler, interpreter
	- Nạp, thực thi, giúp tìm lỗi chương trình: loader, debugger
	- Giao tiếp: email, talk, web browser
Người dùng chủ yếu làm việc thông qua các system program, không làm việc trực tiếp với systemcall
# Cấu trúc hệ thống 
- Hệ điều hành là một chương trình lớn 
- Nó có nhiều dạng cấu trúc khác nhau 
	- Cấu trúc Monolithic 
	- Layered Approach
	- Microkernals 
	- Modules 
	- Hybrid systems
## Monolithic 
- Unix - do giới hạn về chức năng phần cứng nên Original UNIXcung có cấu trúc rất giới hạn
- UNIX gồm hai phần tách rời nhau 
	- Nhân (cung cấp file system, CPU scheduling, memory managemnet và một số chức năng khác)
	- System program

![[Pasted image 20250407175650.png]]
## Layered approach
- Hệ điều hành được phân chia thành nhiều layer
	- Layer dưới cùng: hardware
	- Layer trên cùng: giao tiếp với user 
	- Layer trên chỉ phụ thuộc layer dưới 
	- Một layer chỉ có thể gọi các hàm của layer dưới và các hàm của được được gọi bởi layer trên
	- VD: hệ điều hành THE
	
![[Pasted image 20250407175828.png]]

## Microkernels
- Phân chia module theo micro kernel (CMU Mach OS, 1980)
- Chuyển một số chức năng của OS từ kernal space sang user space
- Thu gọn kernal --> microkernel, microkernel chỉ bao gồm các chức năng tối thiểu như quản lý tiến trình, bộ nhớ và cơ chế giao tiếp giữa các tiến trình
- Giao tiếp giữa các user module qua cơ chế truyền message passing
![[Pasted image 20250407180033.png]]
## Modules 
- Nhiều hệ điều hành hiện đại triển khai các loadable kernel modules : 
	- Sử dụng cách tiếp cận hướng đối tượng
	- Mỗi core thành phần là tách biệt nhau 
	- Trao đổi thông qua các interfaces 
	- Mỗi module như một phần của nhân
- Nhìn chung,, cấu trúc Modules giống với cấu trúc Layer nhưng phức tạp hơn 
- Ví dụ: Linux, Solaris 
![[Pasted image 20250407180210.png]]
## Cấu trúc hybrid systems 
- Hầu hết các hệ điều hành hiện đại không theo một cấu trúc thuần túy nào mà lai giữa các cấu trúc với nhau:
	- Cấu trúc lai là sự kết hợp nhiều cách tiếp cận để giải quyết các nhu cầu về hiệu suất, bỏa mật, nhu cầu sử dụng
	- Nhân Linux và Solaris theo cấu trúc kết hợp không gian địa chỉ kernel, cấu trúc monnolithic và Modules 
	- Nhân Windows hầu như theo cấu trúc liền khối, cộng với cấu trúc vi nhân cho các hệ thống khác nhau
![[Pasted image 20250407180417.png]]
![[Pasted image 20250407180426.png]]
![[Pasted image 20250407180436.png]]