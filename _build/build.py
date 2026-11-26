# -*- coding: utf-8 -*-
"""Genera las páginas de venta, el blog y el sitemap del sitio fredymor.github.io/fredymor.
Ejecutar desde la raíz del repo: python3 _build/build.py
"""
import os, re, html, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://fredymor.github.io/fredymor"
WA = "573057842072"
LUDO_PAY = "https://pay.hotmart.com/X108428929J"
VCS_PAY = "https://pay.hotmart.com/E108443780E"
TODAY = datetime.date.today().isoformat()

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

HEAD = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="es_CO">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{base}/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}/assets/site.css">
{jsonld}
</head>
<body>
<header class="site-header"><div class="wrap nav">
  <a class="brand" href="{base}/"><span class="brand-mark">FM</span><span><span class="brand-name">Fredy Moreno</span><span class="brand-role">Psicólogo</span></span></a>
  <ul class="nav-links">
    <li><a href="{base}/ludopatia/">Curso de ludopatía</a></li>
    <li><a href="{base}/vida-con-sentido/">Vida Con-Sentido</a></li>
    <li><a href="{base}/blog/">Artículos</a></li>
    <li><a href="{base}/#contacto">Contacto</a></li>
  </ul>
  <a class="btn btn-primary" style="min-height:42px;padding:.5em 1.1em;font-size:.93rem" href="{wa}">WhatsApp</a>
</div></header>
<main>
"""

FOOT = """
</main>
<footer class="footer"><div class="wrap">
  <span>© {year} Fredy Moreno Quintero · Psicólogo · Mg. en Asesoría Familiar · Bogotá, Colombia</span>
  <span><a href="{base}/">Inicio</a> · <a href="{base}/ludopatia/">Curso de ludopatía</a> · <a href="{base}/vida-con-sentido/">Vida Con-Sentido</a> · <a href="{base}/blog/">Artículos</a></span>
</div></footer>
<a class="wa-float" href="{wa}" aria-label="Escribir por WhatsApp">WhatsApp</a>
</body>
</html>
"""

def page(path, title, desc, body, ogtype="website", img=None, jsonld="", wamsg="Hola Fredy, vi tu página web y quiero más información."):
    url = f"{BASE}/{path}/" if path else f"{BASE}/"
    img = img or f"{BASE}/og-image.jpg"
    out = HEAD.format(title=html.escape(title), desc=html.escape(desc), url=url, ogtype=ogtype, img=img, base=BASE, jsonld=jsonld, wa=wa(wamsg)) + body + FOOT.format(year=datetime.date.today().year, base=BASE, wa=wa(wamsg))
    full = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)
    return url

PAGES = []

# ---------------------------------------------------------------- LUDOPATÍA
ludo_ld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Course","name":"Curso de formación: Prevención, abordaje y manejo de la ludopatía","description":"Curso online de 60 horas con certificado de participación para prevenir, detectar, intervenir y acompañar la recuperación del juego problemático, con enfoque biopsicosocial y sistémico.","inLanguage":"es","url":"%s/ludopatia/","image":"%s/curso/img/producto-hotmart-1200.jpg","provider":{"@type":"Person","name":"Fredy Moreno Quintero","jobTitle":"Psicólogo"},"offers":{"@type":"Offer","price":"260000","priceCurrency":"COP","url":"%s","category":"Paid"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","courseWorkload":"PT60H","startDate":"2026-12-02"}}
</script>""" % (BASE, BASE, LUDO_PAY)

ludo_msg = "Hola Fredy, quiero información sobre el curso «Prevención, abordaje y manejo de la ludopatía»."
ludo_b2b = "Hola Fredy, represento a una empresa de juegos de suerte y azar y quiero una cotización del curso de ludopatía para mi equipo."
ludo_body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="eyebrow">Curso online · 60 horas · Certificado de participación · Inicia el 2 de diciembre</p>
    <h1 style="margin-top:18px">Aprende a identificar, abordar y acompañar a una persona con <em>problemas de juego</em>.</h1>
    <p class="lead">Las apuestas ya están en el celular, a un clic y a toda hora. Si un familiar apuesta y no sabes cómo hablarle, si atiendes personas con conductas de riesgo o si tu empresa debe cumplir un Programa de Juego Responsable, este curso te da el procedimiento completo: qué mirar, qué decir, qué hacer y a dónde derivar.</p>
    <ul class="facts"><li>Dictado por un psicólogo clínico y familiar</li><li>13 módulos y 3 rutas de aprendizaje</li><li>Casos, simulaciones y laboratorios guiados</li><li><b>Incluye 1 sesión de asesoría familiar sin costo</b></li><li>Garantía de 7 días en Hotmart</li></ul>
    <h2 style="margin-top:2em;font-size:1.6rem">Para quién es</h2>
    <ul class="cards">
      <li class="card"><b>Familiares y parejas</b><span>Para acompañar a alguien que apuesta sin romper la relación ni la economía del hogar.</span></li>
      <li class="card"><b>Profesionales</b><span>Psicólogos, orientadores escolares, trabajadores sociales, docentes y personal de salud que necesitan un protocolo claro.</span></li>
      <li class="card"><b>Operadores de juego</b><span>Personal y líderes del Programa de Juego Responsable que deben cumplir el plan anual de capacitación de la Resolución 22654 de 2024 de Coljuegos.</span></li>
    </ul>
  </div>
  <aside class="offer" aria-label="Precio e inscripción">
    <img src="{BASE}/curso/img/portada-ludopatia-rostro-1200.jpg" width="600" height="600" alt="Curso de formación: Prevención, abordaje y manejo de la ludopatía">
    <div class="offer-body">
      <span class="flag">Black Friday · 40 % del 23 al 30 de noviembre</span>
      <div class="price"><b>$260.000</b><span class="cur">COP</span></div>
      <p class="price-sub">Pago seguro en Hotmart, también en cuotas · Acceso por 12 meses · Certificado de 60 horas · <b>Sesión de asesoría familiar sin costo</b> · Garantía de 7 días</p>
      <div class="offer-ctas">
        <a class="btn btn-accent btn-lg" href="{LUDO_PAY}?sck=web_ludopatia" target="_blank" rel="noopener">Inscribirme · inicia el 2 de diciembre</a>
        <a class="btn btn-ghost" href="{wa(ludo_b2b)}">Cotizar para mi empresa (5+ cupos)</a>
      </div>
      <p class="offer-note">Para mayores de 18 años. Es formación psicoeducativa: no reemplaza diagnóstico ni tratamiento. Si tú o alguien cercano está en crisis en Colombia, llama a la Línea 106 o al 123.</p>
    </div>
  </aside>
</div></section>

<section class="section tint"><div class="wrap narrow">
  <p class="eyebrow">Qué aprenderás</p>
  <h2 style="margin-top:14px">13 módulos, del fundamento al protocolo.</h2>
  <ol class="mods">
    <li><span>00</span><div><b>Inducción, encuadre ético y tamizaje inicial</b></div></li>
    <li><span>01</span><div><b>Fundamentos: juego, azar y ludopatía</b></div></li>
    <li><span>02</span><div><b>Neurobiología y psicología del juego problemático</b><small>Por qué el cerebro mantiene la conducta aunque la persona quiera parar.</small></div></li>
    <li><span>03</span><div><b>Factores de riesgo, protección y poblaciones vulnerables</b></div></li>
    <li><span>04</span><div><b>La industria del juego: diseño, publicidad y entornos digitales</b></div></li>
    <li><span>05</span><div><b>Marco legal, ético y de política pública</b><small>Incluye las obligaciones de juego responsable de los operadores en Colombia.</small></div></li>
    <li><span>06</span><div><b>Detección, tamizaje y evaluación</b><small>Señales de alerta y test de factores de riesgo.</small></div></li>
    <li><span>07</span><div><b>Primeros auxilios psicológicos y manejo de crisis</b></div></li>
    <li><span>08</span><div><b>Modelos de intervención basados en evidencia</b></div></li>
    <li><span>09</span><div><b>Familia y redes de apoyo: enfoque sistémico</b><small>Cómo conversar con la persona que apuesta sin culpa ni enfrentamientos.</small></div></li>
    <li><span>10</span><div><b>Prevención en contextos educativos y comunitarios</b></div></li>
    <li><span>11</span><div><b>Prevención de recaídas y proyecto de vida</b></div></li>
    <li><span>12</span><div><b>Proyecto integrador y evaluación final</b></div></li>
  </ol>
  <p style="margin-top:24px" class="muted">Incluye casos, simulaciones de entrevista, herramientas descargables y cuatro laboratorios guiados en un entorno de juego simulado, sin dinero real y con protocolo de seguridad.</p>
</div></section>

<section class="section band" id="empresas"><div class="wrap narrow">
  <p class="eyebrow" style="color:var(--accent)">Para operadores de juegos de suerte y azar</p>
  <h2 style="margin-top:14px">Cierra el plan de capacitación 2026 antes del informe de enero.</h2>
  <p class="lead" style="margin-top:18px">La Resolución 22654 de 2024 de Coljuegos exige que cada operador tenga un Programa de Juego Responsable con un responsable designado y un plan anual de capacitación del personal, y que presente un informe anual en los primeros 15 días hábiles de enero. Este curso certifica a tu equipo de atención, cajeros, supervisores y al líder del programa.</p>
  <ul class="cards">
    <li class="card" style="background:rgba(255,255,255,.06);border-color:var(--band-line)"><b style="color:var(--band-ink)">Certificado individual</b><span style="color:var(--band-ink-2)">60 horas por participante, con informe de asistencia y aprobación para anexar al informe anual.</span></li>
    <li class="card" style="background:rgba(255,255,255,.06);border-color:var(--band-line)"><b style="color:var(--band-ink)">Sesión en vivo</b><span style="color:var(--band-ink-2)">2 horas con tu equipo sobre protocolos de atención, autoexclusión y derivación.</span></li>
    <li class="card" style="background:rgba(255,255,255,.06);border-color:var(--band-line)"><b style="color:var(--band-ink)">Descuento por grupo</b><span style="color:var(--band-ink-2)">5 cupos: 15 % · 10 cupos: 25 % · 20 o más: 35 %. Factura directa para más de 10 cupos.</span></li>
  </ul>
  <p style="margin-top:28px"><a class="btn btn-accent btn-lg" href="{wa(ludo_b2b)}">Pedir cotización por WhatsApp</a></p>
