> [!question]- Các thành phần của hệ điều hành là gì?  
> - **Quản lý tiến trình (Process Management)**  
> - **Quản lý bộ nhớ chính (Main Memory Management)**  
> - **Quản lý file (File Management)**  
> - **Quản lý hệ thống I/O (I/O System Management)**  
> - **Quản lý lưu trữ thứ cấp (Secondary Storage Management)**  
> - **Bảo vệ hệ thống (Protection System)**  
> - **Hệ thống thông dịch lệnh (Command-Interpreter System)**

> [!question]- Quản lý tiến trình là gì?  
> - Tạo, huỷ, tạm dừng, tiếp tục các tiến trình.  
> - Cung cấp cơ chế đồng bộ, giao tiếp giữa các tiến trình.  
> - Quản lý tắc nghẽn và phân bổ CPU cho tiến trình.

> [!question]- Quản lý bộ nhớ chính là gì?  
> - Theo dõi bộ nhớ được sử dụng và chưa sử dụng.  
> - Cấp phát và thu hồi bộ nhớ khi cần.  
> - Quyết định chương trình nào được nạp khi có vùng nhớ trống.

> [!question]- Quản lý file là gì?  
> - Quản lý các thao tác với file/thư mục: tạo, xoá, đọc, ghi.  
> - Tổ chức dữ liệu và ánh xạ vào thiết bị lưu trữ.  
> - Hỗ trợ sao lưu và phục hồi dữ liệu.

> [!question]- Quản lý hệ thống I/O là gì?  
> - Cung cấp giao diện trừu tượng giữa phần mềm và thiết bị.  
> - Gồm: buffering, caching, spooling, điều khiển thiết bị I/O.  
> - Che giấu sự khác biệt giữa các thiết bị phần cứng.

> [!question]- Quản lý lưu trữ thứ cấp là gì?  
> - Quản lý không gian trống, cấp phát và lên lịch truy xuất đĩa.  
> - Đảm bảo dữ liệu được lưu trữ và truy xuất hiệu quả.

> [!question]- Hệ thống bảo vệ là gì?  
> - Ngăn chặn truy cập trái phép tài nguyên hệ thống.  
> - Gồm: xác thực người dùng, phân quyền, và bảo vệ bộ nhớ.

> [!question]- Hệ thống thông dịch lệnh là gì?  
> - Giao diện giữa người dùng và hệ điều hành.  
> - Ví dụ: shell, GUI, dòng lệnh (CLI), màn hình cảm ứng.

> [!question]- Hệ điều hành cung cấp những dịch vụ nào?  
> - Thực thi chương trình  
> - Thao tác I/O  
> - Quản lý file  
> - Giao tiếp giữa các tiến trình  
> - Phát hiện và xử lý lỗi  
> - Cấp phát tài nguyên  
> - Ghi nhận sử dụng hệ thống  
> - Bảo vệ và an ninh  
> - Giao diện người dùng

> [!question]- System Call là gì?  
> - Giao diện giữa chương trình người dùng và hệ điều hành.  
> - Cho phép chương trình yêu cầu dịch vụ từ hệ điều hành.  
> - Có 3 cách truyền tham số: qua thanh ghi, bộ nhớ, stack.

> [!question]- API là gì?  
> - Giao diện lập trình ứng dụng cung cấp bởi hệ điều hành.  
> - Ví dụ: Win32 API, POSIX API, Java API.  
> - Cho phép lập trình viên viết chương trình không phụ thuộc vào OS cụ thể.

> [!question]- Phân loại chương trình đi kèm với kernel?  
> - **Chương trình hệ thống:** Đóng gói cùng hệ điều hành nhưng không phải là một phần của kernel.  
> - **Chương trình ứng dụng:** Các chương trình không liên kết trực tiếp với hoạt động của hệ thống.

> [!question]- Các cấu trúc hệ điều hành phổ biến là gì?  
> - **Monolithic:** Toàn bộ OS nằm trong một khối kernel (UNIX).  
> - **Layered:** Chia nhiều lớp, mỗi lớp chỉ giao tiếp với lớp gần kề.  
> - **Microkernel:** Chỉ giữ các chức năng tối thiểu, phần còn lại chạy ở user mode (Mach).  
> - **Module:** Có thể nạp hoặc gỡ từng thành phần độc lập (Linux, Solaris).  
> - **Hybrid:** Kết hợp các mô hình trên, ví dụ Windows.

