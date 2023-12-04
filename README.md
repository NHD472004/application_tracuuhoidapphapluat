### Ứng dụng hỗ trợ tra cứu, hỏi đáp tri thức pháp luật
  Xây dựng ứng dụng hỗ trợ người dùng tra cứu, hỏi đáp tri thức pháp luật dựa trên nguồn dữ liệu được khai thác từ Bộ Pháp điển Việt Nam và CSDL văn bản QPPL. 
### Thành  viên thực hiện
 Tên trường: Trường Đại học Mở Hà Nội
 Thành viên thực hiện đề tài:
  . Nguyễn Đình Dũng
  . Nguyễn Hải Đăng
  . Hoàng Minh Hiếu
### Chi tiết ý tưởng
 . Sử dụng các phần mềm Python, Rasa, MongoDB để build môi trường phát triển.
 . Thiết lập một số thông tin: Chủ đề, chỉ mục.
 . Hỗ trợ tra cứu, xem các nội dung văn bản QPPL đang có hiệu lực theo trật tự sắp xếp về chủ đề, đề mục, chỉ mục và các điều giống như Bộ Pháp điển Việt Nam. Cho phép người dùng thực hiện phản hồi lại thông tin về mức độ chính xác của các gợi ý sắp xếp để phần mềm có thể ghi nhớ và đưa ra các cải tiến về sắp xếp phù hợp hơn cho các lần tiếp theo.
 . Phần mềm tự động trích rút các thuật ngữ, từ ngữ được định nghĩa và sử dụng trong các văn bản QPPL.
 . Cho phép người dùng tìm kiếm nhanh để xem các nội dung văn bản QPPL liên quan theo các gợi ý về từng nhóm vấn đề và từ khóa chính hay được sử dụng trong hệ thống tri thức pháp luật của Việt Nam.
 . Hỗ trợ trả lời các câu hỏi của người dùng về pháp luật dựa trên việc trích rút tri thức từ các văn bản QPPL hiện đang có hiệu lực.
### Môi trường phát triển
 . Python
 . Rasa
 . MongoDB
 . Git/Github
### Thiết lập môi trường phát triển
 Đầu tiên ta clone project về
 $ git clone https://github.com/dinhdungne1/mi22ad.git
 Trước khi cài đặt môi trường ảo, chúng ta cần cài đặt các chức năng bổ sung:
 $ sudo apt install python3.11-full
 Mở project vừa clone về, sau đó cài đặt môi trường ảo:
 $ python3 -m venv env
 $ source env/bin/activate
 Cài đặt các thư viện,framework cho project:
  Framework: FastAPI
 $ pip3 install fastapi
 $ pip3 install uvicorn
  Framework: Rasa
 $ pip3 install rasa
  nếu bị lỗi: "MovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0." thì cài thêm:
 $ pip3 install sqlalchemy==1.4.0
  Kết nối python với CSDL MongoDB, dùng thư viện pymongo
 $ pip3 install "pymongo[srv]"

### Hướng dẫn sử dụng
 Xem hướng dẫn sử dụng tại Hướng dẫn sử dụng
### LICENSE
 See LICENSE file for more information.