### Ứng dụng hỗ trợ tra cứu, hỏi đáp tri thức pháp luật
  Xây dựng ứng dụng hỗ trợ người dùng tra cứu, hỏi đáp tri thức pháp luật dựa trên nguồn dữ liệu được khai thác từ Bộ Pháp điển Việt Nam và CSDL văn bản QPPL. 
### Thành viên thực hiện
 Tên trường: Trường Đại học Mở Hà Nội<br>
 Thành viên thực hiện đề tài:
 <ul>
  <li>Nguyễn Đình Dũng</li>
  <li>Nguyễn Hải Đăng</li>
  <li>Hoàng Minh Hiếu</li>
 </ul>
  
### Chi tiết ý tưởng
 <ul>
 <li>Sử dụng các phần mềm Python, Rasa, MongoDB để build môi trường phát triển.</li>
 <li>Thiết lập một số thông tin: Chủ đề, chỉ mục.</li>
 <li>Hỗ trợ tra cứu, xem các nội dung văn bản QPPL đang có hiệu lực theo trật tự sắp xếp về chủ đề, đề mục, chỉ mục và các điều giống như Bộ Pháp điển Việt Nam. Cho phép người dùng thực hiện phản hồi lại thông tin về mức độ chính xác của các gợi ý sắp xếp để phần mềm có thể ghi nhớ và đưa ra các cải tiến về sắp xếp phù hợp hơn cho các lần tiếp theo.</li>
 <li>Phần mềm tự động trích rút các thuật ngữ, từ ngữ được định nghĩa và sử dụng trong các văn bản QPPL.</li>
 <li>Cho phép người dùng tìm kiếm nhanh để xem các nội dung văn bản QPPL liên quan theo các gợi ý về từng nhóm vấn đề và từ khóa chính hay được sử dụng trong hệ thống tri thức pháp luật của Việt Nam.
 </li>
 <li>Hỗ trợ trả lời các câu hỏi của người dùng về pháp luật dựa trên việc trích rút tri thức từ các văn bản QPPL hiện đang có hiệu lực.</li>
 </ul>

### Môi trường phát triển
 <ul>
  <li>Python</li>
  <li>Rasa</li>
  <li>MongoDB</li>
  <li>Git/Github</li>
 </ul>

### Thiết lập môi trường phát triển
 Đầu tiên ta clone project về<br>
 $ git clone git@github.com:NHD472004/application_tracuuhoidapphapluat.git<br>
 Trước khi cài đặt môi trường ảo, chúng ta cần cài đặt các chức năng bổ sung:<br>
 $ sudo apt install python3.11-full<br>
 Mở project vừa clone về, sau đó cài đặt môi trường ảo:<br>
 $ python3 -m venv env<br>
 $ source env/bin/activate<br>
 Cài đặt các thư viện,framework cho project:<br>
  Framework: FastAPI<br>
 $ pip3 install fastapi<br>
 $ pip3 install uvicorn<br>
  Framework: Rasa<br>
 $ pip3 install rasa<br>
  nếu bị lỗi: "MovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0." thì cài thêm:<br>
 $ pip3 install sqlalchemy==1.4.0<br>
  Kết nối python với CSDL MongoDB, dùng thư viện pymongo<br>
 $ pip3 install "pymongo[srv]"<br>

### Hướng dẫn sử dụng
 Xem hướng dẫn sử dụng tại Hướng dẫn sử dụng
### LICENSE
 See <a href="https://github.com/NHD472004/application_tracuuhoidapphapluat/blob/main/LICENSE">LICENSE</a> file for more information.