</div></section>

<section class="section"><div class="wrap narrow">
  <p class="eyebrow">Quién lo dicta</p>
  <div class="author">
    <img src="{BASE}/fredy-moreno.jpg" alt="Fredy Moreno Quintero, psicólogo">
    <div><h2 style="margin-top:0;font-size:1.7rem">Fredy Moreno Quintero</h2>
    <p style="margin-top:10px">Psicólogo, magíster en asesoría familiar (Universidad de La Sabana) y especialista en edumática. Trabaja desde el enfoque sistémico en contextos clínicos, educativos y comunitarios, y es proveedor acreditado de formación en The CPD Group. Diseñó este curso para que familias, profesionales y empresas tengan un mismo lenguaje frente al juego problemático.</p></div>
  </div>
</div></section>

<section class="section tint faq"><div class="wrap narrow">
  <p class="eyebrow">Preguntas frecuentes</p>
  <h2 style="margin-top:14px">Antes de inscribirte.</h2>
  <div style="margin-top:20px">
    <details><summary>¿Necesito ser psicólogo para tomarlo?</summary><p>No. La Ruta Familia y la Ruta Personal están pensadas para cualquier persona; la Ruta Profesional profundiza en evaluación e intervención.</p></details>
    <details><summary>¿Cómo funciona el acceso?</summary><p>Al pagar en Hotmart recibes acceso inmediato al área de miembros. Las lecciones se liberan desde el 2 de diciembre y tienes 12 meses para completarlas a tu ritmo.</p></details>
    <details><summary>¿El certificado es válido?</summary><p>Recibes un certificado de participación de 60 horas emitido por el docente. Es formación no formal: no es un título profesional ni reemplaza tratamiento.</p></details>
    <details><summary>¿Puedo pedir reembolso?</summary><p>Sí. Hotmart ofrece 7 días de garantía desde la compra, sin preguntas.</p></details>
    <details><summary>¿Qué incluye la asesoría familiar sin costo?</summary><p>Con tu inscripción recibes una sesión de asesoría familiar en línea de 60 minutos conmigo, por Google Meet, para revisar tu caso: cómo hablar con la persona que apuesta, cómo proteger la economía del hogar y a dónde buscar tratamiento. La agendas por WhatsApp después de la compra, dentro de los 12 meses de acceso. Es una orientación, no reemplaza un tratamiento clínico.</p></details>
    <details><summary>¿Hay descuento para empresas o grupos?</summary><p>Sí, desde 5 cupos. Escríbeme por WhatsApp y te envío la ficha técnica y la cotización el mismo día.</p></details>
  </div>
</div></section>

<section class="section cta-final"><div class="wrap narrow">
  <h2 style="margin-top:0">Inicia el 2 de diciembre de 2026.</h2>
  <p class="lead" style="margin:16px auto 0">260.000 COP · 60 horas · Certificado · Asesoría familiar sin costo · Garantía de 7 días.</p>
  <a class="btn btn-accent btn-lg" href="{LUDO_PAY}?sck=web_ludopatia_final" target="_blank" rel="noopener">Inscribirme en Hotmart</a>
  <p class="muted" style="margin-top:14px"><a href="{wa(ludo_msg)}">¿Tienes una pregunta? Escríbeme por WhatsApp</a></p>
</div></section>
"""
PAGES.append(page("ludopatia", "Curso de ludopatía con certificado · 60 horas · Fredy Moreno, psicólogo",
    "Curso online certificado de 60 horas: prevención, abordaje y manejo de la ludopatía. Para familiares, profesionales y operadores de juego (Res. 22654 de Coljuegos). Inicia el 2 de diciembre.",
    ludo_body, "product", f"{BASE}/curso/img/producto-hotmart-1200.jpg", ludo_ld, ludo_msg))

# ---------------------------------------------------------------- VIDA CON-SENTIDO
vcs_ld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Course","name":"Vida Con-Sentido: bienestar psicológico y avance personal","description":"Programa de 24 horas en 6 módulos con enfoque sistémico: encuentros en vivo, lecturas y actividades prácticas para ordenar prioridades, relaciones y hábitos, guiado por un psicólogo.","inLanguage":"es","url":"%s/vida-con-sentido/","image":"%s/curso/img/portada-vida-con-sentido-rostro-1200.jpg","provider":{"@type":"Person","name":"Fredy Moreno Quintero","jobTitle":"Psicólogo"},"offers":{"@type":"Offer","price":"120000","priceCurrency":"COP","url":"%s","category":"Paid"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","courseWorkload":"PT24H","startDate":"2026-11-20"}}
</script>""" % (BASE, BASE, VCS_PAY)
vcs_msg = "Hola Fredy, quiero información sobre el programa «Vida Con-Sentido»."
vcs_body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="eyebrow">Programa online · 24 horas · 6 módulos · Inscripciones abiertas</p>
    <h1 style="margin-top:18px">Seis semanas para recuperar el rumbo, <em>con método</em> y sin frases vacías.</h1>
    <p class="lead">Cumples con todo y, aun así, sientes que la vida se te va en lo urgente. No necesitas más motivación; necesitas un método. Vida Con-Sentido es un programa breve, guiado por un psicólogo, que te lleva paso a paso a decidir qué sostener, qué soltar y cómo hacerlo en tus relaciones, tu trabajo y tu descanso.</p>
    <ul class="facts"><li>Un encuentro en vivo de 2 horas por módulo</li><li>Lectura orientadora y actividad práctica por módulo</li><li>Enfoque sistémico y recorrido personalizado</li><li>Certificado de 24 horas</li></ul>
    <h2 style="margin-top:2em;font-size:1.6rem">Es para ti si</h2>
    <ul class="cards">
      <li class="card"><b>Sientes agotamiento</b><span>Estás conectado todo el día, cumples con todos y llegas a la noche sin nada para ti.</span></li>
      <li class="card"><b>Estás estancado</b><span>Sabes que algo debe cambiar, pero no sabes por dónde empezar ni con quién.</span></li>
      <li class="card"><b>Atraviesas una pérdida o un cierre</b><span>Una relación, un trabajo, una etapa. Quieres convertirlo en aprendizaje y no en peso.</span></li>
    </ul>
  </div>
  <aside class="offer" aria-label="Precio e inscripción">
    <img src="{BASE}/curso/img/portada-vida-con-sentido-rostro-1200.jpg" alt="Vida Con-Sentido: bienestar psicológico y avance personal">
    <div class="offer-body">
      <span class="flag">Inscripciones abiertas · cohortes permanentes</span>
      <div class="price"><b>$120.000</b><span class="cur">COP</span></div>
      <p class="price-sub">Pago seguro en Hotmart · 6 encuentros en vivo · Certificado de 24 horas · Garantía de 7 días</p>
      <div class="offer-ctas">
        <a class="btn btn-accent btn-lg" href="{VCS_PAY}?sck=web_vcs" target="_blank" rel="noopener">Quiero inscribirme</a>
        <a class="btn btn-ghost" href="{wa(vcs_msg)}">Preguntar por WhatsApp</a>
      </div>
      <p class="offer-note">Es formación educativa y preventiva: no es psicoterapia ni tratamiento. Si estás en crisis en Colombia, llama a la Línea 106 o al 123.</p>
    </div>
  </aside>
</div></section>

<section class="section tint"><div class="wrap narrow">
  <p class="eyebrow">Los seis módulos</p>
  <h2 style="margin-top:14px">Cada módulo: una charla en vivo, una meditación guiada, una lectura y una actividad que te llevas.</h2>
  <ol class="mods">
    <li><span>1</span><div><b>Transformar pérdidas en aprendizaje</b><small>Qué se cerró, qué queda y qué puedes construir desde ahí.</small></div></li>
    <li><span>2</span><div><b>Relaciones y familia</b><small>Mapa sistémico de quién te sostiene, quién te agota y qué conversación está pendiente.</small></div></li>
    <li><span>3</span><div><b>Gestión emocional</b><small>Reconocer, nombrar y regular sin reprimir ni desbordarse.</small></div></li>
    <li><span>4</span><div><b>Propósito y plan de 90 días</b><small>Lo que de verdad quieres defender, convertido en tres decisiones concretas.</small></div></li>
    <li><span>5</span><div><b>Soledad y vida digital</b><small>Atención, descanso y vínculos en un mundo que no se apaga.</small></div></li>
    <li><span>6</span><div><b>Proyecto integral de bienestar</b><small>Tu portafolio de seis productos aplicables a tu vida y cómo sostenerlo.</small></div></li>
  </ol>
</div></section>

<section class="section"><div class="wrap narrow">
  <p class="eyebrow">Quién lo guía</p>
  <div class="author">
    <img src="{BASE}/fredy-moreno.jpg" alt="Fredy Moreno Quintero, psicólogo">
    <div><h2 style="margin-top:0;font-size:1.7rem">Fredy Moreno Quintero</h2>
    <p style="margin-top:10px">Psicólogo y magíster en asesoría familiar (Universidad de La Sabana). Trabaja desde el enfoque sistémico: con la persona y con el sistema que la rodea. Acompaña procesos de bienestar emocional, aprendizaje y familia en contextos clínicos, educativos y comunitarios.</p></div>
  </div>
</div></section>

<section class="section tint faq"><div class="wrap narrow">
  <p class="eyebrow">Preguntas frecuentes</p>
  <h2 style="margin-top:14px">Antes de inscribirte.</h2>
  <div style="margin-top:20px">
    <details><summary>¿Cuándo son los encuentros en vivo?</summary><p>Uno por módulo, de 2 horas, por Google Meet. Los horarios se acuerdan con la cohorte al inicio y quedan grabados en el área de miembros.</p></details>
    <details><summary>¿Cuánto tiempo necesito a la semana?</summary><p>Unas 4 horas: el encuentro en vivo, una lectura corta y una actividad práctica.</p></details>
    <details><summary>¿Es terapia?</summary><p>No. Es un programa educativo y preventivo de bienestar. Si durante el proceso identificas que necesitas acompañamiento individual, puedes solicitarlo aparte.</p></details>
    <details><summary>¿Puedo pedir reembolso?</summary><p>Sí. Hotmart ofrece 7 días de garantía desde la compra.</p></details>
  </div>
