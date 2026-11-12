# Serein — sản phẩm và tài liệu tham khảo

**Extreme minimalism. Everyday comfort.** Hai bảng màu ấm: Alabaster (sáng) và Obsidian (tối).

Đây là tài liệu tham khảo duy nhất của dự án: cài đặt, bảng màu, cơ sở khoa học, phạm vi hỗ trợ và hướng nâng cấp. Cập nhật 12/11/2026. Các bản nháp, báo cáo lặp và dữ liệu thử đã được dọn; lịch sử vẫn có trong Git.

## Thành phẩm

| Thư mục | Thành phẩm | Cài đặt |
|---|---|---|
| `serein-terminal/` | 2 scheme JSON, script cài/khôi phục và ZIP | Giải nén vào vị trí cố định, dùng PowerShell 7 chạy `./install.ps1 -Mode Light -SetDefault -Launch`. |
| `serein-obsidian/` | `theme.css`, `manifest.json`, Focus snippet và ZIP | Chép thư mục `Serein` trong ZIP vào `<vault>/.obsidian/themes/`, chọn Serein trong Appearance. |
| `serein-vscode/` | 2 theme JSON, package manifest, settings gợi ý và VSIX | Extensions → `…` → Install from VSIX…, chọn file VSIX, rồi Ctrl+K Ctrl+T chọn Serein. |
| `serein-antigravity/` | Preset cho Antigravity App và script copy màu | Nhập Background, Foreground, Accent trong Settings → Appearance cho từng chế độ. Đây là preset do Serein mô tả, không phải định dạng import của Antigravity. |
| `serein-codex/` | 2 chuỗi import native `codex-theme-v1` và script copy | Chạy script copy rồi dùng Import ở đúng ô Light/Dark theme trong Settings → Appearance. |
| `serein-windows/` | 2 theme Windows native, nền đơn sắc, script cài/khôi phục và ZIP | Chạy `./install.ps1 -Mode Light -Apply` từ thư mục đã giải nén, hoặc cài trước rồi chọn theme trong Windows. |
| `serein-sublime-text/` | 2 color scheme, 2 UI theme, gói `.sublime-package`, script cài và ZIP | Cài package rồi chọn cả Color Scheme và Theme Serein trong Preferences của Sublime Text 4. |
| `serein-telegram/` | 2 theme Telegram Desktop `.tdesktop-theme`, palette nguồn và ZIP | Trong Telegram Desktop, dùng Settings → Chat Settings → chọn theme từ file, xem trước rồi xác nhận. |
| `serein-vimium/` | CSS sáng/tối/tự động, script copy và ZIP | Dán CSS vào Vimium Options → Advanced Options → CSS for Vimium UI, rồi lưu. |

Mỗi thư mục có gói chia sẻ riêng. Gói `serein-vscode-0.1.0.vsix` được cài thử thành công trong thư mục extension độc lập. Obsidian là bản 0.1.2; các adapter khác là 0.1.0. Các file theme có thể sửa trực tiếp để nâng cấp; không cần giữ các bản nháp hoặc cache của lần phát triển này.

## Dùng Vimium

Serein Vimium 0.1.0 dành cho **Vimium gốc của philc**, tham chiếu selector hiện hành sau thay đổi UI ở Vimium 2.3. Không cam kết tương thích Vimium C, Surfingkeys hoặc Vim Vixen. Gồm `serein-alabaster.css` (luôn sáng), `serein-obsidian.css` (luôn tối) và `serein-auto.css` (theo `prefers-color-scheme` của trình duyệt/hệ điều hành, không tự phân tích màu trang web).

```powershell
./serein-vimium/copy-theme.ps1 -Mode Auto
# Hoặc -Mode Light / -Mode Dark
```

Mở Options của extension Vimium → Advanced Options → **CSS for Vimium UI**, lưu bản CSS cũ hoặc dùng Download backup trước khi thay, dán toàn bộ nội dung một file CSS rồi **Save Changes**. Không dán vào Custom key mappings. Tải lại tab web nếu UI chưa cập nhật. Có thể mở file CSS và copy thủ công trên macOS/Linux; không cần script PowerShell hay plugin thêm. Để quay về, khôi phục CSS đã lưu hoặc dùng Reset cạnh ô CSS; không reset toàn bộ phím tắt.

Theme áp dụng cho link hints (`f`/`F`), Vomnibar (`o`, `b`, `T`) và HUD/find (`/`). Chữ hint rõ, bỏ gradient vàng mặc định, ký tự đã khớp dùng hồng đất kèm gạch chân thay vì làm mờ; dòng chọn trong Vomnibar giữ tương phản. CSS được giới hạn ở các thành phần Vimium, không tô lại toàn bộ trang web. Không thay vị trí, kích thước iframe hay z-index do Vimium quản lý, không đổi phím tắt, search engine, quyền truy cập hoặc dữ liệu trình duyệt. Help/options UI chưa được bao phủ đầy đủ.

