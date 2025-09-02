from flask import Flask, render_template, jsonify
import os
import psutil
from datetime import datetime
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def dashboard():
    """Главная страница с основными метриками"""
    return render_template('dashboard.html')

@app.route('/api/system')
def api_system():
    """API эндпоинт для получения системных метрик"""
    try:
        # Получаем основные системные метрики
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Время работы системы
        boot_time = psutil.boot_time()
        uptime_seconds = datetime.now().timestamp() - boot_time
        uptime_hours = int(uptime_seconds // 3600)
        uptime_days = uptime_hours // 24
        
        system_info = {
            'cpu_percent': cpu_percent,
            'memory': {
                'total': memory.total,
                'used': memory.used,
                'percent': memory.percent
            },
            'disk': {
                'total': disk.total,
                'used': disk.used,
                'percent': (disk.used / disk.total) * 100
            },
            'uptime': {
                'days': uptime_days,
                'hours': uptime_hours % 24,
                'total_seconds': uptime_seconds
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(system_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Для разработки запускаем на localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
