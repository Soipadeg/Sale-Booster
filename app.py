import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Sales Booster",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre et description
st.title("📊 Sales Booster")
st.markdown("**VpH** = Vente mobile / Heure de travail")
st.markdown("---")

# ============ DEUX COLONNES ============
col_left, col_right = st.columns(2)

# ============ COLONNE GAUCHE: Calculer VpH ============
with col_left:
    st.header("📈 Calcul VpH")

    heures_travail = st.number_input(
        "Nb d'heures de travail",
        min_value=0.0,
        step=0.5,
        value=8.0,
        key="heures_vph"
    )

    vente_mobile = st.number_input(
        "Nb de ventes Mobiles",
        min_value=0,
        step=1,
        value=0,
        key="vente_vph"
    )

    if st.button("🔢 Calculer", key="btn_vph", use_container_width=True):
        if heures_travail > 0:
            vph_resultat = vente_mobile / heures_travail
            st.success("✅ Résultat")
            st.metric("VpH", f"{vph_resultat:.2f}", help="Ventes par heure")
        else:
            st.error("❌ Le nombre d'heures doit être supérieur à 0")

# ============ COLONNE DROITE: Calculer Ventes Mobiles ============
with col_right:
    st.header("🎯 Calcul Ventes Mobiles")

    heures_travail_2 = st.number_input(
        "Nb d'heures de travail",
        min_value=0.0,
        step=0.5,
        value=8.0,
        key="heures_ventes"
    )

    vph_cible = st.number_input(
        "VpH Ciblé",
        min_value=0.0,
        step=0.5,
        value=10.0,
        key="vph_target"
    )

    if st.button("🎯 Calculer", key="btn_ventes", use_container_width=True):
        if heures_travail_2 > 0:
            ventes_necessaires = heures_travail_2 * vph_cible
            st.success("✅ Résultat")
            st.metric("Ventes à faire", f"{ventes_necessaires:.0f}", help="Nombre de ventes mobiles")
        else:
            st.error("❌ Le nombre d'heures doit être supérieur à 0")
