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
        form_data.append({'entry.761092801': name})

    return form_data



url = 'https://docs.google.com/forms/d/e/1FAIpQLSeCBLRqtX9haB5hL5UQqaM2cWavicoaMu3WSL6fFVO6t4t7Vw/formResponse'
user_agent = {
    'Referer': url,
    'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
}

form_data = get_data_list()
send_data(url, form_data, user_agent)

