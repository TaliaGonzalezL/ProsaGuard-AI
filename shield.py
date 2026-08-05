import re
import streamlit as st

#CLASE DE SOBERANÍA TÉNICA:ESCUDO REGEX
class ProsaResilienceShield:
    @staticmethod
    def handle_infrastructure_errors(error_str):
        """
        Escudo de Misión Crítica: Detecta fallos de nube (GCP/Vertex AI) antes de que 
        afecten el Switch de PROSA.
        """
        error_str = str(error_str)

        # 1. FILTRO DE DISPONIBILIDAD (503 - Overloaded)
        if "503" in error_str or "overloaded" in error_str.lower():
            st.warning("⚠️ **PROSA Guard: Nodo de Inteligencia Saturado.**")
            st.info("Detectada latencia en Vertex AI. Activando protocolo de reintento en la sombra...")
            return "INFRA_LATENCY_RETRY"

        # 2. FILTRO DE CUOTA (429 - Rate Limit)
        elif "429" in error_str or "quota" in error_str.lower():
            st.error("🚨 **LÍMITE DE TRANSACCIONES ALCANZADO.**")
            st.info("El volumen de aclaraciones excede el throughput actual. Escalando capacidad...")
            return "QUOTA_EXCEEDED_HALT"

        return None


    @staticmethod
    def sanitize_output(llm_output):
        """
        El cincel de Talia:Limpia el ruido del LLM para asegurar
        que el Switch de PROSA reciba datos atómicos.
        """
        #Extraemos el ID de transacción y la decisión final
        try:
            # Lógica de rescate de Talia: Busca el patrón exacto de la decisión
            # \s* permite manejar espacios accidentales después de los dos puntos
            decision_pattern=r"DECISIÓN:\s*(PROCEDENTE|IMPROCEDENTE|BLOQUEO)"
            # Agregamos re.IGNORECASE para máxima resiliencia
            match=re.search(decision_pattern, llm_output, re.IGNORECASE)
            if match:
                return match.group(1). upper() 
            else:
                #ESTRATEGIA DE RESCATE (Failsafe):
                #Si el patrón falla pero la palabra está en el texto, la rescatamos.
                upper_output = llm_output.upper()
                if "PROCEDENTE" in upper_output: return "PROCEDENTE"
                if "IMPROCEDENTE" in upper_output: return "IMPROCEDENTE"
                if "BLOQUEO" in upper_output: return "BLOQUEO"

                # Rescate final vía "Final Answer" (como en AXA)
                if "FINAL ANSWER:" in upper_output:
                    return upper_output.split("FINAL ANSWER:")[-1].strip()

                return "ERROR_DE_FORMATO"

        except Exception:
            return"RESCATE_MANUAL_REQUERIDO"