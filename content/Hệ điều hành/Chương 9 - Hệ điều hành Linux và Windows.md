---
share_link: https://share.note.sx/yaf82045#08IpAkSYwiSA+JaA8lq48vZyQdVR5DdsznX0Psy6tg0
share_updated: 2025-07-23T21:20:12+07:00
---
# Hệ điều hành Linux
## Tổng quan về Linux 
- Linux là một hệ điều hành miễn phí dựa trên UNIX
	- Nhân linux bắt đầu phát triển bởi Linus Torvalds từ 1991, với mục đích ban đầu để tương thích với UNIX, được phát hành dưới dạng mã nguồn mở 
- Linux được thiết kế để hoạt động hiệu quả trên PC và nhiều nền tảng phần cứng khác, được phát triển và duy trì bởi nhiều người dùng trên thế giới 
- Linux có nhiều distro khác nhau bao gồm nhân, các ứng dụng và công cụ quản lý
## Quá trình phát triển nhân Linux
- ver 0.01: không có kết nối mạng, chỉ chạy trên PC với bộ xử lý 80386
- Phiên bản 1.0: bổ dung nhiều tính năng mới 
	- Hỗ trợ TCP/IP 
	- Giao tiếp socket tương thích BSD
	- Cải thiện hệ thống tập tin
	- Hỗ trợ thêm nhiều phần cứng
- Phiên bản 1.2: là phiên bản cuối cùng chỉ dành cho PC
- Những ver sau đó dùng cho các thiết bị khác 
- Linux 2.0 được phát hành với hai cải tiến: 
	- Hỗ trợ nhiều kiến trúc 
	- Hỗ trợ các kiến trúc đa bộ xử lý 
- Linux 2.0, hoạt động trên nhiều hệ thống khcas nhau: Sun Sparc, PC, PowerMac 
- Các phiên bản 2.4 và 2.6 tiếp tục tăng cường hỗ trợ SMP, cải thiện hệ thống quản lý bộ nhớ với sự hỗ trợ bộ nhớ 64 bit
- Linux 3.0 cải thiện khả năng ảo hóa, quản lý bộ nhớ và định thời 
- Linux 4.0 hỗ trợ thêm nhiều kiến trúc mới, cải thiện các chức năng di động và nhiều cải tiến khác 
## Hệ thống Linux 
- Bao gồm nhân và các phần mềm tạo nên hệ thống Linux,
- Các phần mềm tạo nên hệ thống Linux thường không chỉ dành riêng cho Linux mà còn được sử dụng trên nhiều hệ điều hành dựa trên UNIX khác 
	- Linux sử dụng nhiều công cụ được phát triển bởi hệ điều hành Berkeley BDS, MITs X Window System   và dự án Free Software Foundation GNU
- Việc sử dụng chung các công cụ này diễn ra theo cả hai hướng 
	- Linux sử dụng, dodognf thời cải tiến công cụ đó 
		- Hệ thoogns thư viện chính của Linux bắt đầu từ dự án GNU với nhiều cải tiến được thực hiện bởi cộng đồng Linux 
	- Các dự án khác sử dụng lại không cụ được xây dựng/cải tiến bởi cộng đồng Linux 
		- Các công cụ quản lý mạng trên Linux được kế thừa từ 4.3BSD, nhưng các hệ điều hành dựa trên BSD say này như Free BSD mượn trở lại các mã nguồn từ Linux
## Các bản phân phối Linux 
- Là tập hợp các gói phần mềm đã được biên dịch và tiêu chuẩn hóa, bao gồm hệ thống Linux cơ bản, hệ thống cài đặt, các công cụ qunar lý và các gói công cụ UNIX phổ biến 
- Các bản phân phối phổ biến  hiện nay là RedHat (thương mại) và Debian (miễn phí). Một số bản phân phối thường gặp khác là Canonical và SuSE
- Định dạng gói RPM có tính tương thích cao và được sử dụng bởi nhiều bản phân phối 
## Giấy phép Linux 
- Nhân LInux được phân phối dưới giấy phép GNU General Public License 
- Bất kỳ ai sử dụng Linux, hoặc tạo ra phiên bản phát sinh của Linux không được để sản phẩm là độc quyền, phần mềm được phát hành dưới giấy phép GPL không thể được tái phân phối chỉ dưới dạng nhị phân
	- Có thể bán các bản phân phối, nhưng phải cung cấp kèm mã nguồn
