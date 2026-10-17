# Cuaderno de Gastos (versión independiente)

App web instalable, sin cuenta de Claude. Los gastos de cada persona quedan guardados en su propio dispositivo.
El precio de la soja se actualiza solo (GitHub Actions) y se guarda en `prices.json`.

## Publicar (una sola vez, ~10 minutos)

1. Creá una cuenta en github.com (gratis).
2. Arriba a la derecha: **+ > New repository**. Nombre: `gastos`. Dejalo **Public** (hace falta para Pages gratis). Create repository.
3. En el repositorio nuevo: **uploading an existing file**. Arrastrá TODO el contenido de esta carpeta,
   incluidas las carpetas `.github` y `scripts` (si tu navegador no deja subir carpetas ocultas, usá GitHub Desktop
   o subí el .zip descomprimido desde la compu). Commit changes.
4. **Settings > Pages**: Source = *Deploy from a branch*, Branch = `main`, carpeta `/ (root)`. Save.
   En un minuto aparece el link: `https://TU-USUARIO.github.io/gastos/`
5. **Actions**: si aparece un botón para habilitar workflows, habilitalos. Entrá a
   *Actualizar precio de la soja > Run workflow* para probarlo. Tiene que terminar en verde y el
   `prices.json` va a mostrar la fecha de hoy. Si sale en rojo, mirá el mensaje: casi siempre es que la
   CAC cambió su página o bloquea la consulta.

## Instalar en el celular
- iPhone: abrí el link en **Safari > Compartir > Añadir a pantalla de inicio**.
- Android: Chrome > menú > **Instalar app**.

## Pasarla a otra persona
Mandale el link. Cada uno ve y guarda solo lo suyo, en su dispositivo.

## Cosas a saber
- Los datos viven en el navegador del dispositivo: si se borran los datos del sitio, se pierden.
  Usá **Exportar mes (CSV)** de vez en cuando como respaldo.
- El precio se revisa lunes a viernes a las 10:17 y 18:17 (hora Argentina). Si el repositorio queda
  sin actividad mucho tiempo, GitHub puede pausar las tareas programadas: se reactivan desde la pestaña Actions.
- Si algún día no hay precio, hay un botón **Cargar precio a mano** en la tarjeta de soja.
