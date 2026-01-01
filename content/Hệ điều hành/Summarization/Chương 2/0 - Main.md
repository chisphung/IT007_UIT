# Các thành phần của hệ điều hành
	Tiến trình là một chương trình đang học động
- Quản lý tiến trình - Task Manager 
![[Pasted image 20250408192922.png]]
- Quản lý bộ nhớ chính  - Resource Monitor
![[Pasted image 20250408192345.png]]

- Quản lý file - Window Explorer![[Pasted image 20250408192907.png]]
- Quản lý hệ thống IO - Device Manager
![[Pasted image 20250408192848.png]]
- Quản lý hệ thống lưu trữ thứ cấp (HDD,  SSD) - Disk manager
![[Pasted image 20250408192832.png]]
- Hệ thống bảo vệ - Windows Defender
![[Pasted image 20250408192747.png]]
- Hệ thống thông dịch lệnh - Command Prompt
![[Pasted image 20250408193007.png]]
## [[1 - Cấu trúc hệ thống ]]

| **Structure**        | **Example**          | **Pros**                                           | **Cons**                                                 |
| -------------------- | -------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| **Simple Structure** | MS-DOS               | - Easy to design and implement                     | - No modularity → one failure can crash entire system    |
| **Monolithic**       | Early UNIX           | - High performance due to direct communication     | - Hard to debug & maintain due to **tight coupling**     |
| **Layered**          | THE OS               | - Clear modularity → easy to debug and maintain    | - Slower performance due to layer-by-layer communication |
| **Microkernel**      | QNX, Minix           | - High security, fault isolation, easier to extend | - Overhead from user ↔ kernel mode switches and IPC      |
| **Modular**          | Modern Linux kernels | - Flexible: load/unload modules as needed          | - Managing dependencies between modules can be tricky    |
| **Hybrid**           | Windows NT, macOS    | - Best of both monolithic & microkernel worlds     | - Complexity: may inherit cons from both approaches      |
## References:
- Full text - [[Chương 2 - Cấu trúc hệ điều hành]]
