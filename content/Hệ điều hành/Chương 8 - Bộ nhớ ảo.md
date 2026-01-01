Ref:
[[Chương 7 - Quản lý bộ nhớ#Dynamic loading]]
## Tổng quan về bộ nhớ ảo 
- Nhận xét: không phả tất cả các phần của một process cần thiết phải được nạp vào bộ nhớ chính tại cùng một thời điểm
- Ví dụ: 
	- Đoạn mã điều khiển các lỗi hiếm khi xảy ra 
	- Các array list, tables được cấp phát bộ nhớ (cấp phát tĩnh) nhiều hơn yêu cầu thực sự 
	- Một số tính năng ít khi được dùng của một chương trình 
	- Cả chương trình thì cũng có đoạn code chưa cần dùng 
```
- Bộ nhớ ảo (virtual memory): Bộ nhớ ảo là một kỹ thuật cho phép xử lý một tiến trình không được nạp toàn bộ vào bộ nhớ vật lý
```
**Ưu điểm:**
- Số lượng process trong bộ nhớ nhiều hơn 
- Một process có thể thực thi ngay cả khi kích thước của nó lớn hơn bộ nhớ thực 
- Giảm nhẹ công việc của lập trình viên
Không gian tráo đổi giữa bộ nhớ chính và bộ nhớ phụ (swap space)
Ví dụ: 
- swap partition trong linux 
- file pagefile.sys trong Windows 
## Cài đặt bộ nhớ ảo 
- Có hai kỹ thuật 
	- Demand paging 
	- Demand segmentation
- Phần cứng memory management phải hỗ trợ paging và /hoặc segmentation 
- OS phải quán lý sự di chuyển của trang /đoạn giữa bộ nhớ chính và bộ nhớ thứ cấp 
- Trong chương này: 
	- Chỉ quan tâm đến paging 
	- Phần cứng hỗ trợ thực hiện bộ nhớ ảo 
	- Các giải thuật của hệ điều hành 
ref: [[Chương 7 - Quản lý bộ nhớ#Cơ chế phân trang]], tất cả các trang đều sẽ được nạp vào trong bộ nhớ chính
## Phân trang theo yêu cầu: 
- Demand paging: Các trang của tiến trình chỉ được nạp vào bộ nhớ chính khi được yêu cầu (cần trang nào thì nạp trang đó)
- Khi có một tham chiếu đến một trang mà không  có trong bộ chính (valid bit) thì phần cứng sẽ gây ra một ngắt (gọi là page-fault trap) kích khởi page-fault service routine (PFSR) của hệ điều hành
- PFSR: 
	- Bước 1: chuyển process về trạng thái blocked 
	- Bước 2: Phát ra một yêu cầu độc đĩa để nạp trang được tham chiếu vào một frame trống; trong khi đợi IO, một process khác được cấp CPU để thực thi
	- Bước 3: Sau khi IO hoàn tất, đĩa gây ra một ngắt đến hệ điều hành; PFSR cập nhật page table và chuyên process về trạng thái ready
## Lỗi trang và các bước xử lý: 
- Bắt đầu chạy chương trình:, load biến M trong một trang 
- Tìm trong bảng trang, do đây là cơ chế demand paging, nên trang chưa chắc đã có trong bộ nhớ chính 
- Bít i là invalid 
- Đẩy trap lên cho OS để báo có lỗi trang 
- Hệ điều hành chuyển từ trạng thái running sang waiting 
- Hệ điều hành tìm trang còn thiếu trong bộ nhớ phụ 
- TÌm khung nào còn trống để gán vào bộ nhớ vật lý
- Reset lại page table
![[Pasted image 20250512160623.png]]
## Khi cần thay thế trang: 
![[Pasted image 20250512160641.png]]
Ở Bước 2 của PFSR giả sử phải thay trang vì không tìm được frame trống, PFSR được bổ sung như sau: 
- Xác định vị trí trên đĩa của trang đang cần 
- Tìm một frame trống: 
	- Nếu có frame trống thì dùng nó 
	- Nếu không có frame trống thì dùng một giải thuật thay trang để chọn một trang hy sinh (victim page)
	- Ghi victim page lên đĩa, cập nhật page table và frame table tương ứng 
![[Pasted image 20250512160909.png]]
**Vấn đề:**
- Frame-allocation algorithm: 
	- Cấp phát cho process bao nhiêu frame của bộ nhớ thực 
- Page-replacement algorithm 
	- Chọn frame của process sẽ được thay thế trang nhớ 
	- Mục tiêu: số lượng page-fault nhỏ nhất 
	- Được đánh giá bằng cách thực thi giải thuật đối với một chuỗi tham chiếu bộ nhớ (memory reference string) và xác định số lần xảy ra page fault 

![[Pasted image 20250512161353.png]]
## Giải thuật thay trang 
==Nếu truy xuất trang mà trang không có trong page table sẽ gây ra lỗi trang ==
### FIFO:
- Thay thế trang được nạp vào bộ nhớ sớm nhất.
- **Nghịch lý Belady:** Với một số thuật toán, số lỗi trang có thể tăng khi tăng số frame (ví dụ: FIFO).

## OPT 
OPT stands for optimal
- Thay thế trang sẽ được tham chiếu trễ nhất trong tương lai (không thực tế).
## LRU
_**Least Recently Used**_
- Thay thế trang ít được sử dụng nhất trong quá khứ.
___
# Quiz 
![[Pasted image 20250512155659.png]]

![[Pasted image 20250512174118.png]]![[Pasted image 20250512174704.png]]
 
___
## nội dung thi 
- Chương 5, 6, 7, 8, 9
- Chương 9 ít nhất sẽ có một câu trong đề 
- 