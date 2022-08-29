import requests
from pprint import pprint


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {'Content_Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        return headers

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

# doesn't work...
    # def create_folder(self, folder_name):
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    #     headers = self.get_headers()
    #     response = requests.put(files_url, headers)

    def _get_upload_link(self, yadisk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        parameters = {'path': yadisk_file_path, 'overwrite': 'True'}
        response = requests.get(upload_url, headers=headers, params=parameters)
        return response.json()

    def upload_file_to_disc(self, yadisk_file_path, filename):
        link = self._get_upload_link(yadisk_file_path=yadisk_file_path)
        href = link.get('href', 'такого ключа нет.')
        response = requests.put(href, data=open(filename, 'rb'))


if __name__ == '__main__':
    user_token = 'y0_AgAAAAAi9YUBAADLWwAAAADNap95MEOmc-NPRHOrYTmWkBM8vOJbNSI'
    file_path = 'Folder for Task/IMG_20170904_174826.jpg'
    stepan = YandexDisk(token=user_token)

    stepan.upload_file_to_disc(file_path, 'IMG_20170904_174826.jpg')


