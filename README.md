**ATRIBUTE_FIELDS**

**Descripción:** Tribute_fields agrega campos específicos para gestionar información fiscal en los socios comerciales, compañías y movimientos contables...

**Account_move:** Realiza modificaciones en el modelo account_move de Odoo, mejora la gestión de facturas fiscales al proporcionar campos adicionales y su respectiva lógica para el manejo automático, asegurando que los números de control y correlativo fiscales sean únicos cuando sea necesario.

Campos agregados:

- **control_number**: para almacenar el número de control.
- **fiscal_check:** para indicar si la factura es fiscal o no
- **fiscal_correlative**: para almacenar el correlativo fiscal
![Account_move](https://github.com/3D-Vision-C-A/tribute_fields/assets/96964600/7eb2688b-10b5-4312-abf6-9f2be029a029)


**ResCompany:** Extiende la funcionalidad del modelo res.company. Representa la información de la compañía en el sistema.Agrega tres nuevos campos a este modelo: ruc, taxpayer_license y municipality
![ResCompany](https://github.com/3D-Vision-C-A/tribute_fields/assets/96964600/b35bb1c1-225c-4110-a6db-6f9efe183776)

**ResPartner:** Permiten visualizar y gestionar información fiscal adicional para los socios comerciales en Odoo.

- **ruc:** Representa el Registro Único de Contribuyentes (RUC).
- **taxpayer_license:** Representa la Licencia de Actividad Económica (LAE)
- **is_legal_entity:** Indica si el socio es una entidad legal.
![ResPartner](https://github.com/3D-Vision-C-A/tribute_fields/assets/96964600/ae287eb3-a784-471b-a09c-fc2b900b8b58)

