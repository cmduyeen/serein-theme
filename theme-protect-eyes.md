# KẾ HOẠCH DỰ ÁN: HỆ THỐNG GIAO DIỆN "ZERO-DISTRACTION"

> Bản ý tưởng lịch sử. Một số diễn giải y khoa và thông số bên dưới đã được sửa trong phần 4 và `docs/scientific-basis.vi.md`. Dùng tài liệu cơ sở khoa học làm nguồn chính khi viết README hoặc giới thiệu sản phẩm.
*(Kết hợp Y khoa Nhãn khoa & Chủ nghĩa Siêu Tối giản)*

---

## 1. TỔNG QUAN & MỤC TIÊU DỰ ÁN
* **Mục tiêu sức khỏe:** Giảm thiểu tối đa hiện tượng mỏi cơ thể mi, hiệu ứng quầng sáng (halation) và sắc sai (chromatic aberration) khi làm việc/học tập liên tục trên 4 giờ/ngày.
* **Mục tiêu hiệu suất:** Loại bỏ hoàn toàn nhiễu thị giác ngoại biên, khóa chặt sự tập trung vào nội dung chính thông qua mô hình đơn sắc mô phỏng giấy điện tử (Digital E-Ink) với tỷ lệ phân bổ **90% Nền tĩnh – 8% Văn bản – 2% Điểm neo**.
* **Phạm vi áp dụng:** Đồng bộ hóa trải nghiệm thị giác trên tất cả các công cụ cốt lõi (Hệ điều hành, Trình duyệt web, Công cụ ghi chú/học tập, Trình soạn thảo/Terminal).

---

## 2. LỘ TRÌNH TRIỂN KHAI CHI TIẾT (4 GIAI ĐOẠN)

### Giai đoạn 1: Kỹ thuật Thiết kế Bảng màu & Hệ thống Token (Color Engineering)
*Mục tiêu: Xây dựng bảng màu bằng toán học dựa trên đặc tính sinh học của võng mạc, đảm bảo tính đồng nhất nhận thức (perceptual uniformity) trước khi xuất ra mã HEX.*

#### 1.1. Nguyên lý Toán học & Nhãn khoa khi tạo màu
1. **Chọn Không gian màu OKLCH thay vì HSL/RGB:**
   * Trong hệ HSL thông thường, hai màu có cùng độ sáng $L = 50\%$ (ví dụ Vàng và Xanh dương) lại có độ chói vật lý hoàn toàn khác nhau, làm mắt phải điều tiết lại khi liếc qua.
   * Sử dụng không gian màu **OKLCH** ($L$: Độ sáng nhận thức, $C$: Độ thuần sắc/Chroma, $H$: Sắc độ/Hue) giúp cố định chính xác lượng ánh sáng đi vào mắt trên mọi thành phần giao diện.
2. **Khóa trục sắc độ ấm cho toàn bộ dải trung tính (Warm Neutral Axis):**
   * Thay vì dùng xám trung tính thuần túy ($C = 0$, vốn phản xạ ánh sáng xanh từ đèn nền LED), toàn bộ màu nền và chữ đều được neo tại góc sắc độ ấm **$H \approx 75^\circ - 85^\circ$** (vùng vàng hổ phách nhạt) với độ thuần sắc cực thấp **$C \in [0.005, 0.012]$**.
   * Mức $C$ này đủ nhỏ để não bộ nhận diện là màu trắng giấy/đen than sạch sẽ (không gây cảm giác "màn hình bị ố vàng"), nhưng đủ để cắt giảm năng lượng bước sóng ngắn ($450\text{–}480\text{ nm}$).
3. **Tính toán Vùng Tương phản An toàn (Anti-Halation Contrast Window):**
   * Tỷ lệ tương phản được tính theo công thức độ chói tương đối WCAG:
     $$CR = \frac{Y_{\text{sáng}} + 0.05}{Y_{\text{tối}} + 0.05}$$
   * **Chữ chính (Primary Text):** Khóa chặt trong khoảng **$9.5:1 \le CR \le 10.5:1$**. Mức này vượt chuẩn đọc sâu WCAG AAA ($7:1$) nhưng thấp hơn ngưỡng gây hiệu ứng quầng sáng ($> 13:1$), giúp nét chữ sắc gọn mà không bị nhòe biên.
   * **Chữ phụ & Ghi chú (Muted Text):** Khóa trong khoảng **$4.6:1 \le CR \le 5.2:1$** (đạt chuẩn WCAG AA), đẩy thông tin thứ cấp lùi về phía sau về mặt thị giác.
