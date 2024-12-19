from flask import Flask, request, jsonify

app = Flask(__name__)

# Путь к файлу для сохранения данных
CLIPBOARD_FILE = 'clipboard.txt'

@app.route('/api/clipboard', methods=['POST'])
def save_clipboard_data():
    data = request.json
    clipboard_data = data.get('clipboardData', '')

    # Сохраняем данные в файл
    with open(CLIPBOARD_FILE, 'a', encoding='utf-8') as f:
        f.write(clipboard_data + '\n')

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
