# Đưa Serein lên GitHub và chia sẻ bản cài

## Repository chung

Tên đề xuất: `serein-theme`. README ở root giới thiệu cả ba ứng dụng; các thư mục con giữ nguồn độc lập.

Sau khi tạo repo GitHub rỗng trong tài khoản của bạn:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/serein-theme.git
git push -u origin main
```

Thay `YOUR-USERNAME` bằng tài khoản thực. Repo cục bộ chưa đồng nghĩa đã có repo trên GitHub. Không commit thư mục `dist/`; chia sẻ file cài qua GitHub Releases.

## Release

1. Chỉnh phiên bản component thay đổi trong manifest/package; cập nhật tên gói ở README nếu đổi version. Terminal dùng version trong tools/release.py.
2. Chạy `python tools/release.py` và kiểm tra script Terminal bằng `pwsh -NoProfile -File serein-terminal/verify.ps1`.
3. Cài thử VSIX trong một profile riêng; thử ZIP Obsidian với vault thử; kiểm tra Terminal trên cấu hình mẫu. Kiểm tra màu sáng/tối, chọn chữ, focus và thông báo lỗi.
4. Commit thay đổi. Tạo tag cho bộ phát hành, ví dụ `v0.1.0`.
5. Trên GitHub, tạo Release từ tag, đính kèm các gói trong `dist/` và SHA256SUMS.txt. Không đính kèm `.build/`, backups, install-state hoặc last-session.

Các component có thể khác version (bộ đầu tiên: Terminal 0.1.0, Obsidian 0.1.2, VS Code 0.1.0).

## Đưa lên kho theme chính thức

- **VS Code:** cần publisher Marketplace thật; `serein-local` chỉ là ID phát triển. Cập nhật package metadata/repository, đóng gói và phát hành bằng [vsce theo Microsoft](https://code.visualstudio.com/api/working-with-extensions/publishing-extension). Không cần Marketplace để chia sẻ VSIX trực tiếp.
- **Obsidian:** gói ZIP cài thủ công dùng được trước khi xuất bản. Community directory có [quy trình nộp theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme) riêng và yêu cầu repository/metadata/screenshot phù hợp. Không coi monorepo đã tự động đáp ứng yêu cầu đó.
- **Windows Terminal:** chia sẻ ZIP cùng script cài và hướng dẫn; không cần installer EXE có quyền admin.

Tên Serein chưa được kiểm tra tính độc quyền hoặc khả dụng trên Marketplace. Chốt namespace/publisher trước khi phát hành công khai.
