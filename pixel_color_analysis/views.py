import os
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import re
from PIL import Image


def main_download_page(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            hex_code = str(dict(request.POST.items())['hex_code'])
            result = analysis(str(request.FILES['img']), hex_code)
            return render(request, 'pixel_color_analysis/success.html', {'result': result})
    else:
        form = ImgForm()
    return render(request, 'pixel_color_analysis/index.html', {'form': form})


def analysis(image_name, hex_code):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'media\\{image_name}')
    print(path)
    print(os.getcwd())
    image = Image.open(path)

    rgb = tuple()
    num_pixels_hex = 0

    if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
        rgb = tuple(int(hex_code.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        print(rgb)
    else:
        print('Hex is not valid')

    black = 0
    white = 0

    for pixel in image.getdata():
        if pixel == rgb:
            num_pixels_hex += 1
        if pixel == (0, 0, 0):
            black += 1
        elif pixel == (255, 255, 255):
            white += 1

    if black > white:
        comparison = 'На картинке больше черных пикселей.'
    elif white > black:
        comparison = 'На картинке больше белых пикселей.'
    else:
        comparison = 'Количество белых и черных пикселей на картинке равно.'

    print('black=' + str(black) + '\n white=' + str(white))
    result = Analysis(comparison=f'{comparison}', num_pixels_hex=f'{num_pixels_hex}')
    result.save()
    return result