## Nguyên tắc thiết kế Linux 
- Linux là một hệ thống nhiều người dùng, đa tác với tập đầy đủ các công cụ tương thích với UNIX
	- Hệ thống tập tin tuân thủ theo UNIX. Linux cũng cài đặt đầy đủ mô hình mạng theo tiêu chuẩn của UNIX
	- Giao diện lập trình tuân thủ theo SVR4 UNIX
- Các mục tiêu thiết kế chính là tốc độ, hiệu quả và tiêu chuẩn hóa 
- Linux được thiết kế để đáp ứng các yêu cầu POSIX liên quan 
	- Hỗ trợ Pthreads và một tập con của thư viện quản lý tiến trình real-time POSIX

## Các thành phần của hệ thống Linux 
- Như phần lớn các hệ thống UNIX, hệ thống Linux bao gồm 3 thành phần chính: nhân, thư iện  hệ thống và công cụ hệ thống
- Supercomputer: sử dụng tập trung thông qua SSH, HTTP
- Desktop Computer: Sử dụng thông qua các thiết bị IO 
- Embedded computer: Tập trung thông qua SSH, HTTP
- Nhân chiụ trách nhiệm duy trì các hoạt động ở mức trừu tượng của hệ điều hành, như bộ nhớ ảo và tiến trình 
	- Các mã của nhân thực thi ở kernel mode với đầy đủ quyền truy xuất đến tài nguyên vật lý của máy tính 
	- Tất cả các mã của nhân và cấu trúc dữ liệu được lưu trên cùng một không gian địa chỉ 
- Các thư viện hệ thống định nghĩa một tập chuẩn các hàm thông qua đó các ứng dụng có thể trương tác với nhân. Các thư viện này cài đặt nhiều chức năng của hệ điều hành mà không cần đầy đủ quyền như các mã của nhân
- Các công cụ hệ thống (system ultilities) là các chương trình thực hiện các chức năng quản lý cụ thể
## Các module nhân trong linux 
- Module nhân: Các phần mã của nhân có thể biên dịch, nạp và gỡ rối độc lập với phần còn lại của nhân 
- Một module nhân có thể cài đặt một trình điều khiển thiết bị, một hệ thống tập tin hoặc một giao thức mạng 
- Các module nhân cho phép thiết lập một hệ thống Linux với một nhân Linux tiêu chuẩn tối thiểu mà không  cần bất cứ trình điều khiển thiết bị đi kèm
- Các giao thức của module có thể cho phép bên thứ ba viết và phân phối trình điều khiển thiết bị hoặc hệ thống tập tin của họ, vốn không thể phân phối dưới giấy phép GPL
- ==**Linux hỗ trợ 4 loại module sau:**==
	- ==Module management system: Cho phép module nạp vào bộ nhớ và giao tiếp với phần còn lại của nhân==
	- ==Module loader and unloader: Là các công cụ ở user mode, làm việc với module-management system để nạp một module vào bộ nhớ== 
	- ==Driver-registration system: Cho phép các module thông báo với phần còn lại của nhân là có một trình điều khiển mới sẵn sàng== 
	- ==Conflict resolution mechanism: Cho phép các trình điều khiển khác nhau chiếm lấy tài nguyên máy tính và bảo vệ tài nguyên này khỏi việc truy xuất không phù hợp từ tình điều khiển khác== 
## Quản lý tiến trình 
- Hệ thống quản lý tiến trình của UNIX phân chia việc tạo tiến trình và chạy một chương trình thành hai thao tác riêng biệt 
	- System call fork() tạo ra một tiến trình mới 
	- Một chương trình mới được chạy sau khi gọi excec()
