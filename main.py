from flask import Flask, render_template, redirect, request, make_response, session, abort, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data import db_session

from api.request_img_town import get_coordinates
from api.request_img_town import take_town_img
from data.users import User
from data.aparts import Apartments
from forms.user import RegisterForm
from forms.aparts import ApartsForm
from forms.user import LoginForm

import numpy as np
import pickle

from model import build_and_train

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

address, full_sq, number_rooms = str(), float(), float()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():  # запуск сервера и инициализация БД
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/", methods=['POST', 'GET'])
def index():  # обработчик главной страницы сайта
    global address, full_sq, number_rooms
    form = ApartsForm()
    if not current_user.is_authenticated:  # проверка на авторизацию пользователя
        return redirect('/please_login')
    if form.is_submitted():  # проверка на POST запрос об отправке данных пользователем
        address = form.address.data,
        full_sq = form.full_sq.data,
        number_rooms = form.number_rooms.data
        return redirect('/data_aparts')
    return render_template("index.html", title='Узнайте цену своей квартиры', form=form)


@app.route("/about")
def about():  # обработчик страницы о сервисе
    return render_template("about.html")


@app.route("/please_login")
def please_login():  # обработчик страницы требующей авторизации
    return render_template("please_login.html")


@app.route("/advantages")
def advantages():  # обработчик страницы с преимуществами сервиса
    return render_template("advantages.html")


@app.route("/data_aparts", methods=['GET', 'POST'])
def data_aparts():  # обработчик страницы с вводом данных о квартире
    form = ApartsForm()
    if not current_user.is_authenticated:  # проверка на авторизацию пользователя
        redirect('/please_login')
    if form.is_submitted():  # проверка на POST запрос об отправке данных пользователем
        db_sess = db_session.create_session()
        res = [i for i in request.form]
        apart = Apartments(
            address=address[0],
            number_rooms=number_rooms,
            full_sq=full_sq[0],
            life_sq=form.life_sq.data,
            floor=form.floor.data,
            max_floor=form.max_floor.data,
            material=1,
            build_year=form.build_year.data,
            kitch_sq=form.kitch_sq.data,
            state=form.state.data,
            area_m=form.area_m.data,
            raion_popul=form.raion_popul.data,
            green_zone_part=form.green_zone_part.data,
            indust_part=form.indust_part.data,
            school_education_centers_top_20_raion=form.school_education_centers_top_20_raion.data,
            healthcare_centers_raion=form.healthcare_centers_raion.data,
            university_top_20_raion=form.university_top_20_raion.data,
            sport_objects_raion=form.sport_objects_raion.data,
            additional_education_raion=form.additional_education_raion.data,
            culture_objects_top_25=int('culture_objects_top_25' in res),
            culture_objects_top_25_raion=form.culture_objects_top_25_raion.data,
            shopping_centers_raion=int('shopping_centers_raion' in res),
            thermal_power_plant_raion=int('thermal_power_plant_raion' in res),
            incineration_raion=int('incineration_raion' in res),
            oil_chemistry_raion=int('oil_chemistry_raion' in res),
            radiation_raion=int('radiation_raion' in res),
            railroad_terminal_raion=int('railroad_terminal_raion' in res),
            big_market_raion=int('big_market_raion' in res),
            nuclear_reactor_raion=int('nuclear_reactor_raion' in res),
            detention_facility_raion=int('detention_facility_raion' in res),
            full_all=form.full_all.data,
            ID_metro=form.ID_metro.data,
            metro_min_avto=form.metro_min_avto.data,
            green_zone_km=form.green_zone_km.data,
            industrial_km=form.industrial_km.data,
            water_treatment_km=form.water_treatment_km.data,
            cemetery_km=form.cemetery_km.data,
            railroad_station_avto_km=form.railroad_station_avto_km.data,
            ID_railroad_station_avto=form.ID_railroad_station_avto.data,
            water_km=form.water_km.data,
            water_1line=int('water_1line' in res),
            big_road1_km=form.big_road1_km.data,
            ID_big_road1=form.ID_big_road1.data,
            big_road1_1line=int('big_road1_1line' in res),
            big_road2_km=form.big_road2_km.data,
            ID_big_road2=form.ID_big_road2.data,
            railroad_1line=int('railroad_1line' in res),
            ID_bus_terminal=form.ID_bus_terminal.data,
            big_market_km=form.big_market_km.data,
            market_shop_km=form.market_shop_km.data,
            church_synagogue_km=form.church_synagogue_km.data,
            green_part_500=form.green_part_500.data,
            prom_part_500=form.prom_part_500.data,
            trc_count_500=form.trc_count_500.data,
            trc_sqm_500=form.trc_sqm_500.data,
            cafe_count_500_price_high=int('cafe_count_500_price_high' in res),
            mosque_count_500=form.mosque_count_500.data,
            leisure_count_500=form.leisure_count_500.data,
            sport_count_500=form.sport_count_500.data,
            market_count_500=form.market_count_500.data,
            cafe_count_1000_price_high=int('cafe_count_1000_price_high' in res),
            mosque_count_1000=form.mosque_count_1000.data,
            sport_count_1000=form.sport_count_1000.data,
            market_count_1000=form.market_count_1000.data,
            mosque_count_1500=form.mosque_count_1500.data,
            mosque_count_2000=form.mosque_count_2000.data,
            mosque_count_5000=form.mosque_count_5000.data,
            southern=int(request.form['raion'] == 'southern'),
            southeastern=int(request.form['raion'] == 'southeastern'),
            northwestern=int(request.form['raion'] == 'northwestern'),
            central=int(request.form['raion'] == 'central'),
            eastern=int(request.form['raion'] == 'eastern'),
            northern=int(request.form['raion'] == 'northern'),
            western=int(request.form['raion'] == 'western'),
            zelenograd=int(request.form['raion'] == 'zelenograd'),
            novomoskovskiy=int(request.form['raion'] == 'novomoskovskiy'),
            good=int(request.form['ecology'] == 'good'),
            excellent=int(request.form['ecology'] == 'excellent'),
            poor=int(request.form['ecology'] == 'poor'),
            satisfactory=int(request.form['ecology'] == 'satisfactory'),
        )
        data = [i for i in vars(apart).values()][3:]  # получаем список переданных данных
        data = np.asarray(data).reshape(1, -1)  # переводим в массив numpy
        print(data)
        current_user.apart.append(apart)  # добавляем для текущего пользователя данные о квартире
        db_sess.merge(current_user)
        db_sess.commit()

        clf = 'model_v1.pk'
        with open(clf, 'rb') as f:  # открытие обученной модели ML
            loaded_model = pickle.load(f)

            print("The model has been loaded...doing predictions now...")
            predictions = loaded_model.predict(data)  # передаем данные в модель и получаем предсказание цены

        # res = 1000
        # model = build_and_train()
        # res = model.predict(data.reshape(1, -1))
        # print(res)
        print(predictions)
        return redirect(f'/price/{predictions}')  # перенаправляем на страницу со стоимостью квартиры
    return render_template("data_aparts.html", form=form)


