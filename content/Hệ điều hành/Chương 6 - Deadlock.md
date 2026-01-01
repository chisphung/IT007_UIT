---
share_link: https://share.note.sx/r5q1mb91#EYZG4X86fm7ok0nWA/dwrrY2Vagbdq8iU4BwEz4LyLQ
share_updated: 2025-04-28T12:25:11+07:00
---
	Một tiến trình được gọi là deadlock nếu nó đang đợi một sự kiên mà sẽ không bao giờ xảy ra 

Thông thường, có nhiều hơn một tiến trình bị liên quan trong một deadlock 
Một tiến trình gọi là trì hoãn vô hạn định nếu nó bị trình hoãn trong một khoảng thời gian dài lặpđi lặp lại trong khi hệ thốngđáp ứng cho những tiến trình khác
	Ví dụ: Một tiến trình sẵn sàng để xử lý nhưng nó không bao giờ nhận được CPU
## Vấn đề Deadlock
### Điều kiện cần để xảy ra deadlock
- **Mutual exclusion:** ít nhất một tài nguyên được giữ theo nonshareable mode
	- Ví dụ: Máy in không phải là loại tài nguyên sharable
- **Giữ và chờ cấp thêm tài nguyên:** Một tiến trình đang giữ ít nhất một tài nguyên và đợi thêm tài nguyên do tiến trình khác giữ
- **Không trưng dụng**: tài nguyên không thể bị lấy lại mà chỉ có thể được trả lại từ tiến trình đang giữ tài nguyên đó khi nó muốn
- **Chu trình đợi**: tồn tại một tập (P0,....,Pn) các tiến trình đang đợi sao cho:
	- P0 đợi một tài nguyên mà  P1 giữ 
	- P1 đợi một tài nguyên mà P2 giữ
	- ...
	- Pn đợi một tài nguyên mà P0 giữ
	
 ![[Pasted image 20250414231203.png]]

## Mô hình hóa hệ thống
- Các tài nguyên, kí hiệu R1, R2,... Rm bao gồm: 
	- CPY cycle, không gian bộ nhớ, thiết bị IO, file, semaphore
	- Mỗi loại tài nguyen Ri có Wi thực thể
- Giải sử tài nguyên tái sử dụng theo chu kỳ: 
	- Yêu cầu: tiến trình phải chờ nếu yêu cầu không được đáp ứng ngay
	- Sử dụng: tiến trình sử dụng tài nguyên
	- Hoàn trả: tiến trìn  h hoàn trả tài nguyên
- Các tác vụ yêu cầu và hoàn trả đều là system call
	- Ví dụ:
		- Request/release device
		- Open/close file
		- Allocate/free memory
		- Wait/signal

### Đồ thị cấp phát tài nguyên RAG
- Là đồ thị có hướng, với tập đỉnh V và tập cạnh E
	- Tập đỉnh V gồm 2 loại:
		- P, R
	- Tập cạnh E gồm 2 loại: 
		- Cạnh yêu cầu: Pi -> Rj
		- Cạnh cấp phát Rj -> Pi
![[Pasted image 20250414231618.png]]
### Mối liên hệ giữa RAG và deadlocks 
- RAG không chứa chu trình --> Không có deadlock 
- RAG chứa một (hay nhiều) chu trình 
	- Nếu mỗi loại tài nguyên chỉ có một thực thể --> Deadlock 
	- Nếu mỗi loại tài nguyên có nhiều thực thể --> Có thể xảy ra deadlock 
### Các ví dụ
#### Ví dụ 1: 
	Cho một hệ thống có 3 tiến trình P1 đến P3 và 4 loại tài nguyên R1(1), R2(2), R3(1) và R4(4)
	P1 giữ 1 R2 và yêu cầu 1 R1; P2 giữ 1 R2, 1 R1 và yêu cầu 1 R3; P3 giữ 1 R3

![[Pasted image 20250414231745.png]]
#### Đồ thị cấp phát tài nguyên với một deadlock
- P2 đang giữ R2 và cần R3 để thực hiện (khi thực hiện xong, P2 release thì mới có R2 và R3 cho P3 thực hiên)
- Tuy nhiên, P3 đang giữ R3 và yêu cầu R2 để thực hiện 
- P2 yêu cầu R3
- P3 yêu cầu R2 
- --> Deadlock
![[Pasted image 20250414231814.png]]
#### Đồ thị chứa chu trình nhưng không xảy ra deadlock
![[Pasted image 20250414231837.png]]
#### RAG và deadlock
- ==RAG không chứa chu trình --> không có deadlock==
- ==RAG chứa một hay nhiều chu trình:== 
	- ==Nếu mỗi loại tài nguyên chỉ có một thực thỉ --> Deadlock==
	- ==Nếu mỗi loại tài nguyên có nhiều thực thể --> Có thể xảy ra deadlock==

