# Телеграм бот для агрегации статистических данных

[Тестовое задание](https://docs.google.com/document/d/14DcCb6Pj3PNsFqJzaS_hAhyePqRXF6uvmTzobp_G8PM/edit)

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание](#описание)
- [Установка приложения](#установка-приложения)
- [Запуск приложения](#запуск-приложения)
- [Автор](#автор)

<br>

## Технологии

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=asyncio)](https://docs.python.org/3/library/asyncio.html)
[![aiogram](https://img.shields.io/badge/-aiogram-464646?logo=aiogram)](https://docs.aiogram.dev/en/latest/)


[⬆️Оглавление](#оглавление)

<br>

## Описание

Реализована задача агрегации статистических данных о зарплатах сотрудников компании по 
временным промежуткам. 

Исходные статические данные по которым производиться агрегация:
```bash
src/sampleDB/sample_collection.bson
```

Телеграм бот на вход принимает запрос, который должен иметь следующий вид:
```bash
{
"dt_from":"2022-09-01T00:00:00",
"dt_upto":"2022-12-31T23:59:00",
"group_type":"month"
}
```
* dt_from - дата и время старта агрегации
* dt_upto - дата и время окончания агрегации
* group_type - тип агрегации. Типы агрегации могут быть следующие: hour, day, month. То есть группировка всех данных за час, день, месяц.

Ответным сообщением бот отдает агрегированные данные.

[⬆️Оглавление](#оглавление)

<br>

## Установка приложения:

Клонируйте репозиторий с GitHub:

```bash
git https://github.com/Shone-Kristas/ADBT_bot.git
```
Перейдите в папку проекта.
Выполните установку зависимостей командой:

```bash
pip install -r requirements.txt
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:

Из корневой директории проекта "src" выполните команду:

```bash
python bot_logic.py
```
В телеграме найдите бота с названием:

```bash
@aggregation_data_bot
```

[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Nickolay](https://github.com/Shone-Kristas)

[⬆️В начало](#Телеграм-бот-для-агрегации-статистических-данных)
