> [!question]- Tiến trình là gì? Phân biệt với chương trình.
> - **Tiến trình (Process)** là một chương trình đang được thực thi. Nó là một thực thể *chủ động*.
> - **Chương trình (Program)** là một tập tin thực thi lưu trên ổ đĩa. Nó là một thực thể *bị động*.
> - Chương trình trở thành tiến trình khi được nạp vào bộ nhớ để thực thi.

> [!question]- Một tiến trình bao gồm những thành phần nào trong bộ nhớ?
> - **Text section**: Chứa mã chương trình (program code).
> - **Data section**: Chứa các biến toàn cục (global variables).
> - **Program counter (PC)** và các **thanh ghi (processor registers)**.
> - **Heap section**: Chứa bộ nhớ được cấp phát động trong quá trình thực thi.
> - **Stack section**: Chứa dữ liệu tạm thời như tham số hàm (function parameters), địa chỉ trả về (return address), và biến cục bộ (local variables).

> [!question]- Nêu các trạng thái của một tiến trình.
> - **New**: Tiến trình vừa được tạo.
> - **Ready**: Tiến trình đã có đủ tài nguyên cần thiết (trừ CPU) và sẵn sàng để chạy.
> - **Running**: Các lệnh của tiến trình đang được CPU thực thi.
> - **Waiting** (hay Blocked): Tiến trình đang chờ một sự kiện xảy ra (ví dụ: hoàn tất I/O, nhận tín hiệu).
> - **Terminated**: Tiến trình đã kết thúc thực thi.

> [!question]- Khối điều khiển tiến trình (PCB - Process Control Block) là gì và chứa những thông tin gì?
> - **PCB** là một cấu trúc dữ liệu quan trọng được hệ điều hành cấp phát cho mỗi tiến trình để lưu trữ thông tin về tiến trình đó.
> - Các thông tin chính trong PCB bao gồm:
>     - **Trạng thái tiến trình** (Process state): new, ready, running, waiting, terminated.
>     - **Bộ đếm chương trình** (Program counter - PC): Chỉ địa chỉ lệnh kế tiếp sẽ thực thi.
>     - **Các thanh ghi CPU** (CPU registers): Giá trị các thanh ghi cần lưu khi tiến trình bị ngắt.
>     - **Thông tin lập lịch CPU** (CPU scheduling information): Độ ưu tiên, con trỏ tới hàng đợi lập lịch.
>     - **Thông tin quản lý bộ nhớ** (Memory-management information): Thông tin về vùng nhớ cấp phát cho tiến trình.
>     - **Thông tin kế toán** (Accounting information): Lượng CPU đã sử dụng, giới hạn thời gian,...
>     - **Thông tin trạng thái I/O** (I/O status information): Danh sách thiết bị I/O cấp phát cho tiến trình, danh sách file đang mở,...

> [!question]- Tại sao cần định thời tiến trình? Mục tiêu của đa chương và chia thời là gì?
> - Cần định thời để quản lý việc thực thi luân phiên nhiều tiến trình trên CPU.
> - Mục tiêu của **Đa chương (Multiprogramming)**: Tối đa hóa hiệu suất sử dụng CPU bằng cách luôn giữ cho CPU bận rộn thực thi một tiến trình nào đó.
> - Mục tiêu của **Chia thời (Time-sharing)**: Giảm thiểu thời gian đáp ứng cho người dùng bằng cách chuyển đổi CPU giữa các tiến trình thường xuyên, cho phép người dùng tương tác với nhiều chương trình cùng lúc.

> [!question]- Nêu các loại hàng đợi định thời chính.
> - **Hàng đợi công việc (Job queue)**: Tập hợp tất cả các tiến trình trong hệ thống.
> - **Hàng đợi sẵn sàng (Ready queue)**: Tập hợp các tiến trình đang ở trong bộ nhớ chính, sẵn sàng và chờ được cấp CPU để chạy.
> - **Hàng đợi thiết bị (Device queue)**: Tập hợp các tiến trình đang chờ một thiết bị I/O cụ thể.

> [!question]- Phân loại các bộ định thời (scheduler).
> - **Bộ định thời dài (Long-term scheduler / Job scheduler)**: Chọn tiến trình từ Job queue để nạp vào Ready queue (quyết định tiến trình nào được đưa vào hệ thống).
> - **Bộ định thời ngắn (Short-term scheduler / CPU scheduler)**: Chọn tiến trình từ Ready queue để cấp phát CPU.
> - **Bộ định thời trung gian (Medium-term scheduler)** (tùy chọn): Có thể tạm thời đưa tiến trình ra khỏi bộ nhớ (swap out) để giảm mức độ đa chương hoặc đưa trở lại (swap in) khi cần.

> [!question]- Chuyển ngữ cảnh (Context Switch) là gì?
> - Là quá trình hệ điều hành lưu trạng thái của tiến trình đang chạy hiện tại (lưu vào PCB của nó) và nạp trạng thái của một tiến trình khác (từ PCB của tiến trình đó) để CPU bắt đầu thực thi tiến trình mới.
> - Chuyển ngữ cảnh là hao phí (overhead) vì trong quá trình này CPU không thực hiện công việc hữu ích nào.

> [!question]- Tiến trình được tạo ra như thế nào trong UNIX/Linux? Hàm `fork()` và `exec()` dùng để làm gì?
> - Tiến trình mới thường được tạo bởi một tiến trình đang tồn tại (tiến trình cha) thông qua system call `fork()`.
> - **`fork()`**: Tạo ra một tiến trình mới (tiến trình con) là bản sao gần như hoàn chỉnh của tiến trình cha (sao chép không gian địa chỉ, mã nguồn, biến...).
>     - Trả về giá trị > 0 cho tiến trình cha (là PID của con).
>     - Trả về 0 cho tiến trình con.
>     - Trả về < 0 nếu có lỗi.
> - **`exec()`** (họ hàm): Nạp một chương trình mới vào không gian bộ nhớ của tiến trình gọi nó. Mã và dữ liệu của tiến trình hiện tại bị ghi đè bởi chương trình mới. Thường được gọi bởi tiến trình con sau khi `fork()` để chạy một chương trình khác.