4. **Phân lớp không gian bằng Bước nhảy Độ sáng ($\Delta L$) thay cho Đường viền:**
   * Loại bỏ hoàn toàn đường kẻ phân chia (`border`). Các lớp giao diện (Nền chính $\rightarrow$ Thanh bên $\rightarrow$ Vùng chọn) được tách biệt bằng bước nhảy độ sáng nhận thức cố định **$\Delta L \approx 0.035$** trong không gian OKLCH.
5. **Ràng buộc Đồng độ sáng & Trần bão hòa cho Màu nhấn (Iso-luminant Accent):**
   * Màu nhấn duy nhất (Hồng đất trầm) được giới hạn trần độ thuần sắc **$C \le 0.075$** và có độ sáng $L$ tiệm cận với chữ chính để tránh hiện tượng "rung màu" (chromostereopsis) khi đứng cạnh văn bản.
   * Các màu trạng thái (Lỗi, Cảnh báo) cũng bị hạ bão hòa và kéo về tông ấm (Đỏ gạch trầm, Vàng đất) thay vì dùng màu cơ bản nguyên chất.

#### 1.2. Bảng Thông số Token Kỹ thuật Chi tiết (Master Palette)

**A. Chế độ Ban ngày — Warm Alabaster (Nền chính: `#F6F4F0` | Độ chói $Y = 0.906$)**

| Tên Token | Vai trò Giao diện | Mã HEX | Thông số OKLCH | Tỷ lệ Tương phản ($CR$) |
| :--- | :--- | :--- | :--- | :--- |
| `--bg-canvas` | Nền không gian làm việc chính | `#F6F4F0` | `oklch(0.966 0.007 85)` | `1.00 : 1` *(Chuẩn nền)* |
| `--bg-surface` | Nền thanh bên (Sidebar), thanh tab | `#EDEAE4` | `oklch(0.935 0.009 82)` | `1.08 : 1` *(Tách lớp êm)* |
| `--bg-elevated` | Dòng đang gõ (Active line), vùng chọn | `#E3DFD7` | `oklch(0.901 0.011 80)` | `1.18 : 1` *(Định vị vùng)* |
| `--border-subtle` | Đường phân cách cực mảnh (nếu bắt buộc) | `#D6D1C7` | `oklch(0.858 0.012 78)` | `1.32 : 1` *(Không cắt mắt)* |
| `--text-primary` | Văn bản nội dung chính, tiêu đề | `#3D3A36` | `oklch(0.352 0.008 75)` | **`10.28 : 1`** *(Tối ưu đọc sâu)* |
| `--text-secondary` | Code, từ khóa phụ, nhãn phân loại | `#5C5852` | `oklch(0.465 0.009 75)` | **`6.45 : 1`** *(Phân cấp nhẹ)* |
| `--text-muted` | Chú thích, metadata, số dòng | `#757069` | `oklch(0.552 0.010 75)` | **`4.62 : 1`** *(Chuẩn WCAG AA)* |
| `--accent-primary` | Con trỏ nhập liệu, tab đang mở, link | `#9E525E` | `oklch(0.515 0.072 10)` | **`5.38 : 1`** *(Điểm neo tập trung)* |
| `--accent-tint` | Nền highlight nhẹ cho từ khóa tìm kiếm | `#EFE2E4` | `oklch(0.918 0.018 10)` | `1.14 : 1` *(Không che chữ)* |
| `--semantic-error` | Cảnh báo lỗi nghiêm trọng (tông đỏ gạch) | `#A6443E` | `oklch(0.502 0.095 25)` | **`5.61 : 1`** *(Rõ nhưng không chói)* |

**B. Chế độ Ban đêm — Warm Obsidian (Nền chính: `#191817` | Độ chói $Y = 0.0085$)**

