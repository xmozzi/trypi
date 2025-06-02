class Config:
    # Konfigurasi database SQLite (ganti dengan DB lain jika perlu)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Matikan untuk menghindari peringatan
    SECRET_KEY = 'your_secret_key'  # Gunakan kunci yang lebih aman untuk production
