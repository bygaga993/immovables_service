from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired


class ApartsForm(FlaskForm):  # класс wtf форм для полей ввода данных о квартире
    address = StringField('Адрес', validators=[DataRequired()])
    number = IntegerField('Номер квартиры', validators=[DataRequired()])
    town = StringField('Введите город:', validators=[DataRequired()])
    number_rooms = IntegerField('Количество комнат', validators=[DataRequired()], default=1)
    submit = SubmitField('Подтвердить')

    full_sq = FloatField('Общая площадь(м2)',
                         validators=[DataRequired()])
    life_sq = FloatField('Жилая площадь в квадратных метрах, без учета лоджий, балконов и других нежилых помещений',
                         validators=[DataRequired()])
    floor = FloatField('Этаж', validators=[DataRequired()])
    max_floor = FloatField('Максимальный этаж в доме', validators=[DataRequired()])
    material = StringField('Материал стены', validators=[DataRequired()])
    build_year = FloatField('Год постройки здания', validators=[DataRequired()])
    kitch_sq = FloatField('Площадь кухни', validators=[DataRequired()])
    state = FloatField('Состояние квартиры(от 0 до 5)', validators=[DataRequired()])
    area_m = FloatField('Площадь территории муниципального района', validators=[DataRequired()])
    raion_popul = FloatField('Численное население муниципального округа', validators=[DataRequired()])
    green_zone_part = FloatField('Доля площади зелени в общей площади', validators=[DataRequired()])
    indust_part = FloatField('Доля промышленных зон по площади от общей площади', validators=[DataRequired()])

    school_education_centers_top_20_raion = FloatField('Количество школ из топ-20 лучших школ Москвы',
                                                       validators=[DataRequired()])
    healthcare_centers_raion = FloatField('Количество медицинских учреждений в районе', validators=[DataRequired()])
    university_top_20_raion = FloatField('Количество высших учебных заведений в первой десятке рейтинга федерального '
                                         'рейтинга', validators=[DataRequired()])
    sport_objects_raion = FloatField('Количество спорт объектов', validators=[DataRequired()])
    additional_education_raion = FloatField('Количество организаций дополнительного образования',
                                            validators=[DataRequired()])
    culture_objects_top_25_raion = FloatField('Количество объектов культурного наследия', validators=[DataRequired()])

    full_all = FloatField('Общая численность населения муниципалитета', validators=[DataRequired()])
    build_count_brick = FloatField('Доля кирпичных зданий', validators=[DataRequired()])
    ID_metro = FloatField('Идентификатор метро', validators=[DataRequired()])
    metro_min_avto = FloatField('Время до метро на машине, мин.', validators=[DataRequired()])
    green_zone_km = FloatField('Расстояние до зеленой зоны', validators=[DataRequired()])
    industrial_km = FloatField('Расстояние до промзоны', validators=[DataRequired()])
    water_treatment_km = FloatField('Расстояние до водоочистных сооружений', validators=[DataRequired()])
    cemetery_km = FloatField('Расстояние до кладбища', validators=[DataRequired()])
    railroad_station_avto_km = FloatField('Расстояние до железнодорожного вокзала (авто)', validators=[DataRequired()])
    ID_railroad_station_avto = FloatField('Идентификатор ближайшей железнодорожной станции (авто)',
                                          validators=[DataRequired()])
    water_km = FloatField('Расстояние до водоема/реки', validators=[DataRequired()])
    mkad_km = FloatField('Расстояние до МКАД', validators=[DataRequired()])
    big_road1_km = FloatField('Расстояние до ближайшей главной дороги', validators=[DataRequired()])
    ID_big_road1 = FloatField('Индентификатор ближайшей главной дороги', validators=[DataRequired()])
    big_road2_km = FloatField('Расстояние до следующей отдаленной главной дороги', validators=[DataRequired()])
    ID_big_road2 = FloatField('Идентификатор второй ближайшей большой дороги', validators=[DataRequired()])
    ID_bus_terminal = FloatField('Идентификатор ближайшего автовокзала', validators=[DataRequired()])
    nuclear_reactor_km = FloatField('Расстояние до ядерного реактора', validators=[DataRequired()])
    big_market_km = FloatField('Расстояние до продуктовых/оптовых рынков', validators=[DataRequired()])
    market_shop_km = FloatField('Расстояние до рынков и универмагов', validators=[DataRequired()])
    fitness_km = FloatField('Расстояние до фитнес-центра', validators=[DataRequired()])
    ice_rink_km = FloatField('Расстояние до ледового дворца', validators=[DataRequired()])
    church_synagogue_km = FloatField('Расстояние до христианских церквей и синагог', validators=[DataRequired()])
    catering_km = FloatField('Расстояние до общепита', validators=[DataRequired()])

    green_part_500 = FloatField('Доля зеленых зон в 500-метровой зоне', validators=[DataRequired()])
    prom_part_500 = FloatField('Доля промзон в 500-метровой зоне', validators=[DataRequired()])
    office_count_500 = FloatField('Количество офисных помещений в 500-метровой зоне', validators=[DataRequired()])
    trc_count_500 = FloatField('Количество торговых центров в 500-метровой зоне', validators=[DataRequired()])
    trc_sqm_500 = FloatField('Площадь торговых центров в 500-метровой зоне', validators=[DataRequired()])
    cafe_count_500_price_high = FloatField('Счет в кафе и ресторанах, в среднем более 4000 в зоне 500 метров',
                                             validators=[DataRequired()])
    mosque_count_500 = FloatField('Количество мечетей в 500-метровой зоне', validators=[DataRequired()])
    leisure_count_500 = FloatField('Количество мест отдыха в 500-метровой зоне', validators=[DataRequired()])
    sport_count_500 = FloatField('Количество спортивных сооружений в 500-метровой зоне', validators=[DataRequired()])
    market_count_500 = FloatField('Количество рынков в 500-метровой зоне', validators=[DataRequired()])
    cafe_count_1000_price_high = BooleanField('Счет в кафе и ресторанах, в среднем более 4000 в зоне 1000 метров',
                                              validators=[DataRequired()])
    mosque_count_1000 = FloatField('Количество мечетей в 1000-метровой зоне', validators=[DataRequired()])
    sport_count_1000 = FloatField('Количество спортивных сооружений в 1000-метровой зоне',
                                    validators=[DataRequired()])
    market_count_1000 = FloatField('Количество рынков в 1000-метровой зоне', validators=[DataRequired()])
    mosque_count_1500 = FloatField('Количество мечетей в 1500-метровой зоне', validators=[DataRequired()])
    mosque_count_2000 = FloatField('Количество мечетей в 2000-метровой зоне', validators=[DataRequired()])
    trc_sqm_3000 = FloatField('Количество торговых центров в 3000-метровой зоне', validators=[DataRequired()])
    market_count_3000 = FloatField('Количество рынков в 3000-метровой зоне', validators=[DataRequired()])
    mosque_count_5000 = FloatField('Количество мечетей в 5000-метровой зоне', validators=[DataRequired()])

