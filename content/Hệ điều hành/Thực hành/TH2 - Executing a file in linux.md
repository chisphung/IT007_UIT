# Sử dụng shell như ngôn ngữ lập trình 
	Shell có thể được sử dụng như một ngôn ngữ lập trình. Có hai cách dùng
	- Chạy từ dòng lệnh 
	- Viết script

## Điều khiển shell bằng dòng lệnh
Nếu nhập chương trình dưới đây trong shell thì vẫn được, shell sẽ đợi cho đến khi người dùng nhập xong hết câu lệnh rồi mới thực hiện
```sh 
for file in * 
do 
ì grep - l 'main() ' $file
then 
	more $file 
fi 
done
```
Bất tiện: khi dùng dấu top arrow để xem lại dòng lệnh cũ thì sẽ có dạng 
```sh
$ for file in * ; do ; if grep -1 'main( )’ $file;
then ; more $file; fi; done
```
--> Viết bằng script
### Điều khiển shell bằng script
Cặp ký tự #! là chỉ thị yêu cầu shell hiện tại triệu gọi shell
sh nằm trong thư mục /bin.
```sh
# !/bin/ sh
# first.sh
# Script này sẽ tìm trong thư mục hiện hành các chuỗi mang nội dung
# main( ), nội dung của fìle sẽ được hiển thị ra màn hình nếu tìm thấy.
for file in *
do
if grep -l 'main( ) ' $file
then
more $fỉle
fi
done
```

### Thực thi script
Có hai cách thực thi script vừa tạo ra (first.sh)
Cách 1:
```
.first.sh
```
Tuy nhiên, trước hết cần cấp quyền thực thi 
```
chmod +x first.sh
```
Cách 2:  gọi trình shell với tên tập tin script làm đối số:
```
/bin/sh first.sh
```

## Cú pháp ngôn ngữ shell 
- Biến: string, integer, params, env 
- Điều kiện: boolean bằng shell 
- Điều khiển chương trình: if, elif, for, while, until, case
### Sử dụng biến
Lấy giá trị bằng cách truyền dấu $ 
```sh
xinchao=Hello
echo $xinchao
```
**Output:**
```
Hello
```
___
```sh
xinchao=12+1
echo $xinchao
```
**Ouput:**
```
12+1
```
___
*Lưu ý: 
- sau dấu = không được có dấu khoảng trắng. Nếu gán nội dung có dấu khoảng trắng, caaof bọc chuỗi bằng dấu " " 
- kiểu dữ liệu mặc định là string 
___
**Đọc dữ liệu nhập vào**
```sh
read youname 
# nhập vào XYZ
echo "Hello " $yourname
```
**Output:**
```
Hello XYZ
```
___
### Các ký tự đặc biệt 
#### Chuyển hướng vào/ra
![[Pasted image 20250428235527.png]]
**Ví dụ**
Xuất giá trị đầu ra của date vào file login.time 
```sh
date > login.time
```

```sh
cat < file1
```

## Các ký tự đặc biệt kiểm soát tiến trình 
- **Ampersand** (&): đặt tiến trình từ foreground sang background
- **Semicolon** (;) dùng để nhóm một số lệnh lại, phân cách bởi ; 
	- Ví dụ (date;who) > system.status
	- cat system.status
