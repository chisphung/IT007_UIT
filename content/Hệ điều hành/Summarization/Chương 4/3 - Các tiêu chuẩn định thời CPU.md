## Hướng người dùng 
- Thời gian đáp ứng: khoảng thời gian từ lúc tiến trình gửi yêu cầu thực thi đến khi yêu cầu được đáp ứng lần đầu tiên (trong các hệ thống time-sharing, interactive system) → cực tiểu
- Thời gian hoàn thành (Turnaround time): khoảng thời gian từ lúc một tiến trình được nạp vào hệ thống đến khi tiến trình đó kết thúc → cực tiểu
- Thời gian đợi (Waiting time): tổng thời gian một tiến trình đợi trong ready queue → cực tiểu
![[Pasted image 20250409182553.png]]
Gọi 𝑅, 𝐹, và 𝑊 lần lượt là thời gian đáp ứng, thời gian hoàn thành và thời gian đợi của tiến trình P. 
Khi đó: 
𝑹 = 𝒕𝟎 - 𝒓 
𝑭 = 𝒇 - 𝒓 
𝑾 = 𝒇 - 𝒓 - 𝑬 
**Thời gian chờ = thời gian hoàn thành - burst time** 
Trong đó 𝑬 là thời gian yêu cầu của P để thực thi trên CPU (hay CPU Burst)
𝑬 = 𝑬𝟏 + 𝑬𝟐 + 𝑬𝟑
## Hướng hệ thống 
- Khả năng tận dụng của CPU (processor utilization): định thời sao cho CPU càng bận càng tốt → cực đạ
- Tính công bằng (fairness): tất cả tiến trình phải được đối xử như nhau.
- Thông lượng (throughput): số tiến trình hoàn tất công việc trong một đơn vị thời gian → cực đại