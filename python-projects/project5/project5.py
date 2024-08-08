# Zach McLean
# CSCI 3038
# Tkinter and URLlib

import tkinter as tk
from tkinter import scrolledtext
from urllib.request import urlopen, urljoin
from urllib.parse import urlparse
import os

def get_images(url):
    try:
        response = urlopen(url)
        html = response.read().decode('utf-8')
        images = []
        i = 0
        while True:
            start = html.find('src="', i)
            if start == -1:
                break
            end = html.find('"', start + 5)
            if end == -1:
                break
            img_url = html[start + 5:end]
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            if img_url.endswith('.jpg') or img_url.endswith('.jpeg') or img_url.endswith('.png'):
                images.append(img_url)
            i = end + 1
        return images
    except Exception as e:
        return [str(e)]

def download_images(images):
    for img_url in images:
        try:
            response = urlopen(img_url)
            img_data = response.read()
            filename = os.path.basename(urlparse(img_url).path)
            with open(filename, 'wb') as f:
                f.write(img_data)
        except Exception as e:
            print(f"Error downloading {img_url}: {str(e)}")

def get_and_display_images():
    url = url_entry.get()
    images = get_images(url)
    text_box.delete(1.0, tk.END)
    for img_url in images:
        text_box.insert(tk.END, img_url + '\n')

def download_all_images():
    url = url_entry.get()
    images = get_images(url)
    download_images(images)

root = tk.Tk()
root.title("Image Downloader")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

get_images_button = tk.Button(root, text="Get Images", command=get_and_display_images)
get_images_button.pack()

download_all_button = tk.Button(root, text="Download All Images", command=download_all_images)
download_all_button.pack()

text_box = scrolledtext.ScrolledText(root, width=50, height=10)
text_box.pack()

root.mainloop()