- Trên UNIX, một tiến trình chứa tất cả các thông tin mà hệ điều hành phải lưu vết ngữ cảnh của một thao tác thực thi của một chương trình đơn 
- Trên Linux, các thuộc tính của tiến trình được chia thành 3 nhóm: định dạng của tiến trình, môi trường và ngữ cảnh 
## Định thời trên Linux 
- Trên Linux, định thời không chỉ là việc chạy và tạm dừng các tiến trình, mà còn bao gồm việc thực thi nhiều tác vụ trong nhân 
- Các tác vụ trong nhân bao gồm các tác vụ được yêu cầu bởi tiến trình đang chạy và các  tác vụ thực thi nội tại trong trình điều khiển thiết bị     
- ==Phiên bản 2.5 giới thiệu và sử dụng bộ định thời O(1) dựa trên độ ưu tiên và chế độ quyết định trưng dụng==
- Phiên banr2.6 sử dụng Completely Fair Scheduler 
## Giao tiếp liên tiến trình trên Linux 
- Tương tự UNIX, Linux thông báo cho các tiến trình có một sự kiện xảy ra thông qua các signal 
- Số lượng signal là giới hạn và chúng không chứa thông tin
- Signal có thể được tạo ra bởi tiến trình hoặc nhân. Tuy nhiên, nhân không dùng signal để giao tiếp với tiến trình đang chạy ở kernel mode, thay vào đó, nó sử dụng các trạng thái định thời và cấu trúc wait_queue
## Chuyển dữ liệu giữa các tiến trình trên Linux 
- ==Pipe: Cho phép tiến trình con kế thừa một kênh giao tiếp từ tiến tình cha của nó. Dữ liệu ghi ở một đầu của pipe có thể đọc ở đầu còn lại== 
- ==Network: UNIX cung cấp một tập các công cụ mạng để gửi dữ liệu đến các tiến trình cục bộ từ xa== 
-  ==Shared memory: Cho phép giao tiếp dữ liệu một cách nhanh chóng. Dữ liệu được ghi bởi một tiến trình vào một vùng nhớ chia sẻ có thể được đọc ngay lập tức bởi một tiến trình khác nếu nó đã ánh xạ vùng nhớ đó vào không gian nhớ của nó== 
	- ==Để đặt được tính đồng bộ, shared memory cần được sử dụng kết hợp với các phương thức giao tiếp khác==
## Quản lý bộ nhớ trên Linux 
- Gồm 2 thành phần"
	- Cấp phát và giải phóng bộ nhớ vật lý - trang, nhóm các trang và các khối RAM 
	- Xử lý bộ nhớ ảo - ánh xạ bộ nhớ vào không gian địa chỉ của các tiến trình đang chạy
- Quản lý bộ nhớ vật lý: 
	- Tùy thuộc vào đặc điểm phần cứng, Linux chia bộ nhớ thành 4 vùng: ZONE, DMA, ZONE DMA32, ZONE NORMAL, ZONE HIGHMEM  
	- Mỗi vùng có page allocator riêng, chịu trách nhiệm cấp phát và giải phóng tất cả các trang vật lý, cũng như cấp phát một dãy các trang vật lý liên tiếp khi được yêu cầu 
		- Mỗi vùng nhớ cấp phát có một vùng nhớ liền kề - buddy
		- Nêu hai vùng nhớ liền kề đều trống, chúng được kết hợp thành một vùng nhớ lớn hơn 
		- VÙng nhớ trống kích thước lớn hơn có thể dược chia thành 2 vùng nhớ để đáp ứng các yêu cầu cấp phát nhỏ 