- **Backquotes** (\`) cho phép thực hiện lệnh được bọc nháy trước 
	- Ví dụ: echo Logged in \`date\` > login.time
	- Thực hiện date trước tiên, trước khi thực hiện các thành phần còn lại 
	- Tức: echo Logged in Fri May 12:52:25 UTC 2004 > login.time
- **Pipeline**: dấu |
	- Đầu ra của lệnh trước là đầu vào của lệnh sau:
	- Ví dụ: $who | ls - l 
	- đầu ra của who là đầu vào của ls -l
- **Quoting**(', "): trong trường hợp muốn bao gồm khoảng cách, dùng nháy đơn hoặc nháy kép 
	- Dấu nháy kép vẫn giữ giá trị của biến, dấu nháy đơn thì không
- **Backslash**(\\):  Loại bỏ ý nghĩa của lệnh
	- Ví dụ: `echo "messgae : \$myvar"` sẽ cho ra `mesage: $myvar`
### Biến môi trường
- **$HOME**: chứa nội dung của thư mục chủ 
- $**PATH**: Chứa danh sách các đường dẫn, Linux thường tìm các chương trình cần thực thi trong $PATH
- $**PS1**:  Dấu nhắc (Prompt) hiển thị trên dòng lệnh, thông thường là $
- cho: User không phải là root 
- $**SP2**:  Dấu nhắc thứ cấp, thông báo người dùng nhập thêm thông tin trước khi lệnh thực hiện, thường là dấu >
- $**IFS** (Internal Field Separator): Dấu phân cách các trường trong danh sách chuỗi. Biến này chứa danh sách các ký tự mà shell dùng tách chuỗi (thường là tham số trên dòng lệnh). Ví dụ $IFS thường chứa ký tự Tab, ký tự trắng hoặc ký tự xuống hàng
- $**0**: Chứa tên chương trình gọi trên dòng lệnh
- **$#:** Số tham số truyền trên dòng lệnh
- **\$$:** Mã tiến trình (PID ) của shell script thực thi, bởi số pid của tiến trình là duy nhất trên toàn hệ thống (vào lúc thực thi) nên thường các lệnh trong script dùng con số này để tạo tên các file tạm
### Biến tham số 
![[Pasted image 20250429001452.png]]**Ví dụ**
```sh
$IFS= "A"
$set foo bar bam
$echo “$@”
foo bar bam
$echo "$*"
fooAbarAbam
$unset IFS
$echo "$*"
foo bar bam
```

| Expression               | Output      | Why                                   |
| ------------------------ | ----------- | ------------------------------------- |
| `$@`                     | foo bar bam | Keeps each argument separate          |
| `$*`                     | fooAbarAbam | Joins args using `IFS="A"`            |
| `$*` (after `unset IFS`) | foo bar bam | Joins using default (space) separator |
| `$#`                     | 3           | nums of argument                      |
## Cấu trúc điều kiện
### Lệnh test hoặc \[ ]
**Lệnh test** 
``` sh
if test -f hello.c
	then
	 ...
fi
```
**Lệnh \[ ]**
```sh
if [ -f hello.c ]
then 
 ...
fi
```
### String comparision

| Comparision        | Result                                       |
| ------------------ | -------------------------------------------- |
| string1 = string2  | True if the 2 provided strings are equal     |
| string1 != string2 | True if the 2 provided strings are not equal |
| -n string1         | true if string1 not null                     |
| -z string1         | true if string1 null                         |
### Mathematical comparision 
![[Pasted image 20250429101818.png]]
### Condition in files 
| Cú pháp   | Ý nghĩa                                                               |
| --------- | --------------------------------------------------------------------- |
| `-d file` | Trả về **true nếu `file` là một thư mục**                             |
| `-e file` | Trả về **true nếu `file` tồn tại** trên đĩa (file hoặc folder)        |
| `-f file` | Trả về **true nếu `file` là một tập tin thông thường** (regular file) |
| `-g file` | Trả về **true nếu tập tin có cờ set-group-ID**                        |
| `-r file` | Trả về **true nếu tập tin cho phép đọc**                              |
| `-s file` | Trả về **true nếu kích thước của file lớn hơn 0**                     |
| `-u file` | Trả về **true nếu tập tin có cờ set-user-ID**                         |
| `-w file` | Trả về **true nếu tập tin cho phép ghi**                              |
| `-x file` | Trả về **true nếu tập tin có thể thực thi được** (executable)         |
**Ví dụ**
```sh
if [ -r myfile.txt ]; then
    echo "Tập tin có thể đọc được"
else
    echo "Tập tin không thể đọc"
fi
```
## Cấu trúc điều khiển 
Shell hỗ trợ các cấu trúc điều khiển tương tự ngôn ngữ lập trình như: `if`, `elif`, `for`, `while`, `until`, `case`. 

---
### Lệnh `if`
- **Công dụng:** Kiểm tra điều kiện đúng/sai để chọn lệnh thực thi.
- **Cú pháp:**
    ```sh
    if condition; then
      statements
    else
      statements
    fi
    ```
- **Ví dụ:** Kiểm tra người dùng nhập `"yes"` để chào buổi sáng, ngược lại chào buổi chiều.
###  Lệnh `elif`
- **Công dụng:** Mở rộng lệnh `if` để kiểm tra nhiều điều kiện khác nhau.
- **Ưu điểm:** Tránh việc mặc định mọi câu trả lời không phải `"yes"` là `"no"`.
- **Ví dụ:** Kiểm tra người dùng nhập `"yes"`, `"no"`, hoặc hiển thị thông báo lỗi với giá trị khác.
---
###  Vấn đề với biến rỗng
- **Lỗi phổ biến:** Khi biến rỗng (người dùng chỉ nhấn Enter), shell không hiểu điều kiện.
- **Giải pháp:** Luôn đặt biến trong dấu ngoặc kép `" "`
    ```sh
    if [ "$var" = "something" ]
    ```
---
### Lệnh `for`
- **Công dụng:** Duyệt qua một danh sách giá trị xác định trước.
- **Cú pháp:**
    ```sh
    for variable in value1 value2 ...; do
      statements
    done
    ```
- **Ví dụ:**
    - Duyệt qua chuỗi `"bar fud 13"`.
    - Duyệt qua các file bắt đầu bằng `f` và có đuôi `.sh` dùng `$(ls f*.sh)`
---
### Lệnh `while`
- **Công dụng:** Lặp lại khi điều kiện còn đúng, thích hợp khi không biết trước số lần lặp.
- **Cú pháp:**
    ```sh
    while condition; do
      statements
    done
    ```
- **Ví dụ:** Nhập mật khẩu đúng `"secret"` thì mới thoát vòng lặp.

---
- Shell không yêu cầu thụt dòng nhưng nên canh lề để mã dễ đọc.
- Khi xử lý chuỗi nhập liệu, luôn kiểm tra biến rỗng để tránh lỗi logic
- Có thể dùng `printf` thay cho `echo` nếu cần định dạng nâng cao.
---
