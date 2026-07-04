![[Pasted image 20260511110355.png]]

- Dataset người ta dùng là intention của bức ảnh
- Có hai nhánh là sight với semantic 
	- sight: extract các attributary features từ CLIP thông thường 
	- semantic copy feature của sight để tune deep layers, học các feature về mặt ngữ nghĩa
	- Người ta sinh ra hai text labels là negative và positive prompt, tương ứng với có intention đó và không có intention đó
		- Họ maximize positive, minimize negative

![[Pasted image 20260511124725.png]]