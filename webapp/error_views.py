from django.shortcuts import render

CATEGORY_INFO = {
    "info": {
        "message": "Это информационный ответ сервера. Обычно пользователь его не видит.",
        "hint": "Вернитесь на главную страницу или повторите действие.",
    },
    "success": {
        "message": "Запрос выполнен успешно. Эта страница не требует от вас никаких действий.",
        "hint": "Можно вернуться на главную страницу.",
    },
    "redirect": {
        "message": "Запрошенная страница переместилась. Обычно браузер сам переходит по новому адресу.",
        "hint": "Если этого не произошло, вернитесь на главную страницу.",
    },
    "client": {
        "message": "Не удалось обработать запрос. Проверьте адрес страницы и введённые данные.",
        "hint": "Вернитесь назад или перейдите на главную страницу.",
    },
    "server": {
        "message": "На сервере произошла ошибка. Это не ваша вина, мы уже разбираемся.",
        "hint": "Попробуйте обновить страницу через пару минут. Если ошибка не исчезнет, свяжитесь с поддержкой.",
    },
}

# Особые описания для частых кодов
SPECIFIC_MESSAGES = {
    400: "Сервер не смог понять запрос. Возможно, в нём есть ошибка или он повреждён.",
    401: "Чтобы открыть эту страницу, нужно войти в систему.",
    403: "У вас нет прав для просмотра этой страницы.",
    404: "Такой страницы нет. Возможно, она была удалена или адрес введён неверно.",
    405: "Для этой страницы нельзя использовать такой способ запроса.",
    408: "Сервер слишком долго ждал ответа. Проверьте подключение и повторите попытку.",
    410: "Эта страница была удалена и больше недоступна.",
    413: "Отправленные данные или файл слишком большие.",
    415: "Этот тип файла не поддерживается.",
    418: "Сервер отказывается варить кофе, потому что он чайник.",
    429: "Слишком много запросов за короткое время. Подождите немного и повторите.",
    500: "На сервере произошла непредвиденная ошибка. Мы уже работаем над её устранением.",
    502: "Сервер получил некорректный ответ от другого сервера. Попробуйте позже.",
    503: "Сервис временно недоступен: идут технические работы или высокая нагрузка.",
    504: "Другой сервер слишком долго не отвечал. Попробуйте повторить через минуту.",
}


def get_category(code: int) -> str:
    if code < 200:
        return "info"
    if code < 300:
        return "success"
    if code < 400:
        return "redirect"
    if code < 500:
        return "client"
    return "server"

ERROR_DETAILS = {
    100: "Продолжайте запрос",
    101: "Переключение протоколов",
    102: "Обработка запроса",
    103: "Раннее уведомление",
    200: "Успешно",
    201: "Создано",
    202: "Принято",
    203: "Информация не авторитетна",
    204: "Нет содержимого",
    205: "Сброс содержимого",
    206: "Частичное содержимое",
    207: "Многостатусный ответ",
    208: "Уже сообщено",
    226: "IM использовано",
    300: "Множественный выбор",
    301: "Перемещено навсегда",
    302: "Найдено",
    303: "Смотреть другое",
    304: "Не изменялось",
    305: "Использовать прокси",
    307: "Временное перенаправление",
    308: "Постоянное перенаправление",
    400: "Некорректный запрос",
    401: "Требуется авторизация",
    402: "Требуется оплата",
    403: "Доступ запрещён",
    404: "Страница не найдена",
    405: "Метод не поддерживается",
    406: "Неприемлемо",
    407: "Требуется аутентификация прокси",
    408: "Истекло время ожидания",
    409: "Конфликт",
    410: "Удалено",
    411: "Требуется длина",
    412: "Предусловие не выполнено",
    413: "Слишком большой запрос",
    414: "Слишком длинный URI",
    415: "Неподдерживаемый тип данных",
    416: "Диапазон не достижим",
    417: "Ожидание не удалось",
    418: "Я — чайник",
    421: "Неверный запрос",
    422: "Невозможно обработать",
    423: "Заблокировано",
    424: "Неудачная зависимость",
    425: "Преждевременный запрос",
    426: "Требуется обновление",
    428: "Требуется предусловие",
    429: "Слишком много запросов",
    431: "Слишком большие заголовки",
    451: "Недоступно по юридическим причинам",
    500: "Внутренняя ошибка сервера",
    501: "Не реализовано",
    502: "Ошибка шлюза",
    503: "Сервис недоступен",
    504: "Превышено время ожидания",
    505: "Версия HTTP не поддерживается",
    506: "Вариант тоже проводит согласование",
    507: "Недостаточно места",
    508: "Обнаружен цикл",
    510: "Требуется расширение",
    511: "Требуется сетевая аутентификация",
}


