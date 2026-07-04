---
share_link: https://share.note.sx/bmte9via#yFp9VclBkTVx6NVE2EUo4axFpmCBjgQ9Ru9Je67Xzxc
share_updated: 2026-03-16T22:31:43+07:00
---

- Sau buổi này có những lựa chọn, chọn đề tài do nhóm chọn hoặc do anh chọn cho nhóm

- Làm sao để biết ý tưởng của mình bình thường hay outstanding
- Nếu như bài toán A đang chỉ tận dụng văn bản, chưa ai thêm modality khác --> Quyết định thêm vào video, ảnh
- 2017 transformer ra đời trên text, nhưng đến 2019 mới bắt đầu sử dụng trên ảnh nhưng có impact rất lớn 
- Phai xem sau khi publish sẽ như thế nào 

- Nếu như thêm một thành phần vào mà tốt hơn thì không hẳn sẽ là novel thì thiên về engineer hơn chứ không outstanding. Cách kể chuyện có thể ảnh hưởng đến paper
	- --> Score là điều kiện bắt buộc, phải tăng, nhưng tùy cách kể sẽ chuyện
- Tuy nhiên nếu story kể rất hay nhưng đưa ít insight thì cũng trivial

- Đủ khó: 
	- Tìm được research question đủ khó
	- Lúc mình đi trả lời câu hỏi đó là đủ khó 
		- Anh có quen một prof bên medical có một bài ở nature.
			- Ví dụ có một RQ: Liệu bệnh nhân K (cancer) có phản ứng với thuốc B như nào. Bệnh nhân K có uống được thuốc của bệnh nhân mắc bệnh lao không
			- --> Tìm đâu ra được số lượng samples đó --> rất khó, paper đó tốn 4 năm, trong đó 3.5 năm tìm người 

- Anh lấy ví dụ về research tree
	- Nếu idea mình gần gần giống với A* thì mình cùng level

![[Pasted image 20260315192047.png]]

- Giải quyết cùng lúc nhiều vấn đề, existing methods \cite{paper1, paper2, paper3, paper4} sẽ tốt hơn
- Khi thêm các cách vừa rồi nhưng không được
	- Khi thêm method A vào B thì vừa tạo problem, sau này đọc paper thấy có người làm tương tự thì sẽ biết được limitation như nào. 
	- Chưa đến lúc tốt, với config này ok, nhưng có khi chưa ok, anh lấy ví dụ về việc train RL, hyperparams thay đổi có thể ảnh hưởng rất nhiều 
	- Chưa đủ tốt có thể là do chưa đủ dữ liệu 

![[Pasted image 20260315192824.png]]

- Nhắc lại lỗi sai là tìm method trước rồi tìm research gap sau, lấy ví dụ về bài itself, để model học được nhưng local features (đáng tin cậy)
	- Lúc nghĩ method anh lên google confirm lại tính chất của attention, khi qua attention rồi softmax thì trả ra một similarity matrix
	- Anh tận dụng attention để chọn feature 
	- Anh tiếp tục hỏi nên dùng multi-lay hay single layer, multi tốt hơn 
	- Mới trong research gap và mới trong method thì sẽ tăng độ mạnh của paper 

- Giữa text-encoder và vision-encoder sử dụng \[CLS] token để tiên kết, tuy nhiên, có thể sử dụng các token còn lại

![[Pasted image 20260315193806.png]]

![[Pasted image 20260315194051.png]]

---

- Lần meet tiếp theo sẽ kể về paper, nói về main concept. có thể trình bày nhanh, không cần slide nhưng phải nêu ra được ý chính
- Muốn làm đề tài có sẵn hay đề tài nhóm tự lên?
- Muốn theo hướng A* hay Q1

---

- Phải đặt mục tiêu lớn chủ yếu không phải vì tự kiêu mà giúp tự tin hơn
	- Tháng 8: AAAI
	- Tháng 9: CVPR
- Nhóm chỉ cần có một bài A thôi là học phd vô tư
- Còn bài toán nào thì chọn benchmark trước rồi 