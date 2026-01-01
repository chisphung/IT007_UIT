> [!question]- Hệ điều hành là gì?  
> Hệ điều hành là chương trình trung gian giữa phần cứng máy tính và người dùng, có nhiệm vụ **điều khiển**, **phối hợp** việc sử dụng các tài nguyên hệ thống và **cung cấp** các dịch vụ cơ bản cho các ứng dụng.

> [!question]- Mục tiêu chính của hệ điều hành là gì?  
> Mục tiêu là giúp người dùng dễ dàng sử dụng hệ thống và quản lý, cấp phát tài nguyên hiệu quả, từ đó tối ưu hóa hiệu suất hoạt động của máy tính.

> [!question]- Cấu trúc cơ bản của hệ thống máy tính gồm những thành phần nào?  
> - **Phần cứng:** CPU, bộ nhớ, thiết bị I/O  
> - **Hệ điều hành:** Quản lý, phân phối tài nguyên và điều phối các hoạt động  
> - **Chương trình ứng dụng:** Sử dụng tài nguyên để giải quyết các bài toán cụ thể  
> - **Người dùng:** Bao gồm con người, máy móc và các máy tính khác

> [!question]- Kernel trong hệ điều hành là gì?  
> Kernel là chương trình luôn chạy tại mọi thời điểm, chịu trách nhiệm quản lý tài nguyên, xử lý ngắt và điều phối các hoạt động của hệ thống.

> [!question]- Phân loại chương trình đi kèm với kernel?  
> - **Chương trình hệ thống:** Đóng gói cùng hệ điều hành nhưng không phải là một phần của kernel.  
> - **Chương trình ứng dụng:** Các chương trình không liên kết trực tiếp với hoạt động của hệ thống.

> [!question]- Ngắt (interrupt) là gì và có đặc điểm gì?  
> Ngắt là tín hiệu từ phần cứng hoặc phần mềm yêu cầu CPU dừng công việc đang làm để xử lý một tác vụ khẩn.  
> Đặc điểm:  
> - Sử dụng bảng vector để điều hướng đến ISR  
> - Lưu lại địa chỉ chương trình bị ngắt  
> - Kích hoạt do lỗi, người dùng hoặc phần cứng

> [!question]- Các tiêu chí trong tổ chức cấu trúc lưu trữ máy tính là gì?  
> - **Tốc độ truy xuất**  
> - **Chi phí**  
> - **Khả năng lưu trữ khi mất điện**

> [!question]- Đặc điểm của bộ nhớ chính là gì?  
> - Dung lượng lớn  
> - Truy xuất trực tiếp bởi CPU (Random Access)  
> - Mất dữ liệu khi mất nguồn  
> - Sử dụng công nghệ DRAM

> [!question]- Vai trò của secondary storage là gì?  
> Lưu trữ dữ liệu lâu dài khi mất nguồn điện, mặc dù có tốc độ chậm hơn main memory.

> [!question]- Hệ điều hành hoạt động ở những chế độ nào?  
> - **User mode:** Mã người dùng thực thi, hạn chế quyền  
> - **Kernel mode:** Mã hệ thống thực thi, quyền truy cập đầy đủ tài nguyên

> [!question]- Sự khác biệt giữa hệ thống đơn bộ xử lý và đa bộ xử lý?  
> - **Đơn bộ xử lý:** Một CPU, xử lý một tiến trình tại một thời điểm  
> - **Đa bộ xử lý:** Nhiều CPU hoặc nhiều lõi, xử lý đồng thời nhiều tiến trình

> [!question]- Các loại hệ thống đa bộ xử lý phổ biến là gì?  
> - **Bất đối xứng:** Mỗi CPU làm việc khác nhau  
> - **Đối xứng (SMP):** Các CPU đồng đều, chia sẻ công việc  
> - **Gom cụm (cluster):** Nhiều máy hoạt động như một hệ thống chung
