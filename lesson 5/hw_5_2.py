from threading import Thread
import requests

def run_in_thread(func):

    def wrapper(*args):
        thread = Thread(target=func, args=args)
        thread.start()
        #print (thread)
        #result = func(*args)
        #return result

    return wrapper

@run_in_thread
def file_download(url):
    print (f'Downloading file from: {url}')
    file_name = url.split('/')[-1]
    r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    print (f'File was downloaded with the name: {file_name}')


url_list = ['http://ivantaxi.com.ua/wp-content/uploads/2019/10/car-big.png',
            'https://www.alpinabook.ru/upload/resize_cache/iblock/663/700_700_1/663f4c67619485c224c5b149b1f65eab.jpg',
            'https://tvoidrug.com/wp-content/uploads/2016/11/foto_49_1_600.png',
            'https://image.cnbcfm.com/api/v1/image/105992231-1561667465295gettyimages-521697453.jpeg',
            'https://i.dailymail.co.uk/1s/2019/11/18/16/21162158-0-image-a-38_1574094224893.jpg',
            'https://static.standard.co.uk/s3fs-public/thumbnails/image/2019/03/15/17/pixel-dogsofinstagram-3-15-19.jpg',
            'https://thumbs-prod.si-cdn.com/Q70MTW0QP4g7kpVoyG3xQn57tQI=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/ad/7b/ad7b3860-ad5f-43dc-800e-af57830cd1d3/labrador.jpg',
            'https://cdn.britannica.com/s:700x500/42/8142-004-4CD3860D/Boxer.jpg',
            'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/20113314/Carolina-Dog-standing-outdoors.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Akita_Inu_dog.jpg/1920px-Akita_Inu_dog.jpg'
            ]

for url in url_list : file_download(url)