def render_error(request, code: int, status: int | None = None):
    category = get_category(code)
    info = CATEGORY_INFO[category]

    context = {
        "code": code,
        "title": ERROR_DETAILS.get(code, "Неизвестная ошибка"),
        "description": SPECIFIC_MESSAGES.get(code, info["message"]),
        "hint": info["hint"],
        "category": category,   # info / success / redirect / client / server
    }
    return render(request, "http_code.html", context, status=status or code)


def handler100(request, exception=None):
    return render_error(request, 100)


def handler101(request, exception=None):
    return render_error(request, 101)


def handler102(request, exception=None):
    return render_error(request, 102)


def handler103(request, exception=None):
    return render_error(request, 103)


def handler200(request, exception=None):
    return render_error(request, 200)


def handler201(request, exception=None):
    return render_error(request, 201)


def handler202(request, exception=None):
    return render_error(request, 202)


def handler203(request, exception=None):
    return render_error(request, 203)


def handler204(request, exception=None):
    return render_error(request, 204)


def handler205(request, exception=None):
    return render_error(request, 205)


def handler206(request, exception=None):
    return render_error(request, 206)


def handler207(request, exception=None):
    return render_error(request, 207)


def handler208(request, exception=None):
    return render_error(request, 208)


def handler226(request, exception=None):
    return render_error(request, 226)


def handler300(request, exception=None):
    return render_error(request, 300)


def handler301(request, exception=None):
    return render_error(request, 301)


def handler302(request, exception=None):
    return render_error(request, 302)


def handler303(request, exception=None):
    return render_error(request, 303)


def handler304(request, exception=None):
    return render_error(request, 304)


def handler305(request, exception=None):
    return render_error(request, 305)


def handler307(request, exception=None):
    return render_error(request, 307)


def handler308(request, exception=None):
    return render_error(request, 308)


def handler400(request, exception=None):
    return render_error(request, 400, status=400)


def handler401(request, exception=None):
    return render_error(request, 401, status=401)


def handler402(request, exception=None):
    return render_error(request, 402, status=402)


def handler403(request, exception=None):
    return render_error(request, 403, status=403)


def handler404(request, exception=None):
    return render_error(request, 404, status=404)


def handler405(request, exception=None):
    return render_error(request, 405, status=405)


def handler406(request, exception=None):
    return render_error(request, 406, status=406)


def handler407(request, exception=None):
    return render_error(request, 407, status=407)


def handler408(request, exception=None):
    return render_error(request, 408, status=408)


def handler409(request, exception=None):
    return render_error(request, 409, status=409)


def handler410(request, exception=None):
    return render_error(request, 410, status=410)


def handler411(request, exception=None):
    return render_error(request, 411, status=411)


def handler412(request, exception=None):
    return render_error(request, 412, status=412)


def handler413(request, exception=None):
    return render_error(request, 413, status=413)


def handler414(request, exception=None):
    return render_error(request, 414, status=414)


def handler415(request, exception=None):
    return render_error(request, 415, status=415)


def handler416(request, exception=None):
    return render_error(request, 416, status=416)


def handler417(request, exception=None):
    return render_error(request, 417, status=417)


def handler418(request, exception=None):
    return render_error(request, 418, status=418)


def handler421(request, exception=None):
    return render_error(request, 421, status=421)


def handler422(request, exception=None):
    return render_error(request, 422, status=422)


def handler423(request, exception=None):
    return render_error(request, 423, status=423)


def handler424(request, exception=None):
    return render_error(request, 424, status=424)


def handler425(request, exception=None):
    return render_error(request, 425, status=425)


def handler426(request, exception=None):
    return render_error(request, 426, status=426)


def handler428(request, exception=None):
    return render_error(request, 428, status=428)


def handler429(request, exception=None):
    return render_error(request, 429, status=429)


def handler431(request, exception=None):
    return render_error(request, 431, status=431)


def handler451(request, exception=None):
    return render_error(request, 451, status=451)


def handler500(request):
    return render_error(request, 500, status=500)


def handler501(request, exception=None):
    return render_error(request, 501, status=501)


def handler502(request, exception=None):
    return render_error(request, 502, status=502)


def handler503(request, exception=None):
    return render_error(request, 503, status=503)


def handler504(request, exception=None):
    return render_error(request, 504, status=504)


def handler505(request, exception=None):
    return render_error(request, 505, status=505)


def handler506(request, exception=None):
    return render_error(request, 506, status=506)


def handler507(request, exception=None):
    return render_error(request, 507, status=507)


def handler508(request, exception=None):
    return render_error(request, 508, status=508)


def handler510(request, exception=None):
    return render_error(request, 510, status=510)


def handler511(request, exception=None):
    return render_error(request, 511, status=511)


def preview_error(request, code: int):
    status = code if 400 <= code <= 599 else None
    return render_error(request, code, status=status)

