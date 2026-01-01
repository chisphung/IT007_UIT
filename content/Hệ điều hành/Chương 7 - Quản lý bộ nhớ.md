## Khái niệm cơ sở
- Chương trình phải được mang vào trong bộ nhớ và đặt nó trong một tiến trình để được xử lý 
- Input Queue - Một tập hợp của những tiến trình trên đĩa mà đang chờ để được mang vào trong bộ nhớ để thực thi 
- User programs trải quả nhiều bước trước khi được xử lý

![[Pasted image 20250429075923.png]]

Hệ điều hành sẽ chiếm một phần của ram, tương tự đối với các tiến trình được cấp phát, 
Tiến trình được hệ điều hành cấp phát địa chỉ nền, từ địa chỉ nền + limit -> khoảng giới hạn của tiến trình 
**Địa chỉ dùng để định vị vị trí, ánh xạ đến từng dòng code hoặc đến biến ở trong chương trình**
___
- **Quản lý bộ nhớ** là công việc của hệ điều hành với sự hỗ trợ của phần cứng nhằm phân phối, sắp xếp các tiến trình trong bộ nhớ sao cho hiệu quả 
- **Mục tiêu cần đạt được**: nạp càng nhiều tiến trình v ào bộ nhớ càng tốt
- Trong hầu hết các hệ thống, **kernel sẽ chiếm một phần cố định của bộ nhớ,** phần còn lại phân phối cho các tiến trình --> Không phải thiết bị nào cũng cần hệ điều hành, bởi bản thân hệ điềuh ành cũng chiếm một phần bộ nhớ 
___
**Các yêu cầu đối với quản lý bộ nhớ**
- Cấp phát bộ nhớ cho các tiến trình 
- Tái định vị (relocation): khi swapping 
	- Trong medium-term scheduling, có swap-in, swap-out
	- Lúc swap-in, swap-out --> mất địa chỉ cũ do đã cấp phát cho tiến trình khác, phải đặt vào vị trí mới -> relocation 
- Bảo vệ: kiểm tra truy xuất bộ nhớ có hợp lệ không
	- Kiểm tra address có lơn hơn base bé hơn limit ko:  $$base\le address < limit$$
	- ![[Pasted image 20250429081956.png]]
- Chia sẻ: cho phép các tiến trình chia sẻ vùng nhớ chung 
- Kết gán địa chỉ nhớ luận lý của user vào địa chỉ thực --->
___
- **Địa chỉ vật lý**: là một vị trí thực trong bộ nhớ chính (cầm cây RAM lên, chỉ định địa chỉ trong thực tế)
- **Địa chỉ luận lý**: là một vị trí nhớ được diễn tả trong một chương trình (còn được gọi là virtual address), một địa chỉ luận lý có thể được ánh xạ ra các địa chỉ vật lý khác nhau
	- Các compiler tạo ra mã lệnh chương trình trong đó, mọi tham chiếu bộ nhớ đều là địa chỉ luận lý 
	- Khi compile một file, các địa chỉ trong file executable đều là địa chỉ luận lý
- **Địa chỉ tuyệt đối**: địa chỉ tương đương với địa chỉ thực 
- **Địa chỉ tương đối**: relocatable, là một dạng của địa chỉ luận lý, trong đó các địa chỉ được biểu diễn tương đối so với một vị trí xác định nào đó trong chương trình
```cpp 
int a = 100;
pid_t pid = fork()
if (pid > 0){
	a += 50;
	printf(&a);
	printf(a);
}else{
	a-=50;
	prinf(&a);
	printf(a);
}
```
```output
parent process = 150 
child process = 50 
&a parent = &a child 
```
Cùng là địa chỉ luận lý, nhưng tiến trình cha và con có giá trị khác nhau. Địa chỉ luận lý chỉ có giá trị trong một tiến trình
___
Địa chỉ truyền vào là địa chỉ vật lý: ![[Pasted image 20250429085523.png]]
![[Pasted image 20250512163800.png]]
___
**Nạp chương trình vào bộ nhớ:**
- Bộ linker: kết hợp các obj thành file nhị phân khả thực thi gọi là module, ngoài ra còn liên kết các thư viện trong hệ thống 
- Bộ loader: nạp module vào bộ nhớ chính
![[Pasted image 20250511222632.png]]
## Chuyển đổi địa chỉ 
	Là quá trình ánh xạ một địa chỉ từ không gian địa chỉ này sang không gian địa chỉ khác 