Không dùng backup JSON cấu hình để cài theme vì có thể vô tình thay key mappings/exclusions. Các trang đặc quyền như `chrome://`, cửa hàng extension hoặc tab không được cấp quyền có thể không chạy Vimium; theme không thay đổi giới hạn đó. Dark Reader hoặc CSS/theme của trang có thể ảnh hưởng kết quả và cần kiểm tra riêng.

Đã kiểm tra CSS tĩnh, selector theo mã upstream và tương phản palette cho chữ/hints/vùng chọn. Chưa áp dụng vào extension hoặc kiểm thử trực tiếp trong trình duyệt. Cần thử trang sáng/tối, nhiều hints sát nhau, lọc hints, Vomnibar có URL dài, tìm kiếm không có kết quả, zoom và chuyển chế độ hệ thống. CSS có media query Auto dùng cùng palette với hai bản cố định.

## Dùng Telegram Desktop

Serein Telegram 0.1.0 dành cho **Telegram Desktop** (bản Windows/Linux/macOS dùng tdesktop), không phải Telegram Web, Telegram Android/iOS hoặc ứng dụng Telegram for macOS native riêng. Hai file `Serein-Alabaster.tdesktop-theme` và `Serein-Obsidian.tdesktop-theme` là gói native, mỗi gói có `colors.tdesktop-theme` và `background.png` ở root.

Mở Telegram Desktop → Settings → Chat Settings → phần Chat Background/theme → **Choose from file** (tên/vị trí có thể khác theo phiên bản), chọn file `.tdesktop-theme`, kiểm tra cửa sổ preview, rồi **Apply This Theme / Keep Changes** nếu thấy phù hợp. Không cần script cài, admin, sửa `tdata` hoặc gửi file cho người khác. Chọn lại theme có sẵn trong Chat Settings để quay về. Nếu thiết lập Night Mode tự đổi theme, kiểm tra lại chế độ đó khi dùng hai bản Serein.

Theme dùng nền chat đơn sắc, bong bóng nhận/gửi phân lớp nhẹ, hồng đất cho liên kết/nút/badge và màu riêng cho lỗi. Danh sách chat đang chọn vẫn dùng chữ tối/sáng dễ đọc thay vì nền nhấn phủ kín. Không thay ảnh đại diện, ảnh/video, sticker, nội dung tin nhắn, cỡ font hoặc thông báo; các mục đó không phải chức năng của gói theme này. Cỡ chữ có thể chỉnh trong Settings nếu phiên bản hỗ trợ.

Các file `.tdesktop-palette` và `background-*.png` là nguồn để nâng cấp. Khi đóng gói lại, đổi tên palette thành `colors.tdesktop-theme`, ảnh thành `background.png`, ZIP cả hai file ở root rồi đổi phần mở rộng ZIP thành `.tdesktop-theme`. Không đặt thư mục bọc bên trong. Dùng các khóa màu của Telegram Desktop; khi phiên bản bổ sung UI mới, phần chưa khai báo sẽ dùng fallback của app và cần kiểm tra riêng.

Đã kiểm tra cú pháp palette, giá trị màu, các cặp chữ/nền chính/selection và cấu trúc ZIP native. Chưa nhập hoặc kích hoạt trong Telegram hiện tại; chưa xác nhận tất cả trạng thái UI, nội dung đa phương tiện hay theme theo từng cuộc chat. Gói không truy cập dữ liệu tài khoản hoặc thư mục `tdata`.

## Dùng Sublime Text

Serein Sublime Text 0.1.0 gồm **Serein Alabaster** và **Serein Obsidian**, mỗi bản có `.sublime-color-scheme` cho editor/syntax và `.sublime-theme` cho sidebar, tab, thanh trạng thái, popup và nút. UI theme kế thừa Default/Default Dark có sẵn trong Sublime Text 4, không yêu cầu plugin chạy nền hoặc tải font. Các menu/cửa sổ native do hệ điều hành vẽ có thể không theo đủ bảng màu.

Windows: mở PowerShell tại `serein-sublime-text` hoặc thư mục giải nén, chạy `./install.ps1`. Script chỉ chép `Serein.sublime-package` vào `%USERPROFILE%/AppData/Roaming/Sublime Text/Installed Packages/`, không tự thay User Preferences. Bản Serein cũ được sao lưu ngoài repo nếu cài đè. Với bản portable hoặc Data directory khác, truyền `-DataPath 'đường-dẫn-Data'` lấy từ vị trí Packages của ứng dụng.

