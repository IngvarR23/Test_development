import requests


def create_folder(token, path):
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': path}
    res = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
    return res.status_code