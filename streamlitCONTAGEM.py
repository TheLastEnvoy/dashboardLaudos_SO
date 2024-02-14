import os
import streamlit as st
import matplotlib.pyplot as plt

def contar_arquivos(caminho, mapeamento):
    contagem_total = 0
    contagem_por_trecho = {trecho: 0 for trecho in mapeamento.values()}
    
    for pasta_atual, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            for trecho, nome_laudo in mapeamento.items():
                if trecho in arquivo:
                    contagem_total += 1
                    contagem_por_trecho[nome_laudo] += 1
    
    return contagem_total, contagem_por_trecho

# Definindo o caminho da pasta e os trechos nos nomes dos arquivos
caminho = "C:/Users/DavidosSantosVillela/ufpr.br/Intranet do LAGEAMB - 03_SO/11_municipiosPAs"
mapeamento = {
    "DecOcupante": "Laudo Declaração de Ocupante",
    "SimpOcupante": "Laudo Simplificado de Ocupante",
    "CompOcupante": "Laudo Completo de Ocupante",
    "DecBeneficiario": "Laudo Declaração de Beneficiário",
    "SimpBeneficiario": "Laudo Simplificado de Beneficiário",
    "CompBeneficiario": "Laudo Completo de Beneficiário",
    "LoteVago": "Laudo Lote Vago"
}

# Obtendo contagem total e contagem por trecho
contagem_total, contagem_por_trecho = contar_arquivos(caminho, mapeamento)

# Exibindo no dashboard
st.title("Quantidade de laudos de supervisão ocupacional salvos no SharePoint (SO - TED INCRA/UFPR)")
st.write(f"Total de laudos: {contagem_total}")

st.subheader("Contagem por tipo de laudo:")
for trecho, contagem in contagem_por_trecho.items():
    st.write(f"{trecho}: {contagem}")

# Criando gráfico de pizza
fig, ax = plt.subplots()
labels = contagem_por_trecho.keys()
sizes = contagem_por_trecho.values()
colors = plt.cm.tab20c.colors[:len(labels)]

wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, explode=[0.05] * len(labels))

ax.set_title("Distribuição dos laudos de supervisão ocupacional", pad=20)

# Adicionando legenda
ax.legend(wedges, labels, title="Tipos de Laudo", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

st.pyplot(fig)
