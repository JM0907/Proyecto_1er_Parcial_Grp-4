from flask import Flask, render_template 
import requests 
from dotenv import load_dotenv, dotenv_values

load_dotenv('.env')
config = dotenv_values ('.env')


app = Flask (__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={API_KEY}'

    r = requests.get(url).json()
    print (r)
    return r


@app.route('/clima')
def clima():
    clima=get_weather_data('Madrid')
    temperatura=str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono=str(clima['weather'][0]['icon'])
    r_json={
        'ciudad': 'Madrid',
        'temperatura':temperatura,
        'descripcion': descripcion,
        'icono': icono
        }
    return render_template('weather.html', clima = r_json)




@app.route('/about1')
def about1():
    return render_template('CurriculumGoyaG.html')

@app.route('/about2')
def about2():
    return render_template('CurriculumLucas.html')

@app.route('/about3')
def about3():
    return render_template('CurriculumLuna.html')

@app.route('/about4')
def about4():
    return render_template('CurriculumMurillo.html')

@app.route('/about5')
def about5():
    return render_template('CurriculumPaez.html')

@app.route('/about6')
def about6():
    return render_template('CurriculumQuizphi.html')

@app.route('/about7')
def about7():
    return render_template('CurriculumVillacis.html')


if __name__ == '__main__':
    app.run(debug = True)


@app.route('/clima')
def clima_page():
    return render_template('weather.html')

@app.route('/clima')
def clima():
    return 'CLIMA'


if __name__ == '__main__':
    app.run(debug = True)