## Bô nhớ ảo trên Linux 
- Hệ thống bộ nhớ ảo của Linux duy trì không gian địa chỉ cho mỗi tiến trình. Nó tạo các trang ảo theo yêu cầu và quản lý việc nạp cac trang ảo từ đĩa cũng như di chuyển chúng trở về địa khi được yêu cầu 
- Không gian địa chỉ của một tiến trình có thể chia thành 2 views riêng biệt
	- Logical view: mô tả các hướng dẫn liên quan đến việc bố trí không gian địa chỉ. Không gian địa chỉ chứa một tập các vùng nhớ không chồng lấn nhau, mỗi vùng nhớ là một tập các trang nhớ liên tục 
	- Physical view: Được lưu trữ trên bảng trang của tiến trình và được quản lý bởi một tập các routines 
- Khi thực thi một chương trình mới, tiến trình được cung cấp một vùng nhớ ảo mới, hoàn toàn trống. Routine chịu trách nhiệm nạp chương trình sẽ nạp đầy (populate) không gian địa chỉ này với các vùng nhớ ảo 
- Quá trình tạo một tiến trình mới với fork() sẽ tạo ra một bản sao đầy đủ của không của không gian địa chỉ ảo của tiến trình hiện tại 
	- Nhân sẽ sao chép các thông tin cấu trúc bộ nhớ ảo của cha, sau đó tạo ra một tập các bảng trang cho con 
	- Các bảng tran của cha cho được sao chép trực tiếp cho con 
	- Kết thúc fork(), cha và con cùng chia sẻ số trang nhớ vật lý trong không gian địa chỉ của chúng 
## Hoán vị và phân trang trong Linux 
- Hệ thống bộ nhớ ảo phân trang cần phải tái định vị các trang nhớ cua bộ nhớ vật lý được đưa ra xuống đĩa khi cần thêm bộ nhớ cho một tác vụ nào đó 
- Hệ thống phân trang được chia thành 2 phần: 
	- Giải thuật pageout policy: Quyết định trang nào sẽ được ghi ra đĩa, khi nào thực hiện 
	- Paging mechanism: Thực hiện việc di chuyển, đồng thời đem dữ liệu trang trở lại bộ nhớ vật lý 
		- Trang có thể được đưa đến thiết bị khác, phân vùng khác hoặc tập tin 
		- ==Sử dụng giải thuật next-fit để ghi các trang liên tục==
- Linux cài đặt cơ chế liên kết động ở user mode thông qua thư viện liên kết đặc biệt 
	- Mỗi chương trình có sử dụng liên kết động chứa một hàm liên kết tĩnh nhỏ, sẽ được gọi khi chương trình bắt đầu chạy 
	- Hàm liên kết tĩnh ánh xạ thư viện liên kết vào bộ nhớ 
	- Thư viện liên kết xác định thư viện động được yêu cầu bởi chương trình cũng như các biến và hà mà nó cần (từ các thư viện động)
	- Thư viện liên kết ánh xạ các thư viện động này vào phần giữa của các bộ nhớ ảo và giải quyết các tham chiếu đên thư viện động
# Hệ điều hành Windows 
## Lịch sử phát triển 
- Từ 1988, bắt đầu phát triển 
- Ban đầu chỉ sử dụng các hàm OS/2, nhưng sau đó được thay đổi sang Win32 API, sau đó là Windows 3.0
- Nhiều phiên bản Windows được phát hành rộng rãi
- Hệ điều hành thành công nhất của Windows là XP
## Nguyên tắc thiết kế 
- Bảo mật: 
	- Nhiều lớp: sử dụng  Access control list, Data execution prevention (DEP), mã hóa hệ thống tập tin, chữ ký số 
- Đáng tin cậy: Sử dụng cơ chế bảo vệ phần cứng đối với bộ nhớ ảo và bảo vệ phần mềm với các tài nguyên của hệ điều hành
- Dễ mở rộng: được xây dựng theo kiến trúc phân tần 
	- Remote procedure calls 
	- Advanced local procedure calls 
