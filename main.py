from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_volume(shape, params, precision):
    if shape == 'cube':
        side_length = float(params['side_length'])
        volume = side_length ** 3
    elif shape == 'sphere':
        radius = float(params['radius'])
        volume = (4/3) * 3.14159 * (radius ** 3)
    elif shape == 'cylinder':
        radius = float(params['radius'])
        height = float(params['height'])
        volume = 3.14159 * (radius ** 2) * height
    else:
        return None
    
    rounded_volume = round(volume, precision)
    return rounded_volume

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        shape = request.form['shape']
        params = request.form.to_dict()
        precision = int(request.form['precision'])
        
        volume = calculate_volume(shape, params, precision)
        
        if volume is None:
            return render_template('error.html')
        
        return render_template('result.html', volume=volume)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
