
# Version 1.1

## Mejoras

- Rectructuración del modulo.

- Clases hechas de nuevo para evitar problemas.

- Campo Many2one insertado.

## Eliminado

- Clases anteriores.

- Kaban.

## Mejoras futuras

- Añadir filtro de busqueda.

- Añadir kanban para clientes y pedidos (con fotos en los pedidos).

- Añadir un boton para exportar la base de datos (para evitar el borrado de la base de datos).

- Modulo de gastos.

- Informes para obtener ganancias.

- Reestructurar el modulo para que este todo una carpeta (un archivo donde contenga todo el modulo de golpe).

- Añadir restriciones (mirar el modulo de pedro y esta pagina https://www.odoo.com/es_ES/forum/ayuda-1/question/unique-sql-constraint-for-a-field-on-a-exisitng-database-odoo-10-124445 )

# Version 2.0

# Mejoras

- Estructura de carpetas y archivos del modulo.

- He añadido kanban en clientes con funcionalidad de editar.


# Mejoras futuras

- Añadir restriciones en fechas.

- Añadir kanban en pedidos. <--- Comprobar si puedo dividir en dos columnas de pedidos pagado o no pagado.

- Insertar campo binario en pedidos para insertar fotografias en pedidos.

- Añadir funcionalidad de informes.

- Añadir nueva clase de gastos.

# Version 2.1

## Mejoras

- Añadido filtros y agrupaciones por clientes.

- Al agrupar hace la sumatoria de precios de los pedidos por cada cliente correctamente.

- Añadido vista kanban en pedidos. Comprobado que funciona el agrupar y filtros.

- Cambiado el campo <code>pagado</code> de tipo booleano a Selection por motivos de interfaz con kanban.

- Agregado el agrupar por tipo de cofección.



## Objetivos futuros

- Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

- Añadir restriciones en fechas para que no inserte una fecha pagada o de recogida antes que la fecha de pedido.

- Insertar campo binario en pedidos para insertar fotografias en pedidos para la vista kanban.

- Añadir funcionalidad de informes.

- Añadir nueva clase de gastos.

# Version 2.2

## Mejoras

- Agregado restricciones en fechas.

- Agregado restriciones en precio.

- Agregado restriciones en telefono.

- Agregado funciones para hacer dichas restricciones.

- Modificado la clase.

## Borrado

- Se ha cambiado el tipo de dato del telefono.



## Objetivos futuros

- Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

- Insertar campo binario en pedidos para insertar fotografias en pedidos para la vista kanban.

- Añadir funcionalidad de informes.

- Añadir nueva clase de gastos.

# Version 2.3

## Mejoras

- Mejoras en la interfaz de formulario con separacion por grupos

- Agregado campo imagen para kanban y formulario

- Mejorado la estructura del kanban en el pedido


## Mejoras futuras

- Agrupacion mensual -->Mirar: https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-group-by-day-25139

- Añadir funcionalidad de informes. --> https://github.com/PacktPublishing/Odoo-10-Development-Essentials/tree/master/Chapter%2010/reports

- Añadir nueva clase de gastos.

# Version 3

## Mejoras
- Arreglado problemas con el boton limpiar en pedidos

- Añadido grafico mensual en pedidos (funciona con filtros y agrupaciones).

- Añadido nueva clase gastos.

- Cambiado la estructura del menu.

- Añadida vista para gastos (tree y form).

## Mejoras futuras

- Añadir gráfico mensual para gastos.

- Mejorar botones de limpiar.

- Añadir funcionalidad de informes. --> https://github.com/PacktPublishing/Odoo-10-Development-Essentials/tree/master/Chapter%2010/reports

# Version 3.1

## Mejoras

- Añadido informe para imprimir el pedido.

- Css en el informe.


## Mejoras futuras

- Añadir gráfico mensual para gastos.

- Añadir informe de gastos.

- Mejorar botones de limpiar.

- Añadir informes para gasto.

# Version 3.2

## Mejoras

- Añadido restricción para que no se pueda insertar una fecha de pago si el producto no esta pagado.

- Añadido restricción para que no se pueda insertar una fecha de recogida anterior a la del pedido.

- Cambiado el tipo de Teléfono por Integer.

- Añadido patrón y restriciones para el telefono (solo se puede colocar de esta manera 123-123-123 o un 0 para aquellos clientes que no quieran darlo)

- Eliminado restricción para que solo se pueda insertar un solo teléfono (debido a cliente familiares entre ellos y para evitar conflictos con la la restricion anterior)

- Añadido restricción para que solo se pueda insertar un solo nombre.

- Mejorado restricción para el campo nombre de clientes evitando que se inserte incialmente un espacio en blanco

- Eliminado problema con limpiar y la fecha recogida y mejorando la restricción de esta para pedidos

- Añadido campo One2many en clientes para poder ver desde clientes los pedidos de cada uno.

# Version 3.3
## Mejoras

- Arreglado problema que no te permita instalar el modulo debido a problemas con informes( hacia falta el modulo informes).
- Arreglado problema en el que no saltaba la restriccion de fecha de pago cuando insertabas una y el pedido no estaba pagado.
- Añadido restricion a fecha de pago cuando el pedido esta pagado y no se inserta una.
- Mejorado apariencia del el informe de resguardo de pedido.
- Añadido total de gastos.
- Añadido campo total para pedidos (con restriciones de que solo recoge los pedido que no estan pagados)


## Mejoras futuras
- Añadir un campo en pedidos para pago parciales

https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-disable-edit-form-when-state-is-done-of-form-121296


# Version 3.4

## Mejoras

- Añadido reseteo del campo adelantado en caso de que haya un cambio en el campo pagado por adelantado.

- Cambiado el campo total para que sea el campo a deber donde se verá lo que debe el cliente y en caso de que sea negativo lo que debe la modista.

- Añadido mas campos para la vista kanban.

- Eliminado el boton limpiar ya que daba conflicto con las contrains que si habia un campo que saltase la constrains y se pulsaba limpiar no te dejaba limpiar y ademas si luego pulsabas descartar se guardaba el registro.

- Agregado Beneficios para preparar la siguiente parte.

## Futuras mejoras

- Alternativa al boton limpiar.

- Hacer que los gastos y los pedidos se confirmen para guardarlos en el modulo beneficios para realizar un grafico y registro para ver los beneficios y gastos mensuales.



# Observaciones Profesor:

## Revisión:

- Tanto en clientes como en gastos, si en el formulario, estamos rellenando datos y pulsamos en “Descartar” se graba el registro aunque no estén rellenos los campos principales. ("En un principio funciona")

- En gastos, al limpiar el registro, la fecha de compra se actualiza a la de hoy, aun cuando no se había puesto ninguna. ¿Esto lo habías planteado así ? 

- En pedidos se puede poner a “No pagado” y luego poner la fecha del pago. ("Arreglado").

## Ampliación:

- Representar en el gráfico los gastos y los beneficios.

- Obtener el total del gasto en la pantalla de “Registros de compra”  (Incluso poder obtenerlo entre unas fechas determinadas (como opción de menú).

- En la vista Kanban, en las tarjetas incluir más información sobre el pedido, tal como si está o no pagado y si está o no entregado, así como la fecha del pedido.

- Los pedidos ya pagados y entregados que dejen de aparecer en la Registro de pedidos. Pero que no sean borrados por si se necesitan,. Puedes crear un “histórico” o “registro de entregados” con los pedidos pagados y entregados.

- Ordenar los pedidos por fecha de pedido.

- Clasificar los pedidos por etapas: como por ejemplo “En proceso” y “Terminados”

- Sería necesario el poder obtener informes. ("Agregado Resguardo en Pedidos")

- ¿Has pensado dar acceso a los clientes a través de web o api externa? Para que puedan ver cómo están sus pedidos, si en proceso o terminados. O incluso al administrador. Esto puedes estudiarlo.