**Biểu diễn địa chỉ nhớ**
- Trong source code: symbolic (các biến, hằng, pointer)
- Trong thời điểm biên dịch, thường là địa chỉ khả tái định vị 
	- Ví dụ: a ở vị trí 12 byte so với vị trí bắt đầu module
- Thời điểm linking/loading: có thể là địa chỉ thực
	- Ví dụ: dữ liệu nằm tại địa chỉ bộ nhớ thực 2030

![[Pasted image 20250429090342.png]]

- Địa chỉ lệnh và dữ liệu được chuyển đổi thành địa chỉ thực có thể xảy ra tại 3 thời điểm khác nhau: 
	- **Compile time**: nếu biết trước địa chỉ bộ nhớ của chương trình thì có thể gán địa chỉ tuyệt đối lúc biên dịch
		- VD: chương trình .COM của MSDOS
		- Khuyết điểm: phải biên dịch lại nếu thay đổi địa chỉ nạp chương trình
	- **Load time**: vào thời điểm loading, loader phải chuyển đổi địa chỉ khả tái định vị thành địa chỉ thực dựa trên một địa chỉ nền  
		- Địa chỉ thực được tính toán vào thời điểm nạp chương trình (ở đây, biết được địa chỉ nền rồi)
		- Phải reload nếu địa chỉ nền thay đổi
	- **Execution time**: khi trong quá trình thực thi, tiến trình có thể được di chuyển từ segment này sang segment khác trong bộ nhớ thì quá trình chuyển đổi được trì hoãn đến thời điểm thực thi
		- (diễn ra trong quá trình swapping hay [thay đổi segment])
		- Cần sự hỗ trợ của phần cứng cho việc ánh xạ địa chỉ 
			- Ví dụ: Trường hợp địa chỉ luận llys là relocatable thì có thể dùng thanh ghi base và limit 
		- Sử dụng trong đa số các OS đa dụng trong đó có các cơ chế swapping, paging, segmentation
- ![[Pasted image 20250429091012.png]]
### Dynamic linking 
- Quá trình link đến một module ngoài được thực hiện sau khi đã tạo xong load module 
	- Trong Windows: module ngoài là các .dll của 
	- Trong UNIX, là các file .so
- Load module chứa các stub tham chiếu đến routine của external module 
	- Lúc thực thi, khi stub được thực thi lần đầu (do process gọi routine lần đầu), stub nạp routine vào bộ nhớ, tự thay thế bằng địa của routine và routine được thực thi 
	- Các lần gọi routine sau sẽ bình thường 
- Stub cần sự hỗ trợ của OS (như kiểm tra xem routine đã được nạp vào bộ nhớ chưa)
**Ưu điểm:**
- Thông thường external module là một thư viện cung cấp các tiện ích của OS. Các chương trình thực thi có thể dùng các phiên bản khác nhau của external module mà không cần sửa đổi, biên dịch lại
- Chia sẻ mã (code sharing): một external module chỉ cần nạp vào bộ nhớ một lần
	- Các process cần dùng external module này thì cùng chia sẻ đoạn mã của external module --> tiết kiện không gian nhớ và đĩa 
	- Phương pháp dynamic linking cần sự ==hỗ trợ của OS== trong việc kiểm tra xem một thủ tục nào đó có thể được chia sẻ giữa các process hay là phần mã của riêng một process (bởi vì chỉ có OS mới có quyền thực hiện việc kiểm tra này)

### Dynamic loading 
	Thay vì nạp toàn bộ tiến tình vào trong ram, chỉ nạp những gì cần thiết 
