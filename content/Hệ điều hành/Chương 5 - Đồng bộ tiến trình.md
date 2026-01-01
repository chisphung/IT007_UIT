---
share_link: https://share.note.sx/36kjz4le#kdIz0OHPuMYC0yBQZ1MFWX7wCxuABKEtq9PC+H1jbgY
share_updated: 2025-04-01T09:16:57+07:00
---
# Race condition: 
## Bài toán producer vs consumer: 
Producer luôn tăng số lượng sản phẩm, Consumer giảm số lượng sản phẩm.
Giả sử có một biến count để quản lý lượng sản phẩm này. 
Thông thời các tiếng trình sẽ được đăt trong một vòng while(1), các tiến trình sẽ thực thi đồng thời nhau, chuyển qua lại.
### Rounded buffer 
	index = (index + 1) % BS -- hashing
Khai báo biến count là biến global 
Cho hai vòng lặp chạy while(1) để chạy, một vòng tăng liên tục, một vòng giảm liên tục 
khi tăng, tăng theo công thức index để quay lại vị trí ban đầu khi tràn.
Biến count trong trường hợp này được gọi là shared data
![[Pasted image 20250323125719.png]]

#### Phân tích lý do: 
count++, count-- 
Đưa dữ liệu từ ram vào register.
sau đó nạp lại vào count
![[Pasted image 20250323131714.png]]
![[Pasted image 20250323131959.png]]
Tuy nhiên, đối với quantum time = 2 cycles: 
![[Pasted image 20250323132129.png]]
Dữ liệu không còn nhất quán (data inconsistency), bị đan xen nhau.
### Bài toán cấp phát PID 
- Hai tiến trinh P0 và P1 cùng gọi hàm fork()
- Biến next_available_pid được kernal sử dụng để tạo ra PID cho tiến trình mới 
- Tiến trình con của P0 và P1 đồng thời yêu cầu PID và nhận được kết quả giống nhau
- ![[Pasted image 20250323132939.png]]
- --> cần có một cơ chế để ngăn P0 và P1 đồng thời yêu cầu cấp PID 
Từ khóa: tranh chấp

	Race condition là hiện tượng các tiến trình truy cập đồng thời vào dữ liệu được chia sẻ 
	Kết quả cuối cùng sẽ phụ thuộc vào thứ tự của các tiến trình đang chạy đồng thời với nhau

- Như trong bài toán producer-consumer, dữ liệu chia sẻ là biến count, bị tác động đồng thời lên cả producer và consumer. 
- Tương tự với việc cấp PID, next_available_pid bị tranh giành giữa P0 và P1 
- Race condition có thể dẫn đến việc dữ liệu không nhất quán 
**Cách giải quyết**: Đảm bảo sao cho mỗi thời điểm chỉ có một tiến trình được thao tác trên dữ liệu chia sẻ 
**-> cần cơ chế đồng bộ hoạt động của các tiến trình**

## Vấn đề vùng tranh chấp 

	Critical section: là vùng code mà các tiến trình thực hiện tác động lên dữ liệu được chia sẻ 
- Mỗi tiến trình có một  vùng tranh chấp là một đoạn code: 
	- Thực hiện việc thay đổi giá trị của dữ liệu chia sẻ, cập nhât, ghi 
	- Khi một tiến trình thực hiện việc thay đổi trên vùng tranh chấp thì các tiến trình khác không được thao tác trên vùng đó 
	![[Pasted image 20250323134417.png]]

### Yêu cầu dành cho lời giải: 
- Mutual exclusion: Khi một tiến trình P đang thực thi vùng CS, không một tiến trình khác có thể tiến vào thực thi vùng CS của nó. Mỗi tiến trình có một đoạn code riêng, chia sẻ chung dữ liệu thì mới gọi là CS
- Progress: Một tiến trình P không vào vùng CS, không được thực hiện một hành động **cản trở** nào đến Q
- Deadlock: P chờ Q, Q cũng chờ P
- Bounded waiting: thời gian chờ đợi để được vào vùng tranh chấp có hạn định. 
- ![[Pasted image 20250323135412.png]]

