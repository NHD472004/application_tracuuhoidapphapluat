def search_definition(text, keyword):
    # Chia văn bản thành các câu
    sentences = text.split('. ')

    # Tìm kiếm từ khóa trong các câu
    for sentence in sentences:
        if keyword in sentence:
            return sentence

    # Trả về thông báo nếu không tìm thấy
    return "Không tìm thấy định nghĩa cho từ này trong pháp điển."

# Ví dụ
dictionary_text = """
1. Quốc môn là cổng quốc gia, được xây dựng tại cửa khẩu, mang đặc trưng văn hóa Việt Nam, thể hiện độc lập dân tộc và là biểu tượng tình hữu nghị, đoàn kết với nước láng giềng.
2. Cửa khẩu biên giới đất liền (sau đây gọi tắt là cửa khẩu biên giới hoặc cửa khẩu) là nơi thực hiện việc xuất cảnh, nhập cảnh, xuất khẩu, nhập khẩu và qua lại biên giới quốc gia trên đất liền. Một cửa khẩu biên giới có thể bao gồm một hoặc nhiều loại tính chất hoạt động: Cửa khẩu đường bộ, cửa khẩu đường sắt và cửa khẩu đường thủy nội địa
3. Cửa khẩu đường thủy nội địa (cửa khẩu đường thủy/cửa khẩu đường sông) là cửa khẩu biên giới được mở trên các tuyến đường thủy đi qua đường biên giới quốc gia trên đất liền
4. Khu vực cửa khẩu biên giới đất liền (sau đây gọi tắt là khu vực cửa khẩu) là khu vực được xác định, có một phần địa giới hành chính trùng với đường biên giới quốc gia trên đất liền, trong đó bao gồm các khu chức năng để đảm bảo cho các hoạt động quản lý nhà nước và hoạt động dịch vụ, thương mại tại cửa khẩu.
"""

keyword_to_search = "Quốc hội"
definition_result = search_definition(dictionary_text, keyword_to_search)

print(f"{keyword_to_search} là: {definition_result}")
