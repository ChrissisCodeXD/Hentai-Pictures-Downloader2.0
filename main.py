from __future__ import unicode_literals

import random

from pybooru import Danbooru
from random import randint
import urllib.request
from colorama import Fore,Back
from tqdm import tqdm
import webbrowser
import requests
image_urls = []
x = []  # link storage
broken_images = []
import shutil
import os
def download(tags,limit,pages):
    try:
        client = Danbooru('danbooru', username='Anime-Bot', api_key='JWLVmzT4JMdchfNTtSDx7Y8h')

        # Collect links
        while True:  # Checks if the list is full
            randompage = randint(1, pages)
            posts = client.post_list(tags=tags, page=randompage, limit=limit)
            for post in posts:

                try:
                    fileurl = post['file_url']
                except:
                    fileurl = 'https://danbooru.donmai.us' + post['source']
                x.append(fileurl)


            if len(x) >=1:
                a=0
                print(f"{Fore.GREEN}Got image/images{Fore.RESET}")
                print(x)
                g = input('do you want to open in webbrowser or download in directory?\nPress d for download and w for web!')
                if g.lower() == 'w':
                    e = int(input(f'How many pictures do you want to open? Max: {len(x)}'))
                    for f in x:
                        a+=1
                        webbrowser.open(f, new=2)
                        if a >= e:
                            break
                elif g.lower() == 'd':
                    response_number =0
                    new_folder = f'{itput}.{random.randint(10,100000)}'
                    os.makedirs(new_folder)
                    for f in x:
                        image_urls.append(f)
                    for f in tqdm(image_urls):
                        try:
                            response=requests.get(f)
                            response_number +=1
                            with open(f'{new_folder}/{response_number}.jpg',"wb")as o:
                                o.write(response.content)
                            print(f'{Fore.RED} Your Pictures are saved in the same folder as the programm! The Folder with the Pictures is named: {new_folder}')
                        except Exception as k:
                            print(k)
                break
            if len(x) == 0:
                print(f"{Fore.RED}failed to get a image trying again...{Fore.RESET}")



        # Download images
        for url in x:
            try:
                randomint = randint(1000, 10000000)
                urllib.request.urlretrieve(url, "tmp/danbooru_/{0}.jpg".format(randomint))
            except:
                continue
    except Exception as e:
        raise e


def main(itput,nput):
    print('input:')
    print(f'? {itput.lower()}')
    # pages: 2000 Gold account limit. Basic Users should have 1000
    download(tags=f'? {itput.lower()}',limit=nput, pages=1000)
print("""Recommended Tags:
1 girl
solo 
long_hair 
highres 
breasts 
thighhighs
photoshop_(medium)""")
print(f'{Fore.MAGENTA}put your tag here:\n{Fore.RESET}')
itput = input()
print(f'{Fore.RED}how many pictures do you want max?:\n{Fore.RESET}')
nput = int(input())
main(itput,nput)