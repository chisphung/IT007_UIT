CLIP is always trained on short caption dataset, text-encoder ngắn (77) ⟶ Giải quyết như nào ⟶ Dùng LLM để đánh label expand caption ⟶ Common pattern (first sumary sentence) LongClip

- Clip được train trên short caption với text-encoder ngắn, hiện tại đang có 77 encoder input token
- --> Giải quyết như nào?
- Để giải quyết thì người ta train thêm trên data có caption dài 
	- Có hai loại: Human annotation, LLM generated
	- Có điểm chung là có một câu summary ở đầu câu
- Long-clip xuất hiện để giải quyết bằng cách kéo dài PE + train trên một lượng ít dataset long caption (?) <ref tới câu anh HUy nói hồi HCMAI>
- Đặt câu hỏi: Nếu như các samples đều có câu summary ở đầu thì nếu xóa câu đầu thì như thế nào
	- Thực nghiệm thì thấy bỏ câu summary ở đầu thì perf giảm ở cả CLIP và Long Clip

![[Pasted image 20260320200833.png]]


![[Pasted image 20260320201430.png]]

- Dẫn vào de-bias:
- Remove first sentence -> các câu sau sẽ có độ chi tiết cao hơn 
- Randomly delete sentences and shuffle. Drop random sentences, lấy tổ hợp các sentences
- Add padding after \<start> token: Tăng độ chú ý cho các sentences phía sau.  Loss = loss_long + loss_short    

**Limitation**

- Chưa có dataset mô tả kiểu mà không có first summary sentence
- Mất tinh liên kết nếu như shuffle, hoặc cắt
---

- **RG**
	- Có chắc là first sentence là nguyên nhân hay không, hay do cách mô tả là main object ở câu đầu 
	- Object-bias, nhắc đến object nhiều lần thì sẽ học nhiều ở object đó
		- Giải quyết: dùng relative pronounces thay vì abs 
		- Paraphrase lại object
		- Trượt trên từng câu rồi bridge gap giống như swin 