Trên macOS/Linux hoặc khi cài thủ công: Preferences → Browse Packages để tìm `Packages`, đi lên thư mục cha và chép `Serein.sublime-package` vào thư mục cạnh nó tên `Installed Packages`. Sau đó:

1. Preferences → Select Color Scheme → chọn **Serein Alabaster** hoặc **Serein Obsidian**.
2. Preferences → Select Theme → chọn **Serein Alabaster** hoặc **Serein Obsidian** cùng chế độ. Có thể mở lại ứng dụng nếu package chưa xuất hiện.
3. Hợp nhất các khóa mong muốn từ `recommended-settings.json` vào Preferences → Settings: Cascadia Mono 16, giãn dòng trên/dưới 3px, hạn chế chuyển động. File gợi ý không bị áp tự động; phím menu có thể khác theo OS/phiên bản.

Sidebar thụt 16px mỗi cấp, giữ mũi tên, trạng thái chọn và màu Git/lỗi cần thiết. Syntax ít màu, comment rõ và không ép italic; có giữ kiểu chữ đậm/nghiêng khi nội dung Markdown yêu cầu. Các file JSON nguồn có thể sửa trực tiếp để nâng cấp; tạo lại `.sublime-package` bằng ZIP với file ở root, không bọc thêm thư mục Serein. Để quay lại, chọn theme/color scheme cũ trong Preferences. Không xóa User Preferences.

Đã kiểm tra cấu trúc JSON, liên kết `extends` với theme mặc định cài trên máy, tương phản palette, script và nội dung gói. Chưa kích hoạt hoặc kiểm thử trực quan trong Sublime Text; syntax/plugin, các lớp phủ và trạng thái khác cần thử bằng tác vụ thật. Không bảo đảm hỗ trợ Sublime Text 3 hoặc các bản theme mặc định có schema khác.

## Dùng Windows

Serein Windows 0.1.0 dùng `.theme` và visual style Aero có sẵn, dành cho Windows 10/11. Bản Alabaster có wallpaper đơn sắc `#F6F4F0`, accent `#914854`, app/system Light; bản Obsidian có wallpaper `#191817`, accent `#C9848F`, app/system Dark. Ảnh nền PNG 3840×2160 được tạo bằng màu thuần, không có chữ hoặc trang trí.

Từ thư mục `serein-windows` hoặc thư mục giải nén:

```powershell
./install.ps1 -Mode Light          # Chỉ cài file, chưa đổi theme hiện tại
./install.ps1 -Mode Dark -Apply    # Sao lưu theme hiện tại, rồi mở theme tối
./restore.ps1                     # Mở theme đã sao lưu, nếu vẫn đang dùng theme vừa áp
```

Script dùng PowerShell 5.1+ trên Windows; không cần admin. Hai theme được cài tại `%USERPROFILE%/AppData/Local/Microsoft/Windows/Themes/Serein/`. Các đường wallpaper được đổi thành đường tuyệt đối khi cài, nên dùng script trước khi mở `.theme`. Bản sao và receipt nằm ngoài repo tại `%USERPROFILE%/AppData/Local/Serein/Windows/`. `-Apply` dừng nếu không tìm được theme hiện tại để sao lưu; có thể lưu theme hiện tại trong Settings rồi thử lại. Các ảnh tham chiếu trong theme cũ cần còn tồn tại khi khôi phục; bản sao theme không phải bản sao toàn bộ wallpaper slideshow, âm thanh hoặc mọi thiết lập Windows.

Windows tự xử lý việc kích hoạt qua file `.theme`; Settings có thể mở khi áp dụng. Kiểm tra kết quả tại Settings → Personalization → Themes. Khi ứng dụng chưa đổi giao diện, mở lại ứng dụng. Nếu không muốn thay wallpaper, chọn lại ảnh nền riêng sau khi áp theme.

Phạm vi native: chế độ sáng/tối, màu nhấn và desktop. Windows vẫn quyết định màu nền/chữ bên trong Settings, File Explorer, menu và taskbar; không bảo đảm tất cả dùng đúng HEX Serein. Theme không ép ứng dụng bỏ theme riêng, không đổi font hệ thống, không thay icon/cursor và không cài visual-style patcher. Mở Personalization → Colors để tắt Transparency effects nếu muốn nền đục; Accessibility → Visual effects để giảm Animation effects theo sở thích. Hai tùy chọn này **không bị script tự thay đổi**. Các theme có thể ảnh hưởng sound scheme mặc định theo hành vi Windows; kiểm tra Sounds nếu có cấu hình âm thanh riêng.

