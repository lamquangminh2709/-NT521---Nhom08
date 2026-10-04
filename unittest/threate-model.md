# Mô hình Mối đe dọa: Thành phần tìm kiếm Đệ quy JSON

## 1. Ngữ cảnh Hệ thống & Tác nhân Đe dọa
Hàm `json_search()` đóng vai trò là một công cụ truy xuất dữ liệu, xử lý các payload JSON thô xuất phát từ API giám sát hạ tầng mạng. 
* **Tác nhân/Vai trò (Actors/Roles):** Hệ thống được gọi bởi các thực thể nội bộ đã xác thực với các mức đặc quyền khác nhau, cụ thể là: `admin`, `operator`, và `viewer`.
* **Mục đích của Tác nhân:** Truy vấn và trích xuất các số liệu vận hành, trạng thái mạng hoặc chi tiết cấu hình từ dữ liệu trả về.

## 2. Tài sản trong phạm vi (Assets in Scope)
Payload JSON chứa dữ liệu có mức độ nhạy cảm hỗn hợp. Các tài sản quan trọng đòi hỏi tính bảo mật nghiêm ngặt bao gồm:
* **Bí mật Xác thực:** Các khóa mật mã như `apiKey` hoặc chuỗi xác thực SNMP.
* **Định danh Hạ tầng:** Địa chỉ IP quản trị (Management IP) và thông tin định danh thiết bị duy nhất.

## 3. Ranh giới Tin cậy (Trust Boundaries)
Hàm `json_search()` là một **Ranh giới Tin cậy** cốt lõi. Nó hoạt động như một trạm trung chuyển dữ liệu giữa payload chưa được lọc và lớp ứng dụng của người dùng cuối. 
* **Vi phạm Ranh giới:** Ranh giới này sẽ bị vi phạm hoàn toàn nếu hàm duyệt qua và trả về tất cả kết quả khớp mà không xác thực vai trò (role) của người gọi có hợp lệ với chính sách bảo mật hay không.

## 4. Phân tích Mối đe dọa (Theo phương pháp STRIDE)

### 4.1. Tiết lộ Thông tin (Information Disclosure)
* **Mối đe dọa:** Một người dùng có đặc quyền thấp (ví dụ: `viewer`) gọi hàm tìm kiếm nhằm mục tiêu vào các trường dữ liệu bị hạn chế (ví dụ: `apiKey`).
* **Lỗ hổng:** Việc thiếu vắng Cơ chế Kiểm soát Truy cập Dựa trên Vai trò (RBAC) trong quá trình trích xuất dữ liệu đệ quy.
* **Tác động:** Phơi bày trái phép các thông tin xác thực và bí mật hạ tầng mang tính nhạy cảm cao cho các tài khoản không có đủ thẩm quyền.

### 4.2. Leo thang Đặc quyền (Elevation of Privilege)
* **Mối đe dọa:** Một kẻ tấn công (hoặc tài khoản cấp thấp bị xâm nhập) tận dụng các thông tin xác thực thu thập được thông qua lỗ hổng Tiết lộ thông tin.
* **Tác động:** Kẻ tấn công sử dụng `apiKey` hoặc chuỗi SNMP bị lộ để vượt qua các cơ chế xác thực, qua đó leo thang đặc quyền để giành quyền kiểm soát quản trị đối với các thiết bị mạng và toàn bộ hạ tầng.
