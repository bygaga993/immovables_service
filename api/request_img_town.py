import requests


def get_coordinates(address):
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    response = requests.get(url)
    data = response.json()
    coordinates_str = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    coordinates = [float(coord) for coord in coordinates_str.split()]
    return coordinates


def take_town_img(coordinates):
    map_request = (f"https://static-maps.yandex.ru/1.x/?&ll={coordinates[0]},{coordinates[1]}&"
                   f"z=12&pt={coordinates[0]},{coordinates[1]},home&l=map")
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")

    map_file = "town.jpg"
    with open(f"static/img/{map_file}", "wb") as file:
        file.write(response.content)


