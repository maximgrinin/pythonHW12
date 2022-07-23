# Импортируем необходимые классы и функции
from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint


def main():
    # Создаем Flask-приложение
    app = Flask(__name__)

    # Регистрируем блюпринты
    app.register_blueprint(main_blueprint)
    app.register_blueprint(loader_blueprint)

    @app.route("/uploads/<path:path>")
    def static_dir(path):
        return send_from_directory("uploads", path)

    # Запускаем приложение
    app.run(host='127.0.0.1', port=80)
    app.run()


if __name__ == '__main__':
    main()
