# Configuración e Instalación ODOO

En la propia página de la [imagen de oficial de Odoo](https://hub.docker.com/_/odoo) en docker hub, tenemos una buena explicación de como instalar y configurarlo

---

## Postgresql

Para instalar postgresql utilizaremos la imagen oficial de docker.

[imagen posytgresql](https://hub.docker.com/_/postgres)

Mapearemos el puerto con nuestro equipo, para poder enlazarlo con nuestro IDE

Comprobar que el puerto `5432` de nuestro S.O. está libre y no hay una insttancia de postgresql ejecutándose.

Si fuera el caso, utilizar la herramienta `service` de Ubuntu para pararlo y poder lanzar el contenedor.

# Cargar/Actualizar modulo

`$ odoo -u dam22 -d odoodb --db_host=db -r odoo -w odoo`