| Tên Token | Vai trò Giao diện | Mã HEX | Thông số OKLCH | Tỷ lệ Tương phản ($CR$) |
| :--- | :--- | :--- | :--- | :--- |
| `--bg-canvas` | Nền không gian làm việc chính | `#191817` | `oklch(0.208 0.004 75)` | `1.00 : 1` *(Chuẩn nền tối)* |
| `--bg-surface` | Nền thanh bên (Sidebar), thanh tab | `#21201E` | `oklch(0.242 0.005 75)` | `1.12 : 1` *(Tách lớp êm)* |
| `--bg-elevated` | Dòng đang gõ (Active line), vùng chọn | `#2B2926` | `oklch(0.281 0.006 75)` | `1.28 : 1` *(Định vị vùng)* |
| `--border-subtle` | Đường phân cách cực mảnh (nếu bắt buộc) | `#363330` | `oklch(0.324 0.007 75)` | `1.51 : 1` *(Không cắt mắt)* |
| `--text-primary` | Văn bản nội dung chính, tiêu đề | `#C7C3BA` | `oklch(0.815 0.011 82)` | **`10.27 : 1`** *(Chống halation)* |
| `--text-secondary` | Code, từ khóa phụ, nhãn phân loại | `#A39E95` | `oklch(0.698 0.011 80)` | **`6.84 : 1`** *(Phân cấp nhẹ)* |
| `--text-muted` | Chú thích, metadata, số dòng | `#827D75` | `oklch(0.588 0.010 78)` | **`4.65 : 1`** *(Chuẩn WCAG AA)* |
| `--accent-primary` | Con trỏ nhập liệu, tab đang mở, link | `#C9848F` | `oklch(0.685 0.068 10)` | **`6.12 : 1`** *(Điểm neo tập trung)* |
| `--accent-tint` | Nền highlight nhẹ cho từ khóa tìm kiếm | `#2E2325` | `oklch(0.265 0.018 10)` | `1.22 : 1` *(Không che chữ)* |
| `--semantic-error` | Cảnh báo lỗi nghiêm trọng (san hô trầm) | `#CF766F` | `oklch(0.658 0.088 25)` | **`5.85 : 1`** *(Dịu mắt ban đêm)* |

#### 1.3. Quy tắc Phân cấp bằng Kiểu chữ (Typography Hierarchy)
* Thay thế việc tô nhiều màu (syntax/tag) bằng trọng lượng nét chữ (Font Weight) và độ chói:
  * **Tiêu đề / Từ khóa cốt lõi:** `--text-primary` + **SemiBold (600)**.
  * **Nội dung đọc / Thân bài:** `--text-primary` + Regular (400), chiều cao dòng `line-height: 1.65`, độ rộng cột tối đa `65–75 ký tự` để mắt không bị mỏi khi quét ngang.
  * **Ghi chú / Comment / Metadata:** `--text-muted` + *Italic*.

---

### Giai đoạn 2: Kiểm thử Thực tế & Cân chỉnh Môi trường (Calibration)
*Mục tiêu: Đảm bảo thông số lý thuyết hoạt động chính xác trên phần cứng màn hình và điều kiện ánh sáng thực tế của bạn.*

1. **Kiểm tra tỷ lệ tương phản thực tế:**
   * Thử nghiệm đọc một đoạn văn bản dài (khoảng 1.500 từ) trên nền `#F6F4F0` (ban ngày) và `#191817` (ban đêm).
   * Đánh giá cảm giác mắt sau 45 phút: Nếu thấy hơi lóa, giảm nhẹ độ sáng màn hình; nếu thấy chữ hơi chìm, dịch chuyển `--text-primary` lên 1 bậc độ sáng ($\Delta L = 0.02$).
2. **Đồng bộ ánh sáng vật lý:**
   * Đặt một tờ giấy trắng lên bàn làm việc, điều chỉnh độ sáng màn hình (thường từ 35%–50%) sao cho độ sáng của vùng nền `#F6F4F0` tương đương với độ phản xạ ánh sáng của tờ giấy đó.
   * Giữ nhiệt độ màu đèn phòng ở mức ấm (3000K – 4000K).

---

### Giai đoạn 3: Đóng gói & Áp dụng theo Tầng Ứng dụng (Implementation)
*Mục tiêu: Triển khai theme theo thứ tự từ ngoài vào trong để tránh tình trạng "sốc tương phản" khi chuyển đổi giữa các cửa sổ.*

* **Tầng 1 – Hệ điều hành & Trình duyệt (Không gian bao quanh):**
  * Chuyển giao diện OS (Windows/macOS) sang chế độ tối giản, tắt hiệu ứng trong suốt (transparency) và đổ bóng rườm rà.
  * Cài đặt extension tùy chỉnh CSS cho trình duyệt (như Stylus hoặc Dark Reader tùy chỉnh mã màu) để đồng bộ các trang web đọc tài liệu/học tập về đúng bảng token trên.
