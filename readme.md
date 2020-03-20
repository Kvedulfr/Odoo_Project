
# Version 1.1

## Mejoras
-Rectructuración del modulo.

-Clases hechas de nuevo para evitar problemas.

-Campo Many2one insertado.

## Eliminado
-Clases anteriores.
-Kaban.

## Mejoras futuras

-Añadir filtro de busqueda.

-Añadir kanban para clientes y pedidos (con fotos en los pedidos).

-Añadir un boton para exportar la base de datos (para evitar el borrado de la base de datos).

-Modulo de gastos.

-Informes para obtener ganancias.

-Reestructurar el modulo para que este todo una carpeta (un archivo donde contenga todo el modulo de golpe).

-Añadir restriciones (mirar el modulo de pedro y esta pagina https://www.odoo.com/es_ES/forum/ayuda-1/question/unique-sql-constraint-for-a-field-on-a-exisitng-database-odoo-10-124445 )

# Version 2.0
# Mejoras
-Estructura de carpetas y archivos del modulo.

-He añadido kanban en clientes con funcionalidad de editar.


# Mejoras futuras

-Añadir restriciones en fechas.

-Añadir kanban en pedidos. <--- Comprobar si puedo dividir en dos columnas de pedidos pagado o no pagado.

-Insertar campo binario en pedidos para insertar fotografias en pedidos.

-Añadir funcionalidad de informes.

-Añadir nueva clase de gastos.

# Version 2.1
## Mejoras
-Añadido filtros y agrupaciones por clientes.

-Al agrupar hace la sumatoria de precios de los pedidos por cada cliente correctamente.

-Añadido vista kanban en pedidos. Comprobado que funciona el agrupar y filtros.

-Cambiado el campo <code>pagado</code> de tipo booleano a Selection por motivos de interfaz con kanban.

-Agregado el agrupar por tipo de cofección.



## Objetivos futuros
-Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

-Añadir restriciones en fechas para que no inserte una fecha pagada o de recogida antes que la fecha de pedido.

-Insertar campo binario en pedidos para insertar fotografias en pedidos para la vista kanban.

-Añadir funcionalidad de informes.

-Añadir nueva clase de gastos.

# Version 2.2

## Mejoras
-Agregado restricciones en fechas.

-Agregado restriciones en precio.

-Agregado restriciones en telefono.

-Agregado funciones para hacer dichas restricciones.

-Modificado la clase.

## Borrado

-Se ha cambiado el tipo de dato del telefono.



## Objetivos futuros
-Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

-Insertar campo binario en pedidos para insertar fotografias en pedidos para la vista kanban.

-Añadir funcionalidad de informes.

-Añadir nueva clase de gastos.

# Version 2.3

## Mejoras

-Mejoras en la interfaz de formulario con separacion por grupos

-Agregado campo imagen para kanban y formulario

-Mejorado la estructura del kanban en el pedido


## Mejoras futuras

-Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

-Añadir funcionalidad de informes. --> https://github.com/PacktPublishing/Odoo-10-Development-Essentials/tree/master/Chapter%2010/reports

-Añadir nueva clase de gastos.