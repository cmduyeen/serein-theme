# Serein for Obsidian

**Extreme minimalism. Everyday comfort.** Bản nền 0.1.2 gồm Serein Alabaster (sáng) và Serein Obsidian (tối), theo chế độ sáng/tối của Obsidian. Không cần community plugin hay tải font từ Internet.

Cây thư mục dùng bước thụt 16px mỗi cấp, cùng khoảng đệm cho file và thư mục, đường dẫn cấp cha–con mảnh, hàng cao tối thiểu 30px (36px trên mobile). Nhãn và mũi tên neo vào node cha thực tế để không bị lệch khi bộ dựng cây cộng dồn padding inline sau đóng/mở. Tên dài rút gọn; khi đổi tên dùng một dòng có thể cuộn ngang. Không thay sắp xếp, kéo thả hay tên file. Nếu cây giữ lề cũ sau khi cập nhật theme, mở lại vault để Obsidian dựng lại cây.

Màu nhấn mặc định được khai báo bằng cả biến gốc Obsidian `--accent-h/s/l` và các biến chức năng. Bản sáng dùng `#914854`, bản tối dùng `#C9848F`. Nếu từng chọn màu nhấn riêng trong Appearance, dùng Reset accent color để quay về màu mặc định của theme. Theme không tự ghi đè lựa chọn màu cá nhân trong cấu hình vault.

## Có gì trong thư mục?

- `manifest.json`, `theme.css`: theme cài cục bộ.
- `snippets/serein-focus.css`: tùy chọn bố cục đọc gọn ở cấp ghi chú.
- `Preview.md`: nội dung thử dấu tiếng Việt, code, bảng, liên kết và callout.
- `verify.py`, `contrast-report.md`: kiểm tra bảng màu và báo cáo tương phản.

## Thiết kế

Nền trắng ngà/đen than, một màu nhấn hồng đất; phân cấp bằng khoảng cách và độ đậm. Chữ phụ vẫn đủ rõ trên ba lớp nền. Giữ đường viền điều khiển, focus bàn phím, scrollbar và điều hướng. Cấu hình bắt đầu là 18px, line-height 1.65, độ rộng 70ch; không phải thông số y khoa tối ưu cho mọi người. Cỡ chữ tùy chỉnh trong Appearance và chế độ Readable line length của Obsidian có thể ảnh hưởng kết quả.

Focus snippet chỉ điều chỉnh chiều rộng/nhịp dòng và tiêu đề của ghi chú có `cssclasses: [serein-focus]`. Không tự ẩn sidebar, status bar hoặc giảm opacity các đoạn khác. Có thể dùng lệnh sidebar tích hợp của Obsidian khi muốn thu gọn không gian làm việc.

Đây là thiết kế nhằm hỗ trợ khả năng đọc và giảm nhiễu; chưa được thử nghiệm lâm sàng. [Cơ sở khoa học và giới hạn](../docs/scientific-basis.vi.md).

## Cài thủ công vào vault

1. Tạo thư mục `<vault>/.obsidian/themes/Serein/` — tên thư mục cài phải khớp `name` trong manifest.
2. Sao chép `theme.css` và `manifest.json` vào đó.
3. Trong Obsidian, vào **Settings → Appearance → Themes**, chọn **Serein**. Nếu chưa thấy, mở lại ứng dụng.
4. Chọn chế độ sáng/tối trong Appearance. Dùng `Preview.md` để kiểm tra Reading view, Live Preview và Source mode.
5. Nếu cần Focus, chép `snippets/serein-focus.css` vào `<vault>/.obsidian/snippets/`, bật trong Appearance → CSS snippets rồi thêm `serein-focus` vào thuộc tính `cssclasses` của ghi chú.

Chưa cài hoặc thay đổi vault nào. Thư mục `serein-obsidian` là mã nguồn, tên thư mục khi cài vào vault là `Serein`.

## Kiểm tra

```powershell
python .\serein-obsidian\verify.py
```

Kiểm tra màu dự kiến: chữ chính >=7:1 trên ba lớp nền và vùng chọn; chữ phụ, accent và semantic text >=4.5:1 trên ba lớp nền; chữ trên nút accent >=4.5:1; focus và đường viền >=3:1. Báo cáo này không chứng nhận toàn bộ ứng dụng đạt WCAG: opacity, plugin, nội dung nhúng, callout mặc định và CSS tùy chỉnh có thể tạo cặp màu khác.

Trạng thái: mới kiểm tra tĩnh cấu trúc và màu; cần kiểm thử trực tiếp trong vault trên desktop/mobile, các chế độ editor, bàn phím, zoom, callout, modal, properties, tìm kiếm và PDF export. `minAppVersion` là mốc dự kiến, chưa là cam kết đã kiểm thử mọi phiên bản từ mốc đó. Chưa đóng gói để xuất bản community theme.

Quay về theme Default trong Appearance để ngừng dùng; tắt snippet riêng nếu đã bật. Không cần xóa ghi chú.

## Nguồn kỹ thuật

- [Obsidian: Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Obsidian: Theme guidelines](https://docs.obsidian.md/Themes/App%20themes/Theme%20guidelines)
- [Obsidian: Manifest](https://docs.obsidian.md/Reference/Manifest)
- [Obsidian: CSS snippets](https://obsidian.md/help/snippets)
