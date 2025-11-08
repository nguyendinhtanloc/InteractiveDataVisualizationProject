# Interactive Data Visualization Project

## Giới thiệu

Dự án này sử dụng **Apache Superset** để trực quan hóa dữ liệu từ **Supabase**. Người dùng có thể import cơ sở dữ liệu, tạo dashboard và khám phá dữ liệu một cách tương tác thông qua giao diện web.

## Mục lục

[Xem flow setup chi tiết](setup-flow.md)
- [Interactive Data Visualization Project](#interactive-data-visualization-project)
  - [Giới thiệu](#giới-thiệu)
  - [Mục lục](#mục-lục)
  - [Yêu cầu](#yêu-cầu)
  - [Cấu trúc thư mục](#cấu-trúc-thư-mục)
  - [Hướng dẫn cài đặt lần đầu](#hướng-dẫn-cài-đặt-lần-đầu)
  - [Cách sử dụng hằng ngày](#cách-sử-dụng-hằng-ngày)
  - [Đổi mật khẩu tài khoản Admin](#đổi-mật-khẩu-tài-khoản-admin)
  - [Phát triển và chạy script Python cục bộ](#phát-triển-và-chạy-script-python-cục-bộ)

## Yêu cầu

- Docker và Docker Compose
- Python 3.12 trở lên (chỉ cần nếu muốn chạy các script Python cục bộ)
- Kết nối Internet để tải Docker image và cài đặt thư viện Python

## Cấu trúc thư mục

```
├── docker-compose.yml             # Cấu hình Docker Compose để chạy Superset
├── superset_config.py             # Cấu hình Superset cục bộ
├── requirements.txt               # Danh sách thư viện Python cần thiết
├── docker-entrypoint-initdb.d     # Thư mục chứa script khởi tạo dữ liệu
│   ├── import_supabase.py         # Script import dữ liệu từ Supabase
│   └── supabase.json              # File dữ liệu mẫu từ Supabase
├── run-all.sh                     # Script tự động setup và khởi động hệ thống
├── .env.example                   # Mẫu file cấu hình môi trường
└── README.md                      # Tài liệu hướng dẫn
```

## Hướng dẫn cài đặt lần đầu

1. Clone repository:

   ```bash
   git clone <repo_url>
   cd InteractiveDataVisualizationProject
   ```

2. Tạo file `.env` từ mẫu:

   ```bash
   cp .env.example .env
   ```

   Sau đó chỉnh sửa nội dung `.env` nếu cần thiết.

3. Cấp quyền thực thi và chạy script:

   ```bash
   chmod +x run-all.sh init_superset.sh
   ./run-all.sh
   ```

   Script sẽ thực hiện các bước sau:

   - Tạo môi trường ảo Python (`venv`) nếu chưa có
   - Cài đặt thư viện từ `requirements.txt`
   - Khởi động Superset bằng Docker Compose
   - Import dữ liệu từ `supabase.json`

4. Truy cập Superset tại địa chỉ: [http://localhost:8080](http://localhost:8080)

   Tài khoản mặc định:  
   - Username: `admin`  
   - Password: `admin`

## Cách sử dụng hằng ngày

Sau khi đã setup lần đầu, những lần sử dụng tiếp theo chỉ cần:

1. Di chuyển vào thư mục dự án:

   ```bash
   cd InteractiveDataVisualizationProject
   ```

2. (Tùy chọn) Kích hoạt môi trường ảo nếu muốn chạy script Python:

   - Trên Mac/Linux:

     ```bash
     source venv/bin/activate
     ```

   - Trên Windows:

     ```bash
     venv\Scripts\activate
     ```

3. Khởi động Superset:

   ```bash
   docker-compose up -d
   ```

4. Truy cập Superset tại: [http://localhost:8088](http://localhost:8088)

5. Khi sử dụng xong, dừng container:

   ```bash
   docker-compose down
   ```

Lưu ý: Nếu không cần chạy script Python, có thể bỏ qua bước kích hoạt môi trường ảo.

## Đổi mật khẩu tài khoản Admin

1. Đăng nhập Superset bằng tài khoản `admin / admin`
2. Vào mục **Profile → Change Password**
3. Nhập mật khẩu mới và lưu lại

## Phát triển và chạy script Python cục bộ

Nếu bạn muốn xử lý dữ liệu hoặc import thủ công:

1. Kích hoạt môi trường ảo:

   ```bash
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

2. Cập nhật pip:

   ```bash
   pip install --upgrade pip
   ```

3. Cài đặt thư viện:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy script ví dụ:

   ```bash
   python docker-entrypoint-initdb.d/import_supabase.py
   ```

5. Thoát môi trường ảo khi hoàn tất:

   ```bash
   deactivate
   ```

6. Nếu muốn thêm thư viện mới:

   ```bash
   pip install <package_name>
   pip freeze > requirements.txt
   ```
