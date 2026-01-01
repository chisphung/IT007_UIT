Xem lại CPU Bound
IO Bound 
Các lưu đồ 
ĐỊnh thời tiểu trình
- A CPU-bound process requires more CPU time or spends more time in the running state. 
- An I/O-bound process requires more I/O time and less CPU time. An I/O-bound process spends more time in the waiting state.
# Các bộ định thời 
## Long-term scheduling (Job scheduler)
- Xác định chương trình nào được chấp nhận nạp vào hệ thống để thực thi 
- Điều khiển mức độ đa chương của hệ thống 
- Long-term scheduler thường cố gắng duy trì xen lẫn giữa CPU bound và IO bound process 
## Medium-term scheduling 
- Process nào được swap in, swap out khỏi bộ nhớ chính 
- Đước thực hiện bởi phần quản lý bộ nhớ và được thảo luận ở phần quản lý bộ nhớ
## Short-term scheduling (CPU Scheduler)
- Xác định process nào trong ready queue sẽ được chiếm CPU để thực thi kế tiếp (còn được gọi là CPU Scheduling)
- Bộ định thời ngắn được gọi mỗi khi có một trong các sự kiện/ngắt xảy ra:
	- Ngắt thời gian
	- Ngắt ngoại vi 
	- Lời gọi hệ thống 
	- Signal
# Bộ định thời 
- Bộ định thời sẽ chuyển quyền điều khiển CPU về cho process được chọn 
- Bao gồm: 
	- Chuyển ngữ cảnh 
	- Chuyển chế độ người dùng 
	- Nhảy đến vị trí thích hợp trong chương trình ứng dụng để khởi động lại chương tình (là PC trong PCB)
- Công việc này gây ra phí tổn
	- Dispatch latency: thời gian mà bộ định thời dừng một process và khởi động một process khác
# Các tiêu chuẩn định thời 
## Hướng người dùng
- Thời gian đáp ứng - Cực đại
- Thời gian hoàn thành -> Cực tiểu
- Thời gian chờ -> Cực tiểu
## Hướng hệ thống
- Tận dụng CPU (Processor utilization): càng bận càng tốt -> cực đại
- Công bằng (fairness): tất cả process phải được đối xử như nhau
- Thông lượng (throughput): số process hoàn tất công việc trong một đơn vị thời gian -> Cực đại
# Yếu tố của giải thuật định thời 
- Hàm chọn lựa: dùng để chọn process nào trong ready queue được thực thi 
- Chế độ quyết định: chọn thời điểm thực thi hàm chọn lựa để định thời
	- Trưng dụng
	- Không trưng dụng
- Service time = burst time: thời gian process cần CPU 
# Giải thuật 
## FCFS
## SJF
- Process có CPU burst lớn sẽ đói nếu có nhiều Process có CPU Burst nhohr 
- Non preemptive không phù hợp với hệ thống timesharing
- Ngầm định đưa ra độ ưu tiên theo burst time 
- CPU Bound có độ ưu tiên thấp hơn so với IO Bound, nhưng khi một process không thực hiện IO được thực thi thì nó độc chiếm CPU cho đến khi kết thúc
- Một kỹ thuật thường được sử dụng để đo burst time là dùng hàm mũ
## Priority 
- Trì hoãn vô hạn định, đói
- Giả pháp: làm mới - độ ưu tiên của process sẽ tang theo thời gian
## Round robin
- Nếu q lớn: RR -> FCFS
- Nếu q nhỏ: tốn phí chuyển ngữ cảnh
- Thời gian đợi trung bình của giải thuật RR khá lớn
- Thời gian TaT cao hơn SJF nhưng có thời gian đáp ứng trung bình tốt hơn 
- Ưu tiên: CPU bound process
	- Ví dụ: Một IO bound process sử dụng CPU trong thời gian ngắn hơn  quantum time và bị Blocked để đợi IO 
	- Một CPU bound process chạy hết time slice và quay trở về hàng đợi ready queue 
- Thời gian hoàn thành trung bình không chắc được cải thiện khi quantum time lớn
- RR sử dụng một giả thiết ngầm là tất cả các process đều có tầm quan trọng ngang nhau
	- Không thể sử dụng RR nếu muốn các process có độ ưu tiên khác nhau
## Highest Response Ratio Next
- Chọn process kế tiếp có Response Ratio lớn nhất 
- Các process ngắn được ưu tiên 
- $$RR = \frac{waiting + burst}{burst}$$
## Multilevel Queue 
- Ready queue được chia thành nhiều hàng đợi riêng biệt thoe: 
	- Đặc điểm và yêu cầu định thời 
	- Foreground và background process
- Process được gán cố định vào một hàng đợi, mỗi hàng đợi sử dụng giải thuật định thời riêng
- Hệ điều hành cần phải định thời cho các hàng đợi: 
	- Fixed priority scheduling: phục vụ từ hàng đợi có độ ưu tiên cao đến thâp--> starvation
	- Timeslice: mỗi hàng đợi được nhân một khoảng thời gian chiếm CPU và phân phối cho các process trong hàng đợi khoảng thời gian đó. Ví dụ 80% cho hàng đợi foreground sử dụng RR và 20% cho background sử dụng FCFS
## Multilevel Feedback Queue
- Cho phép process di chuyển giữa các hàng đơi khác nhau
- Phân loại process dựa trên các đặc tính về CPU burst
- Sử dụng chế độ **trưng dụng**
- sau một khoảng thời gian nàu đó, IO Process và background process sẻ ở các hàng đợi có độ ưu tiên cao hơn, còn CPU bound process sẽ ở các queue có độ ưu tiên thấp hơn 
- Một process đã chờ quá lâu ở một hàng đợi có độ ưu tiên thấp có thể được chuyển đến hàng đợi có độ ưu tiên cao hơn (aging)
- Vấn đề: 
	- Số lượng hàng đợi
	- Giải thuật
	- Thời điểm chuyển đến hàng đợi khác
	- Đưa vào hàng đợi nào là hợp lý