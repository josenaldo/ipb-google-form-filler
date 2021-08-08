import requests
import time
from lista import namelist

def send_data(url, data, user_agent):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            r = requests.post(url, data=d, headers=user_agent),
            print(f'valor enviado: {d}')
            time.sleep(1)
        except:
            print("Error Occured! in: " + d)


def get_data_list():
    form_data = []

    for name in namelist:
        form_data.append({'entry.1336091824': name})

    return form_data



url = 'https://docs.google.com/forms/d/e/1FAIpQLSdHR39eJE_MT116F7jBRoaXfuteDtq14FjJxkcMxOW9uh42mQ/formResponse'
user_agent = {
    'Referer': url,
    'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
}

form_data = get_data_list()
send_data(url, form_data, user_agent)