#### Bài tập 1:
Cho 1 hệ thống có 4 tiến trình P1 đến P4 và 3 loại tài nguyên R1 (3), R2 (2) R3 (2). P1 giữ 1 R1 và yêu cầu 1 R2; P2 giữ 2 R2 và yêu cầu 1 R1 và 1 R3; P3 giữ 1 R1 và yêu cầu 1 R2; P4 giữ 2 R3 và yêu cầu 1 R1.

• Vẽ đồ thị tài nguyên cho hệ thống này?

• Deadlock?

• Chuỗi an toàn? (nếu có)

## Các phương pháp giải quyết deadlock
1. ==**Ngăn deadlock:** không cho phép (ít nhất) một trong 3 điều kiện cần cho deadlock==
2. ==**Tránh deadlock:** các tiến trình cần cung cấp thông tin về tài nguyên nó cần để hệ thống cấp phát tài nguyên môt cách thích hợp== 
3. ==Cho phép hệ thống vào trạng thái deadlock, nhưng sau đó **phát hiện deadlock và phục hồi hệ thống**==
4. ==Bỏ qua mọi vấn đề, xem như deadlock không bao giờ xảy ra trong hệ thống  (được sử dụng nhiều nhất trong các cơ chế trên window và Linux, nếu xảy ra deadlocks cần khởi động lại máy)==
	==--> Deadlock không được phát hiện, dẫn đến việc giảm hiệu suất của hệ thống. Cuối cùng, hệ thống có thể ngừng hoạt dộng d và phải khởi động lại==
### Ngăn deadlock
Ngăn deadlock bằng cách ngăn một trong 4 điều kiện cần của deadlock:
- **Ngăn mutual exclusion**: 
	- Đối với tài nguyên không chia sẻ (printer): không làm được, do máy in nếu như cho phép nhiều người dùng thực hiện cùng lúc có thể gây ra lôi
	- Đối với tài nguyên chia sẻ (read-only file): không cần thiết 
- **Hold and wait** 
	- Cách 1: Mỗi tiến trình yêu cầu toàn bộ tài nguyên cần thiết một lần. Nếu có đủ tài nguyên thì hệ thống sẽ cấp phát, nếu không đủ tài nguyên thì tiến trình phải bị block
	- Cách 2: Khi yêu cầu tài nguyên, tiến trình không được giữ tài nguyên nào. Nếu đang không có thì phải trả lại trước khi yêu cầu
	- Không thực tế, do tiến trình khó có thể dự đoán được lượng tài nguyên sẽ dùng
- **Ngăn no preemption**: Nếu tiến trình A có giữ tài nguyên và đang yêu cầu tài nguyên khác nhưng tài nguyên này chưa được cấp phát ngay thì: 
	- **Cách 1**: Hệ thống lấy lại mọi tài nguyên mà A đang giữ:
		- A chỉ bắt đầu lại được khi có được các tài nguyên đã bị lấy lại cùng với tài nguyên đang yêu cầu
	- **Cách 2:** hệ thống sẽ xem tài nguyên mà A yêu cầu: 
		- Nếu tài nguyên được giữa bởi một tiến trình khác đang đợi thêm tài nguyên, tài nguyên này được hệ thống lấy lại và cấp phát cho A
		- Nếu tài nguyên được giữ bởi tiến trình không đợi tài nguyên, A phải đợi và tài nguyên của A bị lấy lại. Tuy nheien hệ thống chỉ lấy lại các tài nguyên mà tiến trình khác yêu cầu
	- Nguy hiểm: Nếu như A đang thực hiện một tiến trình quan trọng nhưng bị lấy lại, có thể gây ra lỗi chương trình
