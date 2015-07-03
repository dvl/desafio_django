## Instalação

    $ git clonne https://github.com/dvl/python_test.git
    $ cd python_test/
    $ pip install -r requirements.txt
    $ python manage.py migrate
    
Então inicie o servidor:

    $ python manage.py runserver
    
E acesse via [http://localhost:8000/](http://localhost:8000/)

## Notas

Para processar as imagens dos thumbnails esse projeto depende do `django-imagekit` que por sua vez depende do `Pillow` caso tenha problemas com essas dependencias pode ser necessário instalar alguns pacotes no sistema operacional:

    # apt-get install -y python-dev libfreetype6-dev libjpeg-dev zlib1g-dev
    
Então depois tente instalar o `Pillow` novamente

    $ pip install -I pillow