Trạng thái: đã kiểm tra cấu trúc theme, màu/nền, script và đường dẫn khi cài vào thư mục thử. Chưa áp dụng vào Windows đang dùng; chưa xác nhận render trên mọi bản Windows. Đây là tùy biến giao diện, không phải sản phẩm y tế hoặc chế độ High Contrast.

## Dùng Terminal và khôi phục

Yêu cầu Windows Terminal, PowerShell 7 và `pwsh.exe` trên PATH. Chạy từ thư mục `serein-terminal` hoặc thư mục đã giải nén:

```powershell
./install.ps1 -Mode Light -SetDefault -Launch
# Hoặc bản tối:
./install.ps1 -Mode Dark -SetDefault -Launch
# Khôi phục cấu hình trước lần cài gần nhất:
./restore.ps1
```

State và bản sao được lưu tại `%USERPROFILE%/AppData/Local/Serein/Terminal/`, không nằm trong repo. Khôi phục từ chối ghi đè nếu settings thay đổi sau cài. Khi có nhiều bản Windows Terminal, chỉ định `-SettingsPath`. Script giữ profile cũ, nhưng chuẩn hóa lại JSON và không giữ comment; bản sao gốc giữ nguyên. Profile tham chiếu `session.ps1`, vì vậy phải giữ thư mục sau cài. Không tự chỉnh độ sáng màn hình, lịch ngày/đêm hay nhắc nghỉ.

## Dùng Obsidian

Thư mục cài phải tên `Serein`, khớp manifest. Theme theo chế độ sáng/tối của Obsidian. Có thể chỉnh font size và Readable line length trong Appearance. Snippet Focus là tùy chọn: chép `snippets/serein-focus.css` vào `.obsidian/snippets/`, bật snippet và thêm `cssclasses: [serein-focus]` vào ghi chú.

Explorer thụt đều 16px, nhãn và mũi tên neo vào node thực để tránh lỗi cộng dồn padding của bộ dựng cây. Đã kiểm tra 3 cấp và đóng/mở lặp lại trên máy hiện tại. Không đổi sắp xếp, tên file hoặc cấu trúc vault. Plugin tùy biến Explorer khác có thể xung đột; cần thử riêng trên mobile và khi đổi tên/kéo thả. Chọn theme Default và tắt snippet để quay lại.

## Dùng VS Code

`recommended-settings.json` là tùy chọn, không bị theme áp đặt: font 16px, line-height 26px, Explorer indent 16px, bỏ minimap và giảm chuyển động. Chỉ hợp nhất các khóa bạn muốn vào User Settings. Theme có TextMate và semantic highlighting, giữ riêng lỗi/cảnh báo/Git. Chọn lại theme cũ để quay về. Publisher `serein-local` dùng cho gói cục bộ, chưa được đăng ký Marketplace.

## Dùng Antigravity App

Áp dụng cho **Antigravity App độc lập** trên máy này, không phải Antigravity IDE cũ hay extension trong VS Code. Mở Settings → Appearance, chọn Light hoặc Dark để hiện bộ màu tương ứng; nhập 3 màu từ `presets.json`. Các ô màu đã có dấu `#`, nên nhập 6 ký tự HEX.

```powershell
./serein-antigravity/copy-color.ps1 -Mode Dark -Color background
./serein-antigravity/copy-color.ps1 -Mode Dark -Color foreground
./serein-antigravity/copy-color.ps1 -Mode Dark -Color accent
```

Mỗi lệnh copy một màu để dán vào đúng ô. Giữ font Google Sans và Contrast Default làm điểm bắt đầu; các tùy chọn là sở thích thiết kế, không phải ngưỡng y khoa. Bản tối đã được nhập và đọc lại đúng trong UI. Bản sáng có preset hoàn chỉnh nhưng chưa được xác minh áp dụng trên máy. Giao diện không có nút import theme trong phần đã kiểm tra; không đưa VSIX vào ứng dụng này. Không sửa `app.asar` hoặc trạng thái đăng nhập. Nếu cập nhật app bổ sung import/export, xây adapter mới theo schema thực tế.

## Dùng Codex đang mở cuộc trò chuyện này

```powershell
./serein-codex/copy-theme.ps1 -Mode Light
./serein-codex/copy-theme.ps1 -Mode Dark
```

Sau từng lệnh, vào Settings → Appearance → đúng mục Light theme hoặc Dark theme → Import. Import của mỗi chế độ tách riêng; chọn Theme System nếu muốn theo hệ điều hành. Trước khi thay, dùng Copy theme trong ứng dụng để lưu chuỗi cũ nếu muốn hoàn tác.