- ==Chỉ khi nào cần được gọi đến thì thủ tục mới được nào vào bộ nhớ chính -> tăng độ hiệu dụng của bộ nhớ vì thủ tục không được gọi đến sẽ không chiếm chỗ trong bộ nhớ== 
- Rất hiệu quả trong trường hợp tồn tại khối tượng lớn mã chương trình có tần suất sử dụng thấp, không được sử dụng thường xuyên (ví dụ các thủ tục xử lý lỗi) 
- ==Hỗ trợ từ hệ điều hành==
	- ==Thông thường, user chịu trách nhiệm thiết kế và thực hiện các chương trình có dynamic loading== 
	- ==Hệ điều hành chủ yếu cung cấp một số thủ tục thư viện hỗ trợ, tạo điều kiện dễ dàng hơn cho lập trình viên== 
### So sánh Dynamic linking và Dynamic Loading

| **Tiêu chí**               | **Dynamic Loading**                                                                                 | **Dynamic Linking**                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **1. Thời điểm thực hiện** | Xảy ra **trong thời gian chạy (runtime)** khi đoạn mã cần thiết được gọi đến.                       | Xảy ra **trong thời gian chạy (runtime)**, khi liên kết với thư viện ngoài hoặc module.                                           |
| **2. Hỗ trợ của HĐH**      | Không **bắt buộc hệ điều hành phải hỗ trợ**, có thể được cài đặt ở cấp độ người dùng hoặc thư viện. | **Cần sự hỗ trợ của hệ điều hành**, đặc biệt là trình liên kết (linker/loader) và quản lý thư viện dùng chung (shared libraries). |
___ 
## Mô hình quản lý bộ nhớ 
- Ở đây, mô hình quản lý bộ nhớ làm ô hình đơn giản, không có bộ nhớ ảo 
- Mỗi tiến trình phải được nạp hoàn toàn vào bộ nhớ thì mới được thực thi
- Các cơ chế quản lý bộ nhớ 
	- fixed partitioning
	- dynamic partitioning 
	- simple paging
	- simple segment
### Fixed partitioning 
- Khi khởi động hệ thống, bộ nhớ chính được chia thành nhiều phần rời nhau được gọi là các partition có kích thước bằng nhau hoặc khác nhau 
- Process nào có kích thước nhỏ hơn hoặc bằng kích thước partition thì có thể được nạp vào partition đó 
- Nếu chương trình có kích thước lớn hơn partition thì phải dùng cơ chế overlay :
	- Cơ chế overlay là tìm phần giao giữa các tiến trình để load
- Nhận xét: 
	- Không hiệu quả do bị phân mảnh nội: một chương trình dù lớn hay nhỏ đều được cấp phát trong một partition
### Phân mảnh
- **Phân mảnh ngoại:**
	Khoảng dư của bộ nhớ không thuộc vào tiến trình nào, hai vùng nhớ ở hai vị trí khác nhau (phân mảnh), cần thực hiện kết khối để gom các  vùng nhớ lại 
	- Kích thước không gian nhớ còn trống đủ để thỏa mãn một yêu cầu cấp phát, tuy nhiên, không gian nhớ này không liên tục --> có thể dùng cơ chế kết khối để gom thành vùng nhớ liên tục 
	- Giải pháp: dùng cơ chế compaction (gom các vùng trống lại)
- **Phân mảnh nội:**
	- Kích thước vùng nhớ được cấp phát có thể hơi lớn hơn vùng nhớ yêu cầu 
	- Hiện tượng phân mành nội xảy ra khi bộ nhớ được chia thành các khối kích thước cố định và các tiến trình được cấp phát theo đơn vị khối. Ví dụ: cơ chế phân trang (paging)![[Pasted image 20250512143833.png]]
	- Giải pháp: dùng chiến lược placement
### Fixed partition
	Bộ nhớ chia thành các  block, các block có thể có cùng dung lượng bộ nhớ hoặc khác nhau 
	Khi cấp tiến trình vào, lựa chọn block phù hợp với tiến trình đó 
