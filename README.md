# Serein

**Extreme minimalism. Everyday comfort.**

Một bộ theme ấm, ít nhiễu cho Windows Terminal, Obsidian và VS Code. Hai bảng màu: **Alabaster** (sáng) và **Obsidian** (tối). Giữ chữ dễ đọc, màu trạng thái và dấu hiệu focus rõ ràng.

## Cài từ gói phát hành

Tải gói tương ứng trong **Releases** khi repository được đưa lên GitHub, hoặc lấy trực tiếp từ thư mục `dist/` của người build.

| Ứng dụng | File | Cách cài |
|---|---|---|
| VS Code | `serein-vscode-0.1.0.vsix` | Extensions → `…` → **Install from VSIX…**, chọn file rồi chọn theme Serein bằng Ctrl+K, Ctrl+T. |
| Obsidian | `serein-obsidian-0.1.2.zip` | Giải nén, chép thư mục `Serein` vào `<vault>/.obsidian/themes/`, chọn Serein trong Appearance. |
| Windows Terminal | `serein-terminal-0.1.0.zip` | Giải nén vào vị trí cố định, mở PowerShell 7 tại đó, chạy `./install.ps1 -Mode Light -SetDefault -Launch`. |

VS Code cũng có thể cài bằng `code --install-extension ./serein-vscode-0.1.0.vsix`. Gói VSIX cục bộ chưa ký và chưa xuất bản Marketplace; tuân theo chính sách extension của máy bạn.

Terminal yêu cầu Windows Terminal và PowerShell 7 (`pwsh`); script lưu bản sao trước khi thay cấu hình. Giữ thư mục giải nén vì profile tham chiếu script tại đó. Chạy `./restore.ps1` để khôi phục, hoặc chọn lại profile cũ. Obsidian/VS Code chỉ cần chọn lại theme trước đó để ngừng dùng.

## Thiết kế và phạm vi

- Nền trắng ngà/đen than, điểm nhấn hồng đất, syntax ít màu.
- Màu chữ được kiểm tra tương phản sRGB cho các cặp được khai báo, bao gồm trạng thái chọn đã chỉ định.
- Font và khoảng dòng tùy chỉnh: VS Code có cấu hình gợi ý riêng, theme màu không tự thay settings cá nhân.
- Không coi màu ấm là phương pháp điều trị. Chưa có thử nghiệm lâm sàng chứng minh Serein giảm mỏi mắt, bảo vệ võng mạc hoặc cải thiện khả năng tập trung.

Đọc [cơ sở khoa học, nguồn dẫn và giới hạn](docs/scientific-basis.vi.md). [Bản ý tưởng ban đầu](theme-protect-eyes.md) là lịch sử thiết kế có các giả định đã được sửa, không phải tài liệu khuyến cáo y tế.

## Mã nguồn

| Thư mục | Nội dung |
|---|---|
| [serein-terminal](serein-terminal/README.md) | Scheme, cài đặt và khôi phục Windows Terminal. |
| [serein-obsidian](serein-obsidian/README.md) | Theme CSS, manifest, Focus snippet và ghi chú thử. |
| [serein-vscode](serein-vscode/README.md) | Extension theme, TextMate/semantic tokens và cửa sổ preview riêng. |
| [docs](docs/scientific-basis.vi.md) | Cơ sở khoa học và hướng dẫn phát hành. |
| `tools/release.py` | Build, kiểm tra và đóng gói ngoại tuyến bằng Python chuẩn. |

## Build gói cài đặt

Yêu cầu Python 3.10+; PowerShell 7 dùng để kiểm tra script Terminal.

```powershell
python tools/release.py
pwsh -NoProfile -File serein-terminal/verify.ps1
```

Kết quả trong `dist/`: ba gói ứng dụng, một ZIP mã nguồn và `SHA256SUMS.txt`. Trình đóng gói dùng danh sách file cho phép; loại bản sao cấu hình, đường dẫn cài đặt cá nhân, receipt phiên, cache và log.

VSIX được tạo trực tiếp theo cấu trúc manifest của VS Code/vsce; không cần Node hoặc tải dependency. Khi xuất bản Marketplace, dùng quy trình chính thức của `@vscode/vsce` và publisher đã đăng ký. Các gói phải được cài thử trước khi phát hành.

## Chia sẻ và đóng góp

Repo dùng [MIT License](LICENSE), cho phép sử dụng, sửa đổi và phân phối lại với thông báo bản quyền/license. Đề xuất thay đổi cần nêu ứng dụng, chế độ sáng/tối, bước tái hiện và kết quả mong muốn. Không đưa vault hoặc bản sao settings cá nhân vào pull request.

Xem [hướng dẫn GitHub và phát hành](docs/releasing.vi.md). Repository này dùng cấu trúc chung cho ba ứng dụng; nếu đưa Obsidian lên community directory, chuẩn bị repository theme riêng có manifest/theme.css ở root theo yêu cầu hiện hành.
