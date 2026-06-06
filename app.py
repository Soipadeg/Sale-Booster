import pandas as pd
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
st.markdown("**VpH** = Vente-migration mobile / Heure de travail")
st.markdown("---")

# ============ DEUX ONGLETS ============
tab1, tab2 = st.tabs(["🎯 Calcul Ventes Mobiles", "📈 Calcul VpH"])

# ============ ONGLET 1: Calculer Ventes Mobiles ============
with tab1:
    st.header("🎯 Calcul Ventes Mobiles")
    st.markdown("Entrez vos données pour voir le récapitulatif en temps réel")

    st.markdown("---")

    # Créer 2 colonnes principales
    col_gauche, col_droite = st.columns([1, 1])

    # ============ COLONNE GAUCHE: INPUTS ============
    with col_gauche:
        st.subheader("📝 Données")

        VpH_cible = st.number_input(
            "🎯 VpH Ciblé",
            min_value=0.0,
            step=0.1,
            value=0.10,
            key="VpH_target"
        )

        heures_totales = st.number_input(
            "⏱️ Heures totales",
            min_value=0.0,
            step=0.5,
            value=8.0,
            key="heures_total"
        )

        heures_realisees = st.number_input(
            "✅ Heures réalisées",
            min_value=0.0,
            step=0.5,
            value=0.0,
            key="heures_realisees"
        )

        ventes_realisees = st.number_input(
            "📊 Ventes réalisées",
            min_value=0,
            step=1,
            value=0,
            key="ventes_realisees"
        )

    # Calculs
    heures_restantes = max(0, heures_totales - heures_realisees)
    ventes_necessaires = heures_totales * VpH_cible
    ventes_restantes = max(0, ventes_necessaires - ventes_realisees)

    # VpH réalisé du moment
    VpH_realise = ventes_realisees / heures_realisees if heures_realisees > 0 else 0

    # Calcul de la progression en %
    progression_ventes = (ventes_realisees / max(ventes_necessaires, 1)) * 100
    progression_heures = (heures_realisees / max(heures_totales, 1)) * 100

    # Déterminer si objectif atteint
    objectif_atteint = VpH_realise >= VpH_cible if heures_realisees > 0 else False

    # ============ COLONNE DROITE: TABLEAU DE BORD ============
    with col_droite:
        st.subheader("📊 Suivi en Temps Réel")

        # Message motivant
        if heures_realisees == 0:
            st.info("💡 Entrez les données pour le suivi!")
        else:
            if objectif_atteint:
                st.success(f"🎉 **EXCELLENT!**\nVpH: {VpH_realise:.4f} ≥ {VpH_cible:.4f} ⭐")
            else:
                deficit = VpH_cible - VpH_realise
                ventes_manquantes = max(0, heures_realisees * VpH_cible - ventes_realisees)
                st.warning(f"⚠️ VpH: {VpH_realise:.4f}\nManque: {deficit:.4f}\nVentes manquantes: {ventes_manquantes:.0f}")

        st.markdown("---")

        # KPIs compacts
        kpi1, kpi2 = st.columns(2)
        with kpi1:
            st.metric("⏱️ Heures", f"{heures_realisees:.1f}h")
            st.caption(f"Réalisées: {progression_heures:.0f}%")
        with kpi2:
            st.metric("✅ Ventes", f"{ventes_realisees:.0f}")
            st.caption(f"Réalisées: {progression_ventes:.0f}%")

        kpi3, kpi4 = st.columns(2)
        with kpi3:
            couleur = "📈" if objectif_atteint else "📉"
            st.metric(f"{couleur} Réalisé", f"{VpH_realise:.4f}")
            if VpH_cible > 0:
                ecart_pct = ((VpH_realise / VpH_cible - 1) * 100)

                # Déterminer la couleur selon l'écart
                if ecart_pct >= 0:
                    color_html = "🟢"  # Vert
                    couleur_text = "green"
                elif ecart_pct >= -50:
                    color_html = "🟠"  # Orange
                    couleur_text = "orange"
                else:
                    color_html = "🔴"  # Rouge
                    couleur_text = "red"

                st.markdown(f"<p style='color:{couleur_text}; font-weight: bold;'>{color_html} Écart: {ecart_pct:+.1f}%</p>", unsafe_allow_html=True)
        with kpi4:
            st.metric("🎯 Objectif", f"{VpH_cible:.4f}")

    st.markdown("---")

    # Row 2: Barres de progression
    st.subheader("📈 Progression")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Heures de travail** : {progression_heures:.1f}%")
        st.progress(min(progression_heures / 100, 1.0))
        st.caption(f"{heures_realisees:.1f}h / {heures_totales:.1f}h")

    with col2:
        st.write(f"**Ventes mobiles** : {progression_ventes:.1f}%")
        st.progress(min(progression_ventes / 100, 1.0))
        st.caption(f"{ventes_realisees:.0f} / {ventes_necessaires:.0f} ventes")

    st.markdown("---")

    # Row 3: Synthèse détaillée en tableau
    st.subheader("📋 Récapitulatif Détaillé")

    # Créer le DataFrame
    df = pd.DataFrame({
        "📊 Métrique": [
            "Heures réalisées",
            "Heures restantes",
            "Ventes réalisées",
            "Ventes nécessaires",
            "Ventes restantes",
            "VpH Réalisé",
            "Objectif VpH"
        ],
        "✅ Valeur": [
            f"{heures_realisees:.1f}h",
            f"{heures_restantes:.1f}h",
            f"{ventes_realisees:.0f}",
            f"{ventes_necessaires:.0f}",
            f"{ventes_restantes:.0f}",
            f"{VpH_realise:.4f}",
            f"{VpH_cible:.4f}"
        ]
    })

    # Afficher le tableau
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Créer un texte formaté pour copier
    recap_texte = df.to_csv(index=False, sep=",")

    # Bouton télécharger avec un layout
    col1, col2 = st.columns([3, 1])

    with col1:
        st.text_area(
            "📋 Aperçu du récapitulatif (Ctrl+A puis Ctrl+C pour copier)",
            value=recap_texte,
            height=150,
            disabled=False
        )

    with col2:
        st.markdown("")  # Espace
        # Bouton télécharger CSV avec bon encodage
        csv_data = df.to_csv(index=False, sep=",").encode('utf-8-sig')
        st.download_button(
            label="📥 Télécharger CSV",
            data=csv_data,
            file_name="recap_VpH.csv",
            mime="text/csv; charset=utf-8",
            use_container_width=True
        )

# ============ ONGLET 2: Calculer VpH ============
with tab2:
    st.header("📈 Calcul VpH")
    st.markdown("Entrez vos heures de travail et le nombre de ventes mobiles pour calculer votre VpH")

    st.markdown("---")

    heures_travail = st.number_input(
        "Nb d'heures de travail",
        min_value=0.0,
        step=0.5,
        value=8.0,
        key="heures_vph"
    )

    vente_mobile = st.number_input(
        "Nb de ventes mobiles",
        min_value=0,
        step=1,
        value=0,
        key="vente_vph"
    )

    if st.button("🔢 Calculer", key="btn_vph", use_container_width=True):
        if heures_travail > 0:
            vph_resultat = vente_mobile / heures_travail
            st.success("✅ Résultat")
            st.metric("VpH", f"{vph_resultat:.4f}", help="Ventes mobiles par heure")
            st.info(f"📊 **Détail du calcul:**\n\n{vente_mobile} ÷ {heures_travail} = **{vph_resultat:.4f} VpH**")
        else:
            st.error("❌ Le nombre d'heures doit être supérieur à 0")
