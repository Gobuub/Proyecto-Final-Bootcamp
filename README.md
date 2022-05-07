# Proyecto-Final-Bootcamp
Proyecto final presentado al final del bootcamp

Estructura de carpetas.

  - En la carpeta ETL:
    - Notebook utilizado para realizar el web scrapping y obtener los datos necesarios para el proyecto.   
  - En la carpeta EDA:
    - Notebook utilizado para generar los dataframes con los que realizar Análisis Exploratorio de los datos, y poder obtener información relevante de los mismos. 
    - Enlace al Dashboard de Tableau
      - (https://public.tableau.com/app/profile/enrique.revuelta.garc.a/viz/Comunio_statsJ18-19/Historia1)
  - En la carpeta ML:
    - Notebook utilizado para crear y entrenar los modelos de ML con los que realizar las predicciones sobre nuestros datos.   
  - En la carpeta img:
    - Imagenes generadas con nuestros datos utilizadas para la ppt. 
  - En la carpeta data
    - Data warehouse con todos los archivos obtenidos con el notebook de web scrapping 

![Image text](https://github.com/Gobuub/Proyecto-Final-Bootcamp/blob/main/img/graph.png)

### Entornos virtuales

  Para asegurar el correcto funcionamiento del proyecto será necesario crear un entorno virtual y ejecutarlo desde el mismo.
  Tanto el Proyecto de Ml como la App de Django tienen su entorno virtual propìo por lo que habrár que crear ambos entornos virtuales por separado, encontrareis el requisitos.txt en cada una de sus carpetas correspodientes
  
   1. Crear un entorno virtual:
      - conda env create -f comunio_ml.yml
   2. Activar entorno virtual:
      - source activate comunio_ml 
   3. Desactivar entorno virtual:
      - conda deactivate
      
    
