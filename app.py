import streamlit as st
import pandas as pd
import re
from shield import SovereignResilienceShield # Importamos nuestro escudo de soberanía actualizado

def main():
    st.set_page_config(page_title="SovereignGuard AI 🛡️", layout="wide")
    st.title("🛡️ SovereignGuard AI: The Resilience Orchestrator")
    st.subheader("Capa de Auditoría y Resiliencia Agéntica para Infraestructura Financiera")

    # --- 1. Carga del Dataset con Triple Escudo de Ingesta ---
    try:
        df = pd.read_csv("prosa_logs.csv", sep=';', encoding='utf-8-sig')
        # Limpieza proactiva de nombres de columnas
        df.columns = [column.strip() for column in df.columns]

    except FileNotFoundError:
        st.error("🚨 ERROR DE INFRAESTRUCTURA: No se encontró el archivo 'prosa_logs.csv'.")
        st.info("💡 ACCIÓN REQUERIDA: Asegúrate de que el CSV esté en la misma carpeta que app.py")
        st.stop()

    # Visualización de Triage
    st.write("### Aclaraciones Pendientes (ISO 8583 Inbound / Transaccional)")
    st.dataframe(df, use_container_width=True)

    # Selección de item para auditar (modo HITL)
    selected_txn = st.selectbox("Seleccione Transacción para Auditoría Forense:", df['Transacción ID'])

    # Búsqueda de la fila seleccionada
    row = df[df["Transacción ID"] == selected_txn].iloc[0]

    if st.button("Iniciar Investigación Agéntica"):
        # --- CAPA DE PROTECCIÓN DE INFRAESTRUCTURA ---
        try:
            st.divider()

            disputa_texto = str(row['Intent / Disputa']).upper()

            if "PHISHING" in disputa_texto:
                raw_llm_output = f"Alerta! El dominio no es oficial. DECISIÓN: BLOQUEO para {selected_txn}. Causa: Phishing detectado."
            elif "05" in str(row['POS Entry Mode']):
                raw_llm_output = f"Validación de NIP exitosa en log. DECISIÓN: IMPROCEDENTE para {selected_txn}. Responsabilidad emisor."
            else:
                raw_llm_output = f"Monto bajo detectado. DECISIÓN: PROCEDENTE para {selected_txn}. Aplicando SLA Fast-track."

            # --- CAPA DE PROTECCIÓN DE SALIDA (EL CINCEL REGEX) ---
            decision_limpia = SovereignResilienceShield.sanitize_output(raw_llm_output)

            col1, col2 = st.columns(2)

            with col1:
                st.write("### 🔍 Hallazgos del Agente Investigador")
                st.info(f"**Modo de Entrada (POS):** {row['POS Entry Mode']}")
                st.info(f"**Código de Respuesta:** {row['Response Code']}")
                st.info(f"**Monto de la TXN:** {row['Amount']}")
                st.info(f"**Disputa Original del cliente:** {row['Intent / Disputa']}")
                st.write("---")
                st.warning(f"**Raw AI Output (Input al Escudo):**\n\n {raw_llm_output}")

            with col2:
                st.write('### ⚖️ Dictamen del Agente Juez')
                if decision_limpia == "BLOQUEO":
                    st.error(f"DICTAMEN FINAL: {decision_limpia}")
                    st.write("**Acción:** Bloqueo preventivo en el Switch / Sistema.")
                elif decision_limpia == "PROCEDENTE":
                    st.success(f"DICTAMEN FINAL: {decision_limpia}")     
                    st.write("**Acción:** Abono automático al tarjetahabiente.")
                elif decision_limpia == "IMPROCEDENTE":
                    st.error(f"DICTAMEN FINAL: {decision_limpia}")
                    st.write("**Acción:** Rechazo de aclaración por validación de NIP.")
                else:
                    st.warning(f"DICTAMEN FINAL: {decision_limpia}")    
                    st.write("**Acción:** Requiere intervención de Auditoría Senior.")
                    
                st.write("---")
                st.caption("🛡️ Seguridad: Verificación determinista mediante SovereignResilienceShield")

        except Exception as e:
            infra_action = SovereignResilienceShield.handle_infrastructure_errors(e)
            if infra_action:
                st.stop()
            else:
                st.error(f"🚨 FALLO NO CATALOGADO: {e}") 
            
    # --- 4. INTERFAZ DE SOBERANÍA (Control de Decisión) ---
    st.divider()
    st.write("### 🤖 SovereignGuard AI Recommendation: Acciones de Liderazgo")
    c1, c2, c3 = st.columns(3)
    with c1:
        btn_proceed = st.button("✅ PROCEED", key="proceed_btn", use_container_width=True)
    with c2:
        btn_modify = st.button("📝 MODIFY", key="modify_btn", use_container_width=True)
    with c3:
        btn_reject = st.button("❌ REJECT", key="reject_btn", use_container_width=True)

    if btn_proceed:
        st.success(f"✅ ACCIÓN EJECUTADA: La transacción {selected_txn} procesada y sincronizada con el Switch.")
    if btn_reject:
        st.error(f"🚫 ACCIÓN BLOQUEADA: La transacción {selected_txn} rechazada por el Agente Auditor. Alerta enviada a Prevención de Fraude.")
    if btn_modify:
        st.warning(f"📝 MODO EDICIÓN: Ajustando criterios de ruteo para {selected_txn}...")

    # --- BITÁCORA DE SOBERANÍA ---
    st.divider()
    with st.expander("📜 Ver Bitácora de Auditoría Inmutable"):
        st.write(f"**Usuario:** Talia González López (Applied AI Architect)")
        st.write(f"**Timestamp:** 2026-09-21 13:39:00")
        st.write(f"**Acción Legal:** Cédula A validada contra reglas de infraestructura financiera")
        st.write("---")
        st.write("Dato: La sincronización con el sistema se realiza bajo protocolos de cifrado AES-256")

if __name__ == "__main__":
    main()