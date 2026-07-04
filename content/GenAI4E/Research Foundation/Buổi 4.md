---
share_link: https://share.note.sx/lfe4e8j9#7VZG2qZKBOWjyhb+iHHNdLyrcWKF/FhzRDISDvBQ7e4
share_updated: 2026-03-14T22:12:17+07:00
---
## How to ask a good question 

- Nhắc lại: Question, variable (mơ hồ), target
- Phải có research gap mới phát triển method 

- A research gap is 
	- Chưa làm
	- Chưa hiểu 
	- Chưa đúng 

- Lấy ví dụ pipeline gen ảnh bình thường, có image, text, đưa qua gen ai, output là edited image 
	- Nhắc lại biến độc lập, phụ thuộc
		- Phụ thuộc (cố định)
		- Độc lâp --> Có thể biến thiên

**Chưa làm**
- Quan sát từ các work trước đó 

![[Pasted image 20260307194935.png]]

- Khi cố định input rồi có thể biến thiên
- Ví dụ về bài Edit one for all: Interactive Batch Image Editing 

**Chưa hiểu:**

- Quan sát xung quanh
- Ví dụ con người bị chi phối bởi cảm xúc, liệu có nghiên cứu nào nhắc về cảm xúc của AI không 
- Ví dụ về bài the good, the bad and why: Unveiling  emotions of AI

--> Chưa làm và chưa hiểu thì không dựa trên một work nào, giúp cung cấp tri thức cho nhân loại, dựa trên trực giác là nhiều 

**Chưa đúng**

- Tấn công vào các works trước đó 

### What makes a good question 

![[Pasted image 20260307201458.png]]

- Nhưng không phải lúc nào paper cũng có limitation
- Dựa vào observation 
	- Con người có few-shot thì giải quyết được 
	- Paper language models are few shot learning 

- Một paper không giải thích được vì sao nó work thì vẫn được chấp nhận 

![[Pasted image 20260307202122.png]]


![[Pasted image 20260307202146.png]]

### What to makes a good question

- Tại sao phải comment trước, người ta bắt đầu bằng việc tìm một paper, sau đó tìm limitation, tuy nhiên, có thể tim được nhưng chưa đủ sâu 
- Lấy ví dụ nhóm làm về transformer comment trên RNN là tính tuần tự

- Model A có các tính chất A + B + C + D +E +F --> decompose 
- Khi làm benchmark dễ hơn do dễ decompose, chỉ cần comment trên các paper hiện có, lập ra được bảng 

![[Pasted image 20260314194107.png]]

- Anh nhắc đến dataset Big bench có 2000 samples, người ta sinh ra big bench hard gồm 10k samples
	- Những research gap của benchmark rất đơn giản, 2000 samples --> 10000 samples: Giải được research gap 

![[Pasted image 20260314194910.png]]

- Decompose có thể giúp mình hiểu sâu được bài toán, phối hợp lại để đưa ra giải pháp trên vấn đề chính 
- CLIP = Text encoder + Img Encoder + Data ---> Decompose 

![[Pasted image 20260314195351.png]]

- Caption của ảnh có thể không đủ --> có thể tăng độ chi tiết của câu mô tả, tuy nhiên nếu tạo một caption dài, model có thể không học được 

![[Pasted image 20260314195701.png]]

- Cho phép model tự chọn các features để học thay vì cho con người chọn...

- Trước khi đi vào một bài toán thì cần decompose để hiểu hơn, sau đó analyze để tấn công vào paper đó 

![[Pasted image 20260314195813.png]]

### Research tree

- Khi đọc paper phải hiểu được nền tảng xây dựng nên paper đó bằng cách decompose 
- Sau đó mới analyze được, analyze là điểm hơn thua 

![[Pasted image 20260314200648.png]]

- Đôi khi  có những lỗi sai khi đưa ra câu hỏi
	- Không phải một bước đi ra được biên của research circle
	- Đọc một paper luôn nghĩ trước limitation thì không tốt, nhưng bản thân không biết trước model gồm những thứ gì, thì phải decompose
	- Anh nhắc đến semi supervised, có phương pháp pseudo-label, người ta dựa trên một fixed threshold để đánh label --> RG: adaptive threshold
	- Bắt cứ một giả định nào đó thì nên nghi ngờ giả định đó thay vì tin tưởng hoàn toan 