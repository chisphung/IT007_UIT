	Bộ định thời CPU giúp sắp xếp công việc cho CPU
	
![[Pasted image 20250409180733.png]]
References, Bộ định thời ngắn, dài trung  [[Hệ điều hành/Summarization/Chương 3/0 - Main|0 - Main]]
## Định thời dài (Long-term scheduling)
	Còn được gọi là job scheduler, sắp xếp công việc cho toàn bộ hệ thống 
- Xác định chương trình nào dược chấp nhận nạp vào hệ thống để thực thi 
--> **Điều khiển mức độ đa chương của hệ thống** 
- Định thời dài thường cố gắng duy trì xem lẫn giữa tiến trình hướng CPU và tiến trình hướng IO
- **Controls the degree of multiprogramming – the more processes that are created, the smaller the percentage of time that each process can be executed**
## Định thời vừa (Medium-term scheduling)
- Định thời vừa quyết định tiến trình nào được đưa vào và đưa ra khỏi bộ nhớ chính trong quá trình thực thi của hệ thống 
- Được thực hiện bởi thành phẩn quản lý bộ nhớ (Reference [Quản lý bộ nhớ])
- **Swapping-in decisions are based on the need to manage the degree of multiprogramming – considers the memory requirements of the swapped-out processes**
## Định thời ngắn (Short-term scheduling)
- **Còn được gọi là định thời CPU**
- Xác định tiến trình nào trong ready queue sẽ được chiếm CPU để thực thi kế tiếp 
- ĐỐi với hệ thống hỗ trợ đa luông (multithreaded kernel), việc định thời CPU là do OS chọn kernel thread được chiếm CPU 
- Bộ định thời ngắ được gọi khi có một trong các sự kiện/interupt sau xảy ra
	- Clock interrupt (ngắt thời gian)
	- IO interrupt
	- Operating system call
	- Tín hiệu đông bộ hóa( Ref: [[Chương 5 - Đồng bộ tiến trình]])
- Bộ ddinnhj thời sẽ chuyển quyền điều khiển CPU cho tiến trình được chọn
- Quá trình chuyển đổi bao gồm 
	- Context switching (ref: [[Hệ điều hành/Summarization/Chương 3/0 - Main|0 - Main]])
	- Chuyển usermode
	- Nhảy đến vị trí thích hợp trong chương trình ứng dụng để khởi động lại chương trình (sử dụng thông tin địa chỉ tại PC trong PCB)
- Công việc này gây ra phí tổn: 
	- Dispatch latency: thời gian mà bộ định thời dừng lại một tiến trình và khởi động một tiến trình khác

|**Type of Scheduler**|**When It Runs**|**Main Role**|**Who/What It Manages**|**Level in OS**|**Frequency**|**Performance Goal**|
|---|---|---|---|---|---|---|
|**Long-term (Dài)**|Before execution|Chooses _which_ programs/processes to admit to system|Manages new jobs entering the system|High-level scheduling|Infrequent|Controls degree of multiprogramming, balance CPU-bound & IO-bound|
|**Medium-term (Vừa)**|During execution|Swaps processes in/out of memory|Suspended processes (swapping)|Memory management|Occasional|Manage memory usage, reduce load|
|**Short-term (Ngắn)**|Frequently (every interrupt/time slice)|Chooses _which_ ready process gets CPU next|Ready queue (kernel threads in multithreaded kernel)|Low-level, CPU-focused|Very frequent|Maximize CPU usage, responsiveness|