File `.codex-theme` là **chuỗi chia sẻ native**, không phải CSS hay VSIX. Payload dùng `codeThemeId: codex`, `variant`, `theme` với accent, surface, ink, fonts, contrast, opaqueWindows và semanticColors. Định dạng được đối chiếu với parser/schema của Codex 26.1106.6628.0 đang cài. Hai payload đã kiểm tra schema/cặp màu; chưa import trực tiếp vào ứng dụng. Dùng engine code theme tích hợp Codex; không khẳng định syntax code cũng giống hoàn toàn VS Code.

Import không tự đặt cỡ font hoặc reduced motion. Gợi ý đặt UI 16px, code 14–16px và reduced motion On nếu có; kiểm tra lại cảm giác thực tế. Slider Contrast 45/60 là tham số riêng của app, **không phải tỷ lệ WCAG 4.5:1 hay 6:1**. App có thể sinh thêm màu bề mặt từ các tham số; phải đánh giá giao diện sau import, không suy toàn bộ UI từ cặp màu gốc.

## Bảng màu và quy tắc nâng cấp

| Vai trò | Alabaster | Obsidian |
|---|---|---|
| Canvas | `#F6F4F0` | `#191817` |
| Surface | `#EDEAE4` | `#21201E` |
| Elevated | `#E3DFD7` | `#2B2926` |
| Chữ chính | `#3D3A36` | `#C7C3BA` |
| Chữ phụ tham chiếu | `#5C5852` | `#A39E95` |
| Accent | `#914854` | `#C9848F` |
| Chữ trên accent | `#F6F4F0` | `#191817` |
| Lỗi | `#963D37` | `#CF8179` |
| Cảnh báo | `#705711` | `#BAA16B` |
| Thành công | `#405D3D` | `#9FAE94` |

Các adapter có điều chỉnh nhỏ theo ngữ cảnh: Terminal có bảng ANSI riêng; Obsidian dùng muted sáng `#625D56`; VS Code dùng selection sáng `#E1DAD2`/tối `#302D29` để giữ rõ syntax màu khi chọn. Không ép một mã màu cho mọi cặp nền/chữ nếu nó làm giảm khả năng đọc.

Chữ chính mục tiêu >=7:1, chữ thường/phụ >=4.5:1 trên từng nền thực sự dùng; dấu hiệu điều khiển cần thiết tham chiếu >=3:1. Công thức: chuyển sRGB mỗi kênh 0–1 sang tuyến tính bằng `c/12.92` nếu `c <=0.04045`, ngược lại `((c+0.055)/1.055)^2.4`; `Y=0.2126R+0.7152G+0.0722B`; `CR=(Ymax+0.05)/(Ymin+0.05)`. Chỉ làm tròn khi hiển thị, không làm tròn trước khi quyết định đạt.

Đã kiểm tra các palette gốc: Terminal 40 cặp, Obsidian 58 cặp, VS Code 94 cặp. Không chứng nhận toàn bộ app đạt WCAG: overlay alpha, truecolor, TUI, nội dung nhúng và plugin có thể tạo cặp khác. Serein chưa qua thử nghiệm lâm sàng. Không dùng số màu ít hơn hoặc thời gian ngồi lâu hơn làm bằng chứng tăng tập trung.

## Nâng cấp và đóng gói sau này

1. Sửa trực tiếp nguồn thành phẩm trong thư mục ứng dụng; giữ một phiên bản đang dùng để so sánh. Đổi version manifest khi có thay đổi.
2. Kiểm tra cả sáng/tối, chữ Việt, zoom, selection, focus bàn phím, lỗi/cảnh báo, Explorer sâu và nhiều lần đóng/mở. So sánh độ hiểu/độ chính xác cùng khó chịu trước–sau.
3. Terminal: ZIP các script cài/khôi phục/session cùng `schemes/`. Obsidian: ZIP thư mục `Serein/` chứa theme.css/manifest và snippet riêng. VS Code: dùng `@vscode/vsce package` tại serein-vscode (cần Node/npm/vsce); không publish bằng publisher tạm.
4. Codex: giữ prefix `codex-theme-v1:` và đúng schema phiên bản đang dùng; Import thử ở đúng chế độ. Antigravity: preset JSON là công thức nhập màu, không gọi nó là file import native.
5. Chỉ chia sẻ thành phẩm, README này và LICENSE. Không đóng gói state, credential, backups, cache hoặc dữ liệu chat. Đính kèm SHA-256 khi phát hành.

Git repo vẫn giữ lịch sử trước dọn. Để đưa lên GitHub, tạo repo trống tên đề xuất `serein-theme`, thêm remote rồi push main. Chưa có repo remote hoặc bản phát hành công khai. Dùng MIT License; tên/publisher chưa được kiểm tra tính độc quyền. Với Obsidian Community, chuẩn bị repo theme riêng đúng yêu cầu hiện hành; monorepo không tự đáp ứng việc nộp theme.

