# Youtube video downloader

Este programa permite descargar vídeos de Youtube, escoger su calidad y descargar únivamente audio o audio y vídeo. Está desarrollado en Python3 y cuenta con una interfaz gráfica creada con Tkinter. Para usarlo requiere lo siguiente: 

- FFMpeg: Es una herramienta que se utiliza des de el terminal para tratar ficheros de audio y vídeo. Es completamente gratuito.

   [Descargar FFMpeg](https://ffmpeg.org/download.html).

   En Windows se debe añadir el directorio **bin** al **PATH**.
   
- pytube: Una librería de python que nos permitirá descargar los vídeos y su respectiva información. 

    >pip install pytube3   ----- Para usuarios de Windows
    
    >pip3 install pytube3  ----- Para usuarios de Linux/iOS


### Fichero downloader.py

En este fichero está la clase Downloader. Esta clase consta del metodo dowload, que a través de un link permite descargar el vídeo. 
El constructor de la clase Dowloader únicamente necesita un path dónde creará una carpeta llamada descargas y guardará allí los 
ficheros descargados. El método download requiere el link del vídeo, un booleano que controla si es audio o vídeo+aduio y finalmente
como parámetro opcional la calidad del vídeo. 

#### Descargar ficheros de audio

En este caso únicamente de descarga un stream de audio y se guarda en la carpeta deseada. 


#### Descargar ficheros de audio y vídeo

En este caso se descarga un fichero de audio, otro de vídeo (sin audio) y se usa FFMpeg mediante un subproceso de Python para sincronizar ambos streams en un único fichero. Una vez se ha generado el fichero con audio y vídeo se eliminan los otros dos ficheros iniciales. 

### Fichero app.py

Aquí encontramos la clase de la interfaz gráfica. Como se puede apreciar es muy sencilla, consta únicamente de un campo para introducir el link, una lista de calidades para escoger y el tipo de medios que se quieren. Tiene un botón para descargar una vez se han rellenado los campos anteriores y otro para abrir el fichero con el reproductor por defecto del equipo. 