</div></section>

<section class="section cta-final"><div class="wrap narrow">
  <h2 style="margin-top:0">Inscripciones abiertas: te unes a la siguiente cohorte.</h2>
  <p class="lead" style="margin:16px auto 0">120.000 COP · 24 horas · 6 encuentros en vivo · Certificado · Garantía de 7 días.</p>
  <a class="btn btn-accent btn-lg" href="{VCS_PAY}?sck=web_vcs_final" target="_blank" rel="noopener">Inscribirme en Hotmart</a>
  <p class="muted" style="margin-top:14px"><a href="{wa(vcs_msg)}">¿Tienes una pregunta? Escríbeme por WhatsApp</a></p>
</div></section>
"""
PAGES.append(page("vida-con-sentido", "Vida Con-Sentido · Programa de bienestar psicológico con un psicólogo · 6 módulos",
    "Programa online de 24 horas en 6 módulos para ordenar prioridades, relaciones y hábitos con enfoque sistémico. Encuentros en vivo con un psicólogo. Inscripciones abiertas.",
    vcs_body, "product", f"{BASE}/curso/img/portada-vida-con-sentido-rostro-1200.jpg", vcs_ld, vcs_msg))

# ---------------------------------------------------------------- BLOG
ARTICLES = []
def article(slug, title, desc, date, body, course):
    ARTICLES.append(dict(slug=slug, title=title, desc=desc, date=date, body=body, course=course))

LUDO_CALL = f"""<div class="callout"><b>Curso certificado: Prevención, abordaje y manejo de la ludopatía</b>60 horas, 13 módulos y tres rutas (personal, familia y profesional), dictado por un psicólogo clínico y familiar. Incluye una sesión de asesoría familiar sin costo. Inicia el 2 de diciembre de 2026. Garantía de 7 días.<br><a class="btn btn-accent" href="{BASE}/ludopatia/">Ver el curso</a></div>"""
VCS_CALL = f"""<div class="callout"><b>Vida Con-Sentido: seis semanas para recuperar el rumbo</b>Programa de 24 horas en 6 módulos con encuentros en vivo, guiado por un psicólogo con enfoque sistémico. Inscripciones abiertas: te unes a la siguiente cohorte.<br><a class="btn btn-accent" href="{BASE}/vida-con-sentido/">Ver el programa</a></div>"""
CRISIS = """<p class="warn">Si tú o alguien cercano está en riesgo inmediato en Colombia, llama a la Línea 106 (salud mental) o al 123. Este artículo es orientación psicoeducativa y no reemplaza una valoración profesional.</p>"""

article("como-ayudar-a-un-familiar-con-ludopatia",
 "Cómo ayudar a un familiar con ludopatía sin destruir la relación",
 "Guía de un psicólogo para familiares: qué decir, qué no hacer, cómo proteger el dinero y cómo conseguir que la persona que apuesta acepte ayuda.",
 "2026-11-12", f"""
