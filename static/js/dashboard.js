let autoRefreshInterval = null;

// Функция для загрузки системных данных
async function loadSystemData() {
    try {
        const response = await fetch('/api/system');
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        updateMetrics(data);
        
    } catch (error) {
        console.error('Error loading system data:', error);
        showError('Failed to load system data');
    }
}

// Функция обновления метрик на странице
function updateMetrics(data) {
    // CPU
    document.getElementById('cpu-percent').textContent = `${data.cpu_percent.toFixed(1)}%`;
    document.getElementById('cpu-progress').style.width = `${data.cpu_percent}%`;
    
    // Memory
    document.getElementById('memory-percent').textContent = `${data.memory.percent.toFixed(1)}%`;
    document.getElementById('memory-progress').style.width = `${data.memory.percent}%`;
    
    // Disk
    document.getElementById('disk-percent').textContent = `${data.disk.percent.toFixed(1)}%`;
    document.getElementById('disk-progress').style.width = `${data.disk.percent}%`;
    
    // Uptime
    document.getElementById('uptime').textContent = `${data.uptime.days}d ${data.uptime.hours}h`;
    
    // Last update
    const updateTime = new Date().toLocaleTimeString();
    document.getElementById('last-update').textContent = updateTime;
}

// Автозагрузка при открытии страницы
document.addEventListener('DOMContentLoaded', function() {
    loadSystemData();
});