---
share_link: https://share.note.sx/wpjsf2kp#6+dl0+lbHe5YXfpXlrSNP+wiO5yBc8MKd55QDnQ1Ra8
share_updated: 2025-04-28T19:37:57+07:00
---
## Basic commands: 
- pwd: Show the current address
- ls: list folder and files in the current folder 
	- ls -l: show files, folders and their attributes
	- ls -laht (address): 
		- l: listing
		- a: all
		- h: human readable
		- t: sort by time
- echo $SHELL: check the current shell 
## Path in linux: 
- cd:
	- cd ~: to home (/home/user)
	- ./ : the working directory
	- / : root directory
	- ~ : home directory
	- .. : the parent folder
	- absolute address: an address located from root
	- relative path: an address located from the current address

## Create and edit files: 
- touch: to create a file 
- vi, nano
	- nano (filename or path to)\
		- ^: ctrl
	- vi (filename or path to)
		- press i to insert
		- press esc and type :q to quit, :wq: to write and quit 
		- /(string that you want to find): to jump to the provided string
## Working with folder: 
- mkdir (folder name or path to folder )
	- -p: create folder in the current location and do not raise error if there is already a folder with the same name 
	- -m 777: with chmod 777
- chmod (option) (xxxxx)(file or folder)
	- r, read: 4
	- w, write: 2
	- x, execute: 1
	chmod = 755: 
	- 7, owner: 4 + 2 + 1
	- 5, same group: 4 + 0 + 1
	- 5, others: 4 + 0 + 1
	chmod a+r file: assign read to all users 
	chmod a+x file: assign execute to all users 
	chmod +rwx : asign to all users 
	chmod u=rwx,go= asign all permission to owner, group and others have no permission
	chmod 777 file: all users, all permission
### Other basic cmds 
- rm (file or folder ), -r with folder to recursively delete all items in it 
- cp (link) (link)
- mv (link) (link)
- echo (value )
	- echo (value) > (file): newly write to file 
	- echo (value) >> (file): concatenatingly write to file 
- cat (option) (file): print out in file or sthing 
	- cat (file) > (file)
	- cat (file) >> (file)
### User management 
- adduser (option) (username): 
- usermod (option) (user name): change personal info
- userdel (option) (username)
- Ta dùng lệnh useradd -m [username] để thêm một người dùng mới. 
- Thêm option -m để chắc chắn rằng user mới được tạo sẽ có thư mục home
- Lệnh passwd [username] để đặt mật khẩu cho user. Thực hiện các thao tác trên cho cả ba users ta đã tạo thành công ba users với tên tương ứng là user1, user2, user3.
    

**