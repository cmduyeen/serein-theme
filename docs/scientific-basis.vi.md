# Cơ sở khoa học cho Serein Theme

Ngày đối chiếu: 12/11/2026. Tài liệu nguồn để viết README và giải thích quyết định thiết kế. Các diễn giải sửa sai ở đây và phần 4 của kế hoạch được ưu tiên hơn các khẳng định trong bản ý tưởng ban đầu.

## 1. Theme tác động được đến đâu?

Mục tiêu là hỗ trợ đọc rõ, giảm yếu tố gây khó chịu và giảm gián đoạn do giao diện. Theme chưa được thử nghiệm lâm sàng, không phải sản phẩm điều trị hoặc phòng bệnh mắt. Khả năng tập trung, sự dễ chịu, tốc độ đọc và độ hiểu là các kết quả khác nhau: không được dùng kết quả này để khẳng định kết quả kia.

## 2. Bằng chứng y tế và khoa học thị giác

### Mỏi mắt do thiết bị số có nhiều nguyên nhân

- **Nguồn:** American Academy of Ophthalmology (AAO), *Computers, Digital Devices, and Eye Strain*, 2024. [Bài hướng dẫn](https://www.aao.org/eye-health/diseases/computer-usage).
- **Loại nguồn:** hướng dẫn chuyên môn cho công chúng; không phải thử nghiệm theme.
- **Diễn giải:** nhìn gần kéo dài, chớp mắt và bề mặt mắt, độ sáng, phản chiếu, điều kiện thị lực và tư thế có liên quan đến khó chịu khi dùng màn hình.
- **Áp dụng:** hướng dẫn người dùng điều chỉnh môi trường, khoảng cách và nghỉ nhìn gần; không hứa theme giải quyết hết các nguyên nhân.

### Cỡ chữ phải đủ lớn để đọc trôi chảy

- **Nguồn:** Atilgan N, Xiong YZ, Legge GE (2020), *Reconciling print-size and display-size constraints on reading*. [Bài nghiên cứu](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720185/).
- **Loại nguồn:** nghiên cứu thực nghiệm về đọc, kích thước chữ và giới hạn hiển thị.
- **Diễn giải:** tốc độ đọc phụ thuộc đồng thời kích thước chữ và lượng ký tự hiển thị. Cỡ chữ nhỏ hơn ngưỡng phù hợp có thể làm chậm đọc; phóng to quá mức cũng làm giảm lượng nội dung trên dòng.
- **Áp dụng:** cho phép tăng cỡ chữ, thử ở khoảng cách sử dụng thật và kiểm tra dấu tiếng Việt. Terminal bắt đầu Cascadia Mono 14 pt, cellHeight 1.3; đây là lựa chọn thử, không phải kích thước được chứng minh tốt nhất.
- **Giới hạn:** pt của Windows Terminal khác CSS px; không suy ra cỡ nhìn thực từ số cấu hình duy nhất.

### Nhiễu thị giác có thể làm việc tìm và nhận diện thông tin khó hơn

- **Nguồn:** van den Berg R, Roerdink JBTM, Cornelissen FW (2009), *A crowding model of visual clutter*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/19757933/), [DOI](https://doi.org/10.1167/9.4.24).
- **Loại nguồn:** mô hình và thử nghiệm khoa học thị giác.
- **Áp dụng:** giới hạn trang trí, nhóm thông tin rõ, giao diện ổn định, giữ tín hiệu chức năng.
- **Giới hạn:** áp dụng vào theme là suy luận thiết kế; chưa chứng minh giao diện đơn sắc giúp tăng chú ý lâu dài. Không có căn cứ từ nguồn này cho tỷ lệ 90/8/2 hoặc tác dụng điều trị ADHD.

### Chữ tối trên nền sáng có lợi thế trong một số tác vụ đọc

- **Nguồn:** Piepenbrock C, Mayr S, Buchner A (2014), *Smaller pupil size and better proofreading performance with positive than with negative polarity displays*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25135324/), [DOI](https://doi.org/10.1080/00140139.2014.948496).
- **Loại nguồn:** thực nghiệm về đồng tử và dò lỗi văn bản.
- **Áp dụng:** cung cấp bản sáng để thử trong môi trường đủ sáng và bản tối như một lựa chọn.
- **Giới hạn:** kết quả dò lỗi không chứng minh mọi người bớt mỏi mắt với light mode; không xác lập CR 9.5–10.5:1 hoặc ngưỡng halation 13:1.

### Bằng chứng về lịch nghỉ 20–20–20 còn chưa đồng nhất

- **Nguồn A:** Talens-Estarelles C và cộng sự, *The effects of breaks on digital eye strain, dry eye and binocular vision: Testing the 20-20-20 rule*, xuất bản trực tuyến 2022, số tạp chí 2023. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35963776/), [DOI](https://doi.org/10.1016/j.clae.2022.101744).
- **Kết quả:** nghiên cứu 29 người có triệu chứng ghi nhận cải thiện triệu chứng khi dùng nhắc nghỉ; không ghi nhận cải thiện tương ứng ở các chỉ dấu bề mặt mắt trong thời gian thử.
- **Nguồn B:** Johnson A, Rosenfield M (2023; trực tuyến 2022), *20-20-20 Rule: Are These Numbers Justified?* [PubMed](https://pubmed.ncbi.nlm.nih.gov/36473088/).
- **Kết quả:** không ủng hộ hiệu quả của các lần nghỉ 20 giây theo lịch trong điều kiện thử nghiệm của nghiên cứu.
- **Áp dụng:** khuyến khích nghỉ nhìn gần đều đặn và chớp mắt đầy đủ; không coi đúng ba con số 20 là phác đồ chắc chắn. Theme Terminal hiện chưa cài bộ nhắc nghỉ.

### Không suy từ màu ấm thành hiệu quả giảm mỏi mắt

- **Nguồn:** Singh S và cộng sự (2023), Cochrane, *Blue-light filtering spectacle lenses for visual performance, sleep, and macular health in adults*. [Tóm tắt Cochrane](https://www.cochrane.org/evidence/CD013244_blue-light-filtering-spectacle-lenses-visual-performance-macular-back-part-eye-protection-and), [DOI](https://doi.org/10.1002/14651858.CD013244.pub2).
- **Loại nguồn:** tổng quan hệ thống 17 thử nghiệm ngẫu nhiên về kính lọc xanh.
- **Diễn giải:** có thể không giảm mỏi mắt ngắn hạn so với kính không lọc; tác động đến giấc ngủ chưa chắc chắn.
- **Giới hạn:** nghiên cứu kính, không trực tiếp thử bảng màu theme; không được khẳng định mọi can thiệp giảm ánh sáng bước sóng ngắn đều vô hiệu.
- **Áp dụng:** màu trắng ngà/đen than là lựa chọn thị giác. Không quảng cáo “cắt ánh sáng xanh bảo vệ võng mạc” từ HEX, hue hoặc chroma.

### Giấc ngủ phụ thuộc ánh sáng thực và thời điểm, không chỉ màu giao diện

- **Nguồn A:** Brown TM và cộng sự (2022), *Recommendations for daytime, evening, and nighttime indoor light exposure to best support physiology, sleep, and wakefulness in healthy adults*. [PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001571), [DOI](https://doi.org/10.1371/journal.pbio.3001571).
- **Loại nguồn:** đồng thuận chuyên gia tổng hợp bằng chứng về phơi sáng và nhịp sinh học ở người trưởng thành khỏe mạnh.
- **Diễn giải:** xét ánh sáng tại mắt, phổ và thời điểm; giảm kích thích ánh sáng buổi tối gắn với giờ ngủ cá nhân. Melanopic EDI khác lux thông thường và không suy được từ màu HEX.
- **Nguồn B:** Duraccio KM và cộng sự (2021), *Does iPhone night shift mitigate negative effects of smartphone use on sleep outcomes in emerging adults?* [PubMed](https://pubmed.ncbi.nlm.nih.gov/33867308/), [DOI](https://doi.org/10.1016/j.sleh.2021.03.005).
- **Kết quả:** thử nghiệm ngẫu nhiên 167 người 18–24 tuổi không thấy khác biệt kết quả ngủ do Night Shift trong toàn bộ mẫu.
- **Áp dụng:** không hứa dark mode hoặc Night Light giúp ngủ tốt; tự động hóa theo giờ chưa nằm trong bản Terminal đầu tiên.

## 3. Chuẩn kỹ thuật hỗ trợ khả năng đọc — không phải bằng chứng điều trị

| Nguồn | Yêu cầu dùng trong dự án | Giới hạn |
|---|---|---|
| [WCAG Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Chữ thường >=4.5:1 | Chuẩn web; dùng làm mục tiêu kỹ thuật tham chiếu cho terminal, không tuyên bố terminal đạt toàn bộ WCAG. |
| [WCAG Contrast Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html) | Chữ chính hướng tới >=7:1 | Không phải cửa sổ tương phản an toàn y khoa. |
| [WCAG Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | Tín hiệu cần thiết để nhận diện điều khiển/trạng thái >=3:1 trong phạm vi áp dụng | Cần kiểm tra từng trạng thái thực tế. |
| [WCAG Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | Giao diện web phải chịu được thay đổi khoảng cách theo tiêu chí | Không áp nguyên bộ giá trị CSS cho lưới terminal. |
| [WCAG Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) | Kiểm soát chuyển động/tự cập nhật thuộc phạm vi tiêu chí | Theme không thể loại hết chuyển động do ứng dụng TUI tạo. |
| [W3C CSS Color 4](https://www.w3.org/TR/css-color-4/) | Phân biệt OKLCH, sRGB và độ chói tương đối | OKLCH không đo phổ ánh sáng hoặc liều phơi sáng tại mắt. |

## 4. Quy tắc diễn đạt khi viết README

**Có thể viết:** “Thiết kế nhằm hỗ trợ đọc rõ và giảm nhiễu giao diện; màu chữ được kiểm tra tương phản sRGB trên nền mặc định. Cỡ chữ và chế độ sáng/tối có thể điều chỉnh.”

**Chưa được khẳng định:** “đã chứng minh giảm mỏi mắt”, “bảo vệ võng mạc”, “ngăn khô mắt”, “hỗ trợ tiết melatonin”, “tăng tập trung X%”, “chống halation ở CR cố định”, “phù hợp cho mọi người”.

Các thông số màu ấm, font 14 pt, cellHeight 1.3, padding, màu hồng đất và syntax ít màu là quyết định thiết kế cần đánh giá; không gắn nhãn là khuyến cáo y khoa.

## 5. Cách kiểm nghiệm cá nhân

So sánh theme hiện tại và theme mới trong các phiên tương đương; giữ gần như nhau về màn hình, ánh sáng, khoảng cách, tác vụ và nghỉ. Ghi độ hiểu/độ chính xác, thời gian, số gián đoạn và khô/rát/nhức/mờ/chói trước–sau (0–10). Thử từng nhóm thay đổi để dễ giải thích. Khoảng hai tuần là lịch thực dụng, không phải thời gian đủ để chứng minh hiệu quả lâm sàng. Không kéo dài phiên chỉ để đạt KPI. Khó chịu dai dẳng cần được đánh giá nguyên nhân thị lực/bề mặt mắt, thay vì chỉ đổi màu theme.