## Nguồn kỹ thuật

- [VS Code Color Theme](https://code.visualstudio.com/api/extension-guides/color-theme), [Theme Color reference](https://code.visualstudio.com/api/references/theme-color), [Publishing extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
- [Obsidian Theme guidelines](https://docs.obsidian.md/Themes/App%20themes/Theme%20guidelines), [Manifest](https://docs.obsidian.md/Reference/Manifest), [Colors](https://docs.obsidian.md/Reference/CSS%20variables/Foundations/Colors).
- [Windows Terminal schemes](https://learn.microsoft.com/windows/terminal/customize-settings/color-schemes), [profile appearance](https://learn.microsoft.com/windows/terminal/customize-settings/profile-appearance).
- [Microsoft: Windows theme file format](https://learn.microsoft.com/windows/win32/controls/themesfileformat-overview), [Windows color personalization](https://support.microsoft.com/en-US/Windows/Experience/Personalization/personalize-your-colors-in-windows). Các trường AppMode/SystemMode còn được đối chiếu với theme Aero/ThemeA đi kèm Windows trên máy này.
- [Sublime Text: Color Schemes](https://www.sublimetext.com/docs/color_schemes.html), [Themes và theme inheritance](https://www.sublimetext.com/docs/themes.html). Các biến UI được đối chiếu với gói Theme - Default của Sublime Text cài trên máy.
- [Telegram Desktop Theme Reference](https://github.com/telegramdesktop/tdesktop/wiki/Theme-Reference), [palette upstream của Desktop App Toolkit](https://github.com/desktop-app/lib_ui/blob/master/ui/colors.palette), [parser theme của Telegram Desktop](https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/SourceFiles/window/themes/window_theme.cpp). Wiki cũ chỉ dùng để tham khảo cách nhập/đóng gói; cú pháp còn được đối chiếu với parser hiện tại.
- [Vimium Options: phạm vi Custom CSS](https://github.com/philc/vimium/blob/master/pages/options.html), [hint selectors](https://github.com/philc/vimium/blob/master/content_scripts/vimium.css), [Vomnibar CSS](https://github.com/philc/vimium/blob/master/pages/vomnibar_page.css), [HUD CSS](https://github.com/philc/vimium/blob/master/pages/hud_page.css).
- [Antigravity App Settings](https://antigravity.google/docs/settings): phần App, không nhầm CLI colorScheme với theme App.
- [OpenAI Settings / Appearance](https://learn.chatgpt.com/docs/reference/settings): giao diện, màu, font và Import/Copy theme. Schema portable bổ sung được kiểm tra từ mã ứng dụng cài trên máy, không coi là API ổn định được tài liệu hóa.

## Cơ sở y tế và khoa học dùng khi phát triển

### 1. Theme tác động được đến đâu?

Mục tiêu là hỗ trợ đọc rõ, giảm yếu tố gây khó chịu và giảm gián đoạn do giao diện. Theme chưa được thử nghiệm lâm sàng, không phải sản phẩm điều trị hoặc phòng bệnh mắt. Khả năng tập trung, sự dễ chịu, tốc độ đọc và độ hiểu là các kết quả khác nhau: không được dùng kết quả này để khẳng định kết quả kia.

## Cơ sở khoa học Bằng chứng y tế và khoa học thị giác

#### Mỏi mắt do thiết bị số có nhiều nguyên nhân

- **Nguồn:** American Academy of Ophthalmology (AAO), *Computers, Digital Devices, and Eye Strain*, 2024. [Bài hướng dẫn](https://www.aao.org/eye-health/diseases/computer-usage).
- **Loại nguồn:** hướng dẫn chuyên môn cho công chúng; không phải thử nghiệm theme.
- **Diễn giải:** nhìn gần kéo dài, chớp mắt và bề mặt mắt, độ sáng, phản chiếu, điều kiện thị lực và tư thế có liên quan đến khó chịu khi dùng màn hình.
- **Áp dụng:** hướng dẫn người dùng điều chỉnh môi trường, khoảng cách và nghỉ nhìn gần; không hứa theme giải quyết hết các nguyên nhân.

#### Cỡ chữ phải đủ lớn để đọc trôi chảy

- **Nguồn:** Atilgan N, Xiong YZ, Legge GE (2020), *Reconciling print-size and display-size constraints on reading*. [Bài nghiên cứu](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720185/).
- **Loại nguồn:** nghiên cứu thực nghiệm về đọc, kích thước chữ và giới hạn hiển thị.
- **Diễn giải:** tốc độ đọc phụ thuộc đồng thời kích thước chữ và lượng ký tự hiển thị. Cỡ chữ nhỏ hơn ngưỡng phù hợp có thể làm chậm đọc; phóng to quá mức cũng làm giảm lượng nội dung trên dòng.
- **Áp dụng:** cho phép tăng cỡ chữ, thử ở khoảng cách sử dụng thật và kiểm tra dấu tiếng Việt. Terminal bắt đầu Cascadia Mono 14 pt, cellHeight 1.3; đây là lựa chọn thử, không phải kích thước được chứng minh tốt nhất.
- **Giới hạn:** pt của Windows Terminal khác CSS px; không suy ra cỡ nhìn thực từ số cấu hình duy nhất.

#### Nhiễu thị giác có thể làm việc tìm và nhận diện thông tin khó hơn

- **Nguồn:** van den Berg R, Roerdink JBTM, Cornelissen FW (2009), *A crowding model of visual clutter*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/19757933/), [DOI](https://doi.org/10.1167/9.4.24).
- **Loại nguồn:** mô hình và thử nghiệm khoa học thị giác.
- **Áp dụng:** giới hạn trang trí, nhóm thông tin rõ, giao diện ổn định, giữ tín hiệu chức năng.
- **Giới hạn:** áp dụng vào theme là suy luận thiết kế; chưa chứng minh giao diện đơn sắc giúp tăng chú ý lâu dài. Không có căn cứ từ nguồn này cho tỷ lệ 90/8/2 hoặc tác dụng điều trị ADHD.

#### Chữ tối trên nền sáng có lợi thế trong một số tác vụ đọc

- **Nguồn:** Piepenbrock C, Mayr S, Buchner A (2014), *Smaller pupil size and better proofreading performance with positive than with negative polarity displays*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25135324/), [DOI](https://doi.org/10.1080/00140139.2014.948496).
- **Loại nguồn:** thực nghiệm về đồng tử và dò lỗi văn bản.
- **Áp dụng:** cung cấp bản sáng để thử trong môi trường đủ sáng và bản tối như một lựa chọn.
- **Giới hạn:** kết quả dò lỗi không chứng minh mọi người bớt mỏi mắt với light mode; không xác lập CR 9.5–10.5:1 hoặc ngưỡng halation 13:1.

#### Bằng chứng về lịch nghỉ 20–20–20 còn chưa đồng nhất

- **Nguồn A:** Talens-Estarelles C và cộng sự, *The effects of breaks on digital eye strain, dry eye and binocular vision: Testing the 20-20-20 rule*, xuất bản trực tuyến 2022, số tạp chí 2023. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35963776/), [DOI](https://doi.org/10.1016/j.clae.2022.101744).
- **Kết quả:** nghiên cứu 29 người có triệu chứng ghi nhận cải thiện triệu chứng khi dùng nhắc nghỉ; không ghi nhận cải thiện tương ứng ở các chỉ dấu bề mặt mắt trong thời gian thử.
- **Nguồn B:** Johnson A, Rosenfield M (2023; trực tuyến 2022), *20-20-20 Rule: Are These Numbers Justified?* [PubMed](https://pubmed.ncbi.nlm.nih.gov/36473088/).
- **Kết quả:** không ủng hộ hiệu quả của các lần nghỉ 20 giây theo lịch trong điều kiện thử nghiệm của nghiên cứu.
- **Áp dụng:** khuyến khích nghỉ nhìn gần đều đặn và chớp mắt đầy đủ; không coi đúng ba con số 20 là phác đồ chắc chắn. Theme Terminal hiện chưa cài bộ nhắc nghỉ.

#### Không suy từ màu ấm thành hiệu quả giảm mỏi mắt

- **Nguồn:** Singh S và cộng sự (2023), Cochrane, *Blue-light filtering spectacle lenses for visual performance, sleep, and macular health in adults*. [Tóm tắt Cochrane](https://www.cochrane.org/evidence/CD013244_blue-light-filtering-spectacle-lenses-visual-performance-macular-back-part-eye-protection-and), [DOI](https://doi.org/10.1002/14651858.CD013244.pub2).
- **Loại nguồn:** tổng quan hệ thống 17 thử nghiệm ngẫu nhiên về kính lọc xanh.
- **Diễn giải:** có thể không giảm mỏi mắt ngắn hạn so với kính không lọc; tác động đến giấc ngủ chưa chắc chắn.
- **Giới hạn:** nghiên cứu kính, không trực tiếp thử bảng màu theme; không được khẳng định mọi can thiệp giảm ánh sáng bước sóng ngắn đều vô hiệu.
- **Áp dụng:** màu trắng ngà/đen than là lựa chọn thị giác. Không quảng cáo “cắt ánh sáng xanh bảo vệ võng mạc” từ HEX, hue hoặc chroma.

#### Giấc ngủ phụ thuộc ánh sáng thực và thời điểm, không chỉ màu giao diện

- **Nguồn A:** Brown TM và cộng sự (2022), *Recommendations for daytime, evening, and nighttime indoor light exposure to best support physiology, sleep, and wakefulness in healthy adults*. [PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001571), [DOI](https://doi.org/10.1371/journal.pbio.3001571).
- **Loại nguồn:** đồng thuận chuyên gia tổng hợp bằng chứng về phơi sáng và nhịp sinh học ở người trưởng thành khỏe mạnh.
- **Diễn giải:** xét ánh sáng tại mắt, phổ và thời điểm; giảm kích thích ánh sáng buổi tối gắn với giờ ngủ cá nhân. Melanopic EDI khác lux thông thường và không suy được từ màu HEX.
- **Nguồn B:** Duraccio KM và cộng sự (2021), *Does iPhone night shift mitigate negative effects of smartphone use on sleep outcomes in emerging adults?* [PubMed](https://pubmed.ncbi.nlm.nih.gov/33867308/), [DOI](https://doi.org/10.1016/j.sleh.2021.03.005).
- **Kết quả:** thử nghiệm ngẫu nhiên 167 người 18–24 tuổi không thấy khác biệt kết quả ngủ do Night Shift trong toàn bộ mẫu.
- **Áp dụng:** không hứa dark mode hoặc Night Light giúp ngủ tốt; tự động hóa theo giờ chưa nằm trong bản Terminal đầu tiên.

## Chuẩn kỹ thuật Chuẩn kỹ thuật hỗ trợ khả năng đọc — không phải bằng chứng điều trị

| Nguồn | Yêu cầu dùng trong dự án | Giới hạn |
|---|---|---|
| [WCAG Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Chữ thường >=4.5:1 | Chuẩn web; dùng làm mục tiêu kỹ thuật tham chiếu cho terminal, không tuyên bố terminal đạt toàn bộ WCAG. |
| [WCAG Contrast Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html) | Chữ chính hướng tới >=7:1 | Không phải cửa sổ tương phản an toàn y khoa. |
| [WCAG Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | Tín hiệu cần thiết để nhận diện điều khiển/trạng thái >=3:1 trong phạm vi áp dụng | Cần kiểm tra từng trạng thái thực tế. |
| [WCAG Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | Giao diện web phải chịu được thay đổi khoảng cách theo tiêu chí | Không áp nguyên bộ giá trị CSS cho lưới terminal. |
| [WCAG Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) | Kiểm soát chuyển động/tự cập nhật thuộc phạm vi tiêu chí | Theme không thể loại hết chuyển động do ứng dụng TUI tạo. |
| [W3C CSS Color 4](https://www.w3.org/TR/css-color-4/) | Phân biệt OKLCH, sRGB và độ chói tương đối | OKLCH không đo phổ ánh sáng hoặc liều phơi sáng tại mắt. |

## Cách diễn đạt Quy tắc diễn đạt khi viết README

**Có thể viết:** “Thiết kế nhằm hỗ trợ đọc rõ và giảm nhiễu giao diện; màu chữ được kiểm tra tương phản sRGB trên nền mặc định. Cỡ chữ và chế độ sáng/tối có thể điều chỉnh.”

**Chưa được khẳng định:** “đã chứng minh giảm mỏi mắt”, “bảo vệ võng mạc”, “ngăn khô mắt”, “hỗ trợ tiết melatonin”, “tăng tập trung X%”, “chống halation ở CR cố định”, “phù hợp cho mọi người”.

Các thông số màu ấm, font 14 pt, cellHeight 1.3, padding, màu hồng đất và syntax ít màu là quyết định thiết kế cần đánh giá; không gắn nhãn là khuyến cáo y khoa.

## Thử nghiệm cá nhân Cách kiểm nghiệm cá nhân

So sánh theme hiện tại và theme mới trong các phiên tương đương; giữ gần như nhau về màn hình, ánh sáng, khoảng cách, tác vụ và nghỉ. Ghi độ hiểu/độ chính xác, thời gian, số gián đoạn và khô/rát/nhức/mờ/chói trước–sau (0–10). Thử từng nhóm thay đổi để dễ giải thích. Khoảng hai tuần là lịch thực dụng, không phải thời gian đủ để chứng minh hiệu quả lâm sàng. Không kéo dài phiên chỉ để đạt KPI. Khó chịu dai dẳng cần được đánh giá nguyên nhân thị lực/bề mặt mắt, thay vì chỉ đổi màu theme.