<p>Si llegaste aquí es porque alguien que quieres apuesta más de lo que puede y ya probaste de todo: hablar, callar, amenazar, prestar dinero, esconderlo. Lo primero que necesitas saber es que la ludopatía no es falta de voluntad ni de amor por la familia. Es un trastorno del control de impulsos que el cerebro mantiene con el mismo circuito de recompensa que una sustancia, y por eso los regaños no funcionan. Lo segundo: la familia no puede curar a nadie, pero sí puede cambiar las condiciones que mantienen el juego y abrir la puerta a la ayuda.</p>
<h2>Primero entiende qué está pasando</h2>
<p>Una persona con juego problemático suele pasar por tres fases. En la fase de ganancia, el juego es emocionante y parece controlable. En la fase de pérdida aparecen las deudas, las mentiras y el intento de "recuperar lo perdido" apostando más. En la fase de desesperación, la persona ya no apuesta por placer sino para escapar de la angustia, y aparecen el aislamiento, los préstamos a terceros y, a veces, ideas de quitarse la vida. Saber en qué fase está tu familiar cambia lo que conviene hacer.</p>
<p>Las apuestas en línea aceleraron todo. Hoy se puede apostar desde la cama, a las tres de la mañana, con el salario que acaba de entrar y con bonos que el operador envía por WhatsApp. En Colombia los operadores legales están obligados a ofrecer autoexclusión y límites de juego, y eso es una herramienta que la familia puede pedir que se use.</p>
<h2>Lo que no funciona (aunque sea lo primero que sale)</h2>
<ul>
<li><b>Pagar las deudas.</b> Cada rescate le quita a la persona la consecuencia que la haría parar. Si pagas, que sea una sola vez, por escrito y a cambio de un compromiso concreto de tratamiento.</li>
<li><b>Vigilar en secreto.</b> Revisar el celular o la cuenta sin acuerdo convierte la relación en policía y sospechoso. La vigilancia solo sirve cuando es acordada y temporal.</li>
<li><b>Amenazar con irse y no irse.</b> Las amenazas que no se cumplen enseñan que nada cambia.</li>
<li><b>Hablar en medio de una crisis.</b> Después de una pérdida grande o de descubrir una mentira, nadie escucha. Espera a un momento tranquilo.</li>
</ul>
<h2>Cómo tener la conversación</h2>
<p>Elige un momento sin prisa y sin público. Empieza por lo que observas, no por lo que concluyes: "He notado que estás despierto hasta tarde con el celular y que este mes faltó dinero para el arriendo", en lugar de "eres un ludópata y nos estás arruinando". Nombra lo que sientes, no lo que la otra persona es: "Tengo miedo y estoy cansada" abre más puertas que "no te importa nadie". Luego pregunta, y escucha de verdad: "¿Cómo lo estás viviendo tú?". La mayoría de personas con juego problemático sienten una vergüenza enorme; si la conversación les da un lugar donde no sean juzgadas, suelen contar más de lo que esperas.</p>
<p>Termina con una petición concreta y pequeña: hacer juntos un test de factores de riesgo, pedir una cita, activar la autoexclusión en la plataforma. No pidas "que dejes de apostar para siempre"; pide el siguiente paso.</p>
<h2>Proteger el dinero sin humillar</h2>
<p>La protección económica es la medida más efectiva a corto plazo y la que más conflicto genera. Funciona cuando se presenta como un acuerdo temporal de cuidado y no como un castigo: una cuenta conjunta para los gastos fijos, un límite de retiro, una tarjeta que la persona entrega voluntariamente por un tiempo definido, con fecha de revisión. Pon el acuerdo por escrito y revísenlo cada mes. Si hay préstamos con terceros o "gota a gota", busca orientación legal antes de pagar nada.</p>
<h2>Cuidarte tú también</h2>
<p>Los familiares de personas con ludopatía presentan niveles altos de ansiedad, insomnio y culpa. No es un lujo buscar apoyo para ti: es lo que te permitirá sostener los acuerdos. Un grupo de familiares, una consulta propia o, al menos, una persona de confianza con quien hablar sin filtro.</p>
<h2>Cuándo buscar ayuda profesional</h2>
<p>Si hay deudas que crecen, mentiras repetidas, intentos fallidos de parar o cualquier mención a no querer vivir, es momento de consultar. En Colombia, Coljuegos publica un directorio de fundaciones e instituciones de salud; tu EPS debe ofrecer atención en salud mental; y un psicólogo con experiencia en adicciones puede evaluar y orientar el tratamiento. Pedir ayuda no es traicionar a tu familiar: es la única forma de ayudarlo de verdad.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("apuestas-en-diciembre-senales-de-alerta",
 "Apuestas en diciembre: 7 señales de alerta y cómo proteger la prima de tu familia",
 "Diciembre trae prima, fiestas y partidos. Un psicólogo explica las señales de alerta de las apuestas y cómo proteger el dinero de la familia sin pelear.",
 "2026-11-23", f"""
<p>Diciembre trae prima, fiestas, partidos y más tiempo libre. Para muchas familias también trae algo que no se ve venir: el dinero de la prima que desaparece en apuestas desde el celular. Como psicólogo y asesor familiar, estas son las señales que conviene mirar y lo que sí funciona para proteger a la familia.</p>
<h2>7 señales de alerta</h2>
<ol>
<li>Habla de "recuperar" lo perdido o de que "ya le toca ganar".</li>
<li>Cambia de humor según los resultados de un partido o de una app.</li>
<li>Pide dinero prestado o adelantos sin explicar bien para qué.</li>
<li>Esconde el celular, borra notificaciones o tiene apps nuevas de apuestas.</li>
<li>Falta dinero de gastos fijos: arriendo, servicios, mercado.</li>
<li>Pasa más tiempo apostando y menos con la familia, incluso en reuniones.</li>
<li>Se irrita o se pone a la defensiva cuando alguien toca el tema.</li>
</ol>
<p>Una sola señal no es un diagnóstico. Varias juntas, y que se repitan, sí son motivo para actuar. Si quieres una primera orientación, haz el <a href="{BASE}/blog/test-ludopatia-tengo-problemas-con-el-juego/">test de autoevaluación</a>.</p>
<h2>Cómo proteger la prima sin pelear</h2>
<ul>
<li><b>Separa el dinero de la casa.</b> Los gastos fijos van primero y a una cuenta aparte, antes de que llegue la tentación.</li>
<li><b>Habla de hechos, no de su carácter.</b> "Faltó el dinero del arriendo" funciona mejor que "eres un irresponsable".</li>
<li><b>No pagues deudas de juego sin un plan.</b> Sin querer, eso mantiene el ciclo.</li>
<li><b>Propón ayuda concreta.</b> La autoexclusión en casinos y plataformas, una cita con un psicólogo o un grupo de Jugadores Anónimos.</li>
<li><b>Cuídate tú también.</b> La familia necesita apoyo propio para sostener los acuerdos.</li>
</ul>
<h2>Si las fiestas ya se complicaron</h2>
<p>No esperes a enero. Las deudas de diciembre suelen empujar a apostar más en enero para "tapar el hueco". Una conversación tranquila, un acuerdo escrito sobre el dinero y una consulta a tiempo evitan que el problema crezca.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("cerrar-el-ano-sin-agotamiento",
 "Cómo cerrar el año sin agotamiento: 5 preguntas para empezar 2027 con sentido",
 "Un psicólogo propone cinco preguntas para hacer un cierre de año honesto, soltar lo que pesa y elegir tres decisiones concretas para 2027.",
 "2026-11-23", f"""
<p>Fin de año suele llegar con una mezcla rara: cansancio acumulado, balances que nadie pidió y propósitos que se olvidan en febrero. No necesitas una lista de veinte metas. Necesitas un cierre honesto. Estas cinco preguntas son las que uso en procesos de bienestar psicológico; tómate una hora tranquila y respóndelas por escrito.</p>
<h2>1. ¿Qué se cerró este año?</h2>
<p>Una relación, un trabajo, una etapa, una idea de ti mismo. Nombrarlo es el primer paso para que deje de pesar en silencio. Pregúntate qué aprendiste de ese cierre y qué queda en pie.</p>
<h2>2. ¿Quién me sostuvo y quién me agotó?</h2>
<p>Haz un mapa simple de tus relaciones: familia, trabajo, amistades, grupos digitales. Marca a quién acudes cuando las cosas van mal y qué vínculos te quitan más energía de la que te dan. Muchas veces el agotamiento no viene del trabajo, sino de conversaciones pendientes.</p>
<h2>3. ¿Qué emoción se repitió más?</h2>
<p>Rabia, tristeza, ansiedad, culpa. No para juzgarla, sino para entender qué estaba protegiendo. Una emoción que se repite suele señalar una necesidad que no estás atendiendo.</p>
<h2>4. ¿Qué tres cosas de verdad quiero defender en 2027?</h2>
<p>No veinte: tres. Convierte cada una en una decisión concreta para los primeros 90 días. "Cuidar mi salud" no es una decisión; "caminar 20 minutos tres veces por semana desde el 10 de enero" sí lo es.</p>
<h2>5. ¿Cuánto de mi descanso se lo llevó la pantalla?</h2>
<p>El agotamiento digital se confunde con vacío. Revisa tu tiempo de pantalla de la última semana y elige un espacio del día que vuelva a ser tuyo, sin celular.</p>
<p>Si al responder sientes que hay más de lo que puedes ordenar solo, no es debilidad: es una señal de que vale la pena hacerlo acompañado.</p>
{CRISIS}
{VCS_CALL}
""", "vcs")

article("ludopatia-que-es-sintomas-causas-tratamiento",
 "Ludopatía: qué es, síntomas, causas y tratamiento (guía de un psicólogo)",
 "Qué es la ludopatía o juego patológico, cuáles son sus síntomas, por qué aparece, cómo se trata y cuándo buscar ayuda. Guía clara de un psicólogo.",
 "2026-11-23", f"""
<p>La ludopatía, también llamada juego patológico o trastorno por juego, es la dificultad persistente para controlar las apuestas aunque estén causando daño a la persona, a su familia o a su economía. No es un problema de voluntad ni de moral: es un trastorno reconocido en los manuales de salud mental, que comparte con otras adicciones el mismo circuito cerebral de recompensa.</p>
<h2>Síntomas principales</h2>
<ul>
<li>Necesidad de apostar cada vez más dinero para sentir la misma emoción.</li>
<li>Inquietud o irritabilidad al intentar reducir o dejar de apostar.</li>
<li>Intentos repetidos y fallidos de controlar el juego.</li>
<li>Pensar todo el tiempo en apostar: planear la próxima apuesta o cómo conseguir dinero.</li>
<li>Apostar para escapar de la tristeza, la ansiedad o los problemas.</li>
<li>Volver al día siguiente para "recuperar" lo perdido.</li>
<li>Mentir a la familia sobre el tiempo o el dinero que se apuesta.</li>
<li>Poner en riesgo el trabajo, los estudios o las relaciones.</li>
<li>Pedir dinero a otros para cubrir deudas de juego.</li>
</ul>
<p>Cuantas más de estas señales aparecen en los últimos doce meses, más probable es que exista un problema. Para una primera orientación puedes hacer el <a href="{BASE}/blog/test-ludopatia-tengo-problemas-con-el-juego/">test de autoevaluación</a>; no reemplaza una valoración profesional.</p>
<h2>¿Por qué aparece?</h2>
<p>No hay una sola causa. Influyen factores biológicos (sensibilidad del sistema de recompensa), psicológicos (impulsividad, ansiedad, depresión, búsqueda de emociones) y sociales (acceso fácil, publicidad constante, apuestas en el celular a cualquier hora, presión del grupo). Las apuestas en línea aceleran el proceso porque eliminan las pausas naturales: se puede apostar en segundos, sin salir de casa y con bonos que invitan a seguir.</p>
<h2>¿Cómo se trata?</h2>
<ul>
<li><b>Psicoterapia.</b> La terapia cognitivo-conductual es la de mejor evidencia: trabaja las creencias que mantienen el juego ("ya me toca ganar") y enseña a manejar los impulsos.</li>
<li><b>Control del acceso.</b> Autoexclusión en casinos y plataformas, bloqueo de apps y, por un tiempo, que otra persona administre el dinero.</li>
<li><b>Familia.</b> El acompañamiento familiar sin humillar mejora mucho el pronóstico; la familia también necesita orientación propia.</li>
<li><b>Grupos de apoyo</b> como Jugadores Anónimos.</li>
<li><b>Atención de lo que acompaña al juego:</b> ansiedad, depresión o consumo de alcohol, que son frecuentes.</li>
</ul>
<p>Las recaídas son parte del proceso de recuperación. Lo importante es detectarlas pronto y retomar el plan.</p>
<h2>¿Cuándo buscar ayuda?</h2>
<p>Si hay deudas que crecen, mentiras repetidas, intentos fallidos de parar o cualquier idea de no querer vivir, es momento de consultar. Aquí tienes una guía de <a href="{BASE}/blog/donde-pedir-ayuda-ludopatia-colombia/">dónde pedir ayuda en Colombia</a>.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("donde-pedir-ayuda-ludopatia-colombia",
 "¿Dónde pedir ayuda para la ludopatía en Colombia? Líneas, autoexclusión y tratamiento",
 "Guía práctica para pedir ayuda por apuestas o ludopatía en Colombia: Línea 106, EPS, autoexclusión, grupos de apoyo y qué hacer si eres familiar.",
 "2026-11-23", f"""
<p>Pedir ayuda por un problema con las apuestas da vergüenza, y por eso mucha gente espera demasiado. Esta guía reúne, en un solo lugar, los caminos concretos que existen en Colombia, tanto para la persona que apuesta como para su familia.</p>
<h2>Si es una urgencia</h2>
<p>Si hay ideas de hacerse daño o una crisis, llama a la <b>Línea 106</b> (orientación en salud mental, gratuita y confidencial, 24 horas) o al <b>123</b>. También puedes acudir a urgencias de cualquier hospital.</p>
<h2>Atención en salud mental por tu EPS</h2>
<p>Tu EPS debe ofrecer atención en salud mental. Pide cita con medicina general y explica que tienes un problema con el juego; desde ahí te remiten a psicología o psiquiatría. Llevar anotado cuánto apuestas, desde cuándo y qué intentos has hecho para parar ayuda a que te atiendan mejor.</p>
<h2>Autoexclusión y límites</h2>
<p>Los operadores legales de juego en Colombia deben ofrecer herramientas de juego responsable, como límites de depósito y autoexclusión. La autoexclusión bloquea tu cuenta por un periodo. Es una de las medidas más efectivas al inicio, porque pone distancia entre el impulso y la apuesta. Aquí explicamos <a href="{BASE}/blog/autoexclusion-apuestas-colombia/">cómo funciona la autoexclusión</a>.</p>
<h2>Grupos de apoyo</h2>
<p>Jugadores Anónimos y otros grupos de ayuda mutua ofrecen reuniones donde personas con el mismo problema comparten su proceso. Son gratuitos y complementan muy bien la terapia.</p>
<h2>Si eres familiar</h2>
<p>La familia también necesita orientación: cómo hablar sin culpa ni enfrentamientos, cómo proteger el dinero del hogar y cómo acompañar sin rescatar. Lee <a href="{BASE}/blog/como-ayudar-a-un-familiar-con-ludopatia/">cómo ayudar a un familiar con ludopatía</a>.</p>
<h2>Un primer paso hoy</h2>
<ul>
<li>Haz el <a href="{BASE}/blog/test-ludopatia-tengo-problemas-con-el-juego/">test de autoevaluación</a>.</li>
<li>Activa la autoexclusión en las plataformas que usas.</li>
<li>Cuéntale a una persona de confianza.</li>
<li>Pide la cita con tu EPS o con un psicólogo.</li>
</ul>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("agotamiento-emocional-sintomas-que-hacer",
 "Agotamiento emocional: síntomas, causas y qué hacer para recuperarte",
 "Cómo reconocer el agotamiento emocional, en qué se diferencia del cansancio normal y qué pasos concretos ayudan a recuperarte. Guía de un psicólogo.",
 "2026-11-23", f"""
<p>El agotamiento emocional es esa sensación de no tener nada más que dar, incluso después de dormir. No es pereza ni falta de carácter: es la respuesta del cuerpo y la mente a una exigencia sostenida sin suficiente recuperación. Lo viven mucho quienes cuidan a otros, quienes trabajan bajo presión y quienes están conectados todo el día.</p>
<h2>Síntomas frecuentes</h2>
<ul>
<li>Cansancio que no se va con el descanso.</li>
<li>Irritabilidad o poca paciencia con personas cercanas.</li>
<li>Sensación de distancia o indiferencia frente a lo que antes importaba.</li>
<li>Dificultad para concentrarse y olvidos.</li>
<li>Problemas de sueño, dolores de cabeza o tensión muscular.</li>
<li>Sensación de que todo es urgente y nada es tuyo.</li>
</ul>
<h2>¿De dónde viene?</h2>
<p>Suele combinar tres cosas: demandas altas (trabajo, cuidado de otros, problemas económicos), poco control sobre el propio tiempo y poca recuperación real. La hiperconexión digital agrava las tres: nunca se termina la jornada.</p>
<h2>Qué hacer: cinco pasos concretos</h2>
<ol>
<li><b>Nombra lo que te agota.</b> Haz una lista de tareas, relaciones y situaciones que más energía te quitan.</li>
<li><b>Protege un espacio diario sin pantalla.</b> Aunque sean 30 minutos.</li>
<li><b>Recupera el cuerpo.</b> Sueño regular, movimiento suave, comida a horas fijas.</li>
<li><b>Ten una conversación pendiente.</b> Muchas veces el agotamiento viene de un límite que no se ha dicho.</li>
<li><b>Elige tres decisiones para los próximos 90 días.</b> Pocas y concretas, no veinte propósitos.</li>
</ol>
<p>Si los síntomas duran varias semanas, afectan tu trabajo o tus relaciones, o aparece tristeza profunda, consulta con un profesional.</p>
{CRISIS}
{VCS_CALL}
""", "vcs")

article("programa-de-juego-responsable-resolucion-22654",
 "Programa de Juego Responsable: qué exige la Resolución 22654 de 2024 y cómo capacitar a tu equipo",
 "Resumen práctico para operadores de juegos de suerte y azar en Colombia: obligaciones, plazos, plan anual de capacitación e informe a Coljuegos.",
 "2026-11-12", f"""
<p>Desde la Resolución 22654 de 2024, todo operador de juegos de suerte y azar en Colombia debe tener un Programa de Juego Responsable documentado, con un responsable designado y un plan anual de capacitación de su personal, y debe reportarlo a Coljuegos. Esta guía resume lo que exige la norma y cómo convertir la capacitación en algo que proteja a los jugadores y a la empresa, no solo en un requisito.</p>
<h2>Qué dice la resolución, en cinco puntos</h2>
<ol>
<li><b>Programa documentado (art. 10.1).</b> Cada operador crea o ajusta su Programa de Juego Responsable y lo envía en PDF a Coljuegos. Cualquier modificación posterior debe remitirse antes de ejecutarla.</li>
<li><b>Un empleado responsable (art. 10.1, literal a).</b> La empresa designa a una persona idónea que lidera el programa.</li>
<li><b>Plan anual de capacitación (art. 10.1, literal b).</b> El programa incluye la formación del personal, que puede integrarse al cronograma de actividades, junto con las señales de advertencia y las estrategias de autocontrol que deben conocer.</li>
<li><b>Herramientas para el jugador (art. 10.2).</b> El test de identificación de factores de riesgo es la herramienta oficial y debe estar accesible; en la modalidad por internet, además, autoexclusión con registro, límites de juego definidos por el jugador y prohibición de otorgar créditos.</li>
<li><b>Informe anual (art. 11).</b> En los primeros 15 días hábiles de enero, correspondiente al año anterior. El incumplimiento puede generar multas y cláusula penal según el contrato de concesión (art. 3).</li>
</ol>
<p>El texto completo está publicado en el <a href="https://normograma.supersalud.gov.co/compilacion/docs/resolucion_coljuegos_22654_2024.htm" rel="noopener" target="_blank">normograma de la Supersalud</a>.</p>
<h2>Qué debe saber hacer tu personal</h2>
<p>La norma pide capacitación, pero no detalla el contenido. Desde la práctica clínica, un empleado de sala, un cajero o un agente de soporte de una plataforma necesita cuatro competencias:</p>
<ul>
<li><b>Reconocer señales de riesgo:</b> sesiones cada vez más largas, apuestas crecientes para "recuperar", irritabilidad al perder, préstamos entre jugadores, visitas en horarios de trabajo o de madrugada, comentarios sobre deudas o problemas familiares.</li>
<li><b>Conversar sin confrontar:</b> cómo acercarse a un jugador en problemas, qué decir y qué evitar, cómo ofrecer el test de factores de riesgo o la autoexclusión sin que se sienta acusado.</li>
<li><b>Aplicar el protocolo interno:</b> a quién reportar, cómo registrar, cómo activar límites o autoexclusión, qué hacer ante una crisis en el local o en el chat.</li>
<li><b>Derivar correctamente:</b> conocer el directorio de atención de Coljuegos y las rutas de salud mental del municipio.</li>
</ul>
<h2>Cómo organizar el plan anual</h2>
<p>Un plan defendible ante Coljuegos tiene fechas, horas, asistentes y evidencia. Una estructura que funciona: una formación base certificada para todo el personal al inicio del año (o al ingreso de cada empleado), un refuerzo corto cada trimestre con casos reales de la operación, y una sesión anual con el líder del programa para revisar indicadores: cuántos jugadores pidieron autoexclusión, cuántas situaciones se reportaron, qué falló.</p>
<p>Lo que más valoran los auditores es la trazabilidad: lista de asistencia, certificados individuales con horas, temario y nombre del formador, y un acta de la sesión. Si la formación la dicta un profesional de la salud mental, el informe gana peso.</p>
<h2>Cerrar el año a tiempo</h2>
<p>Si tu empresa aún no ejecutó la capacitación de este año, noviembre y la primera semana de diciembre son el plazo real: la formación debe quedar certificada antes de preparar el informe de enero. Una formación virtual con certificado individual permite cubrir a todo el equipo sin cerrar la operación.</p>
{LUDO_CALL}
<p class="muted">Para equipos de 5 personas o más hay descuentos por grupo, certificado individual de 60 horas, informe de asistencia y una sesión en vivo con el equipo. <a href="{wa(ludo_b2b)}">Pide la ficha técnica por WhatsApp</a>.</p>
""", "ludopatia")

article("senales-de-alerta-adiccion-al-juego-jovenes",
 "10 señales de alerta de la adicción al juego en adolescentes y adultos jóvenes",
 "Las señales tempranas de ludopatía en jóvenes, por qué las apuestas en línea los afectan más y qué pueden hacer padres y docentes.",
 "2026-11-12", f"""
<p>Las apuestas deportivas y los casinos en línea se promocionan con los ídolos de los jóvenes, con bonos de bienvenida y con la misma estética de los videojuegos. El resultado es que la edad de inicio del juego con dinero bajó y que muchos padres y docentes descubren el problema cuando ya hay deudas. Estas son las señales que vemos con más frecuencia en consulta y en orientación escolar.</p>
<h2>Las diez señales</h2>
<ol>
<li><b>Hablar de apuestas como si fuera una habilidad.</b> "Yo sí sé analizar los partidos", "tengo un método". La ilusión de control es la primera trampa del juego.</li>
<li><b>Pedir dinero con explicaciones cambiantes.</b> Para una salida, para un libro, para un amigo. Las cantidades suben y las razones no cuadran.</li>
<li><b>Vender o "perder" objetos.</b> Audífonos, consola, bicicleta, ropa. A veces reaparecen; a veces no.</li>
<li><b>Cambios de humor ligados a resultados deportivos.</b> Euforia desproporcionada o rabia tras un partido que no le importaba antes.</li>
<li><b>Celular bajo llave.</b> Pantalla hacia abajo, notificaciones apagadas, borrado frecuente de historial, cuentas en plataformas de pago que no conocías.</li>
<li><b>Desvelo y bajo rendimiento.</b> Las apuestas en vivo ocurren de noche. Llega a clase sin dormir y las notas caen sin otra explicación.</li>
<li><b>Aislamiento de los amigos de siempre.</b> Nuevas amistades "de apuestas", o ninguna.</li>
<li><b>Mentiras que no eran su estilo.</b> Mentir sobre dónde estuvo, en qué gastó, cuánto debe.</li>
<li><b>Préstamos entre compañeros o con adultos.</b> En colegios ya vemos pequeñas redes de "fiado" para apostar. Es una señal de que el problema dejó de ser individual.</li>
<li><b>Promesas de parar que duran días.</b> "Ya no más" después de una pérdida, y vuelta a empezar con el siguiente ingreso.</li>
</ol>
<h2>Por qué los jóvenes son más vulnerables</h2>
<p>La corteza prefrontal, encargada del control de impulsos y de evaluar consecuencias, madura hasta los 25 años. Un cerebro adolescente responde con más intensidad a la recompensa inmediata y menos a la pérdida futura, exactamente el diseño de una apuesta en línea. Súmale la publicidad dirigida, la facilidad de pago desde el celular y la normalización social: "todos apuestan".</p>
<h2>Qué hacer si reconoces varias señales</h2>
<p>Tres o más señales sostenidas en el tiempo justifican una conversación y, probablemente, una valoración. Evita el interrogatorio; empieza por lo observable y por tu preocupación, no por la acusación. Revisa juntos cuánto dinero ha pasado por las plataformas: la cifra real suele sorprender al propio joven. Pacta medidas de protección temporales (control del dinero, bloqueo de plataformas, autoexclusión) con fecha de revisión. Y si hay deudas, mentiras repetidas o señales de desesperanza, consulta con un profesional de salud mental.</p>
<h2>Para docentes y orientadores</h2>
<p>El colegio es el lugar donde las señales aparecen primero: sueño en clase, préstamos entre compañeros, conversaciones sobre cuotas y parlays. Un protocolo escolar sencillo (detectar, conversar, informar a la familia, derivar) y una sesión de prevención con estudiantes de bachillerato reducen el riesgo. La prevención funciona mejor cuando habla del diseño del juego y de la ilusión de control que cuando solo prohíbe.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("agotamiento-digital-que-hacer",
 "Agotamiento digital: por qué te cansa estar conectado y qué hacer esta semana",
 "Qué es el agotamiento por hiperconectividad, cómo se relaciona con la ansiedad y la atención, y cinco cambios concretos para esta semana, desde el enfoque sistémico.",
 "2026-11-12", f"""
<p>Terminas el día sin haber hecho nada físicamente exigente y, aun así, estás exhausto. Te cuesta leer más de dos párrafos, revisas el celular sin saber por qué y duermes con la sensación de haber dejado algo pendiente. Eso tiene nombre: agotamiento digital, el cansancio que produce estar disponible y estimulado todo el tiempo. No es debilidad ni falta de organización; es la respuesta normal de un cerebro al que se le pide atención fragmentada durante dieciséis horas.</p>
<h2>Qué le pasa a tu atención</h2>
<p>Cada notificación es una pequeña decisión: atender o no atender. Cientos de decisiones al día agotan el mismo recurso que usas para concentrarte, regular emociones y tomar decisiones importantes. Además, el cambio constante de tarea tiene un costo: después de cada interrupción el cerebro tarda varios minutos en recuperar el foco. El resultado es la sensación de haber trabajado todo el día sin terminar nada, y una irritabilidad que no sabes de dónde sale.</p>
<p>A esto se suma la hiperconexión social: grupos de WhatsApp de la familia, del trabajo, del colegio de los hijos; redes donde todos parecen estar mejor; correos que llegan a las diez de la noche. No es solo cantidad de pantalla: es que nunca hay un momento en que no se espere algo de ti.</p>
<h2>Cómo se relaciona con la ansiedad</h2>
<p>La disponibilidad permanente mantiene el sistema de alerta encendido. El cuerpo interpreta cada vibración como algo que podría requerir respuesta y se queda en un estado de vigilancia leve pero constante. De ahí la dificultad para dormir, la tensión muscular, la sensación de "no poder parar" incluso en vacaciones. Y como el celular también es la forma más rápida de calmar esa inquietud, se cierra un círculo: la ansiedad lleva a revisar, revisar mantiene la ansiedad.</p>
<h2>Cinco cambios para esta semana</h2>
<ol>
<li><b>Un bloque sin notificaciones cada mañana.</b> Noventa minutos, con el celular en otra habitación. No para "ser productivo": para que tu atención recuerde cómo se siente estar entera.</li>
<li><b>Hora de cierre.</b> Decide a qué hora dejas de responder mensajes de trabajo y comunícalo. La mitad del agotamiento es no saber cuándo termina el día.</li>
<li><b>Silenciar grupos, no personas.</b> Deja los grupos sin notificación y revísalos una vez al día. Si alguien te necesita, te escribe directo.</li>
<li><b>Una actividad sin pantalla que ya te gustaba.</b> Caminar, cocinar, un instrumento, una conversación larga. No es "desintoxicación", es recuperar lo que la pantalla desplazó.</li>
<li><b>Dormir sin el celular en la mesa de noche.</b> Un despertador de cinco mil pesos resuelve la excusa más común.</li>
</ol>
<h2>La mirada sistémica: no eres solo tú</h2>
<p>El agotamiento digital rara vez se resuelve con fuerza de voluntad individual, porque las reglas las pone el sistema: el jefe que escribe de noche, la familia que espera respuesta inmediata, el colegio que informa todo por grupo. Por eso los cambios que funcionan son conversaciones: con tu equipo sobre horarios de respuesta, con tu pareja sobre pantallas en la mesa, con tus hijos sobre un acuerdo que aplique a todos, adultos incluidos. Cuando el sistema cambia una regla, el esfuerzo individual deja de ser una batalla diaria.</p>
<h2>Cuándo pedir ayuda</h2>
<p>Si el cansancio viene con insomnio sostenido, pérdida de interés por cosas que disfrutabas, irritabilidad que afecta tus relaciones o la sensación de no poder parar aunque quieras, vale la pena una consulta. No tiene que ser un proceso largo: a veces bastan unas sesiones para reorganizar el sistema.</p>
<div class="callout"><b>Charla gratuita: Estrategias en la era digital</b>El lunes 30 de noviembre de 2026 a las 6 p. m. (hora Colombia) doy una conferencia online gratuita sobre agotamiento por hiperconectividad digital, con enfoque sistémico. Cupos limitados con inscripción previa.<br><a class="btn btn-primary" href="{BASE}/#charla">Inscribirme a la charla</a></div>
{VCS_CALL}
""", "vcs")

article("como-salir-del-estancamiento-personal",
 "Cómo salir del estancamiento personal con un método sistémico (sin frases motivacionales)",
 "Por qué te sientes estancado aunque cumplas con todo, y un método en cuatro pasos para decidir qué sostener, qué soltar y por dónde empezar.",
 "2026-11-12", f"""
<p>Estancamiento no es lo mismo que fracaso. La mayoría de personas que llegan a consulta sintiéndose estancadas tienen trabajo, familia, responsabilidades cumplidas. Lo que falta no es logro; es sentido: la sensación de que lo que haces va hacia algún lado que elegiste. Y la respuesta habitual, más motivación, suele empeorarlo, porque añade exigencia a un sistema que ya está saturado.</p>
<h2>Por qué el "ánimo" no funciona</h2>
<p>El estancamiento casi nunca es un problema de la persona aislada. Es un problema del sistema en el que vive: los roles que asumió, las expectativas que heredó, las conversaciones que lleva años sin tener. Puedes leer veinte libros de hábitos, pero si tu día está organizado alrededor de lo que otros necesitan y nunca te preguntaste qué quieres defender, cualquier cambio dura dos semanas. Un enfoque sistémico mira primero el mapa, después el paso.</p>
<h2>Un método en cuatro pasos</h2>
<h3>1. Mapa: dónde estás y quién está contigo</h3>
<p>Dibuja, literalmente, tu sistema: en el centro tú; alrededor, las personas, roles y compromisos que ocupan tu semana. Marca con un signo más lo que te sostiene y con un signo menos lo que te agota. La mayoría descubre dos cosas: que lo que más pesa no es lo que creía, y que hay relaciones que sostienen y no están recibiendo tiempo.</p>
<h3>2. Sentido: qué quieres defender</h3>
<p>No "qué quieres lograr" sino qué, de lo que ya tienes o haces, no estás dispuesto a perder. Suele caber en tres frases. Esas tres frases son el criterio para todas las decisiones siguientes.</p>
<h3>3. Decisiones: soltar, delegar, renegociar</h3>
<p>Con el mapa y el criterio, cada carga tiene tres salidas posibles. Soltar lo que ya no tiene sentido (una obligación autoimpuesta, un grupo, una expectativa). Delegar lo que otro puede hacer y no hace porque tú siempre lo haces. Renegociar lo que necesita una conversación pendiente: con la pareja, con el jefe, con los padres. Elige una de cada tipo para los próximos 90 días. Solo tres.</p>
<h3>4. Sostener: hábitos con sentido</h3>
<p>Un hábito dura cuando protege algo que te importa. Dormir siete horas no es un objetivo; es la condición para la paciencia que quieres tener con tus hijos. Caminar no es ejercicio; es la hora en la que piensas sin interrupciones. Ata cada hábito a una de tus tres frases y revísalo cada mes.</p>
<h2>Los errores más comunes</h2>
<ul>
<li><b>Cambiarlo todo a la vez.</b> El sistema se defiende: si mueves diez cosas, las diez vuelven a su sitio. Tres decisiones en 90 días es un ritmo que el sistema tolera.</li>
<li><b>Hacerlo solo.</b> Las decisiones que implican a otros se sostienen cuando esos otros participaron en la conversación.</li>
<li><b>Confundir descanso con desconexión.</b> Ver series hasta la madrugada no descansa; es otra forma de no decidir.</li>
</ul>
<h2>Cuándo hacerlo acompañado</h2>
<p>Si llevas más de seis meses con la misma sensación, si el estancamiento viene con tristeza persistente o si cada intento de cambio termina en culpa, hacerlo con un profesional acorta el camino. No porque no puedas solo, sino porque alguien externo ve el mapa completo y te ayuda a sostener la decisión cuando el sistema empuja de vuelta.</p>
{VCS_CALL}
""", "vcs")

article("como-dejar-de-apostar",
 "Cómo dejar de apostar: un plan de 30 días explicado por un psicólogo",
 "Si quieres dejar las apuestas y no lo logras solo, este plan de cuatro semanas te explica qué hacer con el dinero, el celular, las ganas y las recaídas.",
 "2026-11-13", f"""
<p>Si estás leyendo esto, probablemente ya intentaste parar varias veces. Borraste la aplicación, prometiste que la última apuesta era la última, y a los pocos días volviste. Eso no significa que no tengas voluntad: significa que estás usando la herramienta equivocada. La voluntad sirve para decisiones puntuales; para cambiar una conducta que el cerebro ya automatizó hacen falta condiciones, no promesas. Este plan de 30 días es el que uso en consulta con personas que quieren dejar de apostar y no saben por dónde empezar.</p>
<h2>Antes de empezar: por qué no puedes "solo parar"</h2>
<p>Cada apuesta activa el circuito de recompensa con una intensidad parecida a la de una sustancia, y lo hace de forma intermitente: a veces ganas, casi siempre pierdes, y esa incertidumbre es justo lo que más engancha. Con el tiempo el cerebro deja de apostar por placer y apuesta para calmar la ansiedad de no apostar. Por eso las ganas aparecen cuando estás aburrido, estresado, solo o con dinero en la cuenta, y por eso "recuperar lo perdido" se siente tan lógico aunque nunca funcione.</p>
<h2>Semana 1: cerrar las puertas</h2>
<ul>
<li><b>Autoexclusión en todas las plataformas donde tienes cuenta.</b> En Colombia los operadores legales están obligados a ofrecerla. Hazlo por el periodo más largo disponible, no por un mes.</li>
<li><b>Dinero fuera de tu alcance inmediato.</b> Entrega temporalmente la tarjeta a alguien de confianza, baja el cupo de retiro, cierra las billeteras digitales que usabas para apostar, y pide que tu salario llegue a una cuenta con un segundo control. Suena extremo; es lo que más protege en el primer mes.</li>
<li><b>Bloqueo técnico.</b> Aplicaciones de bloqueo de sitios de apuestas en el celular y el computador, con la contraseña en manos de otra persona.</li>
<li><b>Una persona que lo sepa.</b> Una sola, elegida por ti. Decirlo en voz alta rompe el secreto que mantiene el juego.</li>
</ul>
<h2>Semana 2: entender tus disparadores</h2>
<p>Lleva un registro simple en el celular: cada vez que sientas ganas de apostar, anota la hora, dónde estabas, qué sentías y qué pasó justo antes. A la semana verás un patrón: los partidos de la noche, el día de pago, las discusiones en casa, el aburrimiento del domingo. Para cada disparador, define de antemano una acción incompatible con apostar: salir a caminar, llamar a tu persona de confianza, ducharte, cocinar. El impulso dura entre 15 y 30 minutos; tu trabajo es atravesarlo, no vencerlo.</p>
<h2>Semana 3: hacer las cuentas y las conversaciones</h2>
<p>Esta es la semana que casi todos evitan. Suma cuánto dinero has perdido y cuánto debes. La cifra real suele ser peor de lo que creías, y aun así verla es un alivio: deja de ser un fantasma. Haz una lista de deudas por orden de urgencia y, si hay préstamos informales, busca orientación antes de pagar. Luego ten las conversaciones pendientes con las personas afectadas: sin promesas grandes, con hechos: qué hiciste en las semanas 1 y 2, qué sigues haciendo.</p>
<h2>Semana 4: construir lo que el juego desplazó</h2>
<p>El juego ocupaba horas, atención y emoción. Si no pones algo en ese espacio, vuelve. Recupera una actividad que disfrutabas antes de apostar, retoma a las personas de las que te alejaste y define una rutina de sueño: la mayoría de las recaídas ocurren de noche. Si en este punto notas que la ansiedad o la tristeza no ceden, es el momento de pedir ayuda profesional; no es un fracaso del plan, es parte del plan.</p>
<h2>Si recaes</h2>
<p>Una recaída no borra el progreso. Lo que importa es qué haces en las 24 horas siguientes: cerrar la puerta que quedó abierta, contárselo a tu persona de confianza y volver al registro de disparadores. Las personas que se recuperan no son las que nunca recaen; son las que cada vez tardan menos en volver al plan.</p>
<h2>Cuándo buscar ayuda profesional</h2>
<p>Si has apostado dinero que no tenías, has mentido para apostar, has pensado que no vale la pena seguir, o llevas más de dos intentos serios sin lograrlo, consulta con un psicólogo con experiencia en adicciones. El tratamiento del juego problemático tiene buena evidencia y suele ser más corto de lo que la gente imagina.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("autoexclusion-apuestas-colombia",
 "Autoexclusión de apuestas en Colombia: cómo activarla y qué hacer para que funcione",
 "Qué es la autoexclusión, qué obliga la Resolución 22654 a los operadores, cómo pedirla en plataformas en línea y en salas, y por qué sola no basta.",
 "2026-11-13", f"""
<p>La autoexclusión es el acuerdo por el que tú mismo pides a un operador de juego que te impida apostar durante un tiempo. Es la herramienta más rápida para cortar el acceso, y en Colombia los operadores legales están obligados a ofrecerla. Esta guía explica cómo pedirla y, sobre todo, cómo hacer que sirva, porque la autoexclusión sola rara vez resuelve el problema.</p>
<h2>Qué obliga la norma</h2>
<p>La Resolución 22654 de 2024 de Coljuegos exige que los operadores tengan un Programa de Juego Responsable con herramientas para el jugador: el test de identificación de factores de riesgo, y, en la modalidad por internet, autoexclusión con registro, límites de juego definidos por el propio jugador y prohibición de otorgar créditos. El texto está en el <a href="https://normograma.supersalud.gov.co/compilacion/docs/resolucion_coljuegos_22654_2024.htm" target="_blank" rel="noopener">normograma de la Supersalud</a>. Si una plataforma legal no te ofrece la opción o te la dificulta, puedes reportarlo a Coljuegos.</p>
<h2>Cómo pedirla en plataformas en línea</h2>
<ol>
<li>Entra a tu cuenta y busca en el perfil o en la sección de "Juego responsable" las opciones de autoexclusión o límites.</li>
<li>Elige el periodo más largo que ofrezcan. Seis meses o un año protegen más que treinta días; el impulso de "reabrir" aparece justo cuando vence el plazo corto.</li>
<li>Si no encuentras la opción, escribe al soporte con el asunto "Solicitud de autoexclusión" y pide confirmación por escrito. Guarda esa respuesta.</li>
<li>Repite el proceso en cada plataforma donde tengas cuenta, incluidas las que "ya no usas".</li>
<li>Retira el dinero que quede en las cuentas antes de cerrarlas, o pide que lo transfieran.</li>
</ol>
<h2>En casinos y salas de máquinas</h2>
<p>Pide hablar con el responsable del Programa de Juego Responsable del local. Debe existir por norma. Solicita por escrito que no te permitan el ingreso durante el periodo que definas y pregunta cómo lo registran. Si frecuentas varias salas, hazlo en cada una.</p>
<h2>Por qué la autoexclusión sola no basta</h2>
<p>Cierra una puerta, pero no cambia las condiciones que te llevaban a esa puerta: el dinero disponible, el celular siempre a la mano, el aburrimiento, la angustia por las deudas. En la práctica vemos tres fallas frecuentes: abrir una cuenta en otra plataforma (muchas veces ilegal, sin ninguna protección), apostar a través de la cuenta de otra persona, o esperar a que venza el plazo. Por eso conviene combinarla con control del dinero, bloqueo técnico de sitios y una persona de confianza que lo sepa. Si quieres un plan completo, lee <a href="{BASE}/blog/como-dejar-de-apostar/">cómo dejar de apostar en 30 días</a>.</p>
<h2>Para familiares</h2>
<p>No puedes pedir la autoexclusión por otra persona: debe hacerlo ella. Lo que sí puedes es acompañar el proceso, ayudar a hacer la lista de plataformas y estar presente cuando la solicite. Si tu familiar no quiere hacerlo, el camino es la conversación, no la presión; aquí tienes una <a href="{BASE}/blog/como-ayudar-a-un-familiar-con-ludopatia/">guía para hablar con un familiar que apuesta</a>.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

article("test-ludopatia-tengo-problemas-con-el-juego",
 "¿Tengo problemas con el juego? Las 9 preguntas que usan los psicólogos",
 "Un autotest breve basado en los criterios clínicos del juego patológico, cómo interpretar el resultado y qué hacer según tu puntaje.",
 "2026-11-13", f"""
<p>La mayoría de personas con juego problemático pasan años diciéndose que lo tienen bajo control. Este autotest no diagnostica, pero sí te dice con honestidad en qué punto estás. Está construido sobre los criterios que usan los manuales clínicos para el juego patológico, traducidos a preguntas sobre los últimos 12 meses. Responde sí o no, sin negociar contigo mismo.</p>
<h2>Las nueve preguntas</h2>
<ol>
<li>¿Has necesitado apostar cantidades cada vez mayores para sentir la misma emoción?</li>
<li>¿Te has sentido inquieto o irritable cuando intentaste reducir o dejar de apostar?</li>
<li>¿Has intentado controlar, reducir o dejar el juego sin lograrlo, más de una vez?</li>
<li>¿Pasas mucho tiempo pensando en apuestas pasadas, planeando las siguientes o buscando dinero para apostar?</li>
<li>¿Apuestas cuando te sientes angustiado, culpable, ansioso, triste o aburrido?</li>
<li>¿Después de perder, vuelves otro día para intentar recuperar lo perdido?</li>
<li>¿Has mentido a tu familia, pareja o amigos sobre cuánto apuestas o cuánto has perdido?</li>
<li>¿El juego ha puesto en riesgo o te ha hecho perder una relación, un empleo, una oportunidad de estudio o dinero que no era tuyo?</li>
<li>¿Has pedido dinero a otros para resolver problemas económicos causados por las apuestas?</li>
</ol>
<h2>Cómo leer tu resultado</h2>
<ul>
<li><b>0 a 1 respuestas afirmativas:</b> juego recreativo o de bajo riesgo. Aun así, si apuestas en línea con frecuencia, pon límites de depósito: el diseño de las plataformas está hecho para que el riesgo suba sin que lo notes.</li>
<li><b>2 a 3:</b> juego de riesgo. Es el momento ideal para intervenir, porque el patrón todavía no se ha consolidado. Activa límites, reduce el acceso y revisa qué estás buscando cuando apuestas.</li>
<li><b>4 o más:</b> patrón compatible con juego problemático. No es una etiqueta para avergonzarte: es información. Lo que sigue es cerrar accesos (autoexclusión, control del dinero) y hablar con un profesional de salud mental.</li>
</ul>
<h2>Lo que el test no te dice</h2>
<p>Un puntaje alto no describe quién eres; describe una conducta que se puede cambiar, y que cambia con tratamiento en la mayoría de los casos. Un puntaje bajo tampoco es un permiso: si alguien que te quiere está preocupado por tus apuestas, esa preocupación cuenta como una respuesta afirmativa más.</p>
<h2>Qué hacer hoy</h2>
<p>Si sacaste 2 o más, lee <a href="{BASE}/blog/como-dejar-de-apostar/">el plan de 30 días para dejar de apostar</a> y <a href="{BASE}/blog/autoexclusion-apuestas-colombia/">cómo activar la autoexclusión en Colombia</a>. Si prefieres hablarlo con alguien, puedes escribirme por WhatsApp y te oriento sobre el paso siguiente.</p>
{CRISIS}
{LUDO_CALL}
""", "ludopatia")

# ---------------------------------------------------------------- AFILIADOS
afil_body = f"""
<section class="hero"><div class="wrap narrow">
  <p class="eyebrow">Programa de afiliados en Hotmart</p>
  <h1 style="margin-top:18px">Gana hasta el 50 % recomendando cursos de salud mental <em>dictados por un psicólogo</em>.</h1>
  <p class="lead" style="margin-top:22px">Si tienes una audiencia de psicología, educación, desarrollo personal, familia o finanzas personales, puedes promover estos dos cursos con tu enlace de Hotmart. Hotmart paga la comisión de forma automática por cada venta confirmada; tú no manejas cobros ni soporte.</p>
  <ul class="cards">
    <li class="card"><b>Vida Con-Sentido · 50 %</b><span>Programa de bienestar psicológico de 24 horas (120.000 COP). Audiencias de bienestar, productividad, maternidad/paternidad y crecimiento personal.</span><br><a class="btn btn-accent" style="margin-top:16px" href="https://affiliate.hotmart.com/affiliate-recruiting/view/0339V108443801" target="_blank" rel="noopener">Afiliarme en Hotmart</a></li>
    <li class="card"><b>Curso de ludopatía · 60 %</b><span>Formación certificada de 60 horas (260.000 COP). Audiencias de psicología, trabajo social, adicciones, educación y finanzas personales; también empresas de juego.</span><br><a class="btn btn-primary" style="margin-top:16px" href="https://go.hotmart.com/X108428929J" target="_blank" rel="noopener">Ver el curso en Hotmart</a></li>
  </ul>
  <h2 style="font-size:1.6rem">Qué recibes como afiliado</h2>
  <ul>
    <li>Atribución por último clic, sin caducidad: si tu referido compra meses después, la comisión es tuya.</li>
    <li>Banners, textos para historias y correos, y un video de presentación del docente.</li>
    <li>Bono automático para tus compradores (guía descargable), que mejora tu conversión.</li>
    <li>Acceso gratuito al curso para conocerlo antes de promocionarlo, a los primeros 10 afiliados activos.</li>
    <li>Para ventas corporativas de 5 cupos o más, la comisión se paga sobre el total.</li>
  </ul>
  <h2 style="font-size:1.6rem">Reglas</h2>
  <p>Presenta los cursos como formación psicoeducativa, nunca como terapia ni con promesas de curación. Sin spam, sin testimonios inventados, sin anuncios dirigidos a menores ni junto a casas de apuestas, sin imágenes de fichas o tragamonedas. Las afiliaciones que incumplan se cancelan.</p>
  <p style="margin-top:28px"><a class="btn btn-ghost" href="{wa('Hola Fredy, quiero ser afiliado de tus cursos en Hotmart y recibir los materiales.')}">Pedir materiales y acceso por WhatsApp</a></p>
</div></section>
"""
PAGES.append(page("afiliados", "Programa de afiliados · Cursos de salud mental en Hotmart · Fredy Moreno",
    "Gana hasta el 60 % por recomendar cursos de salud mental dictados por un psicólogo: Vida Con-Sentido y el curso certificado de ludopatía. Afiliación por Hotmart.", afil_body))

# ---------------------------------------------------------------- CONCURSO DOCENTE ORIENTADOR
CON_MSG = "Hola Fredy, quiero postularme a uno de los 5 cupos de evaluador del curso Concursa (concurso de docente orientador)."
con_ld = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Course","name":"Concursa: preparación para el concurso de docente orientador","description":"Curso online de 120 horas con certificado para preparar el concurso de ingreso a la carrera docente en el cargo de docente orientador en Colombia.","inLanguage":"es","provider":{"@type":"Person","name":"Fredy Moreno Quintero","jobTitle":"Psicólogo y docente orientador"},"offers":{"@type":"Offer","price":"80000","priceCurrency":"COP","category":"Paid"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","courseWorkload":"PT120H"}}</script>"""
con_body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="eyebrow">Concurso docente 2026–2027 · Docente orientador</p>
    <h1 style="margin-top:16px">Prepárate para el concurso de <em>docente orientador</em> con quien ya hace el trabajo.</h1>
    <p class="lead">Las inscripciones del concurso docente se esperan entre enero y febrero de 2027 y la prueba escrita en el segundo semestre de 2027, con más de 28.000 vacantes que incluyen docentes orientadores. Quien empieza a estudiar ahora llega con ventaja.</p>
    <ul class="facts"><li>120 horas certificadas</li><li>Plataforma en línea y app</li><li>Dictado por un docente orientador en ejercicio</li><li>A tu ritmo</li></ul>
  </div>
  <aside class="offer" aria-label="Cupos fundadores">
    <div class="offer-body">
      <span class="flag">5 cupos para evaluadores fundadores</span>
      <div class="price"><s>80.000</s> 2.400 <span class="cur">COP</span></div>
      <p class="price-sub">Buscamos 5 aspirantes al concurso que tomen el curso completo con 97 % de descuento (2.400 COP, el mínimo que permite la plataforma de pago) y, al terminar, lo evalúen con un formulario corto y una opinión honesta.</p>
      <div class="offer-ctas"><a class="btn btn-accent btn-lg" href="{wa(CON_MSG)}">Postularme como evaluador</a></div>
      <p class="offer-note">Postúlate por WhatsApp y te enviamos tu código personal. Cuando se completen los 5 cupos, el curso sigue a su precio normal de 80.000 COP.</p>
    </div>
  </aside>
</div></section>
<section class="section tint"><div class="wrap narrow">
  <h2 style="margin-top:0">¿Qué hace un docente orientador y por qué es un cargo distinto?</h2>
  <p>El docente orientador pertenece a la planta docente, pero su trabajo no es dictar una asignatura: acompaña el bienestar, la convivencia y el desarrollo integral de los estudiantes, articula las rutas de atención con familias e instituciones y apoya la orientación vocacional. Por eso la prueba y la entrevista exigen dominar normas, protocolos y casos reales de convivencia escolar.</p>
  <h2>Lo que necesitas preparar</h2>
  <ul>
    <li><b>Marco normativo:</b> convivencia escolar, rutas de atención integral, protección de niños, niñas y adolescentes.</li>
    <li><b>Funciones del docente orientador</b> y su relación con el comité de convivencia, la familia y las entidades externas.</li>
    <li><b>Casos y situaciones:</b> cómo responder preguntas de análisis de caso, que son las que más pesan.</li>
    <li><b>Competencias socioemocionales</b> y orientación vocacional.</li>
    <li><b>Estrategia de prueba:</b> lectura de enunciados, descarte de opciones y manejo del tiempo.</li>
  </ul>
  <h2>Requisitos generales del concurso</h2>
  <p>Ser ciudadano colombiano sin inhabilidades y tener título de licenciado o de otra profesión con formación pedagógica (por ejemplo, 100 horas de pedagogía o 4 créditos universitarios en pedagogía). Los títulos exactos para cada cargo se publican en la Oferta Pública de Empleos de Carrera (OPEC) de la CNSC; revisa siempre la convocatoria oficial.</p>
  <h2>Cupos gratuitos para evaluadores fundadores</h2>
  <p>Antes de abrir el curso al público queremos que lo prueben personas que de verdad se están preparando para el concurso. Por eso ofrecemos <b>5 cupos con 97 % de descuento</b>: pagas 2.400 COP en lugar de 80.000, el mínimo que permite la plataforma de pago.</p>
  <ul>
    <li><b>Qué recibes:</b> acceso completo al curso de 120 horas, a la plataforma en línea y a la app, y el certificado al terminar.</li>
    <li><b>Qué te pedimos:</b> terminar el curso y, al final, responder un formulario de evaluación (contenido, claridad, utilidad para la prueba) y dejar una opinión honesta, positiva o negativa.</li>
    <li><b>Quién puede postularse:</b> aspirantes al cargo de docente orientador (psicólogos, psicopedagogos, trabajadores sociales, licenciados con énfasis en orientación u otros perfiles afines).</li>
    <li><b>Cómo se eligen:</b> por orden de postulación y perfil, hasta completar los 5 cupos.</li>
  </ul>
  <div class="callout"><b>5 cupos para evaluadores: 2.400 COP</b>Curso de 120 horas con certificado, a cambio de tu evaluación honesta al terminar.<br><a class="btn btn-primary" href="{wa(CON_MSG)}">Postularme por WhatsApp</a></div>
  <p class="muted">Fechas tomadas de noticias de septiembre de 2026 (RCN Radio, RTVC); el cronograma oficial lo publica la CNSC.</p>
</div></section>
"""
PAGES.append(page("concurso-docente-orientador", "Concurso docente orientador 2027: qué estudiar y curso de preparación · Fredy Moreno",
    "Prepara el concurso de docente orientador: fechas esperadas, qué estudiar y curso de 120 horas con certificado. 5 cupos para evaluadores con 97 % de descuento.", con_body, "website", None, con_ld, CON_MSG))

# render articles
for a in ARTICLES:
    url = f"{BASE}/blog/{a['slug']}/"
    ld = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":%s,"description":%s,"datePublished":"%s","inLanguage":"es","author":{"@type":"Person","name":"Fredy Moreno Quintero","jobTitle":"Psicólogo","url":"%s/"},"mainEntityOfPage":"%s","image":"%s/og-image.jpg"}</script>""" % (
        __import__("json").dumps(a["title"], ensure_ascii=False), __import__("json").dumps(a["desc"], ensure_ascii=False), a["date"], BASE, url, BASE)
    d = datetime.date.fromisoformat(a["date"])
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    body = f"""
<article class="article"><div class="wrap narrow">
  <p class="eyebrow">Artículo · {"Ludopatía" if a['course']=='ludopatia' else "Bienestar"}</p>
  <h1 style="margin-top:16px">{html.escape(a['title'])}</h1>
  <p class="meta">Por Fredy Moreno Quintero, psicólogo · {d.day} de {meses[d.month-1]} de {d.year} · {max(4, len(re.sub('<[^>]+>','',a['body']).split())//200)} min de lectura</p>
  <div class="body">{a['body']}</div>
  <p class="muted" style="margin-top:40px"><a href="{BASE}/blog/">← Más artículos</a></p>
</div></article>
"""
    page(f"blog/{a['slug']}", a["title"] + " · Fredy Moreno, psicólogo", a["desc"], body, "article", None, ld)
    PAGES.append(url)

# blog index
items = "".join(f"""<li><a href="{BASE}/blog/{a['slug']}/">{html.escape(a['title'])}</a><p>{html.escape(a['desc'])}</p></li>""" for a in ARTICLES)
blog_body = f"""
<section class="section"><div class="wrap narrow">
  <p class="eyebrow">Artículos</p>
  <h1 style="margin-top:16px;font-size:clamp(2rem,4vw,3rem)">Salud mental, aprendizaje y familia, <em>en contexto</em>.</h1>
  <p class="lead" style="margin-top:18px">Herramientas prácticas y reflexiones desde el enfoque sistémico, escritas por un psicólogo.</p>
  <ul class="post-list">{items}</ul>
</div></section>
"""
PAGES.append(page("blog", "Artículos sobre salud mental, ludopatía y bienestar · Fredy Moreno, psicólogo",
    "Artículos de un psicólogo con enfoque sistémico: ludopatía, agotamiento digital, bienestar emocional y familia.", blog_body))


# FAQPage schema para páginas de curso
import json as _json
for _p in ["ludopatia", "vida-con-sentido"]:
    _f = os.path.join(ROOT, _p, "index.html"); _h = open(_f, encoding="utf-8").read()
    _qs = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", _h, re.S)
    if _qs:
        _ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":re.sub("<[^>]+>","",q),"acceptedAnswer":{"@type":"Answer","text":re.sub("<[^>]+>","",a)}} for q,a in _qs]}
        _h = _h.replace("</head>", '<script type="application/ld+json">'+_json.dumps(_ld, ensure_ascii=False)+"</script>\n</head>", 1)
        open(_f, "w", encoding="utf-8").write(_h)

# sitemap + robots
urls = [f"{BASE}/", f"{BASE}/diplomado/"] + PAGES
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("\n".join(urls))
