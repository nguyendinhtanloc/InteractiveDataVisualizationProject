# Flow setup và chạy Superset

┌───────────────────────────────┐
│ Clone repository & tạo .env   │
└─────────────┬─────────────────┘
              │
              ▼
┌───────────────────────────────┐
│ Cấp quyền chạy script         │
│ chmod +x run-all.sh init_superset.sh │
└─────────────┬─────────────────┘
              │
              ▼
┌───────────────────────────────┐
│ Chạy script lần đầu: ./run-all.sh │
└─────────────┬─────────────────┘
              │
   ┌──────────┴──────────┐
   ▼                     ▼
[Python venv]        [Docker Compose]
   │                     │
   │                     ▼
   │             ┌─────────────────┐
   │             │ Build & start   │
   │             │ container Superset │
   │             └─────────┬───────┘
   │                       │
   │                       ▼
   │             ┌─────────────────┐
   │             │ init_superset.sh│
   │             │ - DB upgrade    │
   │             │ - Create admin  │
   │             │ - Import data   │
   │             │ - superset init │
   │             │ - Start server  │
   │             └─────────┬───────┘
   │                       │
   └───────────────────────┘
                           ▼
             ┌───────────────────────────┐
             │ Superset chạy tại         │
             │ http://localhost:8088     │
             │ Login: admin / admin (.env) │
             └───────────────────────────┘

# Flow các lần chạy tiếp theo

┌───────────────────────────────┐
│ Vào thư mục dự án             │
└─────────────┬─────────────────┘
              │
              ▼
┌───────────────────────────────┐
│ docker-compose up -d          │
│ - Start container             │
│ - Superset đã có DB, admin    │
│ - Không cần tạo lại            │
└─────────────┬─────────────────┘
              │
              ▼
┌───────────────────────────────┐
│ Truy cập Superset             │
│ http://localhost:8088         │
└───────────────────────────────┘

