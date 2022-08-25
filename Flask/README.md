## Crear un entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
- Windows: source venv/Scripts/activate
- Mac / Linux: source venv/bin/activate
```

## Desactivar entorno virtual

```
deactivate
```

### Endpoints

## Put - Patch

```
Put -> Actualización completas
Patch -> Actualización parcial

Usuario
- nombres
- apellidos
- fecha_nacimiento
- genero

PUT
----------------
http://dominio.com/users/:id
{
 "nombres": "Nuevo Nombre",
 "apellidos": "",
 "fecha_nacimiento": "",
 "genero": ""
}


PATCH
-----------------
http://dominio.com/users/:id
{
 "nombres": "Nuevo Nombre",
 "apellidos": "Nuevo Apellido"
}
```

## Variables de entorno (.env)
````
FLASK_APP=main.py
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=false
```