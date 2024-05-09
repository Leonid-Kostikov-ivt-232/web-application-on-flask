from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_volume(shape, params, precision):
    if shape == 'cube':
        try:
            side_length = float(params['side_length'])
        except ValueError:
            return "Ошибка вычисления. Введите длину стороны куба!"
        if side_length < 0:
            return "Ошибка вычисления. Длина стороны не может быть отрицательным!"
        volume = side_length ** 3
    elif shape == 'sphere':
        try:
            radius = float(params['radius'])
        except ValueError:
            return "Ошибка вычисления. Введите радиус сферы!"
        if radius < 0:
            return "Ошибка вычисления. Радиус не может быть отрицательным!"
        volume = (4/3) * 3.14159 * (radius ** 3)
    elif shape == 'cylinder':
        try:
            radius = float(params['radius_с'])
            height = float(params['height'])
        except ValueError:
            return "Ошибка вычисления. Введите значения радиуса и высоты цилиндра!"
        if radius < 0:
            return "Ошибка вычисления. Радиус и высота не могут быть отрицательными!"
        if height < 0:
            return "Ошибка вычисления. Радиус и высота не могут быть отрицательными!"
        volume = 3.14159 * (radius ** 2) * height
    else:
        return None

    rounded_volume = round(volume, precision)
    return rounded_volume

def error_precision(precision):
    error = 0
    if precision < 0:
        error += 1
    return error

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        shape = request.form['shape']
        params = request.form.to_dict()
        try:
            precision = int(request.form['precision'])
        except ValueError:
            precision = 1

        if precision < 0:
            error = error_precision(precision)
            return render_template('error.html')
        
        volume = calculate_volume(shape, params, precision)
        
        if volume is None:
            return render_template('error.html')
        
        return render_template('result.html', volume=volume)
    
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)


