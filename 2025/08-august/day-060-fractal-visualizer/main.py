from flask import Flask, render_template, send_file
from fractal import get_mandelbrot_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fractal.png')
def fractal_image():
    # You can customize the parameters here if you want
    # For example: /fractal.png?width=1024&height=768
    width = 800
    height = 600
    max_iter = 256

    img_buf = get_mandelbrot_image(width, height, max_iter)

    return send_file(img_buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