- Nếu process có kích thước lớn hơn: dùng cơ chế overlay
- Nhận xét: kém hiệu quả do phân mảnh nội
- Chiến lược placement: 
	- Partition có kích thước bằng nhau
		- Với partition trống -> nạp vào 
		- Không còn partition trống -> swap process đang bị blocked ra bộ nhớp phụ, nhường chỗ cho process mới    
	- Partition có kích thước khác nhau: 
		- Giải pháp 1
			- Gán mỗi tiến trình vào partition nhỏ nhất phù hợp với nó 
			- Có hàng đợi cho mỗi partition 
			- Giảm thiểu phân mảnh nội 
			- Vấn đề: có thể có một số hàng đợi trống không (vì không có tiến trình với kích thước tương ứng) và hàng đợi dày đặc
			
			![[Pasted image 20250512165523.png]]

		- Giải pháp 2
			- Chỉ có một hàng đợi chung cho mọi partition 
			- Khi cần nạp một tiến trình vào bộ nhớ chính 
			- --> Chọn partition nhỏ nhất còn trống
			
			![[Pasted image 20250512165535.png]]

### Dynamic partition 
	Cần bao nhiêu bộ nhớ --> cấp bấy nhiêu 
Gây ra hiện tượng phân mảnh ngoại

![[Pasted image 20250512165608.png]]
___
**Các chiến lược placement:** 
- Best-fit: vừa vặn nhất thì chọn
- First-fit: chọn khối đầu tiên nhìn thấy  
- Next-fit: từ vị trí trước đó tới vị trí cuối cùng
- Worst-fit: chọn khối nhớ trống lớn nhất
## Cơ chế phân trang 
- Cơ chế cấp phát bộ nhớ không liên tục
- Chia bộ nhớ vật lý thành các khối cố định, gọi là các khung trang 
- Chia bộ nhớ luận lý thành các khối bằng nhau gọi là các trang 
	- Kích thước của page bằng kích thước của frame 
- Chương trình có N trang cần N khung trống trong bộ nhớ để nạp vào 
- Thiết lập bảng phân trang để ánh xạ địa chỉ luận lý thành địa chỉ thực 
### Chuyển đổi địa chỉ trong paging 
- Địa chỉ luận lý gồm có 
	- Số hiệu trang (page number) p 
	- Địa chỉ tương đối trong trang (page offset) d 
- Nếu kích thước của không gian địa chỉ ảo là 2^m,  và kích thước của trang là 2^n
	- ![[Pasted image 20250506092139.png]]
- Dựa trên mô hình này, tính toán được có bao nhiêu trang 
- Bảng trang sẽ có tổng cộng 2^m/2^n = 2^m-n
	- Ánh xạ trang nào ở vị trí nào 
![[Pasted image 20250506093255.png]]
![[Pasted image 20250506093308.png]]
## Cài đặt bảng trang 
- Bảng phân trang thường được lưu giữ trong bộ nhớ chính 
	- Mỗi process được hệ điều hành cấp một bảng p;hân trang 
	- Thanh ghi page-table base (PTBR) trỏ đến bảng phân trang
	- Thanh ghi page-table length (PTLB) biểu thị kích thước của bảng phân trang (có thể dduocj dùng trong cơ chế bảo vệ bộ nhớ)
- Theo cơ chế cài đặt này thì một thao tác truy cập lệnh hoặc dữ liệu cần đến 2 lần truy cập bộ nhớ chính 
	- Lần 1 cho bảng trang 
	- Lần 2 cho lệnh hoặc dữ liệu 
- Thương dùng một bộ phân cache phần cứng có tốc độ truy xuất và tìm kiếm cao, gọi là thanh ghi kết hơp (associative register) hoặc translation look-aside buffers (TLBs)
- Dùng thanh ghi Page-Table Base Register (PTBR)![[Pasted image 20250512150932.png]]
- DÙng TLB ![[Pasted image 20250512151003.png]]
## Effective access time (EAT)
- Tính thời gian truy xuất hiệu dụng (effective access time, EAT)
- Thời gian tìm kiếm trong TLB (associative lookup): `epsilon` 
- Thời gian một chu kỳ truy xuất bộ nhớ  `x`
- Hit ratio: tỉ số giữa số lần chỉ số trang được tim fthayas (hit) trong TLB và số lần truy xuất khởi nguồn từ CPU 
	- Kí hiệu hit ratio: `alpha` 