> [!question]- Tiến trình kết thúc như thế nào?
> - **Tự kết thúc**: Tiến trình thực hiện xong lệnh cuối cùng và yêu cầu hệ điều hành xóa nó thông qua system call `exit()`.
> - **Bị kết thúc bởi tiến trình khác**: Một tiến trình (thường là cha hoặc có đủ quyền) yêu cầu hệ điều hành kết thúc một tiến trình khác thông qua system call như `abort()` hoặc `kill()`, cung cấp PID của tiến trình cần kết thúc.
> - Khi tiến trình kết thúc, hệ điều hành thu hồi tài nguyên đã cấp phát cho nó.

> [!question]- Giao tiếp liên tiến trình (IPC - Inter-Process Communication) là gì? Có những mô hình IPC nào?
> - **IPC** là cơ chế do hệ điều hành cung cấp để các tiến trình có thể giao tiếp và đồng bộ hóa hoạt động với nhau.
> - Hai mô hình IPC chính:
>     - **Shared Memory (Bộ nhớ chia sẻ)**: Các tiến trình chia sẻ một vùng nhớ chung. Việc đọc/ghi vào vùng nhớ này do các tiến trình tự quản lý và cần cơ chế đồng bộ.
>     - **Message Passing (Truyền thông điệp)**: Các tiến trình trao đổi thông tin bằng cách gửi và nhận các thông điệp qua kênh giao tiếp do HĐH quản lý (có thể trực tiếp hoặc gián tiếp qua mailbox/port).

> [!question]- Tiểu trình (Thread) là gì?
> - **Tiểu trình** là một đơn vị cơ bản của việc sử dụng CPU trong một tiến trình.
> - Mỗi tiểu trình có:
>     - Thread ID
>     - Program Counter (PC) riêng
>     - Tập thanh ghi (Registers) riêng
>     - Ngăn xếp (Stack) riêng
> - Các tiểu trình trong cùng một tiến trình chia sẻ chung:
>     - Vùng mã (Code section)
>     - Vùng dữ liệu (Data section)
>     - Các tài nguyên của HĐH như file đang mở, tín hiệu.

> [!question]- Nêu các lợi ích của lập trình đa tiểu trình (Multithreading).
> - **Đáp ứng nhanh (Responsiveness)**: Cho phép chương trình tiếp tục chạy (ví dụ: cập nhật UI) ngay cả khi một phần của nó bị chặn (ví dụ: đang chờ I/O).
> - **Chia sẻ tài nguyên (Resource Sharing)**: Các tiểu trình chia sẻ bộ nhớ và tài nguyên của tiến trình cha, hiệu quả hơn tạo tiến trình mới.
> - **Kinh tế (Economy)**: Tạo và chuyển đổi giữa các tiểu trình thường nhanh và tốn ít tài nguyên hơn so với tiến trình.
> - **Khả năng mở rộng (Scalability)**: Có thể tận dụng kiến trúc đa lõi (multicore) để thực thi song song các tiểu trình.

> [!question]- Phân biệt Thực thi đồng thời (Concurrency) và Thực thi song song (Parallelism).
> - **Thực thi đồng thời (Concurrency)**: Hệ thống quản lý nhiều tác vụ cùng một lúc, cho phép chúng tiến triển xen kẽ (interleaving) trên một lõi CPU duy nhất. Tạo cảm giác các tác vụ chạy song song.
> - **Thực thi song song (Parallelism)**: Hệ thống có thể thực hiện nhiều tác vụ *thực sự* cùng một thời điểm, thường yêu cầu phần cứng có nhiều đơn vị xử lý (đa lõi).

> [!question]- Phân loại tiểu trình dựa trên nơi quản lý.
> - **Tiểu trình người dùng (User Threads)**: Được quản lý bởi thư viện tiểu trình ở tầng người dùng, không cần sự can thiệp trực tiếp của nhân HĐH. Nhanh chóng tạo và quản lý, nhưng nếu một tiểu trình bị chặn bởi system call, toàn bộ tiến trình có thể bị chặn.
> - **Tiểu trình hạt nhân (Kernel Threads)**: Được hỗ trợ và quản lý trực tiếp bởi nhân hệ điều hành. Tạo và quản lý chậm hơn user thread, nhưng nếu một tiểu trình bị chặn, nhân có thể lập lịch cho tiểu trình khác trong cùng tiến trình (hoặc tiến trình khác) chạy.

> [!question]- Nêu các mô hình đa tiểu trình phổ biến.
> - **Nhiều-Một (Many-to-One)**: Nhiều user thread ánh xạ vào một kernel thread duy nhất. Hiệu quả nhưng nếu một user thread bị block thì toàn bộ tiến trình bị block.
> - **Một-Một (One-to-One)**: Mỗi user thread ánh xạ tới một kernel thread riêng. Cung cấp tính song song tốt hơn nhưng có thể tốn nhiều tài nguyên kernel thread. (Ví dụ: Linux, Windows).
> - **Nhiều-Nhiều (Many-to-Many)**: Ánh xạ nhiều user thread tới một số lượng kernel thread nhỏ hơn hoặc bằng. Kết hợp ưu điểm của hai mô hình trên nhưng phức tạp hơn để cài đặt. Cho phép HĐH tạo đủ số lượng kernel thread cần thiết.