* **Tầng 2 – Không gian Học tập & Ghi chú (Obsidian / Notion / Anki):**
  * Viết file CSS Snippet ánh xạ trực tiếp các biến `--bg-canvas`, `--text-primary`, `--accent-primary`.
  * Ẩn thanh công cụ bên (Sidebar), thanh trạng thái và thanh cuộn khi đang gõ (chế độ Focus/Zen Mode).
* **Tầng 3 – Không gian Kỹ thuật & Lập trình (VS Code / Windows Terminal):**
  * Tạo file cấu hình JSON định nghĩa bảng màu Terminal và Theme Editor đơn sắc (Monochrome/Duotone).
  * Chỉ giữ lại `--accent-primary` (`#9E525E` / `#C9848F`) cho con trỏ nhập liệu, dòng đang chọn và `--semantic-error` cho cảnh báo lỗi nghiêm trọng.

---

### Giai đoạn 4: Tự động hóa Nhịp sinh học (Circadian Automation)
*Mục tiêu: Giao diện tự động thích ứng với ánh sáng tự nhiên mà không cần thao tác thủ công.*

1. **Thiết lập lịch chuyển đổi tự động:**
   * **06:30 – 17:30:** Tự động kích hoạt bản **Warm Alabaster (Sáng)** để đồng bộ với ánh sáng ban ngày, giúp đồng tử co tự nhiên và chữ đạt độ sắc nét cao nhất.
   * **17:30 – 06:30:** Tự động chuyển sang bản **Warm Obsidian (Tối)** để cắt giảm tổng lượng quang thông đi vào mắt, hỗ trợ tiết melatonin chuẩn bị cho giấc ngủ.
2. **Công cụ hỗ trợ:** Sử dụng tính năng Night Light/Night Shift có sẵn hoặc phần mềm tự động hóa (như Auto Dark Mode trên Windows) kết hợp đồng bộ biến màu CSS.

---

## 3. TIÊU CHÍ ĐÁNH GIÁ THÀNH CÔNG (CHECKLIST)
- [ ] **Không còn ranh giới thị giác gắt:** Mọi cửa sổ làm việc liền mạch như một trang giấy, không có viền trắng/đen chói mắt.
- [ ] **Thời gian tập trung liên tục:** Duy trì được các phiên làm việc sâu (Deep Work) kéo dài 90–120 phút mà không có cảm giác khô, nhức hốc mắt hay nhòe chữ.
- [ ] **Tính nhất quán 100%:** Khi chuyển từ trình duyệt sang ứng dụng ghi chú hoặc terminal, mắt không phải điều tiết lại độ sáng.

---

## 4. BỔ SUNG DỰA TRÊN BẰNG CHỨNG: DỄ ĐỌC VÀ HỖ TRỢ TẬP TRUNG

*Cập nhật ngày 12/11/2026. Các quy tắc trong phần này được ưu tiên khi mâu thuẫn với bản ý tưởng phía trên. Đây là đặc tả thiết kế cần kiểm thử, không phải phác đồ điều trị hay bằng chứng theme cải thiện sức khỏe.*

### 4.1. Điều chỉnh cơ sở khoa học của bản gốc

- Mục tiêu: đọc rõ, giảm khó chịu và nhiễu không cần thiết; hỗ trợ nghỉ nhìn gần. Không cam kết ngăn bệnh mắt, chữa khô mắt hoặc kéo dài thời gian làm việc không nghỉ.
- OKLCH hỗ trợ thiết kế màu theo cảm nhận, không cố định lượng ánh sáng đi vào mắt. Màu HEX không xác định được phổ phát xạ hay tác động sinh học của màn hình.
- Bỏ khẳng định CR 9.5–10.5:1 là cửa sổ y khoa an toàn và CR >13:1 gây halation. Không đặt trần tương phản phổ quát.
- Màu ấm, tỷ lệ 90/8/2, trần chroma và bước ΔL là lựa chọn thiết kế; chưa có bằng chứng chúng tối ưu cho sức khỏe hoặc tập trung.
- Tính lại tương phản từ HEX sRGB: muted sáng #757069 trên #F6F4F0 chỉ khoảng 4.47:1; muted tối #827D75 trên #191817 chỉ khoảng 4.34:1. Cần sửa trước khi dùng cho chữ thường. Kiểm tra mọi nền thực tế, không chỉ canvas.
- Thay tiêu chí làm việc liên tục 90–120 phút bằng khả năng hoàn thành tác vụ với nghỉ nhìn gần đều đặn, không tăng triệu chứng. Nhất quán giao diện không bảo đảm mắt không cần thích nghi độ sáng.
- Độ sáng phần cứng, phản chiếu, khoảng cách nhìn, thị lực và chớp mắt cần được xét riêng. Không quy định chung độ sáng màn hình 35–50% hoặc hứa hẹn màu ấm cải thiện giấc ngủ [6–9].

