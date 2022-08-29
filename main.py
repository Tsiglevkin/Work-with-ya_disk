import requests
from pprint import pprint


class YandexDisk:
    def __init__(self, token):  # функция инициализации класса. При создании каждого объекта требуется его токен.
        self.token = token

    def get_headers(self):
        """This function makes headers"""
        headers = {'Content_Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        # Заголовки нужны для авторизации
        return headers

    def get_files_list(self):
        """This function can take files in Json format"""
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'  # эта ссылка из двух частей
        # первую берем на полигоне, вторую в документации.
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)  # запрос при помощи метода GET(ссылка, заголовки)
        return response.json()  # возвращаем список файлов в формате JSON.

    def _get_upload_link(self, yadisk_file_path):
        """This function can get upload link from Yandex Disk"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        parameters = {'path': yadisk_file_path, 'overwrite': 'True'}  # параметры запроса для определения пути файла и
        # и его перезаписи в случае, если он там уже есть. Параметры берутся из документации API.
        response = requests.get(upload_url, headers=headers, params=parameters)  # запрос с заголовками для авторизации
        # и параметрами.
        return response.json()  # возврат ссылки в виде словаря JSON.

    def upload_file_to_disc(self, yadisk_file_path, filename):
        """This function can upload chosen file to yandex disk"""
        upload_link = self._get_upload_link(yadisk_file_path=yadisk_file_path)  # получаем ссылку в виде json
        href = upload_link.get('href', 'такого ключа нет.')  # получаем обяз. параметр href для метода put, что ниже)
        response = requests.put(href, data=open(filename, 'rb'))  # делаем запрос, указываем href и переменную/откр.
        # файл в режиме чтения в байтовом виде (позволит отправить любой вид данных).


if __name__ == '__main__':
    user_token = ''  # введите токен
    file_path = ''  # введите путь файла на Я.Диске.
    file_name = ''  # введите имя файла.
    some_user = YandexDisk(token=user_token)

    some_user.upload_file_to_disc(file_path, file_name)