- Hiệu năng cao:
	- Các thành phần của hệ điều hành có thể giao tiếp với nhau thông quan hệ thông struyeenf thông điệp hiệu năng cao: 
		- ==Có cơ chế trưng dụng ==, áp dụng cho các tiểu trình có độ ưu tiên thấp, cho phép hệ điều hành đáp ứng nhanh với các sự kiện bên ngoài
		- ==Được thiết kế theo cơ cheesdda xử lý đối xứng==
	- Khả năng tương thích cao, các ứng dụng được xây dựng theo tiêu chuẩn IEEE 1003.1 (POSIX) có thể được biên dịch để chạy mà không cần thay đổi mã nguồn 
	- Di động: Hdh Windows có thể chạy được trên nhiều kiến trúc khác nhau mà không cần thay đổi nhiều
	- Hỗ trợ quốc tế: Nhiều ngôn ngữ kahcs nhau 
	- Sử dụng năng lượng hiệu quả
	- Hỗ trợ nhiều thiết bị
- 
### Kiến trúc Windows 10
- Hệ thống phân lớp gồm nhiều modules hoạt động ở nhiều cấp quyền khác nhau 
	- Kernel mode: hardware abstraction layer, nhân, các tác vụ điều hành 
	- User mode: Tập hợp của các hệ thống con (subsystem)
		- Các hệ thống subsystem mô phỏng các hệ điều hành khác nhau
		- Các hệ thống subsystem bảo vệ khác nhau 
### Các thành phần hệ thống Windows 10
- Nhân: 
	- Chịu trách nhiệm quản lý, định thời tiểu trình, context switch, đồng bộ tiểu trình, xử lý ngắt và ngoại lệ, chuyển đổi giữa user model và kernel mode (thông qua system call)
	- Phần lớp được cài đặt bằng C, một số ít sử dụng hợp ngữ 
- Hyper-V Hypervisor 
	- Cung cấp chức năng ảo hóa
- HAL (Hardware Abstraction Layer)
	- Che dấu sự khác biệt về phần cứng 
	- Cung cấp giao diện phần cứng ảo để phục vụ cho bộ định thời trong nhân các tác vụ điều hành và trình điều khiển thiết bị
- Nhân bảo mật (secure kernel)
	- Hoạt động như môi trường kernel mode cho các ứng dụng Trustlet (các ứng dụng cài đặt theo mô hình bảo mật Windows)
	- Hỗ trợ truy xuất đến các khóa bí mật phần cứng, trusted platform module (TPM)
- Các tác vụ hệ điều hành (executive)
	- Tập hợp các tác vụ mà các hệ thống con môi trường sẽ sử dụng: 
		- Quản lý bộ nhớ ảo, 
		- quản lý tiến trình, 
		- quản lý IO
		- quản lý năng lượng 
		- cơ chế plug and play 
		- registry 
		- local procedure call facility 
	- Được tổ chức theo nguyên tắc thiết kế hướng đối tượng
### Quản lý tiến trình - tiểu trình 
- Mỗi tiến trình có một không gian địa chỉ ảo riêng, các thông tin về hoạt động của tiến trình và một affinity với một hoặc nhiều bộ xử lý 
- Tiểu trình là các đơn vị thực thi được định thời bởi nhân 
- Mỗi tiểu trình có trạng thái riêng, bao gồm độ ưu tiên, processor affinity và các thông tin dành cho việc kế toán 
- Có 8 trạng thái tiểu trình: initalizing, ready, deferred-ready, standby running, waiting, transition và terminated
- Mỗi tiểu trình có hai chế độ thực thi: user-mode thread và kernel mode thread 
	- Mỗi chế độ sử dụng một stack riêng 
	- Việc chuyển đổi giữa các stack và thay đổi chế độ CPU được thực hiện bởi nhân
### Định thời trên Windows
- Bộ định thời sử dụng 32 độ ưu tiên để xác định thứ tự thực thi của các tiểu trình 
	- Độ ưu tiên được chai thành 2 lớp 
		- Lớp realtime có độ ưu tiên từ 16 đến 31 
		- Lớp variable có độ ưu tiên từ 0 đến 15 
- Định thời theo độ ưu tiên trên Win 10:
	- Có xu hướng đem lại thời gian đáp ứng nhanh cho các tiểu trình interactive đang sử dụng chuột và các cửa sổ 
	- Cho phép các tiến trình hướng IO được giữ các thiết bị IO đang bận
