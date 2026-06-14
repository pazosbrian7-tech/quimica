

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import plotly.express as px
# from rdkit import Chem
# from rdkit.Chem import Draw

import os

st.set_page_config(
    page_title="Química Orgánica Interactive",
    page_icon="🧪",
    layout="wide"
)

os.makedirs("database", exist_ok=True)

conexion = sqlite3.connect("database/quimica.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS progreso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modulo TEXT,
    puntos INTEGER
)
""")
conexion.commit()
conexion.close()

# =====================================================
# 💾 FUNCIÓN PARA GUARDAR PUNTOS
# =====================================================

def guardar_puntos(modulo, puntos):

    conexion = sqlite3.connect("database/quimica.db")

    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO progreso (modulo, puntos) VALUES (?, ?)",
        (modulo, puntos)
    )

    conexion.commit()
    conexion.close()
     # =====================================================
# CONFIGURACIÓN
# =====================================================

st.markdown("""
<style>

/* TÍTULO PRINCIPAL */

h1 {
    color: #000814 !important;
    text-align: center;
    font-size: 80px !important;
    font-weight: 1000 !important;
    letter-spacing: -2px;
    text-shadow:
        0px 2px 0px rgba(0,0,0,0.15),
        0px 4px 10px rgba(0,0,0,0.10);
    margin-bottom: 25px !important;
}

.stApp {
    background: #F8FAFC;
    color: #0F172A;
}

p, li, span, div, label {
    color: #0F172A !important;
    font-size: 17px;
    font-weight: 500;
}

h1 {
    color: #020617 !important;
    text-align: center;
    font-size: 65px !important;
    font-weight: 900;
}

h2 {
    color: #020617 !important;
    font-weight: 900;
}

h3 {
    color: #0F172A !important;
    font-weight: 800;
}

.nav-link.active {
    background: linear-gradient(90deg, #22C55E, #38BDF8) !important;
    color: white !important;
    font-weight: 900 !important;
    border-left: 8px solid #FDE047 !important;
    box-shadow: 0px 0px 14px rgba(34,197,94,0.45);
    border-radius: 14px !important;
}

.card {
    padding: 24px;
    border-radius: 22px;
    background: #FFFFFF;
    border: 2px solid #BAE6FD;
    box-shadow: 0px 8px 20px rgba(15,23,42,0.10);
}

section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 2px solid #BAE6FD;
}
 /* =====================================================
💛 CUADROS AMARILLO CLARO
===================================================== */

.card{
    background: #FFFDE7 !important;
    border: 2px solid #FDE68A !important;
    color: #0F172A !important;
}

div[data-testid="stAlert"]{
    background: #FFFDE7 !important;
    color: #0F172A !important;
}