# Các giải pháp dựa trên ngắt
Thao tác đơn nguyên là thao tác không bị chia cắt. 
Giả sử có hai thao tác đơn nguyên là load và store 
## Giải pháp phần mềm 1: 
	Giải pháp dành cho 2 tiến trình Pi và Pj 
	Có hai thao tác đơn nguyên là load và store 
	Hai tiến trình chia sẻ một biến turn 
	Biến turn cho biết chương trình nào tới lượt. Turn được khởi tạo là i 

![[Pasted image 20250323140224.png]]
**while(turn == j)  --> busy waiting để chờ đến turn == i**
Nếu lập trình là while (turrn == i ){ } thì chương trình pass qua vòng lặp và thực hiện các lệnh sau đó, không có busy waiting 
key word: while (turn == i) là busy waiting 99
![[Pasted image 20250323140402.png]]
### Kiểm tra tính đảm bảo: 
- Mutual exclustion: thỏa mãn![[Pasted image 20250323141023.png]]
- Progress: không đảm bảo
	Khi remainder section của P1 quá dài, không quay lại kiểm tra được turn
	Trong khi P0 có remainder section quá ngắn, đặt chưa đặt lại turn P0 
	P0 phải chờ P1 trả turn = 0 
- Bounded Waiting: không đảm bảo![[Pasted image 20250323141440.png]]
	Giải sử thời gian trong remainder section (RS) của P1 rất dài, 
