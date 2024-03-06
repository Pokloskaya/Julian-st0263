## info de la materia: ST0263 Tópicos Especiales En Telematica
#
## Estudiante: Julian Romero, jaromeroh@eafit.edu.co
#
## Profesor: Alvaro Enrique Ospina, aeospinas@eafit.edu.co

## P2P - Comunicación entre procesos mediante API REST y gRPC (reto 1y2)

## 1. breve descripción de la actividad

El trabajo consiste en el desarrollo de un sistema de intercambio de archivos entre pares (peer-to-peer), centralizado y no estructurado. Esto utilizando gRPC para la comunicación entre los clientes y el servidor central, y utilizando REST API para la comunicación entre peers. Durante el reto, se abordaron aspectos como la definición de mensajes en archivos .proto, la configuración de servidores gRPC, la gestión de conexiones de clientes y la manipulación de archivos y solicitudes HTTP en los clientes. Además, se resolvieron varios problemas y desafíos relacionados con el manejo de archivos y la búsqueda de archivos en la base de datos.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Se definió la arquitectura para un sistema P2P
- Se utilizó comunicación gRPC y REST API
- El sistema admite multiconcurrencia
- Cada peer tiene una función de carga y descarga
- Cada componente del sistema implementa un archivo de configuración

### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- El código podría ser más limpio y desacoplado.
- Uso de docker 

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![image](https://github.com/Pokloskaya/Julian-st0263/assets/83888452/7cb09ef0-415f-41b6-9136-3a35c500fa2d)


## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lenguaje de Programación: Python 3.12.0

Librerías y Paquetes:

- Pip: Herramienta de línea de comandos para instalar y gestionar paquetes de Python.
- Env: Herramienta para crear y gestionar entornos virtuales de Python, que son ambientes aislados para instalar paquetes específicos de un proyecto
- gRPC: Utilizado para implementar la comunicación entre los clientes y el servidor centralizado
- Flask: Utilizado para implementar un servidor HTTP que actúa como punto de entrada para las solicitudes de los clientes
- Requests: Utilizado para realizar solicitudes HTTP entre los clientes y para enviar mensajes entre los pares en el sistema P2P
- Threading: Utilizado para manejar múltiples hilos de ejecución y permitir la ejecución simultánea de diferentes partes del programa
- Socket: Utilizado para obtener la dirección IP del host y para manejar la comunicación a nivel de red.
- Signal: Utilizado para registrar manejadores de señales, como la detección de que un programa se termina (y por lo tanto se desconecta un peer).

## como se compila y ejecuta.
Primero, irse al directorio dónde se encuentra el código del servidor central (python.py) y ejecutar el código del servidor central:

>python server.py

luego, ejecutar el código de algún peer, dirigiendose a la carpeta donde este el archivo peer(número del peer).py:

>python peer.py

## descripción y como se configura los parámetros del proyecto:
- Los parametros estan en los archivos bootstrap.py

## como se lanza el servidor.

python server.py

## una mini guia de como un usuario utilizaría el software o la aplicación
1 - El usuario (representado con un peer) inicia sesión 
2 - El usuario busca un archivo que le interesa
3 - Si el archivo se encuentra, el usuario recibe el nombre del peer y la dirección de este. Entonces, el usuario por medio de la consola ingresa el nombre del archivo que quiere y la dirección de ese peer que lo tiene.
4 - Cuando se quiera desvincular del sistema, el usuario puede cerrar sesión. 

## 5. otra información que considere relevante para esta actividad.
Más información en el video enviado a interactiva.

## referencias:

### https://grpc.io/docs/
### https://flask.palletsprojects.com/en/3.0.x/