### 4.2. Cỡ chữ và nhận diện ký tự

**Cơ sở:** Nghiên cứu đọc cho thấy cỡ chữ quá nhỏ làm giảm tốc độ đọc; cỡ chữ lớn hơn cũng phải cân đối với số ký tự hiển thị. Kích thước góc nhìn phụ thuộc cỡ ký tự thực và khoảng cách, nên cùng số pixel chưa chắc cho cùng khả năng đọc [1].

**Yêu cầu thiết kế:**
- Văn xuôi bắt đầu thử ở 18 CSS px, code 16 CSS px; đây là cấu hình thử, không phải ngưỡng y khoa. Cho phép tăng/giảm cỡ chữ độc lập và zoom ít nhất 200% không mất nội dung hay thao tác.
- Ưu tiên font có dấu tiếng Việt đầy đủ, nét rõ, phân biệt I/l/1 và O/0. Không mặc định một nhóm serif/sans-serif tốt nhất cho tất cả mọi người.
- Thân bài weight 400–500 tùy font; tránh nét quá mảnh. Không dùng italic cho toàn bộ comment hoặc đoạn dài theo mặc định.
- Kiểm tra chữ có dấu nhiều tầng và không cắt dấu khi tăng cỡ chữ/giãn dòng; kiểm tra thực tế trên màn hình người dùng.

### 4.3. Khoảng cách, cấu trúc và khả năng theo dõi dòng

**Cơ sở:** Nhiễu và crowding có thể cản trở nhận diện, tìm kiếm thị giác. Việc chuyển các kết quả này thành bố cục theme là suy luận thiết kế, không chứng minh một khoảng cách cụ thể sẽ tăng tập trung [2].

**Yêu cầu thiết kế:**
- Văn xuôi bắt đầu với line-height 1.6–1.7, bề rộng khoảng 60–75ch; code thử 1.45–1.6. Cho phép tùy chỉnh; ch là đơn vị bố cục, không đếm chính xác ký tự trong font tỷ lệ.
- Căn trái văn xuôi tiếng Việt, không ép căn đều hai lề theo mặc định; nhóm đoạn và tiêu đề rõ, tránh quá nhiều mức phân cấp.
- Giữ letter-spacing bình thường làm mặc định, không tự động giãn chữ mạnh với lý do giảm crowding.
- Không mất nội dung/chức năng khi người dùng ghi đè line-height 1.5, khoảng sau đoạn 2em, letter-spacing 0.12em và word-spacing 0.16em. Đây là kiểm tra khả năng thích ứng WCAG, không phải bộ khoảng cách tối ưu bắt buộc [3].

### 4.4. Tương phản phục vụ đọc và định hướng

- Chữ thường đạt >=4.5:1 trên tất cả nền được phép sử dụng; thân bài hướng tới >=7:1. Các mức này là tiêu chí tiếp cận, không phải liều điều trị [5].
- Không làm mờ đoạn ngoài tiêu điểm đến mức không đọc được. Không hạ opacity cả vùng nội dung để tạo Focus Mode theo mặc định.
- Giữ focus bàn phím, con trỏ, vùng chọn và lỗi đủ rõ. Liên kết và trạng thái quan trọng có dấu hiệu ngoài màu sắc.
- Light mode là cấu hình khởi đầu khi phòng đủ sáng; dark mode là lựa chọn cá nhân và môi trường. Không khẳng định chế độ nào tốt nhất cho tất cả mọi người [10].

### 4.5. Hỗ trợ tập trung bằng giảm cạnh tranh chú ý

**Mục tiêu:** Giảm các nguồn gián đoạn do giao diện, không cam kết điều trị ADHD hay tăng năng lực chú ý sinh học.

