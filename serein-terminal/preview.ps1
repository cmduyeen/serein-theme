$esc = [char]27
Write-Host ''
Write-Host 'Đọc rõ tiếng Việt: Nguyễn, tưởng tượng, khuỷu tay, sự tập trung.'
Write-Host 'Phân biệt ký tự: I l 1 | O 0 | {} [] () <> / \ ; : , .'
Write-Host 'Regular text / chữ thường; chọn đoạn này để thử selection.'
Write-Host "$esc[1mBold / chữ đậm$esc[0m    $esc[3mItalic / chữ nghiêng$esc[0m"
$labels = @('neutral','error','success','warning','info','accent','path','text')
for ($i=0; $i -lt 8; $i++) {
    Write-Host ("{0}[{1}m{2,-10}{0}[0m {0}[{3}m{4}{0}[0m" -f $esc, (30+$i), $labels[$i], (90+$i), "bright $($labels[$i])")
}
Write-Host ''
Write-Host '[OK] Build completed.  [WARN] Check configuration.  [ERROR] Example only.'
Write-Host 'Thử đọc, chọn chữ, resize cửa sổ, Ctrl+Plus/Minus và gõ lệnh có comment.'
Write-Host 'Đổi profile Light/Dark bằng menu tab. Không cần làm việc liên tục để thử theme.'
