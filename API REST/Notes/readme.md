# Curso de API REST


## Clase 2: Qué es una API y para qué sirve
### Notas

- API: APLICATION PROGRAMMING INTERFACE
- Es conjunto de reglas de como dos apps se comunican: ¿Quien inicia la comunicación, mensajes enviados, respuestas
- EN POO una API es el conjunto de miembros públicos que ofrece una clase atributos y métodos.

**RESUMEN**: 
API son las siglas de Aplication Programming Interface, en español Interfaz de Programación de Aplicaciones. Se trata de un conjunto de reglas que va a definir cómo se comunican dos aplicaciones entre sí.

## Clase 3: Qué es y cómo funciona el protocolo HTTP

### Notas

- Rest se apoya fuertemente en Http
- Http es un protocolo comunicador entre dos aplicaciones.
- **Protocolo**: Conjunto de reglas que establece como se comunicarán dos entidades.
- Hypertexto: Un texto que tiene referencia a otros textos.
- Curl [http://platzi.com](http://platzi.com) hacer pedido a platzi
- ver solo los encabezados: curl -v [link] > /dev/null

**RESUMEN**: 
HTTP son las siglas de Hypertext Transfer Protocol o protocolo de transferencia de hipertexto, es el conjunto de reglas en las que se van a comunicar dos entidades, en este caso dos computadoras.

Así como nosotros nos comunicamos en español gracias a poder mover las cuerdas vocales, producir y escuchar sonidos, las computadoras se pueden comunicar a través de HTTP gracias al modelo de TCP/IP.

## Clase 4: ¿Qué significa REST? y ¿qué es una API RESTful?

### Notas

- REST:  transferencia de estado representacional
- Es una arquitectura enfocado en el intercambio de recursos basado en http. Eleva la abstracción, ya son recursos y no archivos.
- ¿Qué es una API Restfull? Un API diseñada alrededor de los conceptos de REST

**Conceptos:**

- **Recurso:** ¿Cuál es el recurso sobre el que aplicaremos una acción?
- **URI:** Nos permite identificar el recurso sobre el cual se va a actual
- **Acción:**
- **Petición REST Se basa en:**
    - **URL:** Dominio, protocolo
    - **Verbo HTTP:** GET, PUT, POST, DELEATE
- **Recurso:** Cualquier cosa ej: un libro, autor.
- ¿Cuando conviene REST?
    - Interacciones Simples
    - Recursos limitados
    - Si las interacciones son muy complejas no conviene REST
    - Debe bastar con el intercambio de recursos para solucionar el problema para usar rest.

**RESUMEN**: 
REST es un acrónimo de Representational State Transfer o transferencia de estado representacional, le agrega una capa muy delgada de complejidad y abstracción a HTTP. Mientras que HTTP es transferencia de archivos, REST se basa en la transferencia de recursos.

Una API RESTful es una API diseñada con los conceptos de REST:

- **Recurso:** todo dentro de una API RESTful debe ser un recurso.
- **URI:** los recursos en REST siempre se manipulan a partir de la URI, identificadores universales de recursos.
- **Acción:** todas las peticiones a tu API RESTful deben estar asociadas a uno de los verbos de  **HTTP: GET** para obtener un recurso, POST para escribir un recurso, PUT para modificar un recurso y DELETE para borrarlo.
REST es muy útil cuando:

- Las interacciones son simples.
- Los recursos de tu hardware son limitados.
- No conviene cuando las interacciones son muy complejas.

## Clase 5: Cómo realizar una petición REST e interpretar sus resultados

**RESUMEN**: 
Utilizando el comando ‘curl’ dentro de nuestra terminal podemos realizar peticiones a cualquier sitio web, por ejemplo una API como la de xkcd.

```bash
    curl https://xkcd.com/info.0.json
 ```
El anterior comando nos regresa información del API, pero de manera poco legible. para poder verlo de manera más ordenada podemos usar el siguiente comando:

```bash
    curl https://xkcd.com/info.0.json | jq
 ```
## Clase 6: Exponer datos a través de HTTP GET|

### Notas

- Cuando vamos a exponer los recursos, tenemos que definir cuales serán esos recursos.

**RESUMEN**: 

## Clase 9: Modificar datos a través de HTTP PUT

### **Para Recordar**

```bash
# AGREGAR CON POST
curl -X 'POST' "[http://localhost:8000/books](http://localhost:8000/books/1)" -d '{"title":"Nuevo Libro","id
_author:1, id_genre:2"}'
```

```bash
curl -X 'PUT' http://localhost:8000/books/1 -d '{"titulo": "Nuevo Libro", "id_autor": 1, "id_genero": 2}'
```

```bash
curl -X 'DELETE' http://localhost:8000/books/1
```

### Notas

- 

**RESUMEN**: 

## Clase 11: Autenticación vía HTTP

### **Para Recordar**

Se debe enviar el usuario y la contraseña para la autenticación via HTTP

```bash
curl http://korkux:123@localhost:8000/books
```

### Notas

- Se puede restringuir la API por recursos, acciones o toda la API.

**RESUMEN**: 

## Clase 12: Autenticación vía HMAC

### **Para Recordar**

```bash
curl http://localhost:8000/books -H 'X-HASH:' -H 'X-UID: 1' -H 'X-TIMESTAMP:'
```

### Notas

- Código de autorización basado en hash de mensajes

**RESUMEN**: 
Para esta autenticación necesitamos 3 elementos:

- Función Hash: Difícil de romper, que sea conocida por el cliente y servidor.
- Clave secreta: Solamente la pueden saber el cliente y el servidor, será utilizada para corroborar el hash.
- UID: El id del usuario, será utilizado dentro de la función hash junto con la clave secreta y un timestamp.
Es mucho más segura que la autenticación vía HTTP, por ello la información que se envía a través de este método no es muy sensible.

## Clase 14: Manejo de errores de un servicio REST


### Notas

- Los errores en REST se manejan los errores con códigos de error.

**RESUMEN**: 
De momento nuestra API no nos indica que haya ocurrido un error, solamente nos regresa un código 200 de HTTP que significa que la petición se realizó sin problemas.

Para mejorar nuestra API añadiremos respuestas con los códigos HTTP más comunes:

400 Bad Request: indica que el servidor no puede o no procesa la petición debido a algo que es percibido como un error del cliente
404 Not Found: el servidor no encuentra el recurso solicitado.
500 Internal Server Error: la petición no pudo procesarse por un error del servidor.

## Clase 15: Introducción a Ajax

### Notas

- Las aplicaciones de una sola página son un escenario muy comun en las API REST
- El cliente necesita comunicarse con el sv para pedir más datos
- AJAX: Asyncronous Javascript XML. El cliente no espera que el servidor le responda. SI no que trabaja hasta que la info este disponible
- El cliente no se queda esperando a que el servidor le responda si no que puede seguir trabajando. Por eso es asincronico

**RESUMEN**: 
Es muy común tener comunicaciones con API REST al momento de tener una aplicación de una sola página o SPA, ya sea para obtener o guardar datos. Esta comunicación se realiza a través de AJAX, Asynchronous JavaScript XML. la clave es la parte de asincronismo pues el cliente no se queda bloqueado.

## Clase 19: 7 Buenas prácticas del diseño de APIs RESTful


### Notas

- Los recursos deben ser sustantivos
- Los nombres en plural, ya sea colecciones o objetos individuales
- Modificaciones: POST, PUT O DELETE
- Para las relaciones debe usarse URL que incorporen otros recursos: Ej: /Autos/1/Choferes. Esto devolverá los Choferes del auto 1
- Hay que usar links dentro de las respuestas cuando se devuelve la relación a un objeto Ej: /autos/1 debería tener un link asociado a /autos/1/choferes
- Las colecciones deben ser filtreables, ordenables y páginables. Ej: Un usuario deberia poder escoger bajo que parametros traer los recursos.
- API Versionadas

**RESUMEN**: 
1. Siempre utiliza sustantivos para nombrar tus recursos.
2. Añade los nombres en plural para las urls.
3. Las modificaciones a recursos deben hacerse con su verbo HTTP correspondiente: POST, PUT o DELETE.
7. Para devolver recursos asociados a otro recurso utiliza url que incorporen subrecursos: /Autos/1/Choferes.
5. Navegabilidad vía vínculos.
6. Cuando devuelvas colecciones deben ser filtrables, ordenables y paginables.
7. Versiona tu API, añade el número de versión en la url: v1/Autos.

## Examen

[Examen del Curso de API REST.pdf](Curso%20de%20API%20REST/Examen_del_Curso_de_API_REST.pdf)