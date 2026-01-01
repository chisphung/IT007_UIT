## Tạo tiến trình 
### fork()
- Tiến trình con sao chép không gian địa chỉ của tiến trình cha -> Tiến trình con: 
	- Sao chép toàn bộ source code của tiến trình cha 
	- Sao chép giá trị của các biến đã được tạo 
	- **Bắt đầu thực thi tại vị trí mà tiến trình được**
- Giá trị trả về của hàm fork sẽ thuộc 1 trong 3 trường hợp:
	- Lớn hơn 0: Cho biết đây là tiến trình cha 
	- Bằng 0: Cho biết đây là tiến trình con 
	- Nhỏ hơn 0: Hàm fork() thất bại
### Họ hàm exec()
- Nạp một tác vụ mới vào không gian địa chỉ của tiến trình gọi hàm 
	- Tác vụ mới sẽ được ghi đè vào không gian địa chỉ của tiến trình 
	- Tiến trình thực thi tác vụ mới thay vì source code ban đầu
### Bài tập [[Chương 3 - Tiến trình]]
