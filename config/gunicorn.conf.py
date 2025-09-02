# config/gunicorn.conf.py
bind = "127.0.0.1:5001"  # Внутренний порт для nginx
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True