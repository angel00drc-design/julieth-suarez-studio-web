# Julieth Suárez Studio · sitio web

Página de maquillaje profesional para novias, quinceañeras y eventos sociales. Sitio estático (HTML, CSS y JS sin dependencias), listo para Netlify.

## Estructura

- `index.html`: la página. Se genera con `herramientas/build.py`.
- `css/estilos.css`, `js/main.js`: estilos e interacciones (cambio de línea Nacional/Deluxe, galería, formulario de agenda que abre WhatsApp).
- `img/`: fotos retocadas de clientas reales.
- `logos/`, `fonts/`: identidad del manual de marca v1 (Cormorant, Jost, Pinyon Script).
- `catalogos/`: catálogos 2026 en PDF.

## Cambiar precios o textos

Los paquetes, precios, preguntas frecuentes y fotos de la galería están al inicio de `herramientas/build.py`. Edita los datos y vuelve a generar la página desde la raíz del repositorio:

```
python3 herramientas/build.py index.html
```

## Publicar en Netlify

En Netlify: *Add new site → Import an existing project → GitHub* y elige este repositorio. No necesita comando de compilación; la carpeta de publicación es la raíz (ya está en `netlify.toml`).