- **Ngăn chu trình đợi**: gán một thứ tự cho tất cả các tài nguyên trong hệ thống
	- Tập hợp tài nguyên R = {R1, R2, R3,..., Rn}
		- Hàm ánh xạ F: R-> N
	- Ví dụ F(file) = 1, F(disk) = 5, F(printer) = 12
		- F là hàm định nghĩa thứ tự trên tập các loại tài nguyên
	- Mỗi tiến trình chỉ có thể yêu cầu thực thể của một loại tài nguyên theo thứ tự tăng dần (định nghĩa bởi hàm F) của loại tài nguyên
	- **Ví dụ**
		- Chuỗi yêu cầu thực thể hợp lệ file -> disk -> printer
		- Khi một tiến trình yêu cầu một thực thể của loại tài nguyên Rj thì nó phải trả lại các tài nguyên Ri với F(Ri) > R(Rj)
	- Là cách hợp lý nhất, trước khi thực hiện, hệ thống chạy qua một thuật toán để kiểm tra có an toàn không, có chu trình đợi hay không rồi mới cho phép thực hiện
### Tránh deadlock
- Ngăn deadlock sử dung tài nguyên không hiệu quả 
- Tránh deadlock vẫn đảm bảo hiệu suất sử dụng tài nguyên tối đa đến mức có thể 
- Yêu cầu mỗi tiến trình khai báo số lượng tài nguyên tối đa cần để thực hiện công việc 
- Giải thuật tránh deadlock sẽ kiểm tra trạng thái cấp tài nguyên để đảm bảo hệ thống không rơi vào deadlock 
- Trạng thái cấp phát tài nguyên được định nghĩa dựa trên số tài nguyên còn lại, số tài nguyên đã được cấp phát và yêu cầu tối đa của các tiến trình 

#### Trạng thái safe và unsafe 
- Một trạng thái của hệ thống được gọi là safe nếu tồn tại một chuỗi thứ tự an toàn 
- Một chuỗi tiến trình <P2, P2,..., Pn> là một chuỗi an toàn nếu 
	-  Với mọi i = 1,...., n yêu cầu tối đa về tài nguyên của Pi có thể được thỏa bởi 
		- tài nguyên mà hệ thống đang có sẵn sàng
		- Cùng với tài nguyên mà tất cả các Pj (j<i) đang giữ
- Một trạng thái của hệ thống được gọi là unsafe nếu không tồn tại một chuỗi an toàn
- Nếu hệ thống đang ở trạng thái safe -> Không deadlock 
- Nếu hệ thống đang ở trạng thái unsafe -> có thể dẫn đến deadlock 
- Tránh deadlock bằng cách đảm bảo hệ thống không đi đến trạng thái unsafe 
![[Pasted image 20250518202608.png]]
#### Các giải thuật tránh deadlock 
- Mỗi tài nguyên chỉ có một thực thể 
	- Giải thuật đồ thị cấp phát tài nguyên 
- Mỗi tài nguyên có nhiều thực thể 
	- Giải thuật banker
##### Giải thuật Banker: 
ref: [[Giải thuật Banker]]
- Mỗi loại tài nguyên có nhiều thực thể 
- Bắt chước nghiệp vụ ngân hàng 
- Điều kiện 
	- Mỗi tiến trình phải khai báo số lượng thực thể tối đa của mỗi loại tài nguyên mà nó cần 
	- Khi tiến trình yêu cầu tài nguyên thì có thể phải đợi 
	- Khi tiến trình đã có được đầy đủ tài nguyên thì phải hoàn toàn trả trong một khoảng thời gian hữu hạn nào đó
**Cấu trúc dữ liệu cho giải thuật Banker**

n: số tiến trình; m: số loại tài nguyên 
- Available: vector độ dài m 
- Max: ma trận n x m 
- Allocation: ma trận n x m
- Need: ma trận n x m

**Giải thuật an toàn**

1. Gọi Work và Finish là hai vector độ dài là m và n. Khởi tạo
	- Work = Available
	- Finish[i] = false, i = 0, 1, …, n-1
2. Tìm i thỏa 
	- Finish[i] = false
	- Needi ≤ Work (hàng thứ i của Need)
	- Nếu không tồn tại i như vậy, đến bước 4
3. Work = Work + Allocation_i
	- Finish[i] = true
	- quay về bước 2
4. Nếu Finish[i] = true, i = 1,..., n, thì hệ thống đang ở trạng thái safe

**Ví dụ**

![[Pasted image 20250518203512.png]]

**Giải thuật yêu cầu tài nguyên cho tiến trình Pi**

