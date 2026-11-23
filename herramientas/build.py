# -*- coding: utf-8 -*-
"""Genera index.html de Julieth Suárez Studio a partir de los datos de los catálogos 2026."""
import html, json, sys

OUT = sys.argv[1]
WA = "573108128227"
IG = "https://instagram.com/julieth5suarez"

def e(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- datos
NOVIA_BASE = [
    "Maquillaje de novia con aerógrafo y acabado de larga duración con blindaje",
    "Peinado de novia",
    "Instalación de tocado, corona y accesorios, como cortesía",
    "Pestañas postizas, si las quieres",
    "Asesoría personalizada para definir tu look",
    "Atención exclusiva para la novia",
]
NOVIAS = [
    dict(id="esencia", num="01", name="Esencia de Novia", tag="Tu belleza, en su forma más pura.",
         n="$330.000", d="$430.000", base=NOVIA_BASE, plus=[], plus_of=None,
         ideal="La novia que ya tiene claro su estilo y quiere un look impecable que dure toda la jornada.",
         note="Si quieres ver tu look antes del gran día, puedes sumar la prueba de maquillaje y peinado como servicio adicional."),
    dict(id="signature", num="02", name="Signature Bride", tag="Elegancia y armonía en cada detalle.",
         n="$615.000", d="$800.000", base=NOVIA_BASE,
         plus=["Prueba de maquillaje y peinado en el estudio",
               "Spa facial y masaje relajante de 30 minutos el día de la boda"], plus_of="Esencia de Novia",
         ideal="La novia que quiere ver y ajustar su look con calma antes de la boda.",
         note="En la prueba definimos juntas el maquillaje y el peinado según tu vestido, tu tocado y el concepto de tu boda."),
    dict(id="glam", num="03", name="Glam Bride", tag="Un look impecable para un día inolvidable.",
         n="$780.000", d="$1.015.000",
         base=NOVIA_BASE + ["Prueba de maquillaje y peinado en el estudio",
                            "Spa facial y masaje relajante de 30 minutos el día de la boda"],
         plus=["Limpieza facial profunda, unos 15 días antes de la boda",
               "Diseño de cejas personalizado", "Kit de retoque para la novia", "Champaña de obsequio"],
         plus_of="Signature Bride", featured=True,
         ideal="La novia que quiere llegar con la piel y las cejas preparadas desde antes.",
         note="La limpieza facial se agenda con anticipación para que la piel tenga tiempo de recuperarse."),
    dict(id="luxury", num="04", name="Luxury Bride", tag="Una experiencia hecha a tu medida.",
         n="$960.000", d="$1.250.000",
         base=NOVIA_BASE + ["Prueba de maquillaje y peinado en el estudio",
                            "Spa facial y masaje relajante de 30 minutos el día de la boda",
                            "Limpieza facial profunda, unos 15 días antes de la boda",
                            "Diseño de cejas personalizado", "Kit de retoque para la novia", "Champaña de obsequio"],
         plus=["Maquillaje para la mamá o la suegra de la novia (una persona, a elección)",
               "Tarifa preferencial en peinado para mamá y suegra",
               "Coordinación de los tiempos de preparación de todo el grupo"],
         plus_of="Glam Bride",
         ideal="La novia que quiere que su mamá o su suegra también se preparen con nosotras y olvidarse de los tiempos.",
         note="El maquillaje de novio es opcional y tiene valor adicional."),
]

XV_BASE = [
    "Maquillaje con aerógrafo y acabado de larga duración con blindaje, que aguanta el vals, las fotos y la pista",
    "Peinado de quinceañera",
    "Instalación de corona o tiara y accesorios, como cortesía",
    "Pestañas postizas, si las quieres",
    "Asesoría personalizada para definir tu look",
    "Atención exclusiva para la quinceañera",
]
QUINCE = [
    dict(id="prequince", num="01", name="Prequince", tag="El comienzo de tu gran celebración.",
         n="$250.000", d="$325.000",
         base=["Maquillaje según el concepto de tu sesión de fotos", "Peinado u ondas",
               "Pestañas postizas, si las quieres",
               "Asesoría para que tu look combine con el vestuario y el lugar de la sesión"],
         plus=[], plus_of=None,
         ideal="La sesión de fotos antes de la fiesta, en estudio o en exteriores.",
         note="Si eliges Royal XV, el prequince ya va incluido."),
    dict(id="esencia-xv", num="02", name="Esencia XV", tag="Tus quince, tu momento de brillar.",
         n="$320.000", d="$415.000", base=XV_BASE, plus=[], plus_of=None,
         ideal="La quinceañera que ya sabe qué look quiere para su fiesta.",
         note="Cuidamos que el maquillaje se vea fresco y acorde a tu edad, con el brillo justo para la noche."),
    dict(id="princesa", num="03", name="Princesa XV", tag="Todo listo antes del gran día.",
         n="$480.000", d="$625.000", base=XV_BASE,
         plus=["Prueba de maquillaje y peinado en el estudio", "Diseño de cejas personalizado",
               "Kit de retoque para la fiesta"], plus_of="Esencia XV", featured=True,
         ideal="La quinceañera que quiere probar su look con calma y llegar con las cejas perfectas.",
         note="En la prueba trae fotos de tu vestido, tu corona y los looks que te gustan. Puede acompañarte tu mamá."),
    dict(id="royal", num="04", name="Royal XV", tag="La experiencia completa, para ti y tu mamá.",
         n="$720.000", d="$935.000",
         base=XV_BASE + ["Prueba de maquillaje y peinado en el estudio", "Diseño de cejas personalizado",
                         "Kit de retoque para la fiesta"],
         plus=["Prequince: maquillaje y peinado para tu sesión de fotos",
               "Maquillaje para la mamá el día de la fiesta",
               "Coordinación de los tiempos de preparación de todo el grupo"], plus_of="Princesa XV",
         ideal="La familia que quiere resolver la sesión de fotos, la fiesta y el arreglo de mamá con una sola persona.",
         note="Por separado, todo esto costaría $838.000 en línea Nacional. En Royal XV ahorras $118.000."),
]

NOVIA_TABLE = [
    ("Maquillaje con aerógrafo y blindaje", "1111"), ("Peinado de novia", "1111"),
    ("Instalación de tocado y accesorios", "1111"), ("Pestañas postizas, si las quieres", "1111"),
    ("Asesoría personalizada", "1111"), ("Prueba de maquillaje y peinado", "0111"),
    ("Spa facial y masaje de 30 min", "0111"), ("Limpieza facial profunda", "0011"),
    ("Diseño de cejas", "0011"), ("Kit de retoque y champaña", "0011"),
    ("Maquillaje para mamá o suegra", "0001"), ("Coordinación de tiempos del grupo", "0001"),
]
XV_TABLE = [
    ("Maquillaje para la sesión de fotos", "1001"), ("Maquillaje de fiesta con aerógrafo y blindaje", "0111"),
    ("Peinado", "1111"), ("Instalación de corona y accesorios", "0111"),
    ("Pestañas postizas, si las quieres", "1111"), ("Asesoría personalizada", "1111"),
    ("Prueba de maquillaje y peinado", "0011"), ("Diseño de cejas", "0011"), ("Kit de retoque", "0011"),
    ("Maquillaje para la mamá", "0001"), ("Coordinación de tiempos del grupo", "0001"),
]

SOCIAL = [
    dict(id="soft", name="Maquillaje Soft", price="$90.000", dur="1 h 15 a 1 h 30",
         items=["Preparación de piel", "Maquillaje personalizado", "Acabado fresco y natural"], plus=[]),
    dict(id="social", name="Maquillaje Social", price="$120.000", dur="1 h 30 a 2 h",
         items=["Preparación de piel", "Maquillaje personalizado", "Ojos más elaborados", "Pestañas",
                "Iluminación y contorno", "Sellado de larga duración"], plus=[]),
    dict(id="glam-social", name="Maquillaje Glam", price="$150.000", dur="1 h 30 a 2 h",
         items=["Preparación de piel", "Maquillaje personalizado", "Pestañas", "Iluminación y contorno",
                "Sellado de larga duración"],
         plus=["Piel de mayor cobertura", "Ojos con cortes, delineados elaborados y brillos"], featured=True),
    dict(id="ondas", name="Social + Ondas Glam", price="$190.000", dur="2 h a 2 h 30",
         items=["Preparación de piel", "Maquillaje personalizado", "Ojos más elaborados", "Pestañas",
                "Iluminación y contorno", "Sellado de larga duración"],
         plus=["Ondas glam en el cabello"]),
    dict(id="editorial", name="Editorial / Creativo", price="Desde $120.000", dur="2 a 3 h",
         items=["Maquillaje diseñado según tu concepto", "Sesiones de fotos, disfraces, Halloween y caracterización",
                "El valor depende de la complejidad y el tiempo"], plus=[]),
]

ADICIONALES = [
    ("Cabello", [("Planchado", "Liso con brillo y movimiento.", "$50.000"),
                 ("Ondas glam", "Ondas definidas y duraderas para cualquier evento.", "$70.000"),
                 ("Peinado recogido o semirrecogido", "Incluye la instalación de accesorios.", "$80.000")]),
    ("Rostro, cejas y piel", [
        ("Maquillaje para hombre", "Piel uniforme y natural. Para novios, grados y sesiones de fotos.", "$70.000"),
        ("Pestañas postizas", "Para los servicios que no las incluyen, como el Soft.", "$15.000"),
        ("Perfilamiento de cejas", "", "$10.000"),
        ("Diseño de cejas", "", "$50.000"),
        ("Limpieza facial profunda", "Ideal unos días antes de tu evento.", "$70.000"),
        ("Spa facial y masaje relajante", "30 minutos.", "$40.000")]),
    ("Para novias y quinceañeras", [
        ("Solo maquillaje de novia", "Aerógrafo y blindaje, con pestañas si las quieres. Sin peinado ni extras.", "$180.000 Nacional · $235.000 Deluxe"),
        ("Peinado de novia", "Para sumar a Solo maquillaje de novia.", "$150.000"),
        ("Prueba de maquillaje y peinado · novia", "En el estudio, unas semanas antes de la boda.", "$270.000"),
        ("Prueba de maquillaje y peinado · quinceañera", "Para sumar a Esencia XV.", "$250.000"),
        ("Damas, mamá y familia", "Con tu paquete, el mismo día, 10 % menos. Precio normal $120.000 / $155.000.", "$108.000 Nacional · $140.000 Deluxe")]),
]

GALERIA = [
    ("w1_novia", "novias", "Novia con tiara de cristales y maquillaje luminoso"),
    ("w3_novia", "novias", "Novia con diadema de perlas y ojos delineados"),
    ("w5_novia", "novias", "Maquillaje de novia con labios rojos"),
        ("w12_quinceanera", "quince", "Quinceañera con corona dorada y ojos ahumados suaves"),
    ("w15_quinceanera", "quince", "Quinceañera con tiara y labios nude"),
    ("w0_quinceanera", "quince", "Look juvenil con delineado y ondas"),
    ("w4_quinceanera", "quince", "Quinceañera con sombras lila y verde"),
    ("w6_quinceanera", "quince", "Ojos lila con brillo para quinceañera"),
        ("video_glam_social", "social", "Maquillaje glam social con delineado"),
    ("w9_social", "social", "Maquillaje social con sombras cobre"),
    ("w7_social", "social", "Maquillaje social para mamá con labios rojos"),
    ("w10_social", "social", "Maquillaje social para piel madura"),
    ("w11_social", "social", "Maquillaje social natural"),
    ("w17_artistico", "artistico", "Maquillaje artístico de catrina"),
    ("w19_artistico", "artistico", "Caracterización de calavera en blanco"),
    ("w16_artistico", "artistico", "Maquillaje de fantasía en verde y morado"),
    ("w21_artistico", "artistico", "Maquillaje de fantasía con pedrería"),
]

FAQ = [
    ("¿Cómo reservo mi fecha?",
     "Escríbeme por WhatsApp con la fecha, la hora y el lugar donde te vas a arreglar. Te confirmo disponibilidad y te envío la cotización con todos los valores. Tu fecha queda reservada cuando pagas el anticipo y recibes la confirmación por escrito."),
    ("¿Cuánto es el anticipo?",
     "Para novias y quinceañeras, el 50 % del valor total; el otro 50 % se paga antes del evento, en la fecha que indica el contrato, nunca el mismo día. Para maquillaje social separas tu cita con el 30 %."),
    ("¿Qué diferencia hay entre la línea Nacional y la Deluxe?",
     "La Nacional usa productos nacionales de alta calidad y la Deluxe, productos importados de gama deluxe. Lo que incluye cada paquete es igual en las dos líneas; la Deluxe cuesta cerca de un 30 % más."),
    ("¿Van a domicilio? ¿Cuánto cuesta?",
     "Sí, voy hasta donde te arregles. El domicilio cuesta $20.000 en el casco urbano y $40.000 en la zona cercana. Si tu servicio empieza de madrugada y tiene recargo, te lo confirmo por escrito antes de que pagues el anticipo."),
    ("¿Puedo cambiar la fecha de mi boda o de mis quince?",
     "Sí. Cambiar la fecha no es cancelar: con aviso oportuno, tu anticipo pasa completo a la nueva fecha, sujeto a disponibilidad."),
    ("¿Qué pasa si cancelo?",
     "En novias y quinceañeras el anticipo no es reembolsable, pero si avisas con 20 días o más queda como saldo a favor para otros servicios del estudio, y si ya pagaste el saldo te lo devolvemos. Si contrataste a distancia, tienes 5 días hábiles desde el pago para retractarte y te devolvemos el 100 %. En maquillaje social, si cancelas con menos de 24 horas la reserva no se devuelve; con más tiempo movemos tu cita sin costo."),
    ("¿Y si ustedes no pueden atenderme?",
     "Por fuerza mayor, te ofrecemos una maquilladora de nuestra confianza con el mismo paquete, o te devolvemos todo lo que pagaste."),
    ("¿Hacen prueba de maquillaje?",
     "Sí, en el estudio, unas semanas antes del evento. Viene incluida en Signature Bride, Glam Bride, Luxury Bride, Princesa XV y Royal XV. Para los demás paquetes se suma como adicional: $270.000 para novias y $250.000 para quinceañeras."),
    ("¿Pueden maquillar a mi mamá, mis damas o mi familia?",
     "Sí. Si se arreglan el mismo día y con tu paquete tienen tarifa especial de $108.000 en línea Nacional y $140.000 en Deluxe por persona (10 % menos). El peinado de familiares se cotiza aparte con tarifa preferencial."),
    ("Tengo la piel sensible o alergias, ¿qué hago?",
     "Cuéntamelo desde el primer mensaje. Antes de la prueba llenas un formulario corto sobre alergias y cuidados. Usamos productos con registro INVIMA y herramientas desinfectadas, y lo desechable es de uso individual."),
    ("¿Cómo debo llegar a mi cita?",
     "Con la cara limpia, sin maquillaje, y con el cabello lavado y seco. Si es a domicilio, necesitamos un espacio bien iluminado, una silla cómoda, una mesa y una toma eléctrica."),
    ("¿Qué medios de pago reciben?",
     "Transferencia bancaria, Nequi, Daviplata, Bre-B y tarjeta de crédito o débito. El efectivo se recibe en el estudio con recibo. Cada pago se confirma por escrito, y solo recibimos pagos en las cuentas que aparecen en tu contrato."),
    ("Si reservo en 2026 para una fecha en 2027, ¿me suben el precio?",
     "No. Si pagas el anticipo en 2026 para un evento en 2027, el precio de tu paquete se mantiene."),
    ("¿Publican mis fotos?",
     "Solo si nos autorizas por escrito, y puedes pedir que dejemos de usarlas cuando quieras. En quinceañeras, la autorización la da la mamá, el papá o el acudiente."),
]

# ---------------------------------------------------------------- helpers
CHECK = '<svg class="ic" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.5 10 6l4.5 2-4.5 2L8 14.5 6 10 1.5 8 6 6Z"/></svg>'

def wa_link(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(text)}"

def package_card(p, kind):
    items = "".join(f"<li>{CHECK}<span>{e(i)}</span></li>" for i in p["base"])
    plus = ""
    if p["plus"]:
        plus = (f'<p class="plus-label">Plus frente a {e(p["plus_of"])}</p>' if p["plus_of"] else "") + \
            "".join(f'<li class="is-plus">{CHECK}<span>{e(i)}</span></li>' for i in p["plus"])
    feat = ""
    badge = ""
    return f'''
<article class="pkg{feat}" id="pkg-{p["id"]}">
  {badge}
  <p class="pkg-num">Paquete {p["num"]}</p>
  <h3 class="pkg-name">{e(p["name"])}</h3>
  <p class="pkg-tag">{e(p["tag"])}</p>
  <p class="pkg-price"><span class="price" data-n="{p["n"]}" data-d="{p["d"]}">{p["n"]}</span> <small>COP</small></p>
  <p class="pkg-line">Línea <span class="line-name">Nacional</span></p>
  <ul class="pkg-list">{items}{plus}</ul>
  <p class="pkg-ideal"><strong>Ideal para:</strong> {e(p["ideal"])}</p>
  <p class="pkg-note">{e(p["note"])}</p>
  <a class="btn btn-block" href="#agenda" data-book="{kind}|{e(p["name"])}">Agendar {e(p["name"])}</a>
</article>'''

def compare_table(rows, names, prices_n, prices_d, caption):
    head = "".join(f"<th scope='col'>{e(n)}</th>" for n in names)
    body = ""
    for label, mask in rows:
        cells = "".join(f"<td>{'<span class=\"yes\" aria-label=\"Incluido\">◆</span>' if c=='1' else '<span class=\"no\" aria-label=\"No incluido\">—</span>'}</td>" for c in mask)
        body += f"<tr><th scope='row'>{e(label)}</th>{cells}</tr>"
    body += "<tr class='row-price'><th scope='row'>Línea Nacional</th>" + "".join(f"<td>{p}</td>" for p in prices_n) + "</tr>"
    body += "<tr class='row-price'><th scope='row'>Línea Deluxe</th>" + "".join(f"<td>{p}</td>" for p in prices_d) + "</tr>"
    return f'''<details class="compare"><summary>Comparar los paquetes en una tabla</summary>
<div class="table-wrap"><table><caption class="sr-only">{e(caption)}</caption><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table></div>
<p class="fine">Precios en pesos colombianos por persona. Domicilio: $20.000 en el casco urbano y $40.000 en la zona cercana.</p></details>'''

def social_card(s):
    items = "".join(f"<li>{CHECK}<span>{e(i)}</span></li>" for i in s["items"])
    if s["plus"]:
        items += '<p class="plus-label">Plus frente al Social</p>' + "".join(f'<li class="is-plus">{CHECK}<span>{e(i)}</span></li>' for i in s["plus"])
    feat = ""
    return f'''
<article class="pkg pkg-sm{feat}">
  <h3 class="pkg-name">{e(s["name"])}</h3>
  <p class="pkg-price">{e(s["price"])}</p>
  <p class="pkg-line">Duración · {e(s["dur"])}</p>
  <ul class="pkg-list">{items}</ul>
  <a class="btn btn-ghost btn-block" href="#agenda" data-book="social|{e(s["name"])}">Agendar</a>
</article>'''

def fmt_price(c):
    if " · " not in c:
        return e(c)
    parts = []
    for part in c.split(" · "):
        val, _, lab = part.partition(" ")
        parts.append(f"{e(val)}<small>{e(lab)}</small>")
    return "<span class='dual'>" + "".join(f"<span>{p}</span>" for p in parts) + "</span>"

def adicionales():
    out = ""
    for title, rows in ADICIONALES:
        trs = "".join(f"<tr><th scope='row'>{e(a)}{('<small>'+e(b)+'</small>') if b else ''}</th><td>{fmt_price(c)}</td></tr>" for a, b, c in rows)
        out += f"<div class='extra'><h3>{e(title)}</h3><table class='price-table'><tbody>{trs}</tbody></table></div>"
    return out

def gallery():
    btns = [("todas", "Todas"), ("novias", "Novias"), ("quince", "Quinceañeras"), ("social", "Social"), ("artistico", "Artístico")]
    f = "".join(f'<button type="button" class="chip{" is-on" if k=="todas" else ""}" data-filter="{k}" aria-pressed="{"true" if k=="todas" else "false"}">{v}</button>' for k, v in btns)
    figs = "".join(
        f'<figure class="g-item" data-cat="{c}"><button type="button" class="g-open" data-src="img/{n}.jpg" data-alt="{e(a)}"><img src="img/{n}.jpg" alt="{e(a)}" loading="lazy" width="300" height="400"></button></figure>'
        for n, c, a in GALERIA)
    return f'<div class="chips" role="group" aria-label="Filtrar galería">{f}</div><div class="grid-gallery">{figs}</div>'

def faq():
    return "".join(f"<details class='faq'><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)

def logo_inline(path, cls, label):
    svg = open(path, encoding="utf-8").read()
    svg = svg.replace("<svg ", f'<svg class="{cls}" role="img" aria-label="{e(label)}" ', 1)
    svg = svg.replace(' width="900" height="560"', "").replace(' width="600" height="600"', "")
    return svg

# ---------------------------------------------------------------- página
pkg_options = {
    "novia": [p["name"] for p in NOVIAS] + ["Solo maquillaje de novia", "Aún no sé, quiero asesoría"],
    "quince": [p["name"] for p in QUINCE] + ["Aún no sé, quiero asesoría"],
    "social": [s["name"] for s in SOCIAL] + ["Solo un servicio adicional"],
}

LOGO = '<img class="logo-mark" src="logos/JS_sello.svg" alt="" width="64" height="64"><img class="logo-name" src="logos/JS_nombre.svg" alt="Julieth Suárez Studio · Makeup" width="300" height="60">'
LOGO_LIGHT = '<img class="logo" src="logos/B_monograma_claro.svg" alt="Julieth Suárez Studio · Makeup" width="900" height="560" loading="lazy">'

jsonld = {
    "@context": "https://schema.org", "@type": "BeautySalon",
    "name": "Julieth Suárez Studio", "description": "Maquillaje profesional para novias, quinceañeras y eventos sociales, con aerógrafo y acabado de larga duración. Servicio a domicilio.",
    "telephone": "+57 310 812 8227", "sameAs": [IG], "priceRange": "$90.000 - $1.250.000 COP",
    "areaServed": "Colombia", "currenciesAccepted": "COP",
    "paymentAccepted": "Efectivo, transferencia bancaria, Nequi, Daviplata, Bre-B, tarjeta de crédito o débito",
}

wa_general = wa_link("Hola, Julieth. Vi tu página web y quiero información sobre tus servicios de maquillaje.")

page = f'''<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Julieth Suárez Studio · Maquillaje profesional para novias, quinceañeras y eventos</title>
<meta name="description" content="Maquillaje profesional con aerógrafo y acabado de larga duración para novias, quinceañeras y eventos sociales. Precios 2026, catálogos, galería y agenda por WhatsApp. Servicio a domicilio.">
<meta name="theme-color" content="#FBF5F1">
<meta property="og:type" content="website">
<meta property="og:title" content="Julieth Suárez Studio · Makeup">
<meta property="og:description" content="Novias, quinceañeras y maquillaje social. Tu belleza, mi propósito.">
<meta property="og:image" content="img/og.jpg">
<link rel="icon" href="logos/B_avatar_rosa.svg" type="image/svg+xml">
<link rel="preload" href="fonts/Cormorant-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/Jost-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/estilos.css">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>

<header class="site-header" id="top">
  <div class="wrap header-in">
    <a class="brand" href="#top" aria-label="Julieth Suárez Studio, inicio">{LOGO}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span><span class="sr-only">Menú</span></button>
    <nav id="menu" class="menu" aria-label="Principal">
      <a href="#novias">Novias</a>
      <a href="#quinceaneras">Quinceañeras</a>
      <a href="#social">Social</a>
      <a href="#galeria">Galería</a>
      <a href="#catalogos">Catálogos</a>
      <a href="#preguntas">Preguntas</a>
      <a class="btn btn-sm" href="#agenda">Agendar</a>
    </nav>
  </div>
</header>

<main id="contenido">

<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-text">
      <p class="eyebrow">Maquillaje profesional · Colombia</p>
      <h1>Novias, quinceañeras y eventos que se recuerdan</h1>
      <p class="script">Tu belleza, mi propósito.</p>
      <p class="lead">Maquillaje con aerógrafo y acabado de larga duración, hecho a la medida de tu piel y de tu estilo. Voy hasta donde te arregles.</p>
      <div class="cta-row">
        <a class="btn" href="#agenda">Agendar mi fecha</a>
        <a class="btn btn-ghost" href="#servicios">Ver servicios y precios</a>
      </div>
      <ul class="trust">
        <li>Aerógrafo y blindaje</li><li>Servicio a domicilio</li><li>Productos con registro INVIMA</li>
      </ul>
    </div>
    <div class="hero-media">
      <div class="arch"><img src="img/w1_novia.jpg" alt="Novia maquillada por Julieth Suárez, con tiara de cristales" width="600" height="843" fetchpriority="high"></div>
      <div class="arch arch-sm"><img src="img/w12_quinceanera.jpg" alt="Quinceañera con corona dorada" width="300" height="490" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="about">
  <div class="wrap about-in">
    <div class="about-mark"><img class="avatar" src="logos/B_avatar_rosa.svg" alt="" width="600" height="600" loading="lazy"></div>
    <div>
      <p class="eyebrow">Bienvenida</p>
      <h2>Hola, soy Julieth</h2>
      <p>Creo en el poder de una mirada que habla por sí sola. Mi trabajo es que te veas como la mejor versión de ti, sin dejar de reconocerte en el espejo.</p>
      <p>Todas las fotos de esta página son de novias y clientas reales que maquillé yo.</p>
      <p class="script script-sm">Una mirada que habla por sí sola.</p>
    </div>
  </div>
</section>

<section class="services" id="servicios">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Servicios</p><h2>¿Para qué ocasión te maquillo?</h2></header>
    <div class="svc-grid">
      <a class="svc" href="#novias"><img src="img/w3_novia.jpg" alt="Novia con diadema de perlas" loading="lazy" width="300" height="400"><span class="svc-body"><span class="svc-title">Novias</span><span class="svc-sub">Cuatro paquetes con aerógrafo y blindaje</span><span class="svc-price">Desde $330.000</span></span></a>
      <a class="svc" href="#quinceaneras"><img src="img/w15_quinceanera.jpg" alt="Quinceañera con tiara" loading="lazy" width="300" height="400"><span class="svc-body"><span class="svc-title">Quinceañeras</span><span class="svc-sub">Prequince, fiesta y paquetes con mamá</span><span class="svc-price">Desde $250.000</span></span></a>
      <a class="svc" href="#social"><img src="img/video_glam_social.jpg" alt="Maquillaje glam social" loading="lazy" width="300" height="400"><span class="svc-body"><span class="svc-title">Social</span><span class="svc-sub">Grados, fiestas, sesiones y eventos</span><span class="svc-price">Desde $90.000</span></span></a>
      <a class="svc" href="#social"><img src="img/w17_artistico.jpg" alt="Maquillaje artístico de catrina" loading="lazy" width="300" height="400"><span class="svc-body"><span class="svc-title">Editorial y artístico</span><span class="svc-sub">Fantasía, Halloween y caracterización</span><span class="svc-price">Desde $120.000</span></span></a>
    </div>
  </div>
</section>

<section class="pricing" id="novias" data-pricing>
  <div class="wrap">
    <header class="sec-head">
      <p class="eyebrow">Novias 2026</p>
      <h2>Tu gran día, mi mayor inspiración</h2>
      <p>Si dudas entre dos paquetes, escríbeme y te ayudo a elegir según tu fecha, tu piel y tu presupuesto.</p>
    </header>
    <div class="line-toggle" role="group" aria-label="Línea de productos">
      <button type="button" class="is-on" data-line="n" aria-pressed="true">Línea Nacional</button>
      <button type="button" data-line="d" aria-pressed="false">Línea Deluxe</button>
    </div>
    <p class="line-help">Nacional: productos nacionales de alta calidad. Deluxe: productos importados de gama deluxe. Lo que incluye cada paquete es igual en las dos líneas.</p>
    <div class="pkg-grid">{"".join(package_card(p, "novia") for p in NOVIAS)}</div>
    {compare_table(NOVIA_TABLE, [p["name"].replace(" de Novia","").replace(" Bride","") for p in NOVIAS], [p["n"] for p in NOVIAS], [p["d"] for p in NOVIAS], "Comparación de paquetes de novia")}
  </div>
</section>

<section class="pricing alt" id="quinceaneras" data-pricing>
  <div class="wrap">
    <header class="sec-head">
      <p class="eyebrow">Quinceañeras 2026</p>
      <h2>Tus quince, tu momento de brillar</h2>
      <p>El Prequince es para la sesión de fotos. Los otros tres son para el día de la fiesta. Un look fresco, juvenil y que dure desde la entrada hasta el último baile.</p>
    </header>
    <div class="line-toggle" role="group" aria-label="Línea de productos">
      <button type="button" class="is-on" data-line="n" aria-pressed="true">Línea Nacional</button>
      <button type="button" data-line="d" aria-pressed="false">Línea Deluxe</button>
    </div>
    <div class="pkg-grid">{"".join(package_card(p, "quince") for p in QUINCE)}</div>
    {compare_table(XV_TABLE, [p["name"] for p in QUINCE], [p["n"] for p in QUINCE], [p["d"] for p in QUINCE], "Comparación de paquetes de quinceañera")}
  </div>
</section>

<section class="pricing" id="social">
  <div class="wrap">
    <header class="sec-head">
      <p class="eyebrow">Maquillaje social 2026</p>
      <h2>Una mirada que habla por sí sola</h2>
      <p>Para grados, fiestas, sesiones de fotos, invitadas y cualquier día que quieras verte increíble.</p>
    </header>
    <div class="pkg-grid pkg-grid-5">{"".join(social_card(s) for s in SOCIAL)}</div>
    <p class="fine center">Precios en pesos colombianos, con productos de línea Nacional. Si prefieres productos importados (línea Deluxe), el valor sube cerca de un 30 %.</p>
  </div>
</section>

<section class="extras alt" id="adicionales">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Complementa tu look</p><h2>Servicios adicionales</h2><p>Suma solo lo que necesitas. Se pueden tomar solos o junto con tu maquillaje.</p></header>
    <div class="extras-grid">{adicionales()}</div>
  </div>
</section>

<section class="gallery" id="galeria">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Galería</p><h2>Trabajos reales</h2><p>Clientas reales maquilladas por Julieth. Mira más en <a href="{IG}" target="_blank" rel="noopener">@julieth5suarez</a>.</p></header>
    {gallery()}
  </div>
</section>

<section class="catalogs alt" id="catalogos">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Catálogos 2026</p><h2>Llévate el catálogo completo</h2><p>Descárgalo en PDF para revisarlo con calma o compartirlo con tu familia.</p></header>
    <div class="cat-grid">
      <a class="cat" href="catalogos/novias-2026.pdf" download><img src="img/w5_novia.jpg" alt="" loading="lazy" width="300" height="400"><span><strong>Novias 2026</strong><small>PDF · 10 páginas</small></span></a>
      <a class="cat" href="catalogos/quinceaneras-2026.pdf" download><img src="img/w0_quinceanera.jpg" alt="" loading="lazy" width="300" height="400"><span><strong>Quinceañeras 2026</strong><small>PDF · 10 páginas</small></span></a>
      <a class="cat" href="catalogos/social-2026.pdf" download><img src="img/w9_social.jpg" alt="" loading="lazy" width="300" height="400"><span><strong>Maquillaje social 2026</strong><small>PDF · 6 páginas</small></span></a>
    </div>
  </div>
</section>

<section class="steps" id="reservar">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Reserva tu fecha</p><h2>Así de fácil</h2></header>
    <ol class="step-list">
      <li><span>01</span><p>Escríbeme por WhatsApp con la fecha, la hora y el lugar donde te vas a arreglar.</p></li>
      <li><span>02</span><p>Te envío la cotización con todos los valores: paquete, adicionales y domicilio.</p></li>
      <li><span>03</span><p>Pagas el anticipo (50 % para novias y quinceañeras, 30 % para social) y recibes la confirmación por escrito.</p></li>
      <li><span>04</span><p>Agendamos tu prueba, si tu paquete la incluye, y llenas el formulario de tu piel.</p></li>
    </ol>
  </div>
</section>

<section class="policies alt" id="politicas">
  <div class="wrap">
    <header class="sec-head"><p class="eyebrow">Sin letra pequeña</p><h2>Condiciones de reserva</h2><p>Lo esencial de nuestras políticas. Para novias y quinceañeras todo queda por escrito en tu contrato.</p></header>
    <div class="pol-grid">
      <div class="pol"><h3>Anticipo</h3><p>Novias y quinceañeras: 50 % del valor total para bloquear la fecha; el saldo se paga antes del evento, nunca el mismo día. Social: 30 % para separar tu cita.</p></div>
      <div class="pol"><h3>Cambio de fecha</h3><p>Cambiar la fecha no es cancelar. Con aviso oportuno, tu anticipo pasa completo a la nueva fecha, sujeto a disponibilidad.</p></div>
      <div class="pol"><h3>Cancelación</h3><p>El anticipo de novias y quinceañeras no es reembolsable; con aviso de 20 días o más queda como saldo a favor. En social, con menos de 24 horas la reserva no se devuelve.</p></div>
      <div class="pol"><h3>Derecho de retracto</h3><p>Si contrataste a distancia, tienes 5 días hábiles desde el pago para retractarte y te devolvemos el 100 %, si aún no recibiste parte del servicio.</p></div>
      <div class="pol"><h3>Tarifas congeladas</h3><p>Si pagas el anticipo en 2026 para un evento en 2027, el precio de tu paquete se mantiene.</p></div>
      <div class="pol"><h3>Domicilio y madrugada</h3><p>$20.000 en el casco urbano y $40.000 en la zona cercana. El recargo de madrugada te lo confirmo antes del anticipo, nunca después.</p></div>
      <div class="pol"><h3>Medios de pago</h3><p>Transferencia, Nequi, Daviplata, Bre-B, tarjeta de crédito o débito, y efectivo en el estudio con recibo. Cada pago se confirma por escrito.</p></div>
      <div class="pol"><h3>Tu piel y tus fotos</h3><p>Productos con registro INVIMA y herramientas desinfectadas. Solo publicamos tus fotos con tu autorización escrita.</p></div>
    </div>
    <p class="alert">Para tu seguridad, solo recibimos pagos en las cuentas oficiales que aparecen en tu contrato. Si alguien te pide pagar en otra cuenta, confírmalo antes por el WhatsApp oficial <a href="{wa_general}" target="_blank" rel="noopener">310 812 8227</a>.</p>
  </div>
</section>

<section class="faqs" id="preguntas">
  <div class="wrap narrow">
    <header class="sec-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Lo que más me preguntan</h2></header>
    {faq()}
  </div>
</section>

<section class="booking" id="agenda">
  <div class="wrap booking-in">
    <div class="booking-text">
      <p class="eyebrow">Agenda</p>
      <h2>Reserva tu fecha</h2>
      <p>Llena estos datos y se abre WhatsApp con tu mensaje listo para enviar. Te respondo con la disponibilidad y la cotización completa.</p>
      <ul class="contact-list">
        <li><span>WhatsApp</span><a href="{wa_general}" target="_blank" rel="noopener">310 812 8227</a></li>
        <li><span>Instagram</span><a href="{IG}" target="_blank" rel="noopener">@julieth5suarez</a></li>
        <li><span>Servicio</span>A domicilio</li>
      </ul>
      <p class="script script-sm">Tu belleza, mi propósito.</p>
    </div>
    <form class="book-form" id="book-form" novalidate>
      <div class="field"><label for="f-nombre">Tu nombre</label><input id="f-nombre" name="nombre" autocomplete="given-name" required></div>
      <div class="field-row">
        <div class="field"><label for="f-tipo">Ocasión</label>
          <select id="f-tipo" name="tipo" required>
            <option value="novia">Novia</option><option value="quince">Quinceañera</option><option value="social">Social o artístico</option>
          </select></div>
        <div class="field"><label for="f-paquete">Paquete o servicio</label><select id="f-paquete" name="paquete"></select></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-fecha">Fecha del evento</label><input id="f-fecha" name="fecha" type="date" required></div>
        <div class="field"><label for="f-hora">¿A qué hora debes estar lista?</label><input id="f-hora" name="hora" type="time"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-lugar">¿Dónde te vas a arreglar?</label><input id="f-lugar" name="lugar" placeholder="Barrio o municipio"></div>
        <div class="field" id="field-linea"><label for="f-linea">Línea de productos</label>
          <select id="f-linea" name="linea"><option>Nacional</option><option>Deluxe</option><option>Aún no sé</option></select></div>
      </div>
      <div class="field"><label for="f-extra">Personas adicionales (mamá, damas, familia)</label><input id="f-extra" name="extra" type="number" min="0" max="20" value="0" inputmode="numeric"></div>
      <div class="field"><label for="f-notas">¿Algo más que deba saber? <small>(opcional)</small></label><textarea id="f-notas" name="notas" rows="3" placeholder="Estilo que te gusta, alergias o piel sensible, adicionales…"></textarea></div>
      <p class="form-error" id="form-error" role="alert" hidden>Escribe tu nombre y la fecha del evento para continuar.</p>
      <button class="btn btn-block" type="submit">Enviar por WhatsApp</button>
      <p class="fine">Tus datos solo se usan para responder tu solicitud. Consulta la <a href="#datos">política de tratamiento de datos</a>.</p>
    </form>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="wrap footer-in">
    <div class="footer-brand">{LOGO_LIGHT}<p class="script">Tu belleza, mi propósito.</p></div>
    <nav class="footer-nav" aria-label="Pie de página">
      <a href="#novias">Novias</a><a href="#quinceaneras">Quinceañeras</a><a href="#social">Social</a>
      <a href="#galeria">Galería</a><a href="#politicas">Condiciones</a><a href="#preguntas">Preguntas frecuentes</a>
    </nav>
    <div class="footer-contact">
      <a href="{wa_general}" target="_blank" rel="noopener">WhatsApp 310 812 8227</a>
      <a href="{IG}" target="_blank" rel="noopener">Instagram @julieth5suarez</a>
    </div>
  </div>
  <div class="wrap">
    <details class="datos" id="datos"><summary>Política de tratamiento de datos personales</summary>
      <p>Julieth Suárez Studio trata los datos que nos entregas (nombre, teléfono, fecha y lugar del evento, y la información de piel que decidas compartir) solo para responder tu solicitud, cotizar, agendar y prestar el servicio, conforme a la Ley 1581 de 2012 y sus decretos reglamentarios. La información sobre salud y alergias es opcional y se trata como dato sensible. Las fotos solo se publican con tu autorización escrita, que puedes retirar cuando quieras. Puedes conocer, actualizar, rectificar o pedir que eliminemos tus datos escribiendo al WhatsApp 310 812 8227. En el caso de menores de edad, los datos los entrega y autoriza su acudiente.</p>
    </details>
    <p class="copy">© 2026 Julieth Suárez Studio · Maquillaje profesional</p>
  </div>
</footer>

<a class="wa-float" href="{wa_general}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3Zm0 23.7a10.7 10.7 0 0 1-5.5-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.7 10.7 0 1 1 16 26.7Zm5.9-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 0 0 2.1-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.2-.3-.3-.6-.4Z"/></svg>
</a>

<dialog class="lightbox" id="lightbox" aria-label="Foto ampliada">
  <button type="button" class="lb-close" aria-label="Cerrar">×</button>
  <img alt="">
</dialog>

<script>window.PAQUETES = {json.dumps(pkg_options, ensure_ascii=False)}; window.WA = "{WA}";</script>
<script src="js/main.js" defer></script>
</body>
</html>
'''
open(OUT, "w", encoding="utf-8").write(page)
print("ok", len(page))
