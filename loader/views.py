# Импортируем необходимые классы и функции
from flask import Blueprint, request, render_template
from utils import is_filename_allowed, add_new_post_to_file
import names

# Создаем блюпринт
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# Создаем вьюшку для страницы создания нового поста
@loader_blueprint.route('/post', methods=['GET'])
def post_page():
    return render_template('post_form.html')


# Добавляем пост к списку постов, создаем вьюшку для страницы добавленного поста
@loader_blueprint.route('/post', methods=['POST'])
def new_post_page():
    # Обрабатываем параметры
    picture = request.files.get("picture")
    content = request.form.get("content")

    new_post = {"pic": f"{names.UPLOAD_FOLDER}/{picture.filename}", "content": content}

    # Сохраняем загруженный файл
    try:
        if is_filename_allowed(picture.filename):
            picture.save(f"{names.UPLOAD_FOLDER}/{picture.filename}")
        add_new_post_to_file(new_post)
    except FileNotFoundError as e:
        names.main_logger.error(f"Произошла ошибка при сохранении файла. [FileNotFoundError]: {e.strerror}, имя файла: {e.filename}")
        return f"<h1>Произошла ошибка при сохранении файла</h1><p>[FileNotFoundError]: {e.strerror}, имя файла: {e.filename}</p>"
    except ValueError:
        names.main_logger.error(f"Недопустимое расширение файла. [ValueError]: имя файла: {picture.filename}")
        return f"<h1>Недопустимое расширение файла</h1><p>[ValueError]: имя файла: {picture.filename}</p>"

    names.main_logger.info(f"Добавили новый пост")

    return render_template('post_uploaded.html', post=new_post)
