# Web Scraping - Data Extraction on the Web

This repository contains the notes and projects of the web scrapping course

## Notes

### Clase 1: Introducción y definiciones

#### Notas

- **Web scrapping:** Es el proceso de extración de datos almacenados en la web.
**Objetivo:** Recopilar información almacenada en un servidor web
- Web Crawling: Es el proceso de mapeo e indexación de páginas web para conocer su contenido
**Objetivo:** Conocer la estructura de la web

 
### Clase 2: Ética y Legalidad

#### Notas

- ¿Scrapear un sitio es legal?

    Depende:

    - ¿Estoy violando alguna reglamentación local?
    - ¿Estoy violando los terminos y condiciones?
    - ¿Estoy accediendo a lugares no autorizado?
    - ¿Es legal el uso que le voy a dar a los datos?
- **Robots.txt:** Es un archivo que define buenas practicas de scrapping con ese sitio web.
    - Dentro del robot se suele definir el **Crawl-delay:** es el tiempo (en segundos) entre peticiones al sitio web


### Clase 11: Instalación y configuración de Selenium

#### **Para Recordar:**

- Selenium necesita un driver para poder generar una interfaz con el navegador. Dependiendo el navegador que se use, se deberá  driver distinto
- importante que el archivo descargado esté en una carpeta accesible desde la Jupyter Notebook, ya que necesitaremos referenciarlo desde el código para poder utilizarlo

#### Notas

- Drivers:
    - Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - Edge: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
    - Firefox: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
    - Safari: [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)


### Clase 13: Selección de elementos

#### Notas

- Cómo armar el xpath:

    [http://labs.timtom.ch/library-webscraping/extras/xpath-cheatsheet.md.pdf](http://labs.timtom.ch/library-webscraping/extras/xpath-cheatsheet.md.pdf)

### Clase 19: Comentarios finales

#### **Para Recordar**

No usar Selenium en la medida de lo posible, mejor usar Request y  Beatifulsuop. O en su defecto APis.

Usar selenium cuando no haya otra alternativa

### Clase 26: Scrapy

#### Notas

- Scrapy es un framework para realizar scrapping. Este framework permite manejar las request de forma asincronica.
- Scrapy también permite usar XPATH
- Puede limitar la cantidad de request en paralelo que se puede realizar.
- Setear demoras entre request
- Limitar los dominios.

 
### Clase 28: Proxies

#### Notas

- El proxy se encarga de hacer de intermediario entre el Scrapper y la página web.
- Por lo tanto el servidor web verá la IP del proxy y no del Scrapper

 

### Examen

[Examen del Curso de Web Scraping Extracción de Datos.pdf](resources/Examen_del_Curso_de_Web_Scraping_Extraccin_de_Datos.pdf)