@app.route("/town", methods=['GET', 'POST'])
def town():  # обработчик страницы для изменения города пользователя
    form = ApartsForm()
    if form.is_submitted():  # проверка на POST запрос об отправке данных пользователем
        cords = get_coordinates(form.town.data)  # получаем координаты города
        take_town_img(cords)  # получаем изображение города на карте
        db_sess = db_session.create_session()
        # меняем город пользователя в базе данных
        db_sess.query(User).filter(User.id == current_user.id).first().town = form.town.data
        db_sess.commit()
    return render_template("town.html", form=form)

#
# @app.route("/later_prices")
# def later_prices():
#     db_sess = db_session.create_session()
#     aparts = db_sess.query(Apartments).filter(Apartments.is_private != True)
#     return render_template("later_prices.html", aparts=aparts)


@app.route('/register', methods=['GET', 'POST'])
def reqister():  # обработчик формы регистрации
    form = RegisterForm()
    if form.validate_on_submit():  # проверка на POST запрос об отправке данных пользователем
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            town=form.town.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)  # добавление нового пользователя в базу данных
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():  # обработчик формы входа в аккаунт
    form = LoginForm()
    if form.validate_on_submit():  # проверка на POST запрос об отправке данных пользователем
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():  # обработчик для выхода из аккаунта
    logout_user()
    return redirect("/")


@app.route('/price/<price>')
@login_required
def get_price(price):  # обработчик страницы выводящей финальную оценку квартиры
    return render_template('price.html', price=price)


if __name__ == '__main__':
    main()
