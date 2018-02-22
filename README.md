# FalconTest
Repositorio creado con la finalidad de hacer pruebas basicas de python con virtualenv y el framework falcon
#### Instalar virtualenv
De acuerdo nuestra instalacion de python (general/o por usuario) es necesario o no el uso de "**sudo**"
```
[sudo] pip install virtualenv
```
Comprobamos la version de nuestro virtualenv y con ello que este instalado correctamente
```
virtualenv --version
```
#### Clonar el repositorio
```
git clone https://github.com/josu3e/falconTest.git
cd falconTest/
```
#### Crear ambiente virtual
En este caso "**env**" va ser el nombre que le vamos asignar a nuestro contenedor de librerias
```
virtualenv env
```
Si deseamos indicar la version de python agregamos **`-p python3`**
```
virtualenv -p python3 env
```
Con el siguiente comando iniciamos nuestro contenedor. Con el nombre mencionado **env** que escogimos	
```
source env/bin/activate
```
Observamos que nuestra linea comando cambia indicanos con "**(env)**" que estamos en el entorno virtual. Si necesitamos detenerlo utilisamos "**deactivate**"
```
➜  falconTest git:(master) 
(env) ➜  falconTest git:(master) deactivate
```
#### Instalamos dependencias
Estando en el contenedor ejecutamos el siguiente comando:
```
pip install -r requirements.txt
```
En nuestro ejemplo "**requirements.txt**" contiene lo las dependencias de falcon y gunicorn:
```
falcon
gunicorn
ujson
```
Validamos los paquetes instalados en nuestro contenedor
```
pip freeze
```
#### Realizar pruebas
Ejecutamos el siguiente comando y verificamos `http://localhost:8000/` o `http://localhost:8000/led/green`
```
gunicorn app:app
```
