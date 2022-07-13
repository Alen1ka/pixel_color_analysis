__WEB-сервис на Python, у которого есть HTML страничка с возможностью загрузить картинку.__ Сервис умеет сообщать каких пикселей больше на картинке, белых или чёрных и по HEX коду цвета считает количество пикселей этого цвета на картинке.

__Инструкции по загрузке:__
* Переходим в командной строке в папку pixel_color_analysis-master, где находится файл manage.py
* Выполняем следующие команды
  * python manage.py migrate --run-syncdb
  * python manage.py makemigrations
  * python manage.py migrate
  * python manage.py runserver
