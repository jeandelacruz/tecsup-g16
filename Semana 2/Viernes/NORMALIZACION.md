# Normalización de base de datos
- Es el proceso para organizar nuestros datos en nuestra BD
- Para que la BD sea flexible con el fin de eliminar redundancias.

## Razones o motivos
- Evitar redundancia de datos
- Disminuir los errores que tengamos al momento de actualizar datos en ciertas entidades
- Optimizar el espacio que consume cada dato (fila)
- Prevenir que se elimine información indeseada

# DDL
## Insert
```
-----------------------------------------------------------------------------------
-- INSERT

-- Tabla area
-- 1ª Forma: INSERT INTO nombre_tabla (campos) VALUES ('valores');
INSERT INTO area (name) VALUES ('Ventas');

-- 2º Forma: Tener en cuenta que se debe mencionar el valor para todos los campos (No recomendable)
-- INSERT INTO area VALUES (2, 'Ingenieria');

-- INSERT MULTIPLE
-- INSERT INTO area (name) VALUES ('Medica');
INSERT INTO area (name) VALUES ('Marketing'), ('RxH');

-- Tabla customer
INSERT INTO customer (name, area_id) VALUES 
('Jose Arriola', 1), ('Roberto Quiroga', 2), ('Joseph Flores', 3), 
('Yesica Chui', 4), ('Germania Toro', NULL);


```