# Serein Terminal — bản thử đầu tiên

**Serein — Extreme minimalism. Everyday comfort.**

Tên thương hiệu gợi cảm giác yên tĩnh, nhẹ và dễ chịu. Hai biến thể là **Serein Alabaster** (sáng) và **Serein Obsidian** (tối). Đây là định hướng thiết kế, không phải tuyên bố hiệu quả y tế hay xác nhận tên thương hiệu độc quyền.

Hai profile riêng cho **Windows Terminal + PowerShell 7**: `Serein Terminal Light` (Warm Alabaster) và `Serein Terminal Dark` (Warm Obsidian).

Thiết kế nhằm hỗ trợ đọc rõ và giảm nhiễu giao diện; chưa được thử nghiệm lâm sàng. Xem [cơ sở khoa học và giới hạn](../docs/scientific-basis.vi.md).

## Cấu hình

- Cascadia Mono 14 **pt**, weight normal; cellHeight 1.3, padding 16/12. Đây là cấu hình thử có thể chỉnh trong Settings > Profiles > Serein Terminal > Appearance.
- Nền đục 100%, không acrylic/ảnh nền; con trỏ dạng thanh. Giữ hành vi nhấp nháy hệ thống, không thay thiết lập accessibility toàn máy.
- Đủ 16 màu ANSI, phân biệt lỗi/cảnh báo/thành công; không ép tất cả màu thành đơn sắc.
- PSReadLine và định dạng PowerShell dùng màu tương ứng trong phiên Serein; không sửa file `$PROFILE` cá nhân.
- [Báo cáo tương phản](contrast-report.md): chữ chính và chữ chính khi chọn >=7:1; 16 màu ANSI dạng chữ trên nền mặc định >=4.5:1.

**Giới hạn:** không bảo đảm mọi cặp nền ANSI, inverse/dim, màu 256 hoặc truecolor do ứng dụng tự phát. TUI, Git, trình prompt hoặc công cụ riêng có thể cần cấu hình bổ sung. Không tuyên bố toàn bộ Terminal tuân thủ WCAG. Không tự chỉnh độ sáng màn hình, chặn thông báo, nhắc nghỉ hoặc đồng bộ theo giờ. Giao diện bao quanh cửa sổ vẫn theo theme Windows Terminal đang có.

## Build và kiểm tra

Chạy tại thư mục dự án:

```powershell
python .\serein-terminal\build.py
pwsh -NoProfile -File .\serein-terminal\verify.ps1
```

## Cài và dùng

```powershell
# Thêm hai profile, chọn bản sáng làm mặc định, mở cửa sổ thử.
pwsh -NoProfile -File .\serein-terminal\install.ps1 -Mode Light -SetDefault -Launch

# Hoặc chọn bản tối làm mặc định.
pwsh -NoProfile -File .\serein-terminal\install.ps1 -Mode Dark -SetDefault
wt -w new new-tab -p "Serein Terminal Dark"
```

Script tự tìm cấu hình Windows Terminal Stable hoặc bản unpackaged. Nếu không xác định duy nhất được cấu hình, truyền `-SettingsPath 'đường dẫn settings.json'`. Cần PowerShell 7 và alias `pwsh.exe` hoạt động trong phiên Windows thường.

Các profile cũ được giữ; mỗi lần cài lưu nguyên nội dung settings vào `backups/` trước khi ghi. Cài lại cập nhật hai profile/scheme có tên/GUID do dự án quản lý. JSONC được đọc bằng PowerShell; khi ghi lại sẽ chuẩn hóa JSON và không giữ comment/định dạng, nhưng bản sao gốc giữ nguyên.

**Giữ thư mục dự án ở vị trí hiện tại:** profile chạy `session.ps1` tại đây. Nếu di chuyển, cài lại để cập nhật đường dẫn. Bản sao cấu hình và receipt cục bộ không đưa vào Git.

## Đọc thử

```powershell
& .\serein-terminal\preview.ps1
```

Thử dấu tiếng Việt, I/l/1 và O/0, selection, 16 màu ANSI, resize và zoom. Gõ lệnh với chuỗi/comment để kiểm tra PSReadLine. Dùng tác vụ thật và theo dõi độ hiểu, lỗi, khó chịu; điều chỉnh cỡ chữ hoặc chế độ theo môi trường. Các câu ERROR/WARN ở preview chỉ là nội dung mẫu.

## Khôi phục

```powershell
pwsh -NoProfile -File .\serein-terminal\restore.ps1
```

Khôi phục bản trước **lần cài gần nhất**. Script từ chối ghi đè nếu settings thay đổi sau cài; khi đó xem `install-state.json` để lấy đường dẫn bản sao và hợp nhất thủ công. Profile đã mở cần đóng/mở tab mới để quay lại phiên cũ.

Trong lần chuyển tên Healthy Terminal sang Serein, điểm khôi phục gốc trước khi cài theme được giữ lại; cấu hình ngay trước chuyển tên cũng được lưu trong `backups/`.

## Tài liệu nền tảng

- [Microsoft: Color schemes](https://learn.microsoft.com/windows/terminal/customize-settings/color-schemes)
- [Microsoft: Profile appearance](https://learn.microsoft.com/windows/terminal/customize-settings/profile-appearance)
- [Microsoft: Command-line arguments](https://learn.microsoft.com/windows/terminal/command-line-arguments)
