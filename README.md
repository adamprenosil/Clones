# Clausura con M

Algoritmos para generar los clones por encima de un álgebra que tenga un término mayoritario.

## Uso

### Instalación

Descargar el repositorio y entrar a la carpeta del repositorio

```bash
git clone https://github.com/gonzigaran/clausura-M.git
cd clausura-M/
```

Crear un entorno virtual y activarlo

```bash
virtualenv env
source env/bin/activate
```

Instalar los paquetes con pip

```bash
pip install -r requirements.txt
```

Ya se puede usar el programa

### Modo de uso

Siempre antes de ejecutar, ubicarse en el directorio y activar el entorno

```bash
cd clausura-M/
source env/bin/activate
```

El programa calcula los coclones a partir de un aĺgebra que sepamos que tiene un término mayoritario, para eso primero tenemos que generar el álgebra y guardarla como `.model`.

En [algebra_generator_example.py](https://github.com/gonzigaran/clausura-M/blob/main/algebra_generator_example.py) hay un ejemplo de cómo generar y almacenar un  álgebra, aprovechando los decoradores para no poner toda la tabla de una función. Para ejecutar este ejemplo:

```bash
python algebra_generator_example.py
```

Esto nos genera el archivo `Models/exampleAlgebra.model` que tiene el universo en la primer linea y luego la tabla de cada función.

Ahora ya se puede ejecutar el programa 