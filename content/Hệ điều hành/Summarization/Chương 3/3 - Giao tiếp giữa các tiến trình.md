![[Pasted image 20250408205135.png]]

## Shared memory 
	Một vùng nhớ chung được chia sẻ giữa các tiến trình 
	Quá trình giao tiếp không được hệ điều hành quản lý 

## Message passing 
• Đặt tên (Naming)
	• Giao tiếp trực tiếp
		• send(P, msg): gửi thông điệp đến tiến trình P
		• receive(Q, msg): nhận thông điệp đến từ tiến trình Q
	• Giao tiếp gián tiếp: thông qua mailbox hay port
		• send(A, msg): gửi thông điệp đến mailbox A
		• receive(Q, msg): nhận thông điệp từ mailbox B
• Đồng bộ hóa (Synchronization): blocking send, nonblocking send, blocking receive, nonblocking receive.
Các tiến trình giao tiếp nhau thông qua vùng đệm (Buffering): dùng queue để tạm chứa các message
	• Khả năng chứa là 0 (Zero capacity hay no buffering).
	• Bounded capacity: độ dài của queue là giới hạn.
	• Unbounded capacity: độ dài của queue là không giới hạn.
