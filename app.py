import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IA en el Trabajo",
    page_icon="🤖",
    layout="wide"
)

# ---- ESTILOS CSS PARA DISEÑO MINIMALISTA ----
st.markdown("""
<style>

.titulo{
    font-size:36px;
    font-weight:700;
}

.frase{
    text-align:right;
    font-style:italic;
    font-size:18px;
    margin-bottom:20px;
}

.articulo{
    background-color:#f9f9f9;
    padding:30px;
    border-radius:18px;
    border:1px solid #e0e0e0;
    line-height:1.6;
}

.subtitulo{
    font-size:22px;
    font-weight:600;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)


# ---- TITULO ----
st.markdown(
    '<div class="titulo">El Robot que te Entrevista: Luces y Sombras de la IA en el Trabajo</div>',
    unsafe_allow_html=True
)

# ---- FRASE MOTIVADORA ----
st.markdown(
    '<div class="frase">"El futuro del trabajo no es humanos contra máquinas, sino humanos con propósito liderando la evolución digital."</div>',
    unsafe_allow_html=True
)

# ---- ARTICULO ----
articulo = """
<div class="articulo">

<h3>El Robot que te Entrevista: Luces y Sombras de la IA en el Trabajo</h3>

Imagina que aplicas al trabajo de tus sueños. Envías tu currículum y, en cuestión de segundos, una "mente" digital decide si eres apto o no. 
No hubo una persona leyendo tus logros; fue un algoritmo. Esta escena, que parece de ciencia ficción, es hoy la realidad de miles de 
empresas que utilizan la Inteligencia Artificial (IA) para gestionar su talento humano.

Pero, ¿qué significa realmente que una máquina decida quién obtiene un empleo? A continuación, exploramos los beneficios y los dilemas éticos de esta revolución tecnológica.

<p class="subtitulo">¿Qué es la IA en la oficina?</p>

En términos sencillos, la IA en el mundo laboral es un conjunto de programas diseñados para aprender y tomar decisiones de forma similar 
a como lo haríamos nosotros, pero a una escala masiva. Mientras que un reclutador humano tardaría semanas en revisar mil solicitudes, 
la IA lo hace en segundos, identificando patrones y habilidades que a veces pasan desapercibidos.

<p class="subtitulo">De la entrevista clásica al análisis de datos</p>

Antes, la selección dependía de una charla frente a frente. Hoy, la IA permite realizar entrevistas asistidas por video, donde un 
programa analiza no solo tus palabras, sino también tus gestos y tono de voz para entender tu personalidad. El objetivo es encontrar 
el "ajuste perfecto" entre la persona y el puesto.

<p class="subtitulo">El factor humano: ¿Nos sentimos "deshumanizados"?</p>

Aquí es donde la psicología entra en juego. Muchos candidatos sienten que ser evaluados exclusivamente por una máquina es frío o injusto. 
Esta sensación de deshumanización puede generar estrés y una percepción de falta de equidad.

<p class="subtitulo">El dilema de los espejos: Sesgos y ética</p>

Uno de los mayores riesgos es el sesgo algorítmico. Las máquinas aprenden de datos del pasado. Si en el pasado una empresa solo contrataba 
a hombres para ciertos puestos, la IA podría aprender erróneamente que los hombres son mejores para ese cargo y excluir a mujeres talentosas.

<p class="subtitulo">El futuro: colaboración, no sustitución</p>

La solución no es prohibir la tecnología, sino usarla con sabiduría. Los expertos sugieren un enfoque de "humano al mando". 
Esto significa que la IA haga el trabajo pesado de organizar datos, pero que la decisión final siga en manos de personas capacitadas.

</div>
"""

st.markdown(articulo, unsafe_allow_html=True)


# ---- BASE DE DATOS DE ARTÍCULOS Y RESÚMENES ----

articulos = {

"AI Decision Making with Dignity? Contrasting Workers’ Justice Perceptions":
"Analiza cómo los empleados perciben la justicia cuando las decisiones de recursos humanos son tomadas por IA frente a cuando son tomadas por humanos.",

"SA Journal of Human Resource Management":
"Revisión sistemática sobre la participación de los empleados en procesos de recursos humanos impulsados por inteligencia artificial y los desafíos éticos asociados.",

"Artificial Intelligence in Personnel Selection":
"Revisión de literatura desde la psicología organizacional sobre el uso de IA en la selección de personal, incluyendo entrevistas automatizadas y análisis de currículos.",

"AI-driven HR practices and employee well-being":
"Examina cómo las prácticas de recursos humanos basadas en IA influyen en el bienestar de los empleados mediante el compromiso laboral.",

"Improving Psychological Empowerment with AI":
"Estudia cómo el uso de redes neuronales y sistemas de IA puede mejorar el empoderamiento psicológico y el rendimiento laboral.",

"Ethics of AI-Enabled Recruiting":
"Revisión centrada en los riesgos éticos del reclutamiento con IA, incluyendo sesgos algorítmicos, privacidad y transparencia.",

"Reducing AI Bias in Recruitment":
"Propone enfoques teóricos para reducir el sesgo algorítmico en los procesos de contratación y mejorar la equidad.",

"Candidate Experiences in AI-Driven Recruitment":
"Estudio que explora cómo los candidatos perciben la selección basada en algoritmos, revelando sensaciones de opacidad y deshumanización.",

"Ethical Implications of AI in Hiring":
"Analiza las implicaciones éticas del uso de inteligencia artificial en decisiones organizacionales como contratación y promoción."

}


# ---- SELECTOR DESPLEGABLE ----
st.markdown("## Explorar investigaciones relacionadas")

seleccion = st.selectbox(
    "Selecciona un artículo",
    list(articulos.keys())
)

# ---- MOSTRAR RESUMEN ----
st.info(articulos[seleccion])
