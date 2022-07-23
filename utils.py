# Импортируем необходимые классы и функции
from json import load as json_load, dump as json_dump, JSONDecodeError
import names


# Функция загружает посты из файла в список
def load_posts_from_json():
    """
    Загружает посты из файла в список
    """
    json = []
    try:
        with open(names.POST_PATH, 'r', encoding="utf-8") as file:
            json = json_load(file)
    except FileNotFoundError as e:
        # Будет выполнено, если файл не найден
        names.main_logger.warning(f"Не смогли прочитать файл с постами. [FileNotFoundError]: {e.strerror}, имя файла: {e.filename}")
    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        names.main_logger.warning(f"Не смогли обработать считанное из файла с постами")

    return json


# Функция возвращает список постов по вхождению тэга
def get_posts_by_tag(tag_name):
    """
    Возвращает посты по тэгу
    """
    post_list = load_posts_from_json()
    posts = []
    for post in post_list:
        if tag_name.strip().lower() in post['content'].strip().lower():
            posts.append(post)

    return posts


# Функция проверки расширения файла на допустимость
def is_filename_allowed(filename):
    if filename.split(".")[-1] in names.ALLOWED_EXTENSIONS:
        return True

    names.main_logger.error(f"Недопустимое расширение файла. Загружать можно: {', '.join(names.ALLOWED_EXTENSIONS)}")

    raise ValueError(f"Недопустимое расширение файла. Загружать можно: {', '.join(names.ALLOWED_EXTENSIONS)}")


# Функция добавления нового поста
def add_new_post_to_file(new_post):
    posts = load_posts_from_json()
    posts.append(new_post)

    try:
        with open(names.POST_PATH, 'w', encoding="utf-8") as file:
            json_dump(posts, file, ensure_ascii=False, indent=4)
    except FileNotFoundError as e:
        # Будет выполнено, если файл не найден
        names.main_logger.warning(f"Ошибка записи файла с постами. [FileNotFoundError]: {e.strerror}, имя файла: {e.filename}")
        raise e
    else:
        return True
