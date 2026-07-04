## Missing modality

- Imbalance data: 
	- Đánh thẳng về data 
	- Đánh vào arch 

![[Pasted image 20260327193541.png]]

- Hướng này phát triển mạnh, 
- Các data hiện tại đang bi thiếu, một phần data bị null 

## Matryoshkha

- Trong lúc search sẽ có một vector D chiều
- Thuật toán search sẽ tốn O(n) --> thuật toán này dùng logn 
- Thay vì search nguyên vector d thì search d/2 

- Để thực hiện được thì thực hiện train 

---
Một số trường hợp dự đoán sai nhưng conf cao, một số trường hợp dự đoán đúng nhưng conf thấp, người ta cho rằng do modality gap
- Modality gap: Khi embed text với ảnh, có cùng ngữ nghĩa 

![[Pasted image 20260327201625.png]]

- Nếu như cùng ngữ nghĩa với nhau thì gần nhau, nhưng không 
- Propose: Không tính dựa trên cosine mà so sánh giữa phân phối 