Request_i là request vector  của Process Pi
Requesti[j] = k <-> Pi cần k instrance cảu tài nguyên Rj
1. Nếu Requesti <= Needi thì đến bước 2. Nếu không, báo lỗi vì tiến trình đã vượt yêu cầu tối đa
2. Nếu Requesti <= Available thì qua bước 3. Nếu không, Pi phải chờ vì tài nguyên không còn đủ để cấp phát 
3. Giả định cấp phát tài nguyên đáp ứng yêu cầu của Pi bằng cách cập nhật hệ thống như sau: 
	Available = Available - Requesti 
	Allocationi =Allocationi + Requesti
	Needi = Needi - Requesti

Áp dụng giả thuật banker để kiểm tra trạng thái an toàn lên trạng thái trên hệ thống mới 
- Nếu trạng thái là an toàn thì tài nguyên đượccấp thực sự cho Pi
- Nếu trạng thái không an toàn thì Pi phải đợi và phục hồi trạng thái 
	- Available = Availalebl + Requesti
	- Allocationi = Allocationi = Requesti
	- Needi = Needi + Requesti
## Ví dụ: P1 yêu cầu (1, 0, 2)
- Kiểm tra Request 1 <= Need1: (1, 0, 2) <= (1, 1, 2) -->> ĐÚng 
- kiểm tra Request 1 <= Available: 1, 0, 2<= 3, 3, 2 --> ĐÚng
- Giải định cấp phát tài nguyên đáp ứng yêu cầu của P1
![[Pasted image 20250415003700.png]]
![[Pasted image 20250415003851.png]]
### Bài tập
![[Pasted image 20250415004054.png]]
![[Pasted image 20250415004111.png]]