ref: [[Giải thuật yêu cầu tài nguyên]]
Request_i là request vector của Process Pi
Request_i[j] = k <-> Pi cần k instance của tài nguyên Rj
1. Nếu Requesti ≤ Needi thì đến bước 2. Nếu không, báo lỗi vì tiến trình đã vượt yêu cầu tối đa.
2. Nếu Requesti ≤ Available thì qua bước 3. Nếu không, Pi phải chờ vì tài nguyên không còn đủ để cấp phát.
3. Giả định cấp phát tài nguyên đáp ứng yêu cầu của Pi bằng cách cập nhật trạng thái hệ thống như sau:
	- Available = Available – Requesti
	- Allocationi = Allocationi + Requesti
	- Needi = Needi – Requesti

- Áp dụng giải thuật kiểm tra trạng thái an toàn lên trạng thái trên hệ thống mới 
	- Nếu trạng thái safe thì tài nguyên được cấp thực sự cho Pi
	- Nếu trạng thái unsafe thì Pi phải đợi và phục hồi trạng thái: 
		- Available = Available + Requesti
		- Allocationi = Allocationi - Requesti
		- Needi = Needi + Requesti
**Ví dụ**

![[Pasted image 20250518203825.png]]

## Các phương pháp giải quyết deadlock 
### Phát hiện deadlock 
- Chấp nhận xảy ra deadlock trong hệ thống 
- Giải thuật phát hiện deadlock 
- Cơ chế phục hồi 
==**Mỗi loại tài nguyên chỉ có một thực thể**==
- ==Sử dụng wait-for graph== 
	- ==Các Node là các tiến trình== 
	- ==Pi -> Pj nếu Pi chờ tài nguyên từ Pj==
- ==Mỗi giải thuật kiểm tra có tồn tại chu trình wait for graph hay không sẽ được gọi là định kì. Nếu có chu trình thì tồn tại deadlock== 
- ==Giải thuật phát hiện chu trình có thời gian chạy là O(n^2), với n là số đỉnh của graph==
==**Đồ thị cấp phát tài nguyên wait-for**==

![[Pasted image 20250518212612.png]]

**Mỗi loại tài nguyên có nhiều thực thể**

- Gọi  là số tiến trình; m là số loại tài nguyên 
- Available: vector độ dài m thể hiện số thực thể sẵn sàng của mỗi loại tài nguyên 
- Allocation: ma trận n x m định nghĩa số thực thể của mỗi loại tài nguyên đã cấp phát cho mỗi tiến trình 
- Request: ma trận n x m xác định yêu cầu hiện tại của mỗi tiến trình 
	- Request[i, j] == k <-> Pi đang yêu cầu thêm k thực thể của Rj









___
### Phục hồi deadlock
- Khi deadlock xảy ra, để phục hồi 
	- Báo người vận hành 
	- Hệ thống tự động phục hồi bằng cách bẻ gãy chu trình deadlock 
		- Chấm dứt một hay nhiều tiến trình 
		- Lấy lại tài nguyên từ một hay nhiều tiến trình
**Chấm dứt tiến trình bị deadlock**
- ==Chấm dứt lần lượt từng tiến trình cho đến khi không còn deadlock== 
	- Sử dụng giải thuật phát hiện deadlock để xác định còn deadlock hay không 
- Dựa trên yếu tố nào để chấm dứt 
	- Độ ưu tiên của tiến trình 
	- Thời gian đã thực thi của tiến trình và thời gian còn lại 
	- Loại tài nguyên mà tiến trình đã sử dụng 
	- Tài nguyên mà tiến trình cần thêm để hoàn tất công việc 
	- Số lượng tiến trình cần được chấm dứt 
	- Tiến trình là intereactive hay batch 
**Lấy lại tài nguyên**
- Lấy lại tài nguyên từ một tiến trình, cấp phát cho tiến trihf khác cho đến khi không còn deadlock nữa 
- Chọn nạn nhân để tối thiểu chi phí (có thể dựa trên số tài nguyên sở hữu, thời gian CPU đã tiêu tốn)
**Chấm dứt tiến trình bị deadlock**
- Trở lại trạng thái trước deadlock (Rollback)
	- Rollback tiến trình bị lấy lại tài nguyên trở về trạng thái safe, tiếp tục tiến trình từ trạng thái đó 
	- Hệ thống cần lưu giữ mốt số thông tin về trạng thái các tiến trình đang thực thi 
- Đói tài nguyên (starvation): để tránh starvation, phải đảm bảo không có tiến trình sẽ luôn luôn bị lấy lại tài nguyên mỗi khi deadlock xảy ra