- Định thời có thể diễn ra khi tiểu trình chuyển sang trạng thái ready hoặc waiting, khi tiểu trình kết thúc hoặc khi ứng dụng thay đổi độ ưu tiên hoặc processor affinity
- Các tiểu trình realtime được ưu tiên sử dụng CPU nhưng Win 10 không đảm bảo chắc chắn một tiểu trình realtime sẽ luôn được thực thi trong bất cứ một khoảng thời gian giới hạn cho trước (soft realtime)

### Quản lý bộ nhớ ảo 
- Thành phần quản lý bộ nhớ ảo trên Win 10 có cơ chế quản lý trang với kích thước trang bất kỳ, miễn là phần cứng có hỗ trợ kích thước đó 
- Thành phần quản lý bộ nhớ ảo trên win 10 sử dụng quy trình 2 bước để cấp phát vugnf nhớ 
	- Bước 1: Dự trữ một phần không gian địa chỉ của tiến trình 
	- Bước 2: Thực hiện cấp phát vùng nhớ bằng cách gán không gian địa chỉ ảo (trong bộ nhớ vật lý hoặc trong các tập tin paging)
- Mỗi trang có thể có một trong sáu trạng thái sau: valid, zeroed, free, standby, modified và bad
![[Pasted image 20250602153018.png]]
- Việc chuyển đổi địa chỉ ảo trên Win 10 sử dụng nhiều cấu trúc dữ liệu 
	- mỗi tiến trình có một page directory chứa 1024 mục (page dir entries) với kích thước mỗi mục là 4 bytes
	- Mỗi mục trong page dir trỏ đến một bảng trang, mỗi bảng trang này chứa 1024 mục với kích thước mỗi mục là 4 bytes 
	- Mỗi PTEs trỏ đến một khung trang kích thước 4KB trong bộ nhớ vật lý
![[Pasted image 20250602153645.png]]

**Quản lý plug and play**

- Các công cụ quản lý plug and play được sử dụng để ghi nhận và đáp ứng khi có các thay đổi về phần ứng 
- Khi các thiết bị mới được thêm vào, công cụ quản lý  PnP nạp các trình điều khiển tương ứng với thiết bị đó 
- Công cụ quản lý này cũng lưu vết quá trình các tài nguyên được sử dụng bởi từng thiết bị
**Local produce call facility**
- Phương thức giao tiếp giữa hai tiến trình trong cùng một máy tính 
- Xây dựng theo mô hình client server 
- Kho một kênh LPC được tạo ra, một trong số 3 loại kỹ thuật chuyển thông điệp phải được khai báo 
	- Loại 1: Dành cho các thông điệp ngắn, tối đa 256 byte. 
		- Được sử dụng cho hàng đợi thông điệp 
	- Loại 2: Sử dụng một vùng nhớ chia sẻ, không cần sao chép các thông điệp lớn mà chỉ cần trỏ đến vùng nhớ đó 
	- Loại 3: Gọi là quick LPC, được sử dụng bởi thành phần giao diện đồ họa của hệ thống con Win32
**Registry**
- Các thông tin cấu hình được lưu trong các khu vực riêng gọi là hives, được quản lý bởi công cụ gọi là registry
- Các thông tin hệ thống, thiết lập của người dùng, thông tin của phần mềm, các tùy chọn bảo mật và hởi động được lưu giữ trong các hive riêng biệt 
- Hệ điều hành Windows tạo ra các điểm phục hồi hệ thống (system restore point) trước khi thực hiện các thay đổi trên registry, tạo điều kiện phục hồi lại phiên bản registry trước đo nếu có sự cố xảy ra
___
# Quiz 

![[Pasted image 20250527153952.png]]![[Pasted image 20250527154024.png]]
![[Pasted image 20250527155443.png]]
![[Pasted image 20250527155715.png]]
![[Pasted image 20250527163244.png]]
![[Pasted image 20250527163300.png]]

**Chúc bạn 10 điểm**