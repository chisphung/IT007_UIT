## Parallelism 
- Thực hiện nhiều việc cùng lúc, trên nhiều core của CPU 
- Bản chất là làm nhiều việc cùng lúc 
![[Pasted image 20250524122923.png]]
## Concurrency
- Các tiến trình thực hiện xen kẻ với nhau trên một core của CPU 
- Công việc của CPU scheduling là sắp xếp tiến trình nào chạy trước, tiến trình nào chạy sau 
- Bản chất là xử lý nhiều việc cùng lúc
- Vấn đề: 
	- Đồng bộ giữa các tiến trình 
	- Tiến trình nào thực thi trước, tiến trình nào thực thi sau 
![[Pasted image 20250524123001.png]]
## Semaphore 
Có thể sử dụng semaphore để đông bộ việc chạy trước sau của tiến trình 
- Khi sử dụng semaphore.h thì phải khai báo thêm thư viện rt
	- Ví dụ: lúc biên dịch: `gcc -o filename filename.c -lpthread -lrt`
- Để tạo ra biến semaphore thì sử dụng sem_t 
	- `sem_t semm_name`
- Khởi tạo một biến semaphore thì dùng sem_init
	- `int sem_init(sem_t *sem_name, int pshared, unsigned int value)`
		- \*sem_name: con trỏ chỉ đến địa chỉ của biến semaphore 
		- pshared: 
			- Nếu được đặt là 0:  sem được chia sẻ giữa các tiểu trình của cùng một tiến trình (và cần đặt ở nơi mà tất cả các tiểu trình đêù có thể truy xuất được như biến toàn cục hoặc biến động)
			- Nếu được đặt khác 0: biến semaphore sẽ được chia sẻ giữa những tiến trình với nhau và cần đặt ở vùng nhớ được chia sẻ (shared memory)
			- value: giá trị khởi tạo cho semaphore là số không âm
			- return value:
				- 0 nếu thành công 
				- -1 nếu thất bại 
- sem_wait():
	- `int sem_wait(sem_t *sem);`
		- Nếu giá trị của semaphore = 0: tiến trình bị block cho đến khi giá trị của sem > 0 (Lưu ý: gí trị của semaphore không là số âm)
		- Nếu giá trị của sem > 0: giá trị của sem trừ đi 1 và return, tiến trình tiếp tục chạy
	- return value:
		- Là 0 nếu thành công 
		- Là -1 neues thất bại 
- Mở khóa 1 sem: `int sem_post(sem_t *sem);`
	- Lấy giá trị của semaphore và gán vào biến được xác định tại dịa chỉ valp
	- Giá trị trả về: 
		- Là 0 nếu thành công, là -1 nếu thất bại 
- Lấy giá trị của một semaphore: `int sem_getvalue(sem_t *sem, int *valp);`
	- Lấy giá trị của semaphore và gán vào biến được xác định tại địa chỉ valp
	- Giá trị trả về: 
		- Là 0 nếu thành công 
		- Là - 1 nếu thất bại 
- Hủy 1 biến semaphore: `int sem_destroy(sem_t *sem)`
	- Nêu đã quyết định hủy một biến em thì cần chắc chán không còn tiến trình hay tiểu trình nào truy xuất vào biến sem đó nữa 
	- return value: 
		- Là 0 nếu thành công 
		- Là -1 nếu thất bại 
## Ví dụ về semaphore 
Ví dụ có 2 process thực thi song song như sau: 
- Phải đảm bảo products >= sells 
![[Pasted image 20250524125649.png]]
- Vấn đề với chương trình khi không đông bộ: 
	- không đảm bảo được products luôn >= sells, do không đảm bảo tiến trình nào phải chạy trước/sau 
**Đồng bộ:**
```c
#include <pthread.h>
#include <stdio.h>
#include <semaphore.h>

int sells = 0, products = 0;
sem_t sem;

void *processA(void* mess){
		while(1){
			sem_wait(&sem);
			sells++;
			printf("Sells = %d\n", sells);
		}
	}
void *processB(void* mess){
		while(1){
			products++;
			printf("Products = %d\n)", products);
			sem_post(&sem);
		}
	}
int main(){
	sem_init(&sem, 0, 0);
	pthread_t pA, pB;
	pthread_create(&pA, NULL, &processA, NULL);
	pthread_create(&pB, NULL, &processB, NULL);
	while(1);
	return 0;
}
```

## Mutex 
Mutex là một trường hợp đơn giản của binary semaphore
![[Pasted image 20250524162136.png]]
- Nếu hai tiểu trinh không được đồng bộ thì có thể dẫn đến sai biến dùng chung 
- Khi thực hiện kiểm tra biến > 0 thì có 3 bước:
	- Nạp vào 
	- Kiểm tra 
	- Trả về
- Nếu đúng lúc nạp vào mà hết time slice thì process khác nạp vào, trừ đi giá trị, nhưng hai gía trị lúc nạp vào tại các thời điểm khác nhau, lúc trả về thì trả về giá trị sai
**Các hàm cơ bản khi sử dụng Mutex**
- pthread_mutex_t mutex_name: khai báo
- int pthread_mutex_init(pthread_mutex_t \*mutex, const pthread_mutexattr_t \*attr);
	- \*mutex: con trỏ chỉ đến địa chỉ của mutex 
	- \*attr: con trỏ chỉ đến địa chỉ nơi mà các thuộc tính cần khỏi tạo ban đầu. Để NULL thì mutex khởi tạo mặc định
	- return value:
		- 0 nếu thành công 
		- -1 nếu thất bại 
- int pthread_mutex_lock(pthread mutex t \*mutex); khóa 1 mutex
	- Truyền vào địa chỉ mutex
	- return value: 
		- 0 nếu thành công 
		- -1 nếu thất bại
- int pthread_mutex_unlock: mở khóa mutex
	- Truyền vào địa chỉ mutex
	- return value: 
		- 0 nếu thành công 
		- -1 nếu thất bại
- int pthread_mutex_destroy: hủy mutex
	- truyền vào địa chỉ mutex
![[Pasted image 20250524212956.png]]
![[Pasted image 20250524213434.png]]
- empty là số lượng ô trống 
- mutex được khởi tạo để đảm bảo mutual exclusion 
- full là số lượng ô đầy 
- wait(empty) để kiểm tra còn ô trống nào để thêm hay không 
- wait(full) để kiểm tra còn số lượng ô đầy nào để xóa hay không 
- signal(full) để tăng sem full lên do mới tăng biến count lên 
- signal(empty) để tăng empty lên do mới xóa
![[Pasted image 20250524213744.png]]
![[Pasted image 20250524213800.png]]

![[Pasted image 20250524163217.png]]
![[Pasted image 20250524163220.png]]

