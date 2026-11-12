# Serein for VS Code

**Extreme minimalism. Everyday comfort.** Hai color theme: **Serein Alabaster** (sáng) và **Serein Obsidian** (tối). Extension chỉ khai báo màu, không có mã chạy nền, dependency, API key hoặc tải font.

## Thiết kế

- Đồng bộ nền và điểm nhấn hồng đất với Serein Terminal/Obsidian.
- Syntax ít màu: tên hàm/biến chủ yếu là màu chữ; keyword hồng đất, string xanh trầm và literal xanh xám. Comment rõ, không ép italic. Có cả TextMate và semantic tokens.
- Khai báo màu editor, Explorer, tab, Quick Open, nút, input, thông báo, Problems, Git và terminal tích hợp. Giữ dấu hiệu lỗi/cảnh báo, focus bàn phím và trạng thái chọn.
- [Cơ sở khoa học](../docs/scientific-basis.vi.md): mục tiêu hỗ trợ đọc và giảm nhiễu; chưa có thử nghiệm lâm sàng chứng minh theme giảm mỏi mắt hoặc tăng tập trung.

## Build và kiểm tra

Từ thư mục dự án:

```powershell
python .\serein-vscode\build.py
python .\serein-vscode\build.py --check
```

`palette.json` là nguồn màu; `build.py` sinh hai file trong `themes/` và [báo cáo tương phản](contrast-report.md). Không chỉnh trực tiếp file theme đã sinh nếu muốn giữ khả năng build lại.

## Thử trong cửa sổ riêng

```powershell
& .\serein-vscode\preview.ps1 -Mode Light
# Hoặc:
& .\serein-vscode\preview.ps1 -Mode Dark
```

Yêu cầu lệnh `code` có trên PATH. Script dùng Extension Development Host với user-data riêng trong `.preview`, không sửa settings của VS Code đang dùng. Mỗi lần chạy sẽ đặt lại settings của riêng cửa sổ preview. Chọn theme bằng **Ctrl+K, Ctrl+T**. Có thể mở riêng thư mục `serein-vscode` trong VS Code rồi F5 với cấu hình `Preview Serein` (cách F5 dùng settings của development host).

Theme màu không thể đặt font, line-height, độ thụt Explorer hay chế độ Zen. `recommended-settings.json` là cấu hình gợi ý riêng: editor 16px/26px, Explorer thụt 16px, ẩn minimap, hạn chế chuyển động và giữ rõ chữ unused. Cửa sổ preview áp bộ này để thử; chỉ hợp nhất các mục bạn muốn vào settings cá nhân khi dùng chính thức. Cỡ chữ là điểm bắt đầu, không phải ngưỡng y khoa.

## Cài lâu dài

Gói `dist/serein-vscode-0.1.0.vsix` được tạo bằng `python tools/release.py` từ root repository. Cài bằng Extensions → **Install from VSIX…** hoặc `code --install-extension đường-dẫn-tới-file.vsix`. Chưa xuất bản Marketplace và `serein-local` là publisher dùng phát triển. Có thể đóng gói bằng công cụ chính thức `@vscode/vsce` khi chuẩn bị phát hành Marketplace:

```powershell
# Chạy trong serein-vscode khi đã có vsce:
vsce package
code --install-extension .\serein-vscode-0.1.0.vsix
```

Sau cài, chọn Serein trong Color Theme. Để quay lại giao diện trước, chọn lại theme cũ. Không cần thay cấu hình project để dùng color theme.

## Phạm vi kiểm tra

Kiểm tra tĩnh các cặp chữ chính, chữ phụ, accent, semantic, vùng chọn và 16 màu ANSI trên nền mặc định. Không khẳng định toàn bộ VS Code đạt WCAG: overlay có alpha, TUI/truecolor, extension UI và tùy chỉnh riêng cần kiểm tra render thực tế. Semantic tokens do language server hoặc theme override cá nhân có thể ảnh hưởng kết quả. Bản 0.1.0 chưa kiểm thử trực quan trong ứng dụng; mốc engine là yêu cầu phát triển, không xác nhận đã kiểm thử mọi phiên bản.

## Nguồn kỹ thuật

- [VS Code Color Theme guide](https://code.visualstudio.com/api/extension-guides/color-theme)
- [Theme Color reference](https://code.visualstudio.com/api/references/theme-color)
- [Semantic Highlight guide](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)
