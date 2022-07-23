import logging

# Определяем глобальные настройки
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Создаем регистратор с именем 'main_logger'
main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.DEBUG)
# Создаем файловый обработчик, который регистрирует отладочные сообщения
file_handler = logging.FileHandler("main_log.log")
file_handler.setLevel(logging.DEBUG)
# Создаем консольный обработчик с более высоким уровнем журнала
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
# Создаем форматтер и добавляем его в обработчики
formatter_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter_date = '%H:%M:%S'
formatter = logging.Formatter(formatter_string, formatter_date)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# Добавляем настроенные обработчики в логгер
main_logger.addHandler(file_handler)
main_logger.addHandler(console_handler)