- Thời gian cần thiết để có được chỉ số frame 
	- Khi chỉ số trang có trong TLB (hit): epsilon + x
	- Khi chỉ số trang không có trong TLB (miss): epsilon + x + x
	- Thời gian truy xuất hiệu dụng:
		- ![[Pasted image 20250512151541.png]]
- Ví dụ: 
- ![[Pasted image 20250512151714.png]]
## Tổ chức bảng trang 
- Các hệ thống hiện đại đều hỗ trợ không gian địa chỉ ảo rất lớn (2^32 đến 2^64), ở đây giả sử là 2^32 
	- Giả sử kích thước trang nhớ là 4KB (2^12)
	- --> Bảng phân trang sẽ có 2^32/2\^12= 2^20 = 1M mục
	- Giả sử mỗi mục gồm 4 byte thì mỗi process cần 4MB cho bảng phân trang 
		- Ví dụ: phân trang 2 cấp
		- ![[Pasted image 20250512152017.png]]
		- Bảng phân trang nghịch đảo![[Pasted image 20250512152131.png]]
## Bảo vệ bộ nhớ 
- Việc bảo vệ bộ nhớ được thực hiện bằng cách gắn với frame các bit bảo vệ (protection bits) được giữ trong bảng phân trang. 
- Các bit này biểu thị các thuộc tính sau
	- readonly, read-write, execute-only 
- Ngoài ra, còn có một valid/invalid bit gắn với mỗi mục trong bảng phân trang
	- valid: cho biết là trang của process, dó đó là một trang hợp lệ 
	- invalid: cho biết là trang không của process , do dó là một trang không hợp lệ 
	- ![[Pasted image 20250512152618.png]]
## Chia sẻ các trang nhớ: 
Ví dụ: có 3 process, nếu như, các vùng code giống nhau, chỉ khác nhau data, nếu 3 tiến trình cùng chạy, process 1 nạp lên bộ nhớ, process 2 không cần nạp thêm mà cập nhập bảng trang giống như process 1![[Pasted image 20250512152836.png]]
Ví dụ như mở một file word, mở thêm một file khác thì không cần load lại chương trình word là chỉ cần nạp data của file word thứ hai
## Cơ chế hoán vị (swapping)
reference: [[2 - Các loại định thời]]
Một process có thể tạm thời bị swap ra khởi bộ nhớ cính và lưu trên một hệ thống lưu trữ phụ. Sau đó, process có thể được nạp lại vào bộ nhớ để tiếp tục quá trình thực thi 
Swapping policy: hai ví dụ
- Round Robin: swap out P1 (vừa tiêu thụ hết quantum của nó), swap in P2, thực thi P3, ...
- Roll out, roll in: dùng trong cơ chế định thời theo độ ưu tiên (priority-based scheduling)
	- Process có độ ưu tiên thấp hơn sẽ bị swap out và nhường chỗ cho process có độ ưu tiên cao hơn mới đến được nào vào bộ nhớ để thực thi
- Hiện nay, ít hệ thống sử dụng cơ chế swapping trên 
![[Pasted image 20250512154238.png]]
___
## Quizz:
![[Pasted image 20250511221612.png]]
![[Pasted image 20250511221903.png]]
![[Pasted image 20250511221918.png]]
![[Pasted image 20250511222830.png]]![[Pasted image 20250512143354.png]]
![[Pasted image 20250512144443.png]]
![[Pasted image 20250512144537.png]]
![[Pasted image 20250512150114.png]]
![[Pasted image 20250512150421.png]]
![[Pasted image 20250512153639.png]]
![[Pasted image 20250512172058.png]]
![[Pasted image 20250512172457.png]]
![[Pasted image 20250512172527.png]]
![[Pasted image 20250512173235.png]]

___
## The next week: 
- Complete the remaining course in learning log 
- Học bù 

