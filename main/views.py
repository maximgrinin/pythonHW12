# Импортируем необходимые классы и функции
from flask import Blueprint, request, render_template
from utils import get_posts_by_tag
import names

# Создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку для главной страницы
@main_blueprint.route('/')
def index_page():
    return render_template('index.html')


# Создаем вьюшку для страницы поиска
@main_blueprint.route('/search')
def search_page():
    # Обрабатываем параметры, отбираем посты, где содержится фраза поиска
    tag = request.args['s']
    post_list = get_posts_by_tag(tag)
    names.main_logger.info(f"Осуществлен поиск по тэгу <{tag}>")

    return render_template('post_list.html', tag=tag, post_list=post_list)
