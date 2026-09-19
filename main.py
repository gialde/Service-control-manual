"""Service-control-manual.

Стартовый сценарий сервиса управления инструкциями (ПР1).
Используются только простые типы данных, операции, преобразование типов,
условные конструкции, функции и импорт модулей.
"""

from datetime import date


def get_instruction_status(is_published: bool, is_archived: bool) -> str:
    """Возвращает текстовый статус инструкции.

    :param is_published: инструкция опубликована
    :param is_archived: инструкция находится в архиве
    :return: строка с описанием статуса
    """
    if is_archived:
        return "Инструкция в архиве"
    if is_published:
        return "Инструкция опубликована"
    return "Инструкция — черновик"


def estimate_reading_time(word_count: int, wpm: int = 200) -> str:
    """Оценивает время чтения инструкции в минутах.

    :param word_count: количество слов в инструкции
    :param wpm: скорость чтения, слов в минуту (по умолчанию 200)
    :return: строка с оценкой времени чтения
    """
    if word_count <= 0 or wpm <= 0:
        return "Некорректное количество слов"
    minutes = word_count // wpm
    if word_count % wpm != 0:
        minutes = minutes + 1
    return f"Примерное время чтения: {minutes} мин."


def check_user_access(role: str, is_public: bool) -> str:
    """Проверяет, разрешён ли пользователю доступ к инструкции.

    :param role: роль пользователя (admin, editor, reader)
    :param is_public: инструкция доступна публично
    :return: строка с результатом проверки
    """
    if is_public:
        return "Доступ разрешён"
    if role == "admin" or role == "editor":
        return "Доступ разрешён"
    return "Доступ запрещён"


if __name__ == "__main__":
    instruction_title = "Инструкция по технике безопасности"
    word_count = 850
    is_published = True
    is_archived = False
    user_role = "editor"
    is_public = False
    today = date.today()

    print(f"Инструкция: {instruction_title}")
    print(f"Дата: {today}")
    print(f"Статус: {get_instruction_status(is_published, is_archived)}")
    print(f"Объём: {word_count} слов")
    print(estimate_reading_time(word_count))
    print(f"Роль пользователя: {user_role}")
    print(f"Проверка доступа: {check_user_access(user_role, is_public)}")