- Focus Mode thu gọn sidebar, minimap và thông tin phụ khi người dùng bật; cung cấp cách mở lại rõ ràng bằng bàn phím và chuột.
- Không ẩn điều hướng hoặc làm bố cục nhảy liên tục mỗi lần gõ. Giữ vị trí đọc và tiêu điểm khi chuyển chế độ.
- Mặc định không có chuyển động trang trí lặp, badge nhấp nháy hoặc tự cuộn nội dung. Tôn trọng prefers-reduced-motion; chuyển động/tự cập nhật thuộc phạm vi WCAG cần cơ chế kiểm soát phù hợp [4].
- Cho phép con trỏ đứng yên; không ép tắt nhấp nháy với mọi người. Highlight dòng hiện tại nhẹ và có thể tắt.
- Giữ một màu nhấn cho thao tác chính; vẫn có màu chức năng cho lỗi/cảnh báo. Syntax ít màu phải được so sánh với syntax hiện tại bằng tác vụ code thực.
- Chặn thông báo, âm thanh hay nội dung feed thuộc ứng dụng/OS, không phải khả năng mặc định của theme CSS. Chỉ tích hợp khi nền tảng hỗ trợ và người dùng cấu hình.
- Nhắc nghỉ tùy chọn, nhẹ, có thể hoãn; không dùng đếm ngược thường trực hay popup chớp sáng. Phiên tập trung vẫn cho phép nghỉ mắt. Bằng chứng cho chính xác lịch 20–20–20 còn không đồng nhất [7].

### 4.6. Kiểm thử và điều kiện chấp nhận

1. Kiểm tra kỹ thuật: tất cả cặp chữ/nền, zoom, giãn chữ, dấu tiếng Việt, focus bàn phím, vùng chọn và reduced motion đều hoạt động.
2. Kiểm tra dễ đọc: đọc đoạn tương đương và trả lời câu hỏi; ghi tốc độ cùng độ hiểu, số lỗi hoặc số lần mất dòng. Không đánh giá chỉ bằng tốc độ.
3. Kiểm tra tập trung: tác vụ cố định, ghi kết quả, lỗi, gián đoạn do giao diện và mức tập trung tự báo cáo. Không dùng thời gian ngồi lâu hơn làm thước đo duy nhất.
4. Thử cá nhân A/B xen kẽ khoảng hai tuần như lịch thực dụng; giữ tương đối ổn định tác vụ, giờ, ánh sáng và nghỉ. Thay từng nhóm biến (typography, màu, Focus Mode) để dễ diễn giải.
5. Ghi khô/rát, nhức, mờ và chói trước/sau phiên theo thang 0–10. Ưu tiên cấu hình giảm khó chịu mà không giảm độ hiểu/độ chính xác. Kết quả một người chỉ hỗ trợ cá nhân hóa; chưa chứng minh hiệu quả y khoa.

### 4.7. Nguồn và phạm vi bằng chứng

1. [Atilgan, Xiong & Legge (2020): Reconciling print-size and display-size constraints on reading](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720185/) — nghiên cứu thực nghiệm về cỡ chữ, số ký tự và đọc.
2. [van den Berg và cộng sự (2009): A crowding model of visual clutter](https://pubmed.ncbi.nlm.nih.gov/19757933/) — mô hình và thực nghiệm về nhiễu thị giác; không phải thử nghiệm theme cải thiện chú ý dài hạn.
3. [W3C: Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) — tiêu chuẩn tiếp cận, không phải hướng dẫn điều trị.
4. [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) — kiểm soát chuyển động và tự cập nhật.
5. [W3C: Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) và [Contrast Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html).
6. [AAO: Computers, Digital Devices, and Eye Strain](https://www.aao.org/eye-health/diseases/computer-usage) — hướng dẫn lâm sàng cho công chúng.
7. [Talens-Estarelles và cộng sự: thử nhắc nghỉ 20–20–20](https://pubmed.ncbi.nlm.nih.gov/35963776/) và [Johnson & Rosenfield: kiểm tra các con số 20–20–20](https://pubmed.ncbi.nlm.nih.gov/36473088/) — kết quả khác nhau theo thiết kế nghiên cứu.
8. [Cochrane (2023): Blue-light filtering spectacle lenses](https://www.cochrane.org/evidence/CD013244_blue-light-filtering-spectacle-lenses-visual-performance-macular-back-part-eye-protection-and) — tổng quan về kính lọc xanh, không trực tiếp kiểm nghiệm theme.
9. [Brown và cộng sự (2022): Recommendations for daytime, evening, and nighttime indoor light exposure](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001571) — đồng thuận về ánh sáng và nhịp sinh học; không thể suy lượng phơi sáng từ HEX.
10. [Piepenbrock và cộng sự (2014): Smaller pupil size and better proofreading performance with positive than with negative polarity displays](https://pubmed.ncbi.nlm.nih.gov/25135324/) — thử nghiệm hiệu suất đọc, không chứng minh light mode giảm triệu chứng với mọi người.
