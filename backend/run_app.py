from app import app

if __name__ == '__main__':
    if app.config['ENV'] == 'development':
        app.run(host='0.0.0.0', port=23931, threaded=False)
    else:
        pass