.stInfo,
.stSuccess,
.stWarning,
.stError{
    background: #FFFDE7 !important;
    color: #0F172A !important;
}
</style>
""", unsafe_allow_html=True)
 
# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    selected = option_menu(
        menu_title="🧪 MENÚ",
        options=[
            "Inicio",
            "Teoría",
            "Mecanismos",
            "Ejercicios",
            "Quiz",
            "Laboratorio",
        ],
        icons=[
            "house",
            "book",
            "diagram-3",
            "beaker",
            "patch-question",
            "flask",
        ],
        default_index=0
    )

 # =====================================================
# INICIO
# =====================================================
if selected == "Inicio":

    st.markdown("""
    <div style="
    text-align:center;
    font-size:60px;
    font-weight:1000;
    color:#020617;
    margin-top:20px;
    margin-bottom:40px;
    text-shadow:0px 0px 10px rgba(245,158,11,0.20);
    ">
    🧪 Reacciones de Adición y Sustitución en Compuestos del Carbono
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-card">
        <p class="creator">Creador: Andrade Pazos Bryan</p>
        <p>
        Plataforma interactiva para estudiar de forma visual,
        ordenada y dinámica las principales reacciones orgánicas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">
        <h2>⚡ Adición</h2>
        <p>
        Reacciones donde se agregan átomos o grupos a una molécula.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h2>🔄 Sustitución</h2>
        <p>
        Reacciones donde un átomo o grupo es reemplazado por otro.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">
        <h2>🧬 Mecanismos</h2>
        <p>
        Observa paso a paso cómo se rompen y se forman enlaces durante cada reacción.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>📌 ¿Qué encontrarás en esta plataforma?</h2>

    📘 Teoría clara y estructurada<br><br>

    🧬 Mecanismos orgánicos paso a paso<br><br>

    🧪 Ejercicios interactivos<br><br>

    📝 Quiz de evaluación<br><br>

    ⚗️ Laboratorio virtual

    </div>
    """, unsafe_allow_html=True)
 # =====================================================
# TEORÍA PARA PREPARATORIA (Estructurada y Visual)
# =====================================================

elif selected == "Teoría":

    # Estilos CSS para tarjetas, badges y diseño moderno
    st.markdown("""
    <style>
        .prep-card {
            background-color: #f8f9fa;
            border-left: 5px solid #3498DB;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 12px;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
        }
        .card-title {
            font-weight: bold;
            color: #2C3E50;
            font-size: 15px;
            margin-bottom: 5px;
        }
        .badge-tipo {
            background-color: #E3F2FD;
            color: #1565C0;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 13px;
            display: inline-block;
        }
       .esquema-text {
            background-color: #23272E7;
            color: #82AAFF;
            font-family: monospace;
            padding: 10px;
            border-radius: 5px;
            line-height: 1.2;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("📘 REACCIONES ORGÁNICAS: GUÍA INTERACTIVA")
    st.markdown("Aprende los mecanismos del carbono de forma visual, estructurada y sin tecnicismos aburridos.")

    tipo_reaccion = st.selectbox(
        "Selecciona el tipo de reacción que deseas estudiar",
        [
            "Reacciones de Adición",
            "Reacciones de Sustitución"
        ]
    )

    # =================================================
    # BLOQUE 1: REACCIONES DE ADICIÓN
    # =================================================
    if tipo_reaccion == "Reacciones de Adición":

        reaccion = st.selectbox(
            "Selecciona una reacción de adición",
            [
                "Hidrogenación",
                "Halogenación",
                "Hidratación",
                "Adición de HX",
                "Hidroboración"
            ]
        )

        # 1. HIDROGENACIÓN
        if reaccion == "Hidrogenación":
            st.header("⚡ HIDROGENACIÓN")
            st.markdown('<span class="badge-tipo">Añadir Hidrógenos (H₂)</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es como ponerle un 'parche' de hidrógenos a una molécula que tiene un doble enlace para volverla una molécula más simple y pesada.")
                st.subheader("📖 Definición")
                st.write("Es una reacción donde se rompe el doble enlace de un Alqueno al reaccionar con gas Hidrógeno ($H_2$). Ambos hidrógenos se pegan por el mismo lado de la molécula, transformándola en un Alcano saturado.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Necesita ayuda:** El hidrógeno es muy flojo, así que requiere un metal como Platino (Pt), Paladio (Pd) o Níquel (Ni) para reaccionar.")
                st.write("• **Libera calor:** Es una reacción que genera calor (exotérmica).")
                st.write("• **Geometría Sin:** Los dos hidrógenos entran al mismo tiempo por la misma cara de la molécula.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_2=CH_2 + H_2 \xrightarrow{Pt} CH_3-CH_3")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Paso a Paso de la Adición:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info("**1. Inicio (Alqueno)**")
                    st.latex(r"H_2C = CH_2")
                    st.caption("Doble enlace con alta densidad de electrones.")
                with col2:
                    st.warning("**2. Intermediario**")
                    st.latex(r"H-H \xrightarrow{Metal} H\cdot \quad \cdot H")
                    st.caption("El platino debilita y rompe el enlace H-H gaseoso.")
                with col3:
                    st.success("**3. Final (Alcano)**")
                    st.latex(r"H_3C - CH_3")
                    st.caption("Los hidrógenos se unen saturando los carbonos.")

                st.subheader("🗺️ Esquema Visual del Mecanismo (Adición SIN)")
                st.markdown("""
                <div class="esquema-text">
                H — H  (Gas Hidrógeno)<br>
                ⬇   ⬇  (Se asientan en el catalizador de Platino)<br>
                =================== [ Metal Pt ]<br>
                ⬆   ⬆<br>
                CH₂ ═ CH₂ (Alqueno abre su doble enlace)<br>
                <br>
                🔬 <b>Resultado:</b> CH₃ — CH₃ (Los dos hidrógenos entraron por abajo)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🍔 Industria de Alimentos</div>
                    <p>Se usa para convertir aceites vegetales líquidos en mantecas sólidas o margarinas comerciales.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("La hidrogenación industrial genera **grasas trans** si el proceso es incompleto, lo cual daña la salud humana. En el ambiente, la minería para extraer los catalizadores metálicos (como el Níquel o Platino) provoca contaminación del suelo y del agua.")

        # 2. HALOGENACIÓN
        elif reaccion == "Halogenación":
            st.header("⚡ HALOGENACIÓN")
            st.markdown('<span class="badge-tipo">Añadir Halógenos (Cl₂ o Br₂)</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es meterle cloro o bromo a un compuesto con doble enlace para crear una sustancia fuertemente enlazada.")
                st.subheader("📖 Definición")
                st.write("Reacción química donde un Alqueno rompe su enlace doble para unirse con dos átomos de un halógeno diatómico ($Cl_2$ o $Br_2$). Al final, cada carbono se queda con un halógeno.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Ataque por la espalda:** Como los halógenos son muy grandes y se estorban, entran por lados opuestos de la molécula (adición Anti).")
                st.write("• **No requiere catalizador:** El Cloro y el Bromo son muy reactivos y entran solitos a temperatura ambiente.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_2=CH_2 + Br_2 \rightarrow Br-CH_2-CH_2-Br")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Paso a Paso de la Adición:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info("**1. Reactivos**")
                    st.latex(r"H_2C=CH_2 + Br-Br")
                    st.caption("El bromo se aproxima a la nube electrónica del alqueno.")
                with col2:
                    st.warning("**2. Ion Halonio**")
                    st.latex(r"[\text{Puente } Br^+]")
                    st.caption("Un Br forma un ciclo temporal bloqueando ese lado.")
                with col3:
                    st.success("**3. Ataque Anti**")
                    st.latex(r"Br-CH_2-CH_2-Br")
                    st.caption("El segundo Br⁻ entra obligatoriamente por el lado opuesto.")

                st.subheader("🗺️ Esquema Visual del Mecanismo (Adición ANTI)")
                st.markdown("""
                <div class="esquema-text">
                       ⬇ [Br] (Primer Bromo ataca por arriba)<br>
                      /     \<br>
                   CH₂ ── CH₂   (Se forma un puente temporal)<br>
                       ⬆<br>
                     [Br⁻] (El segundo Bromo es pateado y ataca por la ESPALDA)<br>
                <br>
                🔬 <b>Resultado:</b> Br-CH₂-CH₂-Br (Quedan en lados opuestos trans)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🧱 Plásticos de PVC</div>
                    <p>La cloración del eteno es el primer paso en las fábricas para crear los tubos de plástico PVC que usas en las cañerías de agua.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("Los compuestos orgánicos con cloro o bromo son **altamente contaminantes**. Many of them do not degrade easily in nature (son bioacumulables) y si se queman plásticos como el PVC sueltan gases ácidos tóxicos para la atmósfera.")

        # 3. HIDRATACIÓN
        elif reaccion == "Hidratación":
            st.header("💧 HIDRATACIÓN")
            st.markdown('<span class="badge-tipo">Añadir Agua (H₂O)</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es literalmente hacer que una molécula orgánica 'tome agua' para convertirse en un alcohol.")
                st.subheader("📖 Definición")
                st.write("Es la adición de agua ($H_2O$) a un Alqueno. La molécula de agua se parte en dos: un hidrógeno ($-H$) va a un carbono y un grupo hidroxilo ($-OH$) va al otro carbono, formando un alcohol.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Ocupa un empujón ácido:** El agua sola no le hace nada al alqueno. Ocupa obligatoriamente unas gotas de un ácido fuerte (como el ácido sulfúrico, $H_2SO_4$).")
                st.write("• **Sigue a Markovnikov:** El hidrógeno del agua siempre prefiere irse al carbono que ya tiene más hidrógenos.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_3-CH=CH_2 + H_2O \xrightarrow{H^+} CH_3-CH(OH)-CH_3")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Paso a Paso según Regla de Markovnikov:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info("**1. Ataque Ácido**")
                    st.latex(r"R-CH=CH_2 + H^+")
                    st.caption("El H⁺ del catalizador busca al carbono con más hidrógenos.")
                with col2:
                    st.warning("**2. Carbocatión**")
                    st.latex(r"R-CH^+ - CH_3")
                    st.caption("Se genera una carga positiva en el carbono secundario (más estable).")
                with col3:
                    st.success("**3. Entrada de OH**")
                    st.latex(r"R-CH(OH)-CH_3")
                    st.caption("El nucleófilo del agua se enlaza al centro positivo cerrando el alcohol.")

                st.subheader("🗺️ Esquema Visual (Regla de Markovnikov)")
                st.markdown("""
                <div class="esquema-text">
                         H-OH (Agua partida en dos)<br>
                         ⬇  ⬇<br>
                CH₃ ── CH ═ CH₂  (El carbono del extremo tiene MÁS hidrógenos)<br>
                         │    │<br>
                       [OH]  [H]<br>
                <br>
                🔬 <b>Resultado:</b> CH₃-CH(OH)-CH₃ (Alcohol en el carbono central)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🧴 Alcohol de Farmacia</div>
                    <p>Se usa para fabricar de forma masiva el alcohol isopropílico usado para desinfectar heridas o limpiar pantallas electrónicas.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("El uso de ácidos fuertes como catalizadores genera **desechos líquidos corrosivos**. Si estos residuos no se neutralizan antes de tirarlos al drenaje, acidifican los ríos y dañan gravemente los ecosistemas acuáticos.")

        # 4. ADICIÓN DE HX
        elif reaccion == "Adición de HX":
            st.header("🔥 ADICIÓN DE HX")
            st.markdown('<span class="badge-tipo">Añadir Ácidos Halogenados (HCl, HBr, HI)</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es meterle un ácido fuerte a un Alqueno para fijar un halógeno en su estructura.")
                st.subheader("📖 Definición")
                st.write("Es la reacción donde un Alqueno se combina con un halogenuro de hidrógeno ($HX$, como el $HCl$). El hidrógeno se une a un carbono y el halógeno al otro, produciendo un halogenuro de alquilo.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Regla de Oro (Markovnikov):** El hidrógeno siempre se pega al carbono que tiene más hidrógenos (los ricos se hacen más ricos).")
                st.write("• **Orden de velocidad:** El ácido $HI$ reacciona más rápido que el $HBr$ y el $HCl$ porque es más fácil de romper.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_3-CH=CH_2 + HCl \rightarrow CH_3-CH(Cl)-CH_3")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Desglose Dinámico de Enlaces:")
                col1, col2 = st.columns(2)
                with col1:
                    st.info("**Paso 1: Captura del Hidrógeno**")
                    st.latex(r"CH_3-CH=CH_2 + H^+ \rightarrow CH_3-CH^+ - CH_3")
                    st.caption("El doble enlace actúa como imán atrayendo al protón H⁺ hacia el extremo libre.")
                with col2:
                    st.success("**Paso 2: Fijación del Halógeno**")
                    st.latex(r"CH_3-CH^+ - CH_3 + Cl^- \rightarrow CH_3-CH(Cl)-CH_3")
                    st.caption("El anión Cloro (-) aprovecha el espacio positivo central para soldarse permanentemente.")

                st.subheader("🗺️ Esquema del Ataque del Ácido")
                st.markdown("""
                <div class="esquema-text">
                Paso 1: El doble enlace agarra al H+ (va al carbono con más hidrógenos)<br>
                CH₃-CH=CH₂ + H⁺ ➔ CH₃-CH⁺-CH₃ (Se forma un Carbocatión estable)<br>
                <br>
                Paso 2: El Cl⁻ que quedó libre ataca al centro positivo:<br>
                CH₃-CH⁺-CH₃ + Cl⁻ ➔ CH₃-CH(Cl)-CH₃
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">⚗️ Materia Prima Química</div>
                    <p>Sirve para crear moléculas intermediarias que luego se usan para fabricar solventes o reactivos especiales de laboratorio.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("Los gases de estos ácidos ($HCl$, $HBr$) son **gases muy corrosivos e irritantes**. Si escapan a la atmósfera, reaccionan con las nubes y contribuyen directamente al fenómeno de la **lluvia ácida**, que destruye bosques.")

      # 5. HIDROBORACIÓN
        elif reaccion == "Hidroboración":
            st.header("⚡ HIDROBORACIÓN - OXIDACIÓN")
            st.markdown('<span class="badge-tipo">Añadir Borano (BH₃) e Hidróxido</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es una técnica de laboratorio muy astuta para obligar a una molécula a recibir agua 'al revés' de lo que dicta la naturaleza, logrando que el grupo alcohol se coloque exactamente en la esquina o extremo menos congestionado.")
                st.subheader("📖 Definición")
                st.write("Es una reacción orgánica consecutiva de dos pasos (secuencial). En la primera etapa (Hidroboración), un Alqueno reacciona con Borano ($BH_3$) o su dímero ($B_2H_6$) disuelto en THF, uniendo el boro al carbono menos sustituido. En la segunda etapa (Oxidación), se añade peróxido de hidrógeno ($H_2O_2$) en medio básico ($NaOH$) para sustituir el átomo de boro por un grupo hidroxilo ($-OH$), produciendo un alcohol **Anti-Markovnikov** con geometría **Sin**.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Orientación Regioespecífica (La Rebelde):** Rompe la regla clásica de Markovnikov. El grupo hidroxilo ($-OH$) se conecta obligatoriamente en el carbono terminal que posee la mayor cantidad de hidrógenos.")
                st.write("• **Estereoquímica SIN:** Tanto el átomo de Hidrógeno como el de Boro se añaden simultáneamente por la misma cara plana del doble enlace del alqueno, evitando que la molécula rote de forma desigual.")
                st.write("• **Ausencia de Transposiciones:** A diferencia de la hidratación ácida común, esta reacción no pasa por un carbocatión libre, lo que significa que la estructura del carbono no se deforma ni se reordena internamente durante el proceso.")
                st.write("• **Alta Pureza:** Al ser un mecanismo coordinado de un solo estado de transición por etapa, produce un rendimiento muy alto del alcohol deseado sin generar compuestos secundarios molestos.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_3-CH=CH_2 \xrightarrow{1.\, BH_3 / \text{THF} \quad 2.\, H_2O_2,\, NaOH} CH_3-CH_2-CH_2-OH")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Mecanismo de Orientación Inversa:")
                col1, col2 = st.columns(2)
                with col1:
                    st.info("**Fase 1: Fijación Voluminosa**")
                    st.latex(r"R-CH=CH_2 + BH_3 \rightarrow R-CH(H)-CH_2-BH_2")
                    st.caption("Por efectos de espacio físico (impedimento estérico), el complejo de Boro ($BH_2$) prefiere anclarse en la esquina desocupada.")
                with col2:
                    st.success("**Fase 2: Oxidación y Reemplazo**")
                    st.latex(r"R-CH_2-CH_2-BH_2 \xrightarrow{H_2O_2,\, NaOH} R-CH_2-CH_2-OH")
                    st.caption("El agua oxigenada en medio básico corta limpiamente el enlace del boro e inserta el grupo hidroxilo en la orilla externa.")

                st.subheader("🗺️ Esquema de la Reacción Rebelde (Anti-Markovnikov)")
                st.markdown("""
                <div class="esquema-text">
                El Boro (por espacio) prefiere acomodarse en la esquina desocupada:<br>
                CH₃-CH ═ CH₂  +  BH₃  ➔  CH₃-CH(H)-CH₂(BH₂)<br>
                <br>
                Luego, el agua oxigenada (H₂O₂) quita el Boro y pone el alcohol:<br>
                CH₃-CH₂-CH₂-BH₂  ➔  CH₃-CH₂-CH₂-OH (Alcohol de Esquina / Primario)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones Industriales")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🌸 Cosméticos, Fragancias y Perfumería</div>
                    <p>Es el método preferido para sintetizar alcoholes primarios de cadena lineal larga (como el 1-hexanol o 1-octanol). Estos compuestos sirven como fijadores de aromas esenciales, humectantes avanzados y bases estructurales para la creación de cremas corporales y emulsiones cosméticas de alta gama.</p>
                </div>
                <div class="prep-card">
                    <div class="card-title">💊 Síntesis Fina de Fármacos</div>
                    <p>Debido a que no altera la estructura interna de los carbonos y respeta la orientación espacial exacta, los laboratorios farmacéuticos la utilizan como un paso clave para construir la arquitectura tridimensional de antibióticos complejos y medicamentos antivirales.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental y Seguridad")
                st.write("El uso del Borano ($BH_3$) representa un desafío importante en la química verde debido a que es un gas altamente inflamable, pirofórico (puede encenderse espontáneamente en el aire) y tóxico para los seres humanos. Para manejarlo de forma segura en la industria, se requiere disolverlo obligatoriamente en solventes orgánicos como el Tetrahidrofurano (THF), los cuales pertenecen al grupo de Compuestos Orgánicos Volátiles (COVs) que si se evaporan o filtran accidentalmente, actúan como severos contaminantes del aire y de mantos acuíferos subterráneos. Además, la etapa de oxidación genera sales de boro residuales en el agua que deben recibir tratamientos químicos de neutralización especializados antes de ser desechadas al drenaje industrial.")
    # =================================================
    # BLOQUE 2: REACCIONES DE SUSTITUCIÓN
    # =================================================
    elif tipo_reaccion == "Reacciones de Sustitución":

        reaccion = st.selectbox(
            "Selecciona una reacción de sustitución",
            [
                "Mecanismo SN1",
                "Mecanismo SN2",
                "Sustitución Aromática",
                "Sustitución Radicalaria"
            ]
        )

        # 1. SN1
        if reaccion == "Mecanismo SN1":
            st.header("⏳ MECANISMO SN1")
            st.markdown('<span class="badge-tipo">Sustitución en Dos Pasos</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es una sustitución lenta y calmada que ocurre en dos tiempos: primero sale la pieza vieja, y luego entra la nueva.")
                st.subheader("📖 Definición")
                st.write("Es una Sustitución Nucleofílica Unimolecular. El compuesto orgánico pierde primero su grupo saliente por sí solo (paso lento), dejando un carbono positivo ($C^+$), y después llega un grupo nuevo a unirse rápidamente.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Prefiere carbonos amontonados:** Funciona excelente en carbonos terciarios ($3^\circ$) porque los grupos alrededor ayudan a aguantar la carga.")
                st.write("• **Mezcla mixta:** Como el carbono queda plano, la pieza nueva puede entrar por el frente o por detrás con la misma facilidad.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"(CH_3)_3C-Cl + OH^- \rightarrow (CH_3)_3C-OH + Cl^-")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Mecanismo Cronológico:")
                col1, col2 = st.columns(2)
                with col1:
                    st.info("**Paso 1 (Lento): Salida de la pieza**")
                    st.latex(r"R_3C-Cl \rightarrow R_3C^+ + Cl^-")
                    st.caption("El Cloro se va debido a la repulsión, formando un Carbocatión plano inestable.")
                with col2:
                    st.success("**Paso 2 (Rápido): Entrada libre**")
                    st.latex(r"R_3C^+ + OH^- \rightarrow R_3C-OH")
                    st.caption("El grupo entrante se une sin resistencia por cualquier cara vacía del carbono.")

                st.subheader("🗺️ Esquema del Mecanismo en Pasos")
                st.markdown("""
                <div class="esquema-text">
                <b>Paso 1 (Lento):</b> El cloro se va solo porque está muy apretado:<br>
                (CH₃)₃C-Cl ➔ (CH₃)₃C⁺ (Carbocatión plano) + Cl⁻<br>
                <br>
                <b>Paso 2 (Rápido):</b> Llega el grupo OH⁻ y ataca por cualquier lado:<br>
                (CH₃)₃C⁺ + OH⁻ ➔ (CH₃)₃C-OH
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">⛽ Aditivos de Gasolina</div>
                    <p>Sintetiza compuestos ramificados pesados que se agregan a combustibles de alta calidad para evitar que el motor explote antes de tiempo.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("Depende mucho del uso de solventes como alcoholes o agua. Genera residuos con haluros solubles (como sales de cloro o bromo). Si bien las sales son de bajo impacto, los subproductos orgánicos volátiles requieren tratamiento.")

        # 2. SN2
        elif reaccion == "Mecanismo SN2":
            st.header("🏹 MECANISMO SN2")
            st.markdown('<span class="badge-tipo">Sustitución en Un Solo Paso</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es un choque directo y rápido donde la pieza nueva saca a la vieja de un solo golpe.")
                st.subheader("📖 Definición")
                st.write("Sustitución Nucleofílica Bimolecular. Ocurre en un solo paso concertado: el grupo atacante golpea al carbono **por la espalda** al mismo tiempo que el grupo viejo va saliendo por enfrente.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Efecto Paraguas:** La molécula se voltea al revés debido al golpe por detrás (Inversión de configuración).")
                st.write("• **Prefiere espacio libre:** Solo funciona bien en carbonos primarios ($1^\circ$) o metilos, porque si hay muchos grupos estorbando, el atacante no puede entrar.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_3-Br + NaOH \rightarrow CH_3-OH + NaBr")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Transición Simultánea del Choque:")
                st.latex(r"HO^- + CH_3-Br \rightarrow \underbrace{[HO \cdots CH_3 \cdots Br]^\ddagger}_{\text{Estado de Transición}} \rightarrow HO-CH_3 + Br^-")
                st.write("")
                col1, col2 = st.columns(2)
                with col1:
                    st.info("**Efecto Estérico:**")
                    st.write("Requiere carbonos despejados ($1^\circ$) para que el nucleófilo pueda aproximarse físicamente por detrás sin chocar.")
                with col2:
                    st.success("**Efecto Paraguas:**")
                    st.write("Al consolidarse el nuevo enlace, los tres hidrógenos remanentes cambian de orientación espacial drásticamente.")

                st.subheader("🗺️ Esquema del Choque Simultáneo")
                st.markdown("""
                <div class="esquema-text">
                El ataque ocurre al mismo tiempo (Estado de Transición):<br>
                HO⁻ ──➔ [ CH₃ ] ──➔ Br<br>
                <br>
                🔒 <b>Momento clave (Todo junto):</b> [ HO ··· CH₃ ··· Br ]⁻<br>
                <br>
                🔬 <b>Resultado:</b> HO-CH₃ + Br⁻ (La molécula se invirtió como un paraguas)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">💊 Farmacia Quirúrgica</div>
                    <p>Es una de las reacciones favoritas para armar medicamentos específicos porque permite controlar con precisión la forma tridimensional de la molécula.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("Esta reacción usa solventes apróticos especiales (como la Acetona o el DMSO). Si estos solventes se derraman, pueden arrastrar sustancias tóxicas a través de la piel de animales y plantas, además de contaminar mantos acuíferos subterráneos.")

        # 3. SUSTITUCIÓN AROMÁTICA
        elif reaccion == "Sustitución Aromática":
            st.header("🛡️ SUSTITUCIÓN AROMÁTICA")
            st.markdown('<span class="badge-tipo">Sustitución en el Benceno</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es cambiarle una pieza exterior al anillo de Benceno sin romper su 'escudo protector' circular.")
                st.subheader("📖 Definición")
                st.write("Reacción donde un anillo de Benceno ($C_6H_6$) intercambia uno de sus hidrógenos externos por un átomo o grupo diferente (como un Cloro o un grupo Nitro), manteniendo intacto su anillo de electrones.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Protección Máxima:** El benceno jamás se deja romper por adición porque perdería su estabilidad de anillo (aromaticidad).")
                st.write("• **Ocupa un súper atacante:** Requiere catalizadores fuertes como el cloruro de hierro ($FeCl_3$) para poder reaccionar.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"C_6H_6 + Cl_2 \xrightarrow{FeCl_3} C_6H_5Cl + HCl")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Estabilidad de la Resonancia (Complejo de Sigma):")
                col1, col2 = st.columns(2)
                with col1:
                    st.info("**1. Ataque Electrofílico**")
                    st.latex(r"C_6H_6 + E^+ \rightarrow [C_6H_6E]^+")
                    st.caption("Un electrófilo muy potente ($E^+$) jala transitoriamente un par de electrones del anillo aromático estable.")
                with col2:
                    st.success("**2. Recuperación Aromática**")
                    st.latex(r"[C_6H_6E]^+ \rightarrow C_6H_5E + H^+")
                    st.caption("Para no morir, el anillo expulsa velozmente al protón $H^+$, restaurando su escudo protector interno.")

                st.subheader("🗺️ Esquema del Intercambio Periférico")
                st.markdown("""
                <div class="esquema-text">
                      [ H ] (Hidrógeno afuera del escudo)<br>
                       │<br>
                   ⎰⎱📌⎰⎱ (Anillo de Benceno Estable)<br>
                       ⬆ ─── [ Cl⁺ ] (Super Cloro activado por FeCl₃)<br>
                <br>
                🔬 <b>Resultado:</b> El Cl⁺ saca a patadas al H⁺, el anillo queda intacto.
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🎨 Tintes y Detergentes</div>
                    <p>Se usa para añadir cadenas de carbonos al benceno y fabricar los compuestos base de los detergentes en polvo domésticos o colorantes textiles.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("El Benceno y sus derivados son **altamente tóxicos, cancerígenos y volátiles**. Su liberación al ambiente es peligrosa porque dañan el sistema nervioso de los seres vivos y persisten durante décadas en el aire y el agua.")

        # 4. SUSTITUCIÓN RADICALARIA
        elif reaccion == "Sustitución Radicalaria":
            st.header("☀️ SUSTITUCIÓN RADICALARIA")
            st.markdown('<span class="badge-tipo">Sustitución en Alcanos (Gases)</span>', unsafe_allow_html=True)
            st.write("")

            t1, t2, t3, t4, t5 = st.tabs(["❓ ¿Qué es y Definición?", "📌 Características", "🧪 Fórmulas y Esquema", "🏭 Aplicaciones", "🌱 Impacto Ambiental"])

            with t1:
                st.subheader("❓ ¿Qué es?")
                st.write("Es obligar a reaccionar a los gases flojos (como el metano) usando la fuerza de la luz solar.")
                st.subheader("📖 Definición")
                st.write("Es un proceso donde la luz ultravioleta abre un halógeno a la mitad creando átomos inestables ('radicales libres') que entran a romper y sustituir los hidrógenos de un alcano en una reacción en cadena.")

            with t2:
                st.subheader("📌 Características")
                st.write("• **Tres etapas:** Funciona como fichas de dominó: Iniciación (con luz), Propagación (reacción en cadena solo) y Terminación (cuando se acaban).")
                st.write("• **Poco selectiva:** El cloro ataca con tanta fuerza que a veces sustituye más hidrógenos de los que querías.")

            with t3:
                st.subheader("🧪 Ecuación Química")
                st.latex(r"CH_4 + Cl_2 \xrightarrow{Luz UV} CH_3Cl + HCl")

                # --- APRENDIZAJE VISUAL MEJORADO ---
                st.subheader("🔬 Las 3 Etapas en Cadena:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info("**1. Iniciación**")
                    st.latex(r"Cl_2 \xrightarrow{h\nu} 2Cl\cdot")
                    st.caption("La energía solar rompe el gas cloro en dos radicales inestables.")
                with col2:
                    st.warning("**2. Propagación**")
                    st.latex(r"CH_4 + Cl\cdot \rightarrow \cdot CH_3 + HCl")
                    st.caption("El cloro roba un hidrógeno, obligando al carbono a volverse radical.")
                with col3:
                    st.success("**3. Terminación**")
                    st.latex(r"\cdot CH_3 + Cl\cdot \rightarrow CH_3Cl")
                    st.caption("Dos electrones libres se encuentran y se cierra el ciclo destructivo.")

                st.subheader("🗺️ Esquema de Reacción en Cadena (Radicales)")
                st.markdown("""
                <div class="esquema-text">
                💥 <b>Iniciación:</b> Cl — Cl + Luz UV ➔ Cl• + •Cl (Átomos con un electrón suelto)<br>
                ⛓️ <b>Propagación:</b> Cl• + CH₄ ➔ HCl + •CH₃ (El radical destruye al gas)<br>
                               •CH₃ + Cl₂ ➔ CH₃Cl + Cl• (¡Vuelve a empezar!)
                </div>
                """, unsafe_allow_html=True)

            with t4:
                st.subheader("🏭 Aplicaciones")
                st.markdown("""
                <div class="prep-card">
                    <div class="card-title">🧪 Solventes Industriales</div>
                    <p>Es el método para producir cloroformo y diclorometano, sustancias líquidas usadas en las industrias pesadas para limpiar piezas metálicas y extraer aceites.</p>
                </div>
                """, unsafe_allow_html=True)

            with t5:
                st.subheader("🌱 Impacto Ambiental")
                st.write("Los compuestos clorados que se escapan por esta vía son los principales responsables de la **destrucción de la capa de ozono** estratosférica y actúan como potentes gases de efecto invernadero.")

# =====================================================
# FIN DEL MÓDULO INTERACTIVO DE PREPARATORIA
# =====================================================
  # =====================================================
# 🧬 MÓDULO MECANISMOS ORGÁNICOS INTERACTIVOS
# PARTE 1 — PANTALLA PRINCIPAL + MENÚ
# =====================================================

if selected == "Mecanismos":

    st.title("🧬 MECANISMOS ORGÁNICOS INTERACTIVOS")

    st.markdown("""
    <div class="card">
    <h2>🏠 Pantalla principal</h2>

    <p>
    Este módulo explica de forma visual e interactiva los mecanismos
    de las reacciones orgánicas de <b>adición</b> y <b>sustitución</b>.
    </p>

    <p>
    Aquí podrás analizar cada reacción paso a paso, identificando:
    reactivos, nucleófilos, electrófilos, intermediarios, enlaces que se rompen,
    enlaces que se forman y producto final.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h2>🎯 Objetivo del módulo</h2>

    <p>
    Comprender cómo ocurre un mecanismo orgánico desde el inicio hasta el producto,
    usando una simulación ordenada, clara y con explicación química en cada paso.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =================================================
    # MENÚ DE SELECCIÓN
    # =================================================

    st.subheader("📌 Menú de selección")
    tipo = st.selectbox(
    "Selecciona el tipo de reacción:",
    [
        "⚡ Reacciones de Adición",
        "🔄 Reacciones de Sustitución"
    ]
)

    if tipo == "⚡ Reacciones de Adición":

        reaccion = st.selectbox(
            "Selecciona una reacción de adición:",
            [
                "1. Hidrogenación",
                "2. Halogenación",
                "3. Hidratación",
                "4. Adición HX",
                "5. Hidroboración-Oxidación"
            ]
        )

    else:

        reaccion = st.selectbox(
            "Selecciona una reacción de sustitución:",
            [
                "6. SN1",
                "7. SN2",
                "8. Sustitución Aromática Electrofílica",
                "9. Sustitución Aromática Nucleofílica",
                "10. Sustitución Radicalaria"
            ]
        )

    st.divider()

    # =================================================
    # PANEL TEMPORAL
    # =================================================

    st.markdown("""
    <div class="card">
    <h2>🧪 Reacción seleccionada</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Tipo de reacción: {tipo}")

    with col2:
        st.success(f"Reacción: {reaccion}")

# =================================================
# PARTE 2 — BASE DE DATOS DE REACCIONES
# =================================================


    mecanismos = {

        "1. Hidrogenación": {
            "formula": "CH₂=CH₂ + H₂ → CH₃-CH₃",
            "tipo": "Adición",
            "mecanismo": "Adición catalítica syn",
            "intermediario": "Alqueno adsorbido en metal",
            "regla": "Los hidrógenos se adicionan por la misma cara.",
            "producto": "Alcano",
            "resumen": "El doble enlace se rompe y se agregan dos hidrógenos.",
            "pasos": [
                "El H₂ se adsorbe sobre el catalizador metálico.",
                "El enlace H-H se debilita sobre la superficie del metal.",
                "El alqueno se acerca y su enlace π interactúa con el metal.",
                "Los hidrógenos se transfieren al doble enlace.",
                "Se libera el alcano como producto final."
            ]
        },

        "2. Halogenación": {
            "formula": "CH₂=CH₂ + Br₂ → BrCH₂-CH₂Br",
            "tipo": "Adición",
            "mecanismo": "Adición anti",
            "intermediario": "Ion bromonio",
            "regla": "El segundo halógeno ataca por el lado opuesto.",
            "producto": "Dihaluro vecinal",
            "resumen": "El alqueno reacciona con Br₂ o Cl₂ formando un dihaluro.",
            "pasos": [
                "El doble enlace polariza la molécula de Br₂.",
                "El alqueno ataca al Brδ⁺.",
                "Se forma un ion bromonio cíclico.",
                "El Br⁻ ataca desde la parte posterior.",
                "Se obtiene un producto con adición anti."
            ]
        },

        "3. Hidratación": {
            "formula": "CH₃-CH=CH₂ + H₂O/H⁺ → CH₃-CH(OH)-CH₃",
            "tipo": "Adición",
            "mecanismo": "Adición electrofílica",
            "intermediario": "Carbocatión",
            "regla": "Sigue la regla de Markovnikov.",
            "producto": "Alcohol",
            "resumen": "Se agrega agua al alqueno para formar un alcohol.",
            "pasos": [
                "El alqueno capta un protón H⁺.",
                "Se forma el carbocatión más estable.",
                "El agua ataca al carbocatión.",
                "Se forma un alcohol protonado.",
                "Ocurre desprotonación y se obtiene el alcohol."
            ]
        },

        "4. Adición HX": {
            "formula": "CH₃-CH=CH₂ + HBr → CH₃-CHBr-CH₃",
            "tipo": "Adición",
            "mecanismo": "Adición electrofílica de halogenuro de hidrógeno",
            "intermediario": "Carbocatión",
            "regla": "Markovnikov: H va al carbono con más hidrógenos.",
            "producto": "Halogenuro de alquilo",
            "resumen": "El alqueno incorpora H y X para formar un halogenuro.",
            "pasos": [
                "El doble enlace ataca al H del HX.",
                "Se rompe el enlace H-X.",
                "Se forma el carbocatión más estable.",
                "El haluro X⁻ ataca al carbocatión.",
                "Se forma el halogenuro de alquilo."
            ]
        },

        "5. Hidroboración-Oxidación": {
            "formula": "CH₃-CH=CH₂ → CH₃-CH₂-CH₂OH",
            "tipo": "Adición",
            "mecanismo": "Adición concertada syn",
            "intermediario": "Organoborano",
            "regla": "Anti-Markovnikov: OH queda en el carbono menos sustituido.",
            "producto": "Alcohol primario",
            "resumen": "Permite obtener alcoholes anti-Markovnikov sin carbocatión.",
            "pasos": [
                "El alqueno reacciona con BH₃.",
                "B y H se adicionan al mismo tiempo.",
                "El boro se une al carbono menos sustituido.",
                "Se forma un organoborano.",
                "H₂O₂/NaOH reemplaza B por OH."
            ]
        },

        "6. SN1": {
            "formula": "R-LG + Nu⁻ → R-Nu + LG⁻",
            "tipo": "Sustitución",
            "mecanismo": "Sustitución nucleofílica unimolecular",
            "intermediario": "Carbocatión",
            "regla": "Favorecida en sustratos terciarios.",
            "producto": "Producto de sustitución",
            "resumen": "Primero sale el grupo saliente y luego entra el nucleófilo.",
            "pasos": [
                "El grupo saliente abandona la molécula.",
                "Se forma un carbocatión plano.",
                "El nucleófilo se acerca al carbocatión.",
                "El nucleófilo forma un nuevo enlace.",
                "Se obtiene el producto sustituido."
            ]
        },

        "7. SN2": {
            "formula": "Nu⁻ + R-LG → R-Nu + LG⁻",
            "tipo": "Sustitución",
            "mecanismo": "Sustitución nucleofílica bimolecular",
            "intermediario": "Estado de transición",
            "regla": "Ataque posterior con inversión de configuración.",
            "producto": "Producto de sustitución invertido",
            "resumen": "El nucleófilo entra mientras el grupo saliente se va.",
            "pasos": [
                "El nucleófilo se aproxima por la parte posterior.",
                "Comienza a formarse el enlace C-Nu.",
                "El enlace C-LG empieza a romperse.",
                "Se alcanza un estado de transición.",
                "Sale el grupo saliente y queda el producto invertido."
            ]
        },

        "8. Sustitución Aromática Electrofílica": {
            "formula": "C₆H₆ + Br₂/FeBr₃ → C₆H₅Br + HBr",
            "tipo": "Sustitución",
            "mecanismo": "Ataque electrofílico al anillo aromático",
            "intermediario": "Complejo sigma",
            "regla": "El anillo recupera la aromaticidad al perder H⁺.",
            "producto": "Aromático sustituido",
            "resumen": "Un electrófilo reemplaza un hidrógeno del benceno.",
            "pasos": [
                "El catalizador genera un electrófilo fuerte.",
                "El anillo aromático ataca al electrófilo.",
                "Se forma el complejo sigma.",
                "Una base retira H⁺ del anillo.",
                "Se recupera la aromaticidad."
            ]
        },

        "9. Sustitución Aromática Nucleofílica": {
            "formula": "Ar-LG + Nu⁻ → Ar-Nu + LG⁻",
            "tipo": "Sustitución",
            "mecanismo": "Adición-eliminación aromática",
            "intermediario": "Complejo de Meisenheimer",
            "regla": "Requiere grupos atractores de electrones.",
            "producto": "Aromático sustituido por nucleófilo",
            "resumen": "Un nucleófilo reemplaza un grupo saliente en un anillo aromático.",
            "pasos": [
                "El nucleófilo ataca al carbono unido al grupo saliente.",
                "Se rompe temporalmente la aromaticidad.",
                "Se forma el complejo de Meisenheimer.",
                "Sale el grupo saliente.",
                "Se recupera la aromaticidad del anillo."
            ]
        },

        "10. Sustitución Radicalaria": {
            "formula": "CH₄ + Cl₂ → CH₃Cl + HCl",
            "tipo": "Sustitución",
            "mecanismo": "Reacción en cadena por radicales libres",
            "intermediario": "Radical libre",
            "regla": "Tiene iniciación, propagación y terminación.",
            "producto": "Halogenuro de alquilo",
            "resumen": "Un halógeno sustituye un hidrógeno de un alcano.",
            "pasos": [
                "La luz UV rompe Cl₂ de forma homolítica.",
                "Se forman radicales Cl•.",
                "Un radical extrae H del alcano.",
                "Se forma un radical alquilo.",
                "El radical alquilo reacciona con Cl₂ y forma el producto."
            ]
        }
    }

    datos = mecanismos[reaccion]

    # =================================================
    # MOSTRAR INFORMACIÓN GENERAL
    # =================================================

    st.markdown("""
    <div class="card">
    <h2>📖 Información general del mecanismo</h2>
    </div>
    """, unsafe_allow_html=True)

    st.code(datos["formula"])

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🧪 Tipo: {datos['tipo']}")
        st.warning(f"⚙️ Mecanismo: {datos['mecanismo']}")

    with col2:
        st.success(f"🧬 Intermediario: {datos['intermediario']}")
        st.error(f"📌 Regla clave: {datos['regla']}")

    st.markdown("### 🧾 Resumen breve")
    st.write(datos["resumen"])

    st.markdown("### ✅ Producto esperado")
    st.success(datos["producto"])
         # =================================================
    # PARTE 3 — SIMULACIÓN PASO A PASO VISIBLE
    # =================================================

    st.divider()

    st.header("🎬 Simulación paso a paso del mecanismo")

    pasos = datos["pasos"]
    total_pasos = len(pasos)

    if "paso_mecanismo" not in st.session_state:
        st.session_state.paso_mecanismo = 0

    if "reaccion_actual" not in st.session_state:
        st.session_state.reaccion_actual = reaccion

    if st.session_state.reaccion_actual != reaccion:
        st.session_state.reaccion_actual = reaccion
        st.session_state.paso_mecanismo = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⏮ Paso anterior"):
            if st.session_state.paso_mecanismo > 0:
                st.session_state.paso_mecanismo -= 1

    with col2:
        if st.button("🔄 Reiniciar"):
            st.session_state.paso_mecanismo = 0

    with col3:
        if st.button("⏭ Siguiente paso"):
            if st.session_state.paso_mecanismo < total_pasos - 1:
                st.session_state.paso_mecanismo += 1

    paso_actual = st.session_state.paso_mecanismo
    def animacion_reaccion(reaccion, paso):

        escenas = {

            "1. Hidrogenación": [
                "H₂ se acerca al catalizador metálico.",
                "El enlace H-H se rompe sobre el metal.",
                "El alqueno se pega al catalizador.",
                "Los H se transfieren al doble enlace.",
                "Se libera el alcano."
            ],

            "2. Halogenación": [
                "El Br₂ se polariza cerca del doble enlace.",
                "El alqueno ataca al Brδ⁺.",
                "Se forma el ion bromonio.",
                "Br⁻ ataca por atrás.",
                "Se forma el dihaluro anti."
            ],

            "3. Hidratación": [
                "El doble enlace ataca al H⁺.",
                "Se forma el carbocatión.",
                "El agua ataca al carbono positivo.",
                "Se forma alcohol protonado.",
                "Sale H⁺ y queda el alcohol."
            ],

            "4. Adición HX": [
                "El alqueno ataca al H de HBr.",
                "Se rompe H-Br.",
                "Se forma carbocatión Markovnikov.",
                "Br⁻ ataca al carbocatión.",
                "Se forma el halogenuro."
            ],

            "5. Hidroboración-Oxidación": [
                "BH₃ se aproxima al alqueno.",
                "B y H entran al mismo tiempo.",
                "Se forma organoborano.",
                "H₂O₂/NaOH oxida el enlace C-B.",
                "B se reemplaza por OH."
            ],

            "6. SN1": [
                "El grupo saliente empieza a separarse.",
                "Sale LG⁻ y queda carbocatión.",
                "El nucleófilo se acerca.",
                "Nu forma enlace con C⁺.",
                "Se obtiene el producto."
            ],

            "7. SN2": [
                "Nu⁻ se acerca por atrás.",
                "Empieza a formarse C-Nu.",
                "C-LG empieza a romperse.",
                "Estado de transición.",
                "Sale LG⁻ con inversión."
            ],

            "8. Sustitución Aromática Electrofílica": [
                "Se genera el electrófilo E⁺.",
                "El anillo ataca a E⁺.",
                "Se forma complejo sigma.",
                "Sale H⁺.",
                "Regresa la aromaticidad."
            ],

            "9. Sustitución Aromática Nucleofílica": [
                "Nu⁻ ataca al anillo.",
                "Se rompe temporalmente la aromaticidad.",
                "Se forma Meisenheimer.",
                "Sale LG⁻.",
                "Regresa la aromaticidad."
            ],

            "10. Sustitución Radicalaria": [
                "Luz UV rompe Cl₂.",
                "Se forman radicales Cl•.",
                "Cl• arranca H del alcano.",
                "Se forma radical alquilo.",
                "Radical + Cl₂ forma producto."
            ]
        }

        texto = escenas[reaccion][paso]

        return f"""
        <div class="sim-box">
            <h3 style="text-align:center;">🎬 Movimiento específico</h3>

            <div class="mol-row">
                <span class="atom carbon">C</span>
                <span class="bond">═</span>
                <span class="atom carbon">C</span>
                <span class="electron">e⁻</span>
                <span class="arrow">➜</span>
                <span class="atom halo">+</span>
                <span class="arrow">➜</span>
                <span class="atom oxygen">P</span>
            </div>

            <p style="text-align:center; font-size:22px;">
            {texto}
            </p>
        </div>
        """
    progreso = int(((paso_actual + 1) / total_pasos) * 100)

    st.progress(progreso)

    st.markdown(f"""
    <div class="card">
        <h2>🔹 Paso {paso_actual + 1} de {total_pasos}</h2>
        <p style="font-size:22px;">
        {pasos[paso_actual]}
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("🧬 Simulación visual interactiva")
    st.subheader("🧬 Simulación molecular interactiva")

    import streamlit.components.v1 as components
    import base64
    import streamlit.components.v1 as components
    import base64
    from io import BytesIO
    from rdkit import Chem
    from rdkit.Chem import Draw

    def mol_base64(smiles):

        mol = Chem.MolFromSmiles(smiles)
        mol = Chem.AddHs(mol)

        drawer = Draw.MolDraw2DCairo(420, 300)
        opciones = drawer.drawOptions()

        opciones.bondLineWidth = 4
        opciones.padding = 0.08
        opciones.addAtomIndices = False

        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()

        img_data = drawer.GetDrawingText()

        return base64.b64encode(img_data).decode()
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()

    if reaccion == "2. Halogenación":

        eteno = mol_base64("C=C")
        br2 = mol_base64("BrBr")
        producto = mol_base64("BrCCBr")

        textos = [
            "El Br₂ se aproxima al doble enlace del alqueno.",
            "El enlace π polariza al Br₂ y comienza el ataque electrónico.",
            "Se forma un ion bromonio como intermediario cíclico.",
            "El Br⁻ ataca por la cara opuesta y abre el intermediario.",
            "Se forma el 1,2-dibromoetano como producto final anti."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#FFFDE7;
             color:#0F172A;
            font-family:Arial;
        }}
         .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

         .mol {{
            width:390px;
            background:#ffffff;
            border-radius:24px;
            padding:18px;
            margin:16px;
            border:4px solid #00E5FF;
            box-shadow:
                0 0 25px #00E5FF,
                0 0 55px rgba(0,229,255,0.5);
        }}
        .br2 {{
            animation: acercar 2s infinite alternate;
        }}

        .shake {{
            animation: vibrar .5s infinite alternate;
        }}

        .attack {{
            animation: ataque 1.5s infinite alternate;
            font-size:45px;
            color:#FFD700;
        }}

        .arrow {{
            font-size:60px;
            color:#00E5FF;
            animation: flecha 1s infinite alternate;
        }}

        .curve {{
            font-size:55px;
            color:#FF4040;
            animation: flecha 1s infinite alternate;
        }}

        .product {{
            animation: brillar 1s infinite alternate;
        }}

        @keyframes acercar {{
            from {{ transform:translateX(130px); opacity:.3; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes ataque {{
            from {{ transform:translateX(-140px); opacity:.3; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0); }}
            to {{ transform:translateX(25px); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}
        </style>
        </head>

        <body>
        <div class="box">
            <h2>🎬 Halogenación de alquenos — Paso {paso_actual + 1}</h2>
            <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{eteno}">
            <span class="arrow">➜</span>
            <img class="mol br2" src="data:image/png;base64,{br2}">
            <h3>Br₂ se mueve hacia el doble enlace.</h3>
            """

        elif paso_actual == 1:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{eteno}">
            <span class="curve">↷</span>
            <img class="mol br2 shake" src="data:image/png;base64,{br2}">
            <h3>Los electrones π atacan al Brδ⁺.</h3>
            """

        elif paso_actual == 2:
            html += """
            <div class="shake" style="font-size:55px; line-height:1.3;">
                Br⁺<br>
               / &nbsp;&nbsp; \\<br>
            CH₂ —— CH₂
            </div>
            <h3>Intermediario: ion bromonio.</h3>
            """

        elif paso_actual == 3:
            html += """
            <span class="attack">Br⁻</span>
            <span class="arrow">➜</span>
            <span class="shake" style="font-size:50px;">
                Br⁺ / CH₂—CH₂
            </span>
            <h3>El Br⁻ ataca por atrás y abre el anillo.</h3>
            """

        else:
            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">
            <h3>Producto final: Br—CH₂—CH₂—Br</h3>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=430, scrolling=False)

    if reaccion == "1. Hidrogenación":

        eteno = mol_base64("C=C")
        h2 = mol_base64("[H][H]")
        producto = mol_base64("CC")

        textos = [
            "El H₂ se acerca al catalizador metálico.",
            "El enlace H-H se debilita sobre la superficie del metal.",
            "El alqueno se adsorbe sobre el catalizador.",
            "Los hidrógenos se transfieren al doble enlace.",
            "Se forma el alcano final."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .metal {{
            background:linear-gradient(90deg,#777,#ddd,#777);
            color:#111;
            font-weight:bold;
            padding:18px;
            border-radius:15px;
            margin:20px auto;
            width:60%;
            box-shadow:0 0 25px #FDE047;
        }}

        .move {{
            animation:mover 2s infinite alternate;
        }}

        .shake {{
            animation:vibrar .5s infinite alternate;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 1s infinite alternate;
        }}

        @keyframes mover {{
            from {{ transform:translateY(-60px); opacity:.4; }}
            to {{ transform:translateY(0); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0); }}
            to {{ transform:translateX(20px); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">
            <h2>🎬 Hidrogenación de alquenos — Paso {paso_actual + 1}</h2>
            <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{eteno}">
            <span class="arrow">➜</span>
            <img class="mol move" src="data:image/png;base64,{h2}">
            <h3>El H₂ se aproxima al alqueno.</h3>
            """

        elif paso_actual == 1:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{h2}">
            <div class="metal">Catalizador metálico: Pt / Pd / Ni</div>
            <h3>El metal debilita el enlace H-H.</h3>
            """

        elif paso_actual == 2:
            html += f"""
            <img class="mol move" src="data:image/png;base64,{eteno}">
            <div class="metal">Superficie metálica</div>
            <h3>El alqueno se fija sobre el catalizador.</h3>
            """

        elif paso_actual == 3:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{eteno}">
            <span class="arrow">+ H + H ➜</span>
            <h3>Los hidrógenos se adicionan al doble enlace.</h3>
            """

        else:
            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">
            <h3>Producto final: etano.</h3>
            <h4>El doble enlace se convirtió en enlace simple.</h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=500, scrolling=False)

    if reaccion == "3. Hidratación":

        propeno = mol_base64("CC=C")
        agua = mol_base64("O")
        producto = mol_base64("CC(O)C")

        textos = [
            "El doble enlace ataca al H⁺ del medio ácido.",
            "Se forma el carbocatión más estable.",
            "El agua actúa como nucleófilo y ataca al carbocatión.",
            "Se forma un alcohol protonado.",
            "Se pierde H⁺ y queda el alcohol final."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .acid {{
            font-size:55px;
            color:#FF4D4D;
            animation:ataque 1.5s infinite alternate;
        }}

        .water {{
            animation:mover 1.6s infinite alternate;
        }}

        .shake {{
            animation:vibrar .5s infinite alternate;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 1s infinite alternate;
        }}

        @keyframes ataque {{
            from {{ transform:translateX(130px); opacity:.3; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes mover {{
            from {{ transform:translateX(-120px); opacity:.4; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0); }}
            to {{ transform:translateX(20px); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">
            <h2>🎬 Hidratación ácida de alquenos — Paso {paso_actual + 1}</h2>
            <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{propeno}">
            <span class="arrow">➜</span>
            <span class="acid">H⁺</span>
            <h3>El enlace π toma un protón del medio ácido.</h3>
            """

        elif paso_actual == 1:
            html += """
            <div style="font-size:55px; color:white;" class="shake">
                CH₃—C⁺H—CH₃
            </div>
            <h3>Se forma un carbocatión secundario más estable.</h3>
            <h4 style="color:#00E5FF;">Regla de Markovnikov</h4>
            """

        elif paso_actual == 2:
            html += f"""
            <img class="mol water" src="data:image/png;base64,{agua}">
            <span class="arrow">➜</span>
            <div style="font-size:45px; display:inline-block;" class="shake">
                CH₃—C⁺H—CH₃
            </div>
            <h3>El agua ataca al carbono positivo.</h3>
            """

        elif paso_actual == 3:
            html += """
            <div style="font-size:45px; color:white;" class="shake">
                CH₃—CH(OH₂⁺)—CH₃
            </div>
            <h3>Se forma un alcohol protonado.</h3>
            """

        else:
            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">
            <h3>Producto final: 2-propanol.</h3>
            <h4>El grupo OH queda en el carbono más sustituido.</h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=500, scrolling=False)
    if reaccion == "4. Adición HX":

        propeno = mol_base64("CC=C")
        hbr = mol_base64("Br")
        producto = mol_base64("CC(Br)C")

        textos = [
            "El doble enlace ataca al H del HBr.",
            "Se rompe el enlace H-Br y se forma Br⁻.",
            "Se forma el carbocatión más estable.",
            "El Br⁻ ataca al carbocatión.",
            "Se obtiene el halogenuro de alquilo final."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .acid {{
            font-size:55px;
            color:#FF4D4D;
            animation:ataque 1.5s infinite alternate;
        }}

        .bromo {{
            font-size:55px;
            color:#FFAA00;
            animation:mover 1.5s infinite alternate;
        }}

        .shake {{
            animation:vibrar .5s infinite alternate;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 1s infinite alternate;
        }}

        @keyframes ataque {{
            from {{ transform:translateX(130px); opacity:.3; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes mover {{
            from {{ transform:translateX(-130px); opacity:.3; }}
            to {{ transform:translateX(0); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0); }}
            to {{ transform:translateX(20px); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">
            <h2>🎬 Adición de HX — Paso {paso_actual + 1}</h2>
            <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:
            html += f"""
            <img class="mol shake" src="data:image/png;base64,{propeno}">
            <span class="arrow">➜</span>
            <span class="acid">H—Br</span>
            <h3>El enlace π actúa como nucleófilo y toma H⁺.</h3>
            """

        elif paso_actual == 1:
            html += """
            <div style="font-size:52px;" class="shake">
                H—Br &nbsp; ⟶ &nbsp; H⁺ + Br⁻
            </div>
            <h3>El enlace H-Br se rompe de manera heterolítica.</h3>
            """

        elif paso_actual == 2:
            html += """
            <div style="font-size:55px; color:white;" class="shake">
                CH₃—C⁺H—CH₃
            </div>
            <h3>Se forma un carbocatión secundario.</h3>
            <h4 style="color:#00E5FF;">Regla clave: Markovnikov</h4>
            """

        elif paso_actual == 3:
            html += """
            <span class="bromo">Br⁻</span>
            <span class="arrow">➜</span>
            <div style="font-size:45px; display:inline-block;" class="shake">
                CH₃—C⁺H—CH₃
            </div>
            <h3>El bromuro ataca al carbono positivo.</h3>
            """

        else:
            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">
            <h3>Producto final: 2-bromopropano.</h3>
            <h4>El Br queda en el carbono más sustituido.</h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=500, scrolling=False)
    if reaccion == "5. Hidroboración-Oxidación":

        propeno = mol_base64("CC=C")
        bh3 = mol_base64("B")
        producto = mol_base64("CCCO")

        textos = [
            "El BH₃ se aproxima al doble enlace.",
            "El boro y el hidrógeno se adicionan simultáneamente.",
            "Se forma el organoborano.",
            "El peróxido de hidrógeno oxida el enlace C-B.",
            "Se forma el alcohol anti-Markovnikov."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .boro {{
            font-size:55px;
            color:#66FF99;
            animation:mover 1.5s infinite alternate;
        }}

        .oxidante {{
            font-size:55px;
            color:#FFD700;
            animation:ataque 1.5s infinite alternate;
        }}

        .shake {{
            animation:vibrar .5s infinite alternate;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 1s infinite alternate;
        }}

        @keyframes mover {{
            from {{ transform:translateX(120px); opacity:.4; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes ataque {{
            from {{ transform:translateX(-120px); opacity:.4; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0px); }}
            to {{ transform:translateX(20px); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Hidroboración-Oxidación — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += f"""
            <img class="mol shake" src="data:image/png;base64,{propeno}">
            <span class="arrow">➜</span>
            <span class="boro">BH₃</span>

            <h3>El BH₃ se aproxima al doble enlace.</h3>
            """

        elif paso_actual == 1:

            html += """
            <div style="font-size:55px;" class="shake">
                H
                \\<br>
                 C — C — BH₂
            </div>

            <h3>Adición sin (syn addition).</h3>
            """

        elif paso_actual == 2:

            html += """
            <div style="font-size:50px;" class="shake">
                CH₃-CH₂-CH₂-BH₂
            </div>

            <h3>Se forma el organoborano.</h3>
            """

        elif paso_actual == 3:

            html += """
            <span class="oxidante">H₂O₂ / OH⁻</span>

            <h3>Oxidación del enlace carbono-boro.</h3>
            """

        else:

            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">

            <h3>Producto final: 1-propanol.</h3>

            <h4 style="color:#66FF99;">
            Alcohol anti-Markovnikov
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=500, scrolling=False)
    if reaccion == "6. SN1":

        sustrato = mol_base64("CC(C)(C)Cl")
        producto = mol_base64("CC(C)(C)O")

        textos = [
            "El grupo saliente empieza a separarse del carbono terciario.",
            "Sale Cl⁻ y se forma un carbocatión estable.",
            "El nucleófilo se acerca al carbocatión plano.",
            "El nucleófilo forma un nuevo enlace con el carbono positivo.",
            "Se obtiene el producto de sustitución."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .leaving {{
            font-size:55px;
            color:#FF4D4D;
            animation:salida 1.5s infinite alternate;
        }}

        .nuc {{
            font-size:55px;
            color:#FFD700;
            animation:ataque 1.5s infinite alternate;
        }}

        .carbo {{
            font-size:55px;
            color:#00E5FF;
            animation:vibrar .5s infinite alternate;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 1s infinite alternate;
        }}

        @keyframes salida {{
            from {{ transform:translateX(0px); opacity:1; }}
            to {{ transform:translateX(140px); opacity:.3; }}
        }}

        @keyframes ataque {{
            from {{ transform:translateX(-140px); opacity:.3; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; }}
            to {{ box-shadow:0 0 35px lime; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0px); }}
            to {{ transform:translateX(20px); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Mecanismo SN1 — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += f"""
            <img class="mol" src="data:image/png;base64,{sustrato}">
            <span class="arrow">➜</span>
            <span class="leaving">Cl</span>

            <h3>El grupo saliente comienza a separarse.</h3>
            """

        elif paso_actual == 1:

            html += """
            <div class="carbo">
                (CH₃)₃C⁺ &nbsp;&nbsp; + &nbsp;&nbsp; Cl⁻
            </div>

            <h3>Se forma un carbocatión terciario estable.</h3>
            <h4 style="color:#00E5FF;">
            Este es el paso lento de la reacción.
            </h4>
            """

        elif paso_actual == 2:

            html += """
            <span class="nuc">OH⁻</span>
            <span class="arrow">➜</span>
            <span class="carbo">(CH₃)₃C⁺</span>

            <h3>El nucleófilo se aproxima al carbocatión.</h3>
            """

        elif paso_actual == 3:

            html += """
            <div class="carbo">
                (CH₃)₃C—OH
            </div>

            <h3>Se forma el nuevo enlace C—O.</h3>
            """

        else:

            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">

            <h3>Producto final: alcohol terciario.</h3>
            <h4 style="color:#FFD700;">
            Sustitución nucleofílica unimolecular.
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=500, scrolling=False)
    if reaccion == "7. SN2":

        sustrato = mol_base64("CBr")
        producto = mol_base64("CO")

        textos = [
            "El nucleófilo se aproxima por la parte posterior del carbono.",
            "Comienza a formarse el enlace C—Nu mientras el enlace C—Br se debilita.",
            "Se alcanza un estado de transición con enlaces parciales.",
            "El grupo saliente Br⁻ se aleja al mismo tiempo que entra el nucleófilo.",
            "Se obtiene el producto con inversión de configuración."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .nuc {{
            font-size:55px;
            color:#FFD700;
            animation:ataquePosterior 1.4s infinite alternate;
            display:inline-block;
        }}

        .leaving {{
            font-size:55px;
            color:#FF4D4D;
            animation:salida 1.4s infinite alternate;
            display:inline-block;
        }}

        .center {{
            font-size:55px;
            color:#00E5FF;
            animation:vibrar .4s infinite alternate;
            display:inline-block;
        }}

        .transition {{
            font-size:50px;
            color:#FFFFFF;
            animation:estado 0.7s infinite alternate;
            display:inline-block;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha 0.8s infinite alternate;
            display:inline-block;
        }}

        .bond-forming {{
            color:#00FF88;
            font-size:50px;
            animation:formarEnlace 1s infinite alternate;
            display:inline-block;
        }}

        .bond-breaking {{
            color:#FF4D4D;
            font-size:50px;
            animation:romperEnlace 1s infinite alternate;
            display:inline-block;
        }}

        .flip {{
            display:inline-block;
            animation:inversion 1.3s infinite alternate;
        }}

        @keyframes ataquePosterior {{
            from {{ transform:translateX(-180px); opacity:.25; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes salida {{
            from {{ transform:translateX(0px); opacity:1; }}
            to {{ transform:translateX(170px); opacity:.25; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-4deg) scale(1); }}
            to {{ transform:rotate(4deg) scale(1.08); }}
        }}

        @keyframes estado {{
            from {{ transform:scale(.95); text-shadow:0 0 8px #00E5FF; }}
            to {{ transform:scale(1.08); text-shadow:0 0 24px #FFD700; }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0px); }}
            to {{ transform:translateX(22px); }}
        }}

        @keyframes formarEnlace {{
            from {{ opacity:.25; transform:scaleX(.55); }}
            to {{ opacity:1; transform:scaleX(1.1); }}
        }}

        @keyframes romperEnlace {{
            from {{ opacity:1; transform:scaleX(1); }}
            to {{ opacity:.25; transform:scaleX(.45); }}
        }}

        @keyframes inversion {{
            from {{ transform:rotateY(0deg); }}
            to {{ transform:rotateY(180deg); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; transform:scale(1); }}
            to {{ box-shadow:0 0 35px lime; transform:scale(1.04); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Mecanismo SN2 — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += f"""
            <div>
                <span class="nuc">OH⁻</span>
                <span class="arrow">➜</span>
                <img class="mol" src="data:image/png;base64,{sustrato}">
            </div>

            <h3>El nucleófilo entra por atrás del carbono unido al Br.</h3>
            """

        elif paso_actual == 1:

            html += """
            <div style="font-size:52px;">
                <span class="nuc">OH⁻</span>
                <span class="bond-forming">···</span>
                <span class="center">CH₃</span>
                <span class="bond-breaking">—</span>
                <span class="leaving">Br</span>
            </div>

            <h3>El enlace C—O empieza a formarse y el enlace C—Br empieza a romperse.</h3>
            """

        elif paso_actual == 2:

            html += """
            <div class="transition">
                [ OH ··· CH₃ ··· Br ]‡
            </div>

            <h3>Estado de transición: ambos enlaces existen parcialmente.</h3>
            <h4 style="color:#FFD700;">Todo ocurre en un solo paso concertado.</h4>
            """

        elif paso_actual == 3:

            html += """
            <div style="font-size:52px;">
                <span class="bond-forming">OH—CH₃</span>
                <span class="arrow">+</span>
                <span class="leaving">Br⁻</span>
            </div>

            <h3>El Br⁻ se va mientras el nucleófilo queda unido al carbono.</h3>
            """

        else:

            html += f"""
            <div class="flip">
                <img class="mol product" src="data:image/png;base64,{producto}">
            </div>

            <h3>Producto final: metanol.</h3>
            <h4 style="color:#00E5FF;">
            Resultado clave: inversión de configuración.
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=520, scrolling=False)
    if reaccion == "8. Sustitución Aromática Electrofílica":

        benceno = mol_base64("c1ccccc1")
        producto = mol_base64("Brc1ccccc1")

        textos = [
            "El catalizador activa al Br₂ y genera un electrófilo fuerte.",
            "El anillo aromático ataca al electrófilo Br⁺.",
            "Se forma el complejo sigma y se pierde temporalmente la aromaticidad.",
            "Una base retira H⁺ del anillo.",
            "Se recupera la aromaticidad y se forma bromobenceno."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:340px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .ring {{
            animation:resonancia 1s infinite alternate;
        }}

        .electro {{
            font-size:55px;
            color:#FFD700;
            animation:entrada 1.5s infinite alternate;
            display:inline-block;
        }}

        .cat {{
            font-size:44px;
            color:#FF4D4D;
            animation:vibrar .5s infinite alternate;
            display:inline-block;
        }}

        .sigma {{
            font-size:48px;
            color:#00E5FF;
            animation:estado 0.7s infinite alternate;
            display:inline-block;
        }}

        .base {{
            font-size:50px;
            color:#66FF99;
            animation:ataqueBase 1.5s infinite alternate;
            display:inline-block;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha .8s infinite alternate;
            display:inline-block;
        }}

        @keyframes entrada {{
            from {{ transform:translateX(160px); opacity:.25; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes ataqueBase {{
            from {{ transform:translateX(-150px); opacity:.25; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes resonancia {{
            from {{ transform:scale(1); filter:drop-shadow(0 0 5px #00E5FF); }}
            to {{ transform:scale(1.05); filter:drop-shadow(0 0 20px #FFD700); }}
        }}

        @keyframes estado {{
            from {{ transform:scale(.95); text-shadow:0 0 8px #00E5FF; }}
            to {{ transform:scale(1.08); text-shadow:0 0 25px #FFD700; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0px); }}
            to {{ transform:translateX(22px); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; transform:scale(1); }}
            to {{ box-shadow:0 0 35px lime; transform:scale(1.04); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Sustitución Aromática Electrofílica — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += """
            <div>
                <span class="cat">Br₂ + FeBr₃</span>
                <span class="arrow">➜</span>
                <span class="electro">Br⁺</span>
            </div>

            <h3>El catalizador genera el electrófilo bromonio.</h3>
            """

        elif paso_actual == 1:

            html += f"""
            <img class="mol ring" src="data:image/png;base64,{benceno}">
            <span class="arrow">➜</span>
            <span class="electro">Br⁺</span>

            <h3>Los electrones π del anillo atacan al Br⁺.</h3>
            """

        elif paso_actual == 2:

            html += """
            <div class="sigma">
                [ Complejo σ ]⁺
                <br>
                C₆H₆—Br⁺
            </div>

            <h3>La aromaticidad se pierde temporalmente.</h3>
            <h4 style="color:#FFD700;">Intermediario clave: complejo sigma.</h4>
            """

        elif paso_actual == 3:

            html += """
            <span class="base">FeBr₄⁻</span>
            <span class="arrow">➜</span>
            <span class="sigma">H⁺</span>

            <h3>Una base retira el protón del anillo.</h3>
            """

        else:

            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">

            <h3>Producto final: bromobenceno.</h3>
            <h4 style="color:#00E5FF;">
            El anillo recupera su aromaticidad.
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=520, scrolling=False)
    if reaccion == "9. Sustitución Aromática Nucleofílica":

        sustrato = mol_base64("O=[N+]([O-])c1ccc(Cl)cc1")
        producto = mol_base64("O=[N+]([O-])c1ccc(O)cc1")

        textos = [
            "El nucleófilo se aproxima al anillo aromático activado.",
            "El nucleófilo ataca al carbono unido al grupo saliente.",
            "Se forma el complejo de Meisenheimer y se pierde temporalmente la aromaticidad.",
            "El grupo saliente Cl⁻ abandona el anillo.",
            "Se recupera la aromaticidad y se forma el producto sustituido."
        ]

        html = f"""
        <html>
        <head>
        <style>
        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:360px;
            background:#ffffff;
            border-radius:22px;
            padding:14px;
            margin:12px;
            box-shadow:0 0 25px #00E5FF;
            border:3px solid #00E5FF;
        }}

        .ring {{
            animation:resonancia 1s infinite alternate;
        }}

        .nuc {{
            font-size:55px;
            color:#FFD700;
            animation:ataqueNuc 1.4s infinite alternate;
            display:inline-block;
        }}

        .leaving {{
            font-size:55px;
            color:#FF4D4D;
            animation:salida 1.4s infinite alternate;
            display:inline-block;
        }}

        .meisen {{
            font-size:48px;
            color:#00E5FF;
            animation:estado 0.7s infinite alternate;
            display:inline-block;
        }}

        .ewg {{
            font-size:42px;
            color:#66FF99;
            animation:vibrar .5s infinite alternate;
            display:inline-block;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha .8s infinite alternate;
            display:inline-block;
        }}

        @keyframes ataqueNuc {{
            from {{ transform:translateX(-160px); opacity:.25; }}
            to {{ transform:translateX(0px); opacity:1; }}
        }}

        @keyframes salida {{
            from {{ transform:translateX(0px); opacity:1; }}
            to {{ transform:translateX(160px); opacity:.25; }}
        }}

        @keyframes resonancia {{
            from {{ transform:scale(1); filter:drop-shadow(0 0 5px #00E5FF); }}
            to {{ transform:scale(1.05); filter:drop-shadow(0 0 20px #FFD700); }}
        }}

        @keyframes estado {{
            from {{ transform:scale(.95); text-shadow:0 0 8px #00E5FF; }}
            to {{ transform:scale(1.08); text-shadow:0 0 25px #FFD700; }}
        }}

        @keyframes vibrar {{
            from {{ transform:rotate(-3deg); }}
            to {{ transform:rotate(3deg); }}
        }}

        @keyframes flecha {{
            from {{ transform:translateX(0px); }}
            to {{ transform:translateX(22px); }}
        }}

        @keyframes brillar {{
            from {{ box-shadow:0 0 8px lime; transform:scale(1); }}
            to {{ box-shadow:0 0 35px lime; transform:scale(1.04); }}
        }}
        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Sustitución Aromática Nucleofílica — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += f"""
            <span class="nuc">OH⁻</span>
            <span class="arrow">➜</span>
            <img class="mol ring" src="data:image/png;base64,{sustrato}">

            <h3>El nucleófilo se acerca a un anillo activado por un grupo atractor de electrones.</h3>
            <h4 style="color:#66FF99;">Grupo activador: NO₂</h4>
            """

        elif paso_actual == 1:

            html += f"""
            <span class="nuc">OH⁻</span>
            <span class="arrow">➜</span>
            <img class="mol ring" src="data:image/png;base64,{sustrato}">

            <h3>El OH⁻ ataca el carbono unido al Cl.</h3>
            """

        elif paso_actual == 2:

            html += """
            <div class="meisen">
                [ Complejo de Meisenheimer ]⁻
                <br>
                Anillo con carga deslocalizada
            </div>

            <h3>La aromaticidad se pierde temporalmente.</h3>
            <h4 style="color:#FFD700;">Intermediario clave de la SNAr.</h4>
            """

        elif paso_actual == 3:

            html += """
            <span class="meisen">Ar—OH</span>
            <span class="arrow">+</span>
            <span class="leaving">Cl⁻</span>

            <h3>El Cl⁻ sale y el anillo empieza a recuperar estabilidad.</h3>
            """

        else:

            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">

            <h3>Producto final: aromático sustituido por OH.</h3>
            <h4 style="color:#00E5FF;">
            Se recupera la aromaticidad del anillo.
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=540, scrolling=False)
    if reaccion == "10. Sustitución Radicalaria":

        metano = mol_base64("C")
        producto = mol_base64("CCl")

        textos = [
            "La luz UV rompe el Cl₂ formando radicales.",
            "Un radical Cl• extrae un H del metano.",
            "Se forma un radical metilo CH₃•.",
            "El radical metilo reacciona con Cl₂.",
            "Se forma clorometano y continúa la cadena."
        ]

        html = f"""
        <html>
        <head>
        <style>

        body {{
            margin:0;
            background:#08111F;
            color:white;
            font-family:Arial;
        }}

        .box {{
            border:2px solid #00E5FF;
            border-radius:22px;
            padding:25px;
            text-align:center;
            overflow:hidden;
        }}

        .mol {{
            width:360px;
            background:white;
            border-radius:22px;
            padding:14px;
            margin:12px;
            border:3px solid #00E5FF;
            box-shadow:0 0 25px #00E5FF;
        }}

        .radical {{
            font-size:60px;
            color:#FF4D4D;
            animation:radicalMove 1s infinite alternate;
            display:inline-block;
        }}

        .uv {{
            font-size:70px;
            animation:flash .5s infinite alternate;
            display:inline-block;
        }}

        .chain {{
            font-size:55px;
            color:#FFD700;
            animation:vibrar .5s infinite alternate;
            display:inline-block;
        }}

        .product {{
            animation:brillar 1s infinite alternate;
        }}

        .arrow {{
            font-size:55px;
            color:#00E5FF;
            animation:flecha .8s infinite alternate;
            display:inline-block;
        }}

        @keyframes flash {{
            from {{
                opacity:.4;
                text-shadow:0 0 5px yellow;
            }}
            to {{
                opacity:1;
                text-shadow:0 0 30px yellow;
            }}
        }}

        @keyframes radicalMove {{
            from {{
                transform:translateX(-40px);
                opacity:.5;
            }}
            to {{
                transform:translateX(40px);
                opacity:1;
            }}
        }}

        @keyframes vibrar {{
            from {{
                transform:rotate(-3deg);
            }}
            to {{
                transform:rotate(3deg);
            }}
        }}

        @keyframes flecha {{
            from {{
                transform:translateX(0px);
            }}
            to {{
                transform:translateX(20px);
            }}
        }}

        @keyframes brillar {{
            from {{
                box-shadow:0 0 8px lime;
                transform:scale(1);
            }}
            to {{
                box-shadow:0 0 35px lime;
                transform:scale(1.04);
            }}
        }}

        </style>
        </head>

        <body>
        <div class="box">

        <h2>🎬 Sustitución Radicalaria — Paso {paso_actual + 1}</h2>
        <h3>{textos[paso_actual]}</h3>
        """

        if paso_actual == 0:

            html += """
            <div class="uv">☀️ UV</div>

            <br><br>

            <div class="chain">
            Cl₂
            </div>

            <span class="arrow">➜</span>

            <div class="radical">
            Cl• + •Cl
            </div>

            <h3>Etapa de iniciación.</h3>
            """

        elif paso_actual == 1:

            html += f"""
            <span class="radical">Cl•</span>

            <span class="arrow">➜</span>

            <img class="mol" src="data:image/png;base64,{metano}">

            <h3>El radical cloro arranca un hidrógeno.</h3>
            """

        elif paso_actual == 2:

            html += """
            <div class="chain">
                CH₃•
            </div>

            <span class="arrow">+</span>

            <div class="chain">
                HCl
            </div>

            <h3>Se forma el radical metilo.</h3>
            """

        elif paso_actual == 3:

            html += """
            <div class="chain">
                CH₃•
            </div>

            <span class="arrow">➜</span>

            <div class="chain">
                Cl₂
            </div>

            <h3>Comienza la propagación de la cadena radicalaria.</h3>
            """

        else:

            html += f"""
            <img class="mol product" src="data:image/png;base64,{producto}">

            <h3>Producto final: clorometano.</h3>

            <h4 style="color:#FFD700;">
            La reacción continúa mediante un mecanismo en cadena.
            </h4>
            """

        html += """
        </div>
        </body>
        </html>
        """

        components.html(html, height=540, scrolling=False)
    else:
        st.info("Por ahora la simulación molecular avanzada está activada para Halogenación.")
    st.subheader("📖 Panel explicativo")

  # =====================================================
# 🧪 PROBLEMAS TIPO OLIMPIADA GAMIFICADOS MEJORADOS
# =====================================================

elif selected == "Ejercicios":

     # CSS visual
    st.markdown("""
    <style>
    .game-card {
        background: #FFFDE7;
        padding: 25px;
        border-radius: 25px;
        border: 2px solid #FDE68A;
        box-shadow: 0 0 20px rgba(245,158,11,0.25);
        color: #0F172A !important;
        margin: 20px 0;
        animation: aparecer 0.8s ease-in-out;
    }

    .game-card p,
    .game-card div,
    .game-card span,
    .game-card b {
        color: #0F172A !important;
    }

    .reto-title {
        text-align: center;
        font-size: 38px;
        color: #0F172A;
        text-shadow: 0 0 10px rgba(245,158,11,0.35);
        animation: brillo 2s infinite alternate;
    }

    .formula-box {
        background: #FFFDE7;
        color: #0F172A !important;
        padding: 18px;
        border-radius: 15px;
        font-size: 24px;
        text-align: center;
        border: 2px solid #FDE68A;
        box-shadow: 0 0 18px rgba(245,158,11,0.25);
        margin: 15px 0;
    }

    .badge-xp {
        background: linear-gradient(90deg, #FEF3C7, #FDE68A);
        color: #0F172A !important;
        padding: 10px 18px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
        border: 1px solid #FACC15;
    }

    @keyframes aparecer {
        from {opacity: 0; transform: translateY(25px);}
        to {opacity: 1; transform: translateY(0);}
    }

    @keyframes brillo {
        from {text-shadow: 0 0 8px rgba(245,158,11,0.25);}
        to {text-shadow: 0 0 20px rgba(245,158,11,0.55);}
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="reto-title">🧪 RETOS OLIMPIADA GAMIFICADOS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="game-card">
    🎮 Bienvenido al modo reto.
    Aquí practicarás <b>reacciones de adición</b>, <b>sustitución</b> y <b>mecanismos orgánicos</b>
    como si fuera un videojuego químico.
    <br><br>
    <span class="badge-xp">⚡ XP</span>
    <span class="badge-xp">🏆 Logros</span>
    <span class="badge-xp">🧠 Pistas</span>
    <span class="badge-xp">🔥 Nivel Olimpiada</span>
    </div>
    """, unsafe_allow_html=True)

    if "xp_ejercicios" not in st.session_state:
        st.session_state.xp_ejercicios = 0

    if "retos_completados" not in st.session_state:
        st.session_state.retos_completados = 0

    # =================================================
    # MENÚ DE RETOS
    # =================================================

    reto = st.selectbox(
        "🎯 Selecciona un reto",
        [
            "🎯 Ordenar mecanismo SN1",
            "🧪 Elegir producto",
            "⚡ ¿Qué sigue?",
            "🧬 Completar reacción",
            "🔁 Comparar SN1 y SN2",
            "💥 Identificar tipo de reacción",
            "🏆 Reto final"
        ]
    )

    def sumar_xp(nombre, puntos):
        st.session_state.xp_ejercicios += puntos
        st.session_state.retos_completados += 1
        guardar_puntos(nombre, puntos)
        st.balloons()
        st.success(f"🎉 ¡Correcto! Ganaste {puntos} XP")

    # =================================================
    # RETO 1
    # =================================================

    if reto == "🎯 Ordenar mecanismo SN1":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("🎯 Ordena el mecanismo SN1")

        st.info("En una reacción SN1, el proceso ocurre por etapas y se forma un carbocatión.")

        opcion1 = st.selectbox(
            "Paso 1",
            ["Ataque nucleofílico", "Formación del carbocatión", "Salida del grupo saliente"],
            key="sn1_1"
        )

        opcion2 = st.selectbox(
            "Paso 2",
            ["Ataque nucleofílico", "Formación del carbocatión", "Salida del grupo saliente"],
            key="sn1_2"
        )

        opcion3 = st.selectbox(
            "Paso 3",
            ["Ataque nucleofílico", "Formación del carbocatión", "Salida del grupo saliente"],
            key="sn1_3"
        )

        if st.button("🚀 Verificar orden"):

            if (
                opcion1 == "Salida del grupo saliente"
                and opcion2 == "Formación del carbocatión"
                and opcion3 == "Ataque nucleofílico"
            ):
                sumar_xp("Ordenar mecanismo SN1", 100)
                st.progress(100)
                st.markdown("### 🧠 Secuencia correcta: Grupo saliente → Carbocatión → Nucleófilo")
            else:
                st.error("❌ Orden incorrecto")
                st.warning("💡 Pista: en SN1 primero se separa el grupo saliente.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO 2
    # =================================================

    elif reto == "🧪 Elegir producto":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("🧪 Predice el producto")

        st.markdown('<div class="formula-box">CH₃–CH=CH₂ + HBr → ?</div>', unsafe_allow_html=True)

        respuesta = st.radio(
            "Selecciona el producto correcto",
            [
                "CH₃–CH₂–CH₃",
                "CH₃–CHBr–CH₃",
                "CH₂Br–CH₂–CH₃"
            ]
        )

        if st.button("✅ Comprobar producto"):

            if respuesta == "CH₃–CHBr–CH₃":
                sumar_xp("Producto Markovnikov", 100)
                st.snow()
                st.info("📌 Se aplica Markovnikov: el Br queda en el carbono más sustituido.")
            else:
                st.error("❌ Incorrecto")
                st.info("💡 Recuerda: en la adición de HBr a propeno, el Br se une al carbono central.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO 3
    # =================================================

    elif reto == "⚡ ¿Qué sigue?":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("⚡ ¿Qué ocurre después?")

        st.markdown("""
        ### Paso actual:
        El alqueno acaba de captar H⁺.
        """)

        respuesta = st.radio(
            "¿Qué sigue ahora?",
            [
                "Ataque nucleofílico",
                "Formación del carbocatión",
                "Eliminación"
            ]
        )

        if st.button("⚡ Verificar paso"):

            if respuesta == "Formación del carbocatión":
                sumar_xp("Secuencia de adición", 100)
            else:
                st.error("❌ Incorrecto")
                st.warning("💡 Después de captar H⁺, se forma un carbocatión.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO 4
    # =================================================

    elif reto == "🧬 Completar reacción":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("🧬 Completa la reacción")

        st.markdown('<div class="formula-box">CH₃–CH=CH₂ + _____ → alcohol</div>', unsafe_allow_html=True)

        respuesta = st.radio(
            "Selecciona el reactivo correcto",
            [
                "H₂O/H⁺",
                "Br₂",
                "H₂/Pt"
            ]
        )

        if st.button("🧪 Completar"):

            if respuesta == "H₂O/H⁺":
                sumar_xp("Hidratación de alqueno", 100)
                st.info("📌 H₂O/H⁺ corresponde a una hidratación ácida.")
            else:
                st.error("❌ Incorrecto")
                st.warning("💡 Para formar un alcohol desde un alqueno se usa agua en medio ácido.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO 5
    # =================================================

    elif reto == "🔁 Comparar SN1 y SN2":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("🔁 Comparación rápida")

        respuesta = st.radio(
            "¿Cuál mecanismo ocurre en una sola etapa?",
            [
                "SN1",
                "SN2",
                "Ambos"
            ]
        )

        if st.button("🔍 Revisar"):

            if respuesta == "SN2":
                sumar_xp("Comparación SN1/SN2", 120)
                st.info("📌 SN2 ocurre en una sola etapa con ataque posterior.")
            else:
                st.error("❌ Incorrecto")
                st.warning("💡 SN1 tiene carbocatión; SN2 ocurre en un solo paso.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO 6
    # =================================================

    elif reto == "💥 Identificar tipo de reacción":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("💥 Identifica la reacción")

        st.markdown('<div class="formula-box">CH₂=CH₂ + Br₂ → BrCH₂–CH₂Br</div>', unsafe_allow_html=True)

        respuesta = st.radio(
            "¿Qué tipo de reacción es?",
            [
                "Sustitución",
                "Adición",
                "Eliminación"
            ]
        )

        if st.button("🧠 Identificar"):

            if respuesta == "Adición":
                sumar_xp("Identificar adición", 100)
                st.info("📌 El doble enlace se rompe y se agregan dos bromos.")
            else:
                st.error("❌ Incorrecto")
                st.warning("💡 Si se rompe un doble enlace y se agregan átomos, es adición.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # RETO FINAL
    # =================================================

    elif reto == "🏆 Reto final":

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.header("🏆 RETO FINAL")

        st.warning("🔥 Nivel Olimpiada")

        st.markdown("""
        <div class="formula-box">
        CH₃–CH=CH₂ <br>
        ↓ HBr <br>
        ↓ NaOH <br>
        Resultado final: ?
        </div>
        """, unsafe_allow_html=True)

        respuesta = st.radio(
            "¿Qué ocurre al final?",
            [
                "Se forma un alcano",
                "Se forma un alcohol",
                "Se forma un alqueno"
            ]
        )

        if st.button("🏆 Resolver reto final"):

            if respuesta == "Se forma un alcohol":
                sumar_xp("Reto Final", 300)
                st.snow()
                st.markdown("""
                # 🎉 ORGANIC MASTER 🎉
                Has completado el reto final.
                """)
                st.progress(100)
            else:
                st.error("❌ Incorrecto")
                st.info("💡 Primero ocurre adición de HBr y después sustitución con NaOH.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =================================================
    # PANEL XP
    # =================================================

    st.divider()

    st.subheader("🎮 Sistema de progreso")

    xp = st.session_state.xp_ejercicios
    retos = st.session_state.retos_completados
    nivel = 1 + xp // 300

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏆 XP", xp)

    with col2:
        st.metric("🔥 Nivel", nivel)

    with col3:
        st.metric("🧪 Retos completados", retos)

    progreso = min(xp / 1000, 1.0)
    st.progress(progreso)

    if xp >= 1000:
        st.success("🏆 ¡Has desbloqueado el rango: Maestro de Reacciones Orgánicas!")
    elif xp >= 500:
        st.info("⚡ Rango actual: Aprendiz Avanzado")
    else:
        st.warning("🧪 Rango actual: Aprendiz Químico")
 # =====================================================
# 📝 QUIZ UNIVERSITARIO AVANZADO
# 20 PREGUNTAS — ADICIÓN Y SUSTITUCIÓN
# =====================================================

elif selected == "Quiz":

    import base64

    st.title("📝 QUIZ UNIVERSITARIO DE QUÍMICA ORGÁNICA")

    st.markdown("""
    <div class="card">
    <h2>🎯 Evaluación general</h2>
    <p>
    Este quiz contiene 20 preguntas sobre reacciones de adición,
    sustitución, mecanismos, intermediarios, reglas, productos,
    aplicaciones e impacto ambiental.
    </p>
    <p>
    Responde todas las preguntas y al final presiona el botón
    <b>Finalizar quiz</b>.
    </p>
    </div>
    """, unsafe_allow_html=True)

    preguntas = [
        {
            "pregunta": "1. ¿Qué ocurre principalmente en una reacción de adición?",
            "opciones": [
                "Se elimina un grupo funcional",
                "Se rompe un doble enlace y se agregan átomos nuevos",
                "Se forma siempre un anillo aromático",
                "Se sustituye un hidrógeno por un radical"
            ],
            "correcta": "Se rompe un doble enlace y se agregan átomos nuevos",
            "explicacion": "En una reacción de adición, el enlace π del alqueno se rompe y permite que nuevos átomos se unan a los carbonos."
        },
        {
            "pregunta": "2. ¿Cuál es el producto principal de la hidrogenación de un alqueno?",
            "opciones": [
                "Alcohol",
                "Alcano",
                "Halogenuro de alquilo",
                "Radical libre"
            ],
            "correcta": "Alcano",
            "explicacion": "La hidrogenación agrega H₂ al doble enlace y convierte el alqueno en un alcano saturado."
        },
        {
            "pregunta": "3. ¿Qué catalizadores se usan comúnmente en hidrogenación?",
            "opciones": [
                "Pt, Pd o Ni",
                "NaOH o H₂O₂",
                "FeBr₃ o AlCl₃",
                "HCl o HBr"
            ],
            "correcta": "Pt, Pd o Ni",
            "explicacion": "La hidrogenación necesita metales como platino, paladio o níquel para activar el hidrógeno."
        },
        {
            "pregunta": "4. ¿Qué intermediario se forma en la halogenación de alquenos con Br₂?",
            "opciones": [
                "Carbocatión libre",
                "Ion bromonio",
                "Carbanión",
                "Radical metilo"
            ],
            "correcta": "Ion bromonio",
            "explicacion": "En la halogenación, el bromo forma un puente cíclico llamado ion bromonio."
        },
        {
            "pregunta": "5. La halogenación de alquenos suele presentar:",
            "opciones": [
                "Adición anti",
                "Adición syn obligatoria",
                "Sustitución radicalaria",
                "Eliminación de agua"
            ],
            "correcta": "Adición anti",
            "explicacion": "El segundo halógeno ataca por la cara opuesta, por eso el producto se forma con adición anti."
        },
        {
            "pregunta": "6. ¿Qué producto se obtiene en la hidratación ácida de un alqueno?",
            "opciones": [
                "Alcano",
                "Alcohol",
                "Dihaluro",
                "Éter aromático"
            ],
            "correcta": "Alcohol",
            "explicacion": "La hidratación agrega H y OH al doble enlace, formando un alcohol."
        },
        {
            "pregunta": "7. ¿Qué regla sigue normalmente la hidratación ácida?",
            "opciones": [
                "Regla anti-Markovnikov",
                "Regla de Markovnikov",
                "Regla de Hund",
                "Regla de octeto únicamente"
            ],
            "correcta": "Regla de Markovnikov",
            "explicacion": "El H se une al carbono con más hidrógenos y el OH queda en el carbono más sustituido."
        },
        {
            "pregunta": "8. ¿Qué tipo de producto se forma en la adición de HX a un alqueno?",
            "opciones": [
                "Halogenuro de alquilo",
                "Alcohol primario",
                "Benceno",
                "Cetona"
            ],
            "correcta": "Halogenuro de alquilo",
            "explicacion": "HX aporta H y X; el halógeno queda unido a un carbono, formando un halogenuro de alquilo."
        },
        {
            "pregunta": "9. En la adición de HX, ¿hacia dónde va el hidrógeno según Markovnikov?",
            "opciones": [
                "Al carbono con más hidrógenos",
                "Al carbono con menos hidrógenos",
                "Al halógeno",
                "Al catalizador"
            ],
            "correcta": "Al carbono con más hidrógenos",
            "explicacion": "La regla de Markovnikov indica que el hidrógeno se une al carbono que ya posee más hidrógenos."
        },
        {
            "pregunta": "10. ¿Qué característica distingue a la hidroboración-oxidación?",
            "opciones": [
                "Forma alcoholes anti-Markovnikov",
                "Siempre forma radicales libres",
                "Rompe el anillo aromático",
                "Produce solamente alcanos"
            ],
            "correcta": "Forma alcoholes anti-Markovnikov",
            "explicacion": "La hidroboración-oxidación coloca el OH en el carbono menos sustituido, por eso es anti-Markovnikov."
        },
        {
            "pregunta": "11. ¿Qué geometría presenta la hidroboración?",
            "opciones": [
                "Syn",
                "Anti",
                "Racemización completa",
                "No tiene geometría"
            ],
            "correcta": "Syn",
            "explicacion": "En la hidroboración, B y H se agregan al mismo tiempo por la misma cara del doble enlace."
        },
        {
            "pregunta": "12. ¿Qué significa SN1?",
            "opciones": [
                "Sustitución nucleofílica unimolecular",
                "Sustitución nucleofílica bimolecular",
                "Síntesis normal de primer orden",
                "Sustitución no polar"
            ],
            "correcta": "Sustitución nucleofílica unimolecular",
            "explicacion": "SN1 significa sustitución nucleofílica unimolecular, porque el paso lento depende de una sola molécula."
        },
        {
            "pregunta": "13. ¿Cuál es el intermediario característico de SN1?",
            "opciones": [
                "Carbocatión",
                "Ion bromonio",
                "Complejo sigma",
                "Radical cloro"
            ],
            "correcta": "Carbocatión",
            "explicacion": "En SN1 primero sale el grupo saliente y queda un carbocatión."
        },
        {
            "pregunta": "14. ¿Qué sustratos favorecen mejor una reacción SN1?",
            "opciones": [
                "Terciarios",
                "Metilo únicamente",
                "Primarios sin ramificación",
                "Aromáticos sin sustituyentes"
            ],
            "correcta": "Terciarios",
            "explicacion": "Los carbonos terciarios estabilizan mejor el carbocatión formado en SN1."
        },
        {
            "pregunta": "15. ¿Qué significa SN2?",
            "opciones": [
                "Sustitución nucleofílica bimolecular",
                "Sustitución nucleofílica unimolecular",
                "Síntesis no reactiva",
                "Sustitución neutra doble"
            ],
            "correcta": "Sustitución nucleofílica bimolecular",
            "explicacion": "SN2 ocurre en un solo paso donde participan el nucleófilo y el sustrato."
        },
        {
            "pregunta": "16. ¿Qué ocurre en una reacción SN2?",
            "opciones": [
                "Ataque posterior e inversión de configuración",
                "Formación de carbocatión plano",
                "Adición de H₂",
                "Ruptura de aromaticidad permanente"
            ],
            "correcta": "Ataque posterior e inversión de configuración",
            "explicacion": "El nucleófilo ataca por detrás y provoca inversión, conocida como efecto paraguas."
        },
        {
            "pregunta": "17. ¿Qué intermediario aparece en la sustitución aromática electrofílica?",
            "opciones": [
                "Complejo sigma",
                "Radical metilo",
                "Ion bromonio",
                "Organoborano"
            ],
            "correcta": "Complejo sigma",
            "explicacion": "El anillo aromático forma temporalmente un complejo sigma antes de recuperar la aromaticidad."
        },
        {
            "pregunta": "18. ¿Por qué el benceno prefiere sustitución en lugar de adición?",
            "opciones": [
                "Porque conserva la aromaticidad",
                "Porque no tiene electrones",
                "Porque siempre forma alcoholes",
                "Porque no puede reaccionar con electrófilos"
            ],
            "correcta": "Porque conserva la aromaticidad",
            "explicacion": "El benceno evita perder su estabilidad aromática; por eso sustituye un H en vez de romper el anillo."
        },
        {
            "pregunta": "19. ¿Cuáles son las etapas de la sustitución radicalaria?",
            "opciones": [
                "Iniciación, propagación y terminación",
                "Oxidación, reducción y neutralización",
                "Ataque, resonancia y equilibrio",
                "Hidratación, halogenación y combustión"
            ],
            "correcta": "Iniciación, propagación y terminación",
            "explicacion": "La sustitución radicalaria ocurre en cadena: se forman radicales, reaccionan y finalmente se terminan."
        },
        {
            "pregunta": "20. ¿Qué genera la luz UV en la sustitución radicalaria con Cl₂?",
            "opciones": [
                "Radicales Cl•",
                "Alcoholes",
                "Iones bromonio",
                "Carbocationes terciarios"
            ],
            "correcta": "Radicales Cl•",
            "explicacion": "La luz UV rompe Cl₂ de forma homolítica y produce radicales cloro."
        }
    ]

    respuestas_usuario = {}

    st.divider()

    for i, item in enumerate(preguntas):

        st.markdown(f"""
        <div class="card">
        <h3>{item["pregunta"]}</h3>
        <p>
        Selecciona la opción que consideres correcta.
        </p>
        </div>
        """, unsafe_allow_html=True)

        respuestas_usuario[i] = st.radio(
            "Opciones:",
            item["opciones"],
            key=f"quiz_pregunta_{i}",
            index=None
        )

        st.write("")

    st.divider()

    st.markdown("## 🏁 Finalizar evaluación")

    finalizar = st.button("✅ Finalizar quiz")


    if finalizar:

        sin_contestar = [
            i + 1 for i, r in respuestas_usuario.items() if r is None
        ]

        if len(sin_contestar) > 0:
            st.error("⚠️ Todavía faltan preguntas por contestar.")
            st.warning(f"Preguntas sin responder: {sin_contestar}")

        else:
            aciertos = 0
            total = len(preguntas)

            for i, item in enumerate(preguntas):
                if respuestas_usuario[i] == item["correcta"]:
                    aciertos += 1

            promedio = (aciertos / total) * 100

            guardar_puntos("Quiz Universitario", aciertos * 50)

            st.balloons()

            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #22c55e, #0ea5e9, #1e1b4b);
                padding: 35px;
                border-radius: 25px;
                text-align: center;
                border: 4px solid #FDE047;
                box-shadow: 0px 0px 35px rgba(253,224,71,0.8);
            ">
                <h1>🎉 RESULTADO FINAL 🎉</h1>
                <h2>✅ Preguntas correctas: {aciertos} de {total}</h2>
                <h2>📊 Promedio obtenido: {promedio:.1f}%</h2>
            </div>
            """, unsafe_allow_html=True)

            st.divider()
            st.header("📋 Revisión de respuestas")

            for i, item in enumerate(preguntas):

                respuesta = respuestas_usuario[i]

                if respuesta == item["correcta"]:

                    st.success(f"✅ Pregunta {i + 1}: Correcta")
                    st.write(f"**Tu respuesta:** {respuesta}")
                    st.info(f"🧠 ¿Por qué es correcta? {item['explicacion']}")

                else:

                    st.error(f"❌ Pregunta {i + 1}: Incorrecta")
                    st.write(f"**Tu respuesta:** {respuesta}")
                    st.write(f"**Respuesta correcta:** {item['correcta']}")
                    st.warning(
                        f"🧠 ¿Por qué es incorrecta? "
                        f"Tu respuesta no corresponde al concepto evaluado. "
                        f"La opción correcta es **{item['correcta']}** porque {item['explicacion']}"
                    )

            st.divider()
            st.metric("✅ Correctas", f"{aciertos}/{total}")
            st.metric("📊 Promedio", f"{promedio:.1f}%")
            st.metric("🏆 XP ganado", aciertos * 50)
            st.progress(int(promedio))
 # =====================================================
# ⚗️ LABORATORIO VIRTUAL AVANZADO
# =====================================================

elif selected == "Laboratorio":

    st.title("⚗️ LABORATORIO VIRTUAL")

    st.markdown("""
    Bienvenido al laboratorio interactivo.

    Aquí podrás:
    • seleccionar reactivos
    • modificar condiciones
    • simular reacciones
    • observar productos
    • analizar mecanismos

    🧪 Tema:
    Reacciones de adición y sustitución.
    """)

    # =================================================
    # TIPO DE REACCIÓN
    # =================================================

    tipo = st.selectbox(
        "Selecciona el tipo de reacción",
        [
            "Reacciones de Adición",
            "Reacciones de Sustitución"
        ]
    )

    # =================================================
    # ADICIÓN
    # =================================================

    if tipo == "Reacciones de Adición":

        reaccion = st.selectbox(
            "Selecciona una reacción",
            [
                "Hidrogenación",
                "Halogenación",
                "Hidratación",
                "Adición HX",
                "Hidroboración-Oxidación"
            ]
        )

    # =================================================
    # SUSTITUCIÓN
    # =================================================

    elif tipo == "Reacciones de Sustitución":

        reaccion = st.selectbox(
            "Selecciona una reacción",
            [
                "SN1",
                "SN2",
                "Sustitución Aromática",
                "Sustitución Radicalaria",
                "Sustitución Nucleofílica Aromática"
            ]
        )

    st.divider()

    # =================================================
    # CONFIGURACIÓN EXPERIMENTAL
    # =================================================

    st.subheader("🧪 Configuración experimental")

    col1, col2 = st.columns(2)

    with col1:

        temperatura = st.slider(
            "🌡️ Temperatura (°C)",
            0,
            300,
            25
        )

        presion = st.slider(
            "⚙️ Presión (atm)",
            1,
            20,
            1
        )

        tiempo = st.slider(
            "⏳ Tiempo de reacción (min)",
            1,
            180,
            30
        )

    with col2:

        solvente = st.selectbox(
            "💧 Solvente",
            [
                "Agua",
                "Etanol",
                "Acetona",
                "Hexano",
                "Metanol"
            ]
        )

        catalizador = st.selectbox(
            "⚡ Catalizador",
            [
                "Ninguno",
                "Pt",
                "Pd",
                "Ni",
                "FeBr3",
                "H2SO4"
            ]
        )

        concentracion = st.slider(
            "🧬 Concentración (mol/L)",
            1,
            10,
            2
        )

    st.divider()

    # =================================================
    # INICIAR SIMULACIÓN
    # =================================================

    if st.button("🚀 Iniciar simulación"):

        st.balloons()

        barra = st.progress(0)

        for i in range(100):
            barra.progress(i + 1)

        st.success("✅ Simulación completada")

        st.divider()

        # =============================================
        # RESULTADOS
        # =============================================

        st.header("📊 Resultados experimentales")

        st.write(f"🧪 Reacción: {reaccion}")
        st.write(f"🌡️ Temperatura: {temperatura} °C")
        st.write(f"⚙️ Presión: {presion} atm")
        st.write(f"💧 Solvente: {solvente}")
        st.write(f"⚡ Catalizador: {catalizador}")
        st.write(f"🧬 Concentración: {concentracion} mol/L")

        st.divider()

        # =============================================
        # RESULTADOS ESPECÍFICOS
        # =============================================

        # ---------------------------------------------
        # HIDROGENACIÓN
        # ---------------------------------------------

        if reaccion == "Hidrogenación":

            st.subheader("⚡ Resultado de Hidrogenación")

            st.code("CH2=CH2 + H2 → CH3-CH3")

            if catalizador in ["Pt","Pd","Ni"]:

                st.success("""
                ✅ Hidrogenación exitosa.
                """)

                st.info("""
                El doble enlace fue reducido.
                """)

                rendimiento = 92

            else:

                st.error("""
                ❌ No ocurrió la reacción.
                """)

                rendimiento = 10

        # ---------------------------------------------
        # HALOGENACIÓN
        # ---------------------------------------------

        elif reaccion == "Halogenación":

            st.subheader("⚡ Resultado de Halogenación")

            st.code("CH2=CH2 + Br2")

            st.success("""
            ✅ Formación de dihaluro.
            """)

            rendimiento = 88

        # ---------------------------------------------
        # HIDRATACIÓN
        # ---------------------------------------------

        elif reaccion == "Hidratación":

            st.subheader("💧 Resultado de Hidratación")

            if catalizador == "H2SO4":

                st.success("""
                ✅ Formación de alcohol.
                """)

                rendimiento = 90

            else:

                st.warning("""
                ⚠️ Reacción poco eficiente.
                """)

                rendimiento = 40

        # ---------------------------------------------
        # ADICIÓN HX
        # ---------------------------------------------

        elif reaccion == "Adición HX":

            st.subheader("🔥 Resultado Adición HX")

            st.success("""
            ✅ Producto Markovnikov obtenido.
            """)

            rendimiento = 87

        # ---------------------------------------------
        # HIDROBORACIÓN
        # ---------------------------------------------

        elif reaccion == "Hidroboración-Oxidación":

            st.subheader("⚡ Hidroboración")

            st.success("""
            ✅ Alcohol anti-Markovnikov obtenido.
            """)

            rendimiento = 91

        # ---------------------------------------------
        # SN1
        # ---------------------------------------------

        elif reaccion == "SN1":

            st.subheader("⚡ Resultado SN1")

            if solvente in ["Agua","Metanol","Etanol"]:

                st.success("""
                ✅ Formación de carbocatión favorecida.
                """)

                rendimiento = 85

            else:

                st.warning("""
                ⚠️ Solvente poco favorable.
                """)

                rendimiento = 45

        # ---------------------------------------------
        # SN2
        # ---------------------------------------------

        elif reaccion == "SN2":

            st.subheader("⚡ Resultado SN2")

            if solvente == "Acetona":

                st.success("""
                ✅ Ataque nucleofílico eficiente.
                """)

                rendimiento = 93

            else:

                st.warning("""
                ⚠️ La reacción disminuyó.
                """)

                rendimiento = 50

        # ---------------------------------------------
        # SUSTITUCIÓN AROMÁTICA
        # ---------------------------------------------

        elif reaccion == "Sustitución Aromática":

            st.subheader("🔥 Sustitución Aromática")

            if catalizador == "FeBr3":

                st.success("""
                ✅ Bromación aromática exitosa.
                """)

                rendimiento = 89

            else:

                st.error("""
                ❌ Falta catalizador de Lewis.
                """)

                rendimiento = 20

        # ---------------------------------------------
        # RADICALARIA
        # ---------------------------------------------

        elif reaccion == "Sustitución Radicalaria":

            st.subheader("🔥 Sustitución Radicalaria")

            st.success("""
            ✅ Formación de radicales libres.
            """)

            rendimiento = 80

        # ---------------------------------------------
        # SAN
        # ---------------------------------------------

        elif reaccion == "Sustitución Nucleofílica Aromática":

            st.subheader("⚡ SAN")

            st.success("""
            ✅ Sustitución aromática completada.
            """)

            rendimiento = 78

        st.divider()

        # =================================================
        # RENDIMIENTO
        # =================================================

        st.subheader("📈 Rendimiento experimental")

        st.progress(rendimiento)

        st.metric(
            "🧪 Rendimiento",
            f"{rendimiento}%"
        )

        # =================================================
        # ANÁLISIS
        # =================================================

        st.subheader("🧠 Análisis químico")

        if rendimiento >= 85:

            st.success("""
            Excelente condición experimental.
            """)

        elif rendimiento >= 60:

            st.warning("""
            Condiciones aceptables.
            """)

        else:

            st.error("""
            Condiciones poco favorables.
            """)

        # =================================================
        # XP
        # =================================================

        guardar_puntos("Laboratorio", rendimiento)

        st.divider()

        st.markdown("""
        # 🏆 EXPERIMENTO COMPLETADO
        """)

        st.snow()
# =====================================================
# PROGRESO
# =====================================================

elif selected == "Progreso":

    st.title("📊 PROGRESO")

    conexion = sqlite3.connect("database/quimica.db")

    datos = pd.read_sql_query(
        "SELECT * FROM progreso",
        conexion
    )

    conexion.close()

    st.dataframe(datos)

    if len(datos) > 0:

        resumen = datos.groupby(
            "modulo"
        )["puntos"].sum().reset_index()

        fig = px.bar(
            resumen,
            x="modulo",
            y="puntos",
            color="modulo",
            text="puntos"
        )

        st.plotly_chart(fig, use_container_width=True)
# =====================================================
# 🧪 MÓDULO RUTAS DE REACCIÓN
# =====================================================

elif selected == "Rutas de Reacción":

    st.title("🧪 RUTAS DE REACCIÓN")

    st.markdown("""
    Este módulo permite descubrir
    qué reacción química utilizar
    para transformar un compuesto
    en otro.

    🔥 Aprende síntesis orgánica
    de forma visual e interactiva.
    """)

    st.divider()

    # =================================================
    # MOLÉCULA INICIAL
    # =================================================

    compuesto_inicial = st.selectbox(
        "Selecciona el compuesto inicial",
        [
            "Eteno",
            "Propeno",
            "Benceno",
            "Metano",
            "2-Bromopropano"
        ]
    )

    # =================================================
    # PRODUCTO OBJETIVO
    # =================================================

    producto_final = st.selectbox(
        "Selecciona el producto objetivo",
        [
            "Etano",
            "Alcohol",
            "Bromobenceno",
            "Halogenuro",
            "Propano"
        ]
    )

    st.divider()

    # =================================================
    # INICIAR ANÁLISIS
    # =================================================

    if st.button("🚀 Analizar ruta"):

        st.balloons()

        barra = st.progress(0)

        for i in range(100):
            barra.progress(i + 1)

        st.success("✅ Ruta encontrada")

        st.divider()

        # =================================================
        # ETENO → ETANO
        # =================================================

        if (
            compuesto_inicial == "Eteno"
            and
            producto_final == "Etano"
        ):

            st.header("⚡ Ruta recomendada")

            st.code("""
            CH2=CH2
                ↓ H2/Pt
            CH3-CH3
            """)

            st.subheader("🧬 Tipo de reacción")

            st.success("""
            Reacción de adición:
            Hidrogenación.
            """)

            st.subheader("📖 Explicación")

            st.write("""
            El doble enlace del alqueno
            se rompe y se adiciona H₂.
            """)

            st.metric("🧪 Dificultad", "Básica")

        # =================================================
        # PROPENO → ALCOHOL
        # =================================================

        elif (
            compuesto_inicial == "Propeno"
            and
            producto_final == "Alcohol"
        ):

            st.header("💧 Ruta recomendada")

            st.code("""
            CH3-CH=CH2
                  ↓ H2O/H+
            CH3-CHOH-CH3
            """)

            st.success("""
            Reacción de adición:
            Hidratación.
            """)

            st.info("""
            Se forma un alcohol
            siguiendo Markovnikov.
            """)

            st.metric("🧪 Dificultad", "Media")

        # =================================================
        # BENCENO → BROMOBENCENO
        # =================================================

        elif (
            compuesto_inicial == "Benceno"
            and
            producto_final == "Bromobenceno"
        ):

            st.header("🔥 Ruta recomendada")

            st.code("""
            Benceno
               ↓ Br2 / FeBr3
            Bromobenceno
            """)

            st.success("""
            Sustitución aromática electrofílica.
            """)

            st.warning("""
            El FeBr3 genera el electrófilo.
            """)

            st.metric("🧪 Dificultad", "Avanzada")

        # =================================================
        # METANO → HALOGENURO
        # =================================================

        elif (
            compuesto_inicial == "Metano"
            and
            producto_final == "Halogenuro"
        ):

            st.header("🔥 Ruta recomendada")

            st.code("""
            CH4
             ↓ Cl2 / luz UV
            CH3Cl
            """)

            st.success("""
            Sustitución radicalaria.
            """)

            st.info("""
            Ocurre mediante radicales libres.
            """)

            st.metric("🧪 Dificultad", "Media")

        # =================================================
        # 2-BROMOPROPANO → PROPANO
        # =================================================

        elif (
            compuesto_inicial == "2-Bromopropano"
            and
            producto_final == "Propano"
        ):

            st.header("⚡ Ruta recomendada")

            st.code("""
            CH3-CHBr-CH3
                   ↓ H2/Pd
            CH3-CH2-CH3
            """)

            st.success("""
            Sustitución seguida de reducción.
            """)

            st.metric("🧪 Dificultad", "Avanzada")

        # =================================================
        # SIN RUTA
        # =================================================

        else:

            st.error("""
            ❌ Ruta aún no disponible.
            """)

            st.info("""
            Próximamente se agregarán
            más rutas orgánicas.
            """)

        st.divider()


# =====================================================
# GAMIFICACIÓN
# =====================================================

elif selected == "Gamificación":

    st.title("🎮 GAMIFICACIÓN")

    st.metric("🏆 Nivel", "12")

    st.metric("🔥 XP", "1450")

    st.progress(85)

    st.success("✅ Medalla desbloqueada")