[link](http://www.cse.hcmut.edu.vn/~hungnq/courses/lopchuyendoi)
![[Pasted image 20250512162257.png]]

## Giải pháp Peterson 
	Giải pháp dành cho 2 tiến trình
	Hai lệnh hợp ngữ load và store là hai thao tác đơn nguyên 
	hai tiến trình cùng chia sẻ hai biến là turn và flag[2]: bool
	turn:  tiến trình nào đến lượt
	flag: xác định tiến trình đã sẵn sàng vào vùng CS chưa 
```cpp
while (flag[j] && turn == j);
```

![[Pasted image 20250323152702.png]]
![[Pasted image 20250323142532.png]]
### Đánh giá: 
- Progress: đảm bảo
	Nếu P0 không vào CS, P0 không ngăn cản P1 vào CS và ngược lại đối với P1
- Bounded Waiting: đảm bảo 
	P1 phải chờ tối đa một lần P0 vào vùng tranh chấp. CS thường rất nhỏ nên thời gian chờ sẽ không dài 
### Giải pháp Peterson và kiến trúc hiện đại 
	Với các tiến trình đa tiểu trình, việc sắp xếp lại các thao tác có thể dẫn đến kết quả không nhất quá hoặc không dự đoán được

![[Pasted image 20250323145023.png]]
Kết quả kỳ vọng được in ra là 100 

Tuy nhiên, ở kiến trúc hiện đại, máy tính sẽ sắp xếp lại các câu lệnh để chạy nhanh hơn, do các thao tác này độc lập 
![[Pasted image 20250323145251.png]]
--> Để đảm bảo giải pháp peterson thực hiện được đúng, ta phải có memory barrier 
## Giải thuật Bakery
![[Pasted image 20250512162617.png]]
## Giả thuật Swap
![[Pasted image 20250512162632.png]]
## Cấm ngắt 
![[Pasted image 20250512162700.png]]
## Chỉ thị TSL
![[Pasted image 20250512162733.png]]
## Memory Barrier 
	Memory model là mô hình của bộ nhớ trong hệ thống, bao gồm cách thức quản lý và truy xuất đến các vùng nhớ được cấp phát cho các tiến trình và luồng trong hệ thống 
Memory model định nghĩa các quy tắc và ràng buộc cho việc sử dụng bộ nhớ, đảm bảo
Hai mô hình bộ nhớ phổ biến: 
	**Mô hình bộ nhớ được sắp xếp mạnh**: các thay đổi trên một bộ xử lý sẽ được các bộ xử lý khác biết ngay lập tức
	**Mô hình bộ nhớ được sắp xếp yếu**: các thay đổi bộ nhớ trên một bộ xử lý có thể sẽ không được các bộ xử lý khác biết ngay lập tức
Memory barrier là một instruction mà bắt buộc mọi thay đổi trong bộ nhớ phải được truyền tải đến tất cả các bộ xử lý khác 

![[Pasted image 20250324131236.png]]
### Chỉ thị Memory Barrier 
- Khi một chỉ thị memory barrier được thực hiện, hệ thống sẽ đảm bảo các thao tác load và store đều đã được hoàn thành trước khi các thao tác load và store sau đó được thực hiện 
- Do đó, kể khi bị sắp xếp lại, memory barrier đảm bảo rằng các thao tác ghi dữ liệu đều đã hoàn thành trong bộ nhớ và được truyền tải đến các bộ xử lý khác trước khi các thao tác nạp duex liệu hoặc ghi dữ liệu được thực thi trong tương lai
#### Ví dụ: 
![[Pasted image 20250323175142.png]]

## Mutex Locks (spinlock)
	In fact, the term mutex is short for mutual exclusion. Suppose the CS is a room, mutex lock is a locker. 
	- acquire lock to request lock 
	- release lock to unlock, set available = true 
	- if mutex lock is not available, have to wait 

Nếu không available thì busy waiting, chuyển available sang false để thực hiện 
Release để chuyên available sang true

![[Pasted image 20250324132028.png]]

### Mutex locks không busy waiting 
- Để tránh busy waiting trong mutex locks, ta đặt tiến trình vào trạng thái sleep khi bị khóa, đánh thức khi khóa được mở 
- 2 thao tác được cung cấp: 
	- block: trạng thái ngủ  running-> waiting, khi tiến trình hiện tại bị blocked thì các tiến trình khác vẫn có thể thực hiện
	- wakeup: đánh thức  waiting -> ready 
	
	Dùng if, thay vì while
	![[Pasted image 20250324132403.png]]
### Cách sử dụng mutex lock: 
**Lưu ý:**
	• Mutex lock thường sẽ được khai báo toàn cục
	và được khởi tạo trong hàm main.
		• Cần phải xác định đúng vùng tranh chấp trước
	khi thực hiện các thao tác trên khóa mutex
	(acquire và release).
![[Pasted image 20250324132940.png]]
![[Pasted image 20250324134656.png]]
![[Pasted image 20250324134704.png]]
### Nhược điểm: 
	Tại một thời điểm chỉ có một tiến trình truy cập được vào CS. 
	Nếu như có nhiều tiến trình thực hiện đồng bộ, cần có cách khác để giải quyết:
## Semaphore 
	Là một công cụ đồng bộ cung cấp cách sử dụng dụng linh hoạt hơn so với Mutex, để các tiến trình có thể đồng bộ hoạt động hành vi của mình 
	Semaphore về bản chất là một biến số nguyên, có thể truy cập qua 2 thao tác: wait() và signal() hay P() và V() 
wait(): to ask if there is any free resource (increase free table in the provided example)
signal(): to increase free the current resources (decrease free table in exp)

![[Pasted image 20250324135759.png]]
### Phân loại semaphore
- Counting semaphore: là một số nguyên không giới hạn 
- Binary semaphore: mang hai giá trị nhị phân 0 và 1
### Hiện thực semaphore
- Đảm bảo không có hai tiến trình cùng wait() và signal(), bản thân semaphore cũng là shared memory, 
- Hai thao tác S-- và S++ cùng thực hiện trên một vùng tranh chấp, wait() và signal() cùng nằm trên vùng tranh chấp
![[Pasted image 20250324140755.png]]
### Hiện thực semaphore không busy waiting
- Mỗi semaphore đoực gắn với một hàng đợi 
- Mỗi phần tử có 2 thành phần:
	- Giá trị 
	- Con trỏ -> linked list, để lưu các tiến trình bị blocked trong semaphore
- Hệ điều hành cung cấp 2 thao tác: 
	- block
	- wake up 

![[Pasted image 20250324141334.png]]
![[Pasted image 20250324141845.png]]
Thứ tự giải phóng: FIFO
### Ứng dụng của semaphore 
#### Đảm bảo mutual exclusion:
- Semaphore hoạt động như một khóa mutex 
- Bảo vệ CS bằng thao tác wait() và signal()
- Khởi tạo giá trị của semaphore là 1 -> chỉ tiến trình nào gọi wait() trước thì mới được tiến vào CS 
-  Việc đảm bảo loại trừ tương hỗ chỉ đúng khi semaphore được cài đặt là 1 kết hợp với việc đặt hàm wait() và signal() đúng vị trí. Mặt khác nếu giá trị của semaphore lớn hơn 1, đồng nghĩa với việc có nhiều hơn 1 tiến trình có thể thực hiên thao tác wait() mà không bị block, từ đó có thể truy cập vùng tranh chấp --> Loại trừ tương hỗ không đảm bảo.
![[Pasted image 20250329175756.png]]
#### Đảm bảo thứ tự thực thi: 
Đồng bộ P1 và P2, S1 luôn thực thi trước S2 
- Khởi tạo semaphore synch = 0 
- Phân tích thứ tự thực thi: 
	-  Nếu S1 thực thi trước: không sao 
	-  Nếu S2 thực thi trước: bị block, do gọi wait() để kiểm tra thì có S1 đang thực thi. 
--> Khởi tạo semaphore synch = 0, khi s1 thực hiện xong, tăng signal để S2 thực hiện 
Khi S2 dùng synch wait(synch) để check S1 thực hiện xong chưa. Nếu thực hiện xong, thực hiện S2
![[Pasted image 20250329182513.png]]
#### Đảm bảo điều kiện: 
Đồng bộ Produce và Consumer sao cho:
sells <= products 
- Bước 1: Dựa vào điều kiện, xác định tài nguyên. số đơn vị mà sells được tăng là số hàng còn lại trong kho (stock)
- Bước 2: Xác định số lượng semaphore 
	-> quản lý tài nguyên -> 1 semaphore
- Bước 3: Đặt wait() và signal()
- Bước 4: Dựa vào trạng thái của hệ thống, xác định giá trị của semaphore
![[Pasted image 20250329184424.png]]
### Một số nhận xét về semaphore
Xét semaphore S: 
- Khi S->value >= 0: số lần mà các tiến trình/tiểu trình có thể thực thi wait(S) mà không bị blocked là S->value
	S = 5 -> các tiến trình có thể thực thi wait(S) 5 lần mà không bị blocked
- Khi S->value < 0: số tiến trình/tiểu trình đang đợi trên S là |S->value|
	S = -5, có 5 tiến trình đang đợi trong semaphore

Atomic và mutual exclusion: Không được xảy ra trường hợp 2 tiến trình cùng đang ở trong thân lệnh wait(S) và signal(S) (cùng semaphore S) tại một thời điểm (ngay cả với hệ thống multiprocessor)
----> Đoạn mã định nghĩa các lệnh wait(S) và signal(S) cũng chính là vùng tranh chấp 
Vùng tranhchaaps của các tác vụ wait(S) và signal(S) thông thường rất nhỏ: khoảng 10 lệnh

Giải pháp cho vùng tranh chấp wait(S) và signal(S): 
- Uniprocessor: dùng disable interrupt. Nhưng phương pháp này không làm việc trên hệ thống multiprocessor
- Multiprocessor: ứng dụng các giải pháp phần mềm: Dekkler, Oeterson. Các giải pháp phần cứng (TestAndSet, Swap)
Vì Cs rất nhỏ nên chi phí cho busy waiting rất thấp
#### Ví dụ: 
![[Pasted image 20250329185716.png]]
![[Pasted image 20250329185856.png]]
##### Giải quyết: 
![[Pasted image 20250329185920.png]]
## Phân loại giải pháp
![[Pasted image 20250518175214.png]]
## Monnitor:
Là một kiểu dữ liệu trừu tượng đóng gói những thành phần sau: 
- Local variables: được khai báo trong monitor và chỉ có thể truy cập bởi các hàm nội bộ trong monitor
- Procedures: Một tập các thao tác được định nghĩa bởi lập trình viên và **được thực thi theo mutual exclusion**, các thủ tục này cũng có thể truyc ập các biến nội bộ khai báo ở trên
- Initialization code
![[Pasted image 20250329190354.png]]

##### Hiện thực monitor: 

![[Pasted image 20250329190614.png]]

Việc khai báo như trên có thể đảm bảo mutual exclusion cho từng semaphore 
##### Đặc điểm của monitor: 
![[Pasted image 20250329190713.png]]
![[Pasted image 20250329190911.png]]

#### Condition Variable
Nhằm cho phép tiến trình đợi trong monitor, chí rcos thể truy cập bên trong monitor 
- Khai báo: condition x, y;
- Chỉ có thể thao tác lên condition variable bằng 2 thao tác: 
	- x.wait(): tiến trình thực thi thao tác này sẽ bị blocked trên condition variable x cho đến khi thao tác x.signal() được thực thi 
	- x.signal(): phục hồi quá trình thực thi của một tiến trình (nếu có) bị blocked trên condition variable x
		- Nếu có nhiều tiến trình bị blocked: chỉ có một tiến trình được phục hồi 
		- Nếu không có tiến trình nào bị blocked: không có tác dụng
![[Pasted image 20250330152108.png]]
![[Pasted image 20250330152336.png]]
## Liveness: 
Tiến trình có thể phải chờ đợi vô thời hạn để cố gắng yêu cầu các công cụ đồng bộ như mutex hay semaphore -> vi phạm tiêu chí progress và bounded waiting 
Liveness là ==thuật ngữ để chỉ một tập các điểm mà hệ thống phải thỏa mãn để đảm bảo tiến trình thực sự chạy== 
Chờ đợi không giới hạn là một ví dụ tiêu biểu của liveness thất bại 

#### Deadlock: 
Là tình trạng hai hay nhiều tiến trình chờ đợi không giới hạn cho một sự kiện này chỉ có thể thực hiện bởi một trong các tiến trình đang chờ ở trên 
**Một số dạng khác của deadlock**: 
- Starvation: 
	- Một tiến trình có thể không bao giờ được thoát ra khỏi hàng đợi của semaphore mà nó đang chờ
- Prority inversion: 
	- Vấn đề định thời khi tiến trình có độ ưu tiên thấp giữ khóa mà đang được cần bởi tiến trình có độ ưu tiên cao
	- Có thể giải quyết bằng priority inheritance protocol
## Phát biểu bài toán bounded-buffer
Khi thêm một phần tử vào mảng, phải đảm bảo mảng chưa đầy 
Khi xóa phần tử khỏi mảng, cần đảm bảo, mảng còn phần tử để xóa (không rỗng)

![[Pasted image 20250330213207.png]]
## Giải pháp cho bài toán bounded-buffer:
Bước 1: Dựa vào điều kiện, xác định tài nguyên:
	Có hai loại tài nguyên: 
		- Tài nguyên 1: số vị trí có thể thêm
		- Tài nguyên 2: số vị trí có thể xóa
	Vùng tranh chấp: vùng code truy cập mảng buffer và count
	Bảo vệ vùng tranh chấp -> mutual exclusion 

![[Pasted image 20250330213618.png]]

Bước 2: Khởi tạo semaphore
- Tài nguyên 1: số vị trí có thể thêm 
	- semaphore empty: khởi tạo là n 
- Tài nguyên 2: số vị trí có thể xóa:
	- semaphore full: khởi tạo là 0
- Bảo vệ vùng tranh chấp -> mutual exclusion 

![[Pasted image 20250330213717.png]]

- empty là số lượng ô trống 
- mutex được khởi tạo để đảm bảo mutual exclusion 
- full là số lượng ô đầy 
- wait(empty) để kiểm tra còn ô trống nào để thêm hay không 
- wait(full) để kiểm tra còn số lượng ô đầy nào để xóa hay không 
- signal(full) để tăng sem full lên do mới tăng biến count lên 
- signal(empty) để tăng empty lên do mới xóa
![[Pasted image 20250330214921.png]]
![[Pasted image 20250330221622.png]]
## Bài toán readers - writers 
- Dữ liệu được chia sẻ giữa các tiến trình đang thực thi đồng thơi f
	- Readers: Chỉ đọc dữ liệu; không thực hiện cập nhật 
	- Writers: Có thể vừa đọc vừa ghi dữ liệu
- Vấn đề: 
	- Cho phép nhiều Readers cùng đọc dữ liệu đồng thời 
	- Chỉ một Writer được phép truy cập dữ liệu tại một thời điểm
### Biến thể 1
Ưu tiên cho Readers: 
- Các readers có thể đọc đồng thời cùng nhau 
- Khi một readers đang đọc, các readers khác cũng có thể đọc chung 
- -> writer có thể bị starvation 
![[Pasted image 20250406170539.png]]
### Biến thể 2
Ưu tiên Writers: 
- Khi một Writers đã sẵn sàng thì Writers nãy sẽ được thực thi càng sớm càng tốt 
- Nếu một Writesr đang chờ để truy cập dữ liệu, không có một Readers mới nào được phép thực thi 
- --> Readers có thể bị starvation 
### Giải pháp cho bài toán Readers - Writers
#### Biến thể 1 - Ưu tiên Readers
- Các dữ liệu được chia sẻ: 
	-  Cơ sở dữ liệu/biến/mảng/...
	- semaphore rw_mutex: khởi tạo là 1 để bảo vệ csdl
	- semaphore mutex: khởi tạo là 1 để bảo vệ read_count
	- Biến read_count: khởi tạo là 0, đếm số Readers, được chia sẻ giữa các readers 
![[Pasted image 20250406170952.png]]

![[Pasted image 20250406211812.png]]
- Nếu một Writer đang ở trong CS và có n Readers đang đợi thì một Reader được sắp xếp trong hàng đợi của rw_mutex và n-1 Reader kia trong hàng đợi của rw-mutex và n-1 Reader kia trong hàng đợi của mutex
- Khi Writer thực thi signal(rw_mutex) hệ thống có thể phục hồi thực thi của một trong các Reader đang đợi hoặc Writer đang đợi

## Bài toán Dining Philosophers
- Giả sử có n triết gia ngồi trên một chiếc bàn tròn với tô cơm ở giữa. 
- Họ chỉ dành thời gian để làm 2 việc: Suy nghĩ và ăn
- Họ không tương tác với những người bên cạnh
- Thi thoảng các Triết gia sẽ cầm lên 2 chiếc đũa (mỗi chiếc một lần)
	- Cần phải có đủ 2 chiếc đũa thì mới ăn được, sau khi ăn xong thì trả lại
	- Số chiếc đũa cũng là n
	
![[Pasted image 20250406213826.png]]

Trường hợp có 5 Triết gia, dữ liệu được chia sẻ như sau: 
- Tô cơm (dữ liệu)
- Mảng semaphore chpostick\[5]: tất cả được khởi tạo là 1
### Giải pháp cho bài toán
![[Pasted image 20250406214039.png]]
![[Pasted image 20250406214132.png]]
Vấn đề: Nếu như cả 5 triết gia cùng đồng thời cầm chiếc đũa bên tay trái, hoặc phải --> Deadlock 
**Một số giải pháp tránh deadlock**
- Cho phép tối đa 4 triết gia ngồi vào bàn 
- Chỉ cho phép triết gia cầm dũa khi cả 2 chiếc đũa sẵn sàng --> Cần phải thực hiện hành động cầm đũa trong CS 
	- Giải pháp bất đối xứng: Triết gia ngồi vị trí lẻ cầm đũa bên trái trước, sau đó cầm dũa bên phải, trong khi triết gia ngồi vị trí chẵn cầm đũa bên phải trước, sau đó cầm đũa bên trái
- Cần phải lưu ý tình trạng starvation vẫn có thể xảy ra
#### Giải pháp sử dụng monitor 
- Triết gia có thể cầm đũa khi cả 2 chiếc đã sẵn sàng 
- Khai báo kiểu dữ liệu 
	- enum {thinking; hungry, eating} state \[5];
- Triết gia thứ i chỉ có thể đặt trạng thái state[i] = eating khi cả 2 người kế bên đang khoogn ăn 
- ![[Pasted image 20250406214713.png]]
- Khai báo condition self\[5]: cho phép triết gia thứ i tự trình hoãn khi mình bị đói nhưng không thể cầm đũa
- ![[Pasted image 20250406214851.png]]
- Không phải các tài nguyên trong máy lúc nào cũng đáp ứng đủ nhu cầu của người dùng 