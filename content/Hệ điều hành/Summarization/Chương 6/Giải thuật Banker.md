- Mỗi loại tìa nguyên có nhiều thực thể 
- Giống như nghiệp vụ ngân hàng 
- Điều kiện
	- Mỗi tiến trình phải khai báo số lượng thực thể tối đa của mỗi loại tài nguyên mà nó cần 
	- Khi tiến trình yêu cầu tài nguyên thì có thể phải đợi 
	- Khi tiến trình đã có được đầy đủ tài nguyên 
	- Khi tiến trình đã có được đầy đủ tài nguyên thì phải hoàn trả trong mộ tkhoangr thời gian hữu hạn nào đó 
## Cấu trúc dữ liệu cho giải thuật banker 
n: số tiến trình, m: số tài nguyên
- Available: vector độ dài m
	- Available[j] = k -->> loại tài nguyên Rj có k instance sẵn sàng 
- Max: ma trận n x m:
	- Max[i, j] --> Tiến trình Pi yêu cầu tối đa k instance của loại tài nguyên Rj
- Allocation: ma trận n x m:
	- Allocation[i, j] = k --> Pi đã được cấp phát k instance của Rj
- Need: ma trận n x m
	- Need [i, j] = k --> Pi cần thêm k instance của Rj
	- ==> Need[i, j] = Max[i, j] - Allocation[i, j]
![[Pasted image 20250415001414.png]]
### Giải thuật an toàn:
1. Gọi Work và Finish là hai vector độ dài m và n. Khởi tạo: 
	Work = Available 
	Finish[i]=false, i = 0, 1, ..., n-1
2. Tìm i thỏa 
	1. Finish[i] = false
	2. Needi <= Work (hàng thứ i của need)
	Nếu không tồn tại i như vậy, đến bước 4 
3. Work = Work + Allocation
	1. Finish[i] = true
	2. Quay về bước 2
4. Nếu Finish[i]=true, i = 1,..., n, thì hệ thống đang ở trạng thái safe
#### Ví dụ: 
Có 5 tiến trình P0 -> P4
3 loại tài nguyên: 
	A(10 thực thể), B(5 thực thể), C(7 thực thể)
Sơ đồ cấp phát hệ thống tại thời điểm T0![[Pasted image 20250415001935.png]]
##### Bước 1: 
Gán work và finish
Dòng đầu tiên của Work là số lượng tài nguyên đang có, tiến hành dò tuyến tính từ trên xuống các tài nguyên bên need, nếu đủ thì cấp phát cho tài nguyên tiến trình đó 
Cập nhật Work = Work + Allocation (vì khi thực hiện xong, hệ thống thu hồi lại được tiến trình)
Sau đó cập nhật trọng số cho Finish là 1 ở tiến trình đó 
![[Pasted image 20250415002451.png]]

##### Bước 2: 
![[Pasted image 20250415002654.png]]
##### Bước 3: 
![[Pasted image 20250415002722.png]]
##### Bước 4: 
![[Pasted image 20250415002742.png]]
##### Bước 5: 
![[Pasted image 20250415002801.png]]
