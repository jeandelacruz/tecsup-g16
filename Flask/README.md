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
