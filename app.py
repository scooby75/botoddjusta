import streamlit as st

def calcular_odd_justa(probabilidade_casa):
    """
    Calcula a Odd Justa a partir da probabilidade da casa.
    :param probabilidade_casa: Probabilidade de vitória da equipe da casa (em %).
    :return: Odd Justa.
    """
    odd_justa = 100 / probabilidade_casa
    return odd_justa


def analisar_aposta(odd_abertura, odd_justa):
    """
    Compara a Odd de Abertura com a Odd Justa e sugere Back ou Lay.
    :param odd_abertura: Odd de Abertura.
    :param odd_justa: Odd Justa calculada.
    :return: Sinalização de Aposta Back ou Lay.
    """
    if odd_abertura > odd_justa:
        return "Aposta Back"
    else:
        return "Aposta Lay"


# Título do App
st.title("Calculadora de Odd Justa para Futebol")

# Entrada dos dados
probabilidade_casa = st.number_input("Informe a probabilidade de vitória da casa (%)", min_value=0.0, max_value=100.0, step=0.01)
odd_abertura = st.number_input("Informe a Odd de Abertura", min_value=1.0, step=0.01)

# Botão para calcular
if st.button("Calcular"):
    if probabilidade_casa > 0:
        # Calcular a Odd Justa
        odd_justa = calcular_odd_justa(probabilidade_casa)

        # Analisar a aposta
        resultado_aposta = analisar_aposta(odd_abertura, odd_justa)

        # Exibir os resultados
        st.write(f"Odd Justa: **{odd_justa:.2f}**")
        st.write(f"Sugestão: **{resultado_aposta}**")
    else:
        st.write("Por favor, insira uma probabilidade válida para calcular a Odd Justa.")
