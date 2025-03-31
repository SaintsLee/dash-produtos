import streamlit as st
import pandas as pd
from graficos_formatados import desenha_barra_formatado, desenha_pie_formatado, plot_metric_fgc, plot_metric_percentual, plot_metric_percentual_cat
from auxiliares import x9_consultores, LISTA_BANCOS_S3_S4

st.set_page_config(page_title='Dashboard - Visualização de produtos',
                   page_icon='📖',
                   layout = 'wide',
                   initial_sidebar_state='expanded')

upload_dataset = st.file_uploader(
    "Anexe a planilha com os dados", accept_multiple_files=False
)

@st.cache_data
def load_data(data_uploaded):
    df_1 = pd.read_excel(data_uploaded,sheet_name='Contratos')
    df_2 = pd.read_excel(data_uploaded,sheet_name='Posições')
    df_3 = pd.read_excel(data_uploaded, sheet_name='Colagem')

    df_1 = df_1.fillna('')
    df_2 = df_2.fillna('')
    df_3 = df_3.fillna('')

    return df_1, df_2, df_3

with st.sidebar:
    st.title('Produtos Portfel')

# Verifica se um arquivo foi enviado antes de tentar carregar os dados
if upload_dataset is not None:
    df_contratos, df_posicoes, df_colagem = load_data(upload_dataset)

    df_bancario = df_colagem[df_colagem['Proteção FGC'] != ''].copy()
    with st.sidebar:

        df_bancarios_completo = df_bancario[['Total (R$)', 'Proteção FGC']].groupby(['Proteção FGC']).sum().sort_values(
            by='Total (R$)', ascending=False)
        TOTAL_BANCARIOS = df_bancarios_completo['Total (R$)'].sum()
        TOTAL_PORTFEL = df_colagem['Total (R$)'].sum()
        TOTAL_CLIENTES_PORTFEL = df_colagem['Contrato'].unique().shape[0]

        # Listagem das ifs
        lista_ifs = list(df_bancarios_completo.index)

        # Seleção das ifs no multiselect
        lista_ifs_selecionadas = st.selectbox('Instituições Financeiras',lista_ifs)

        ck_01 = st.checkbox('Percentual geral')
        if ck_01:
            TOTAL_PL_CUSTOM = st.number_input('Caso desejar, adicione o PL atual da Portfel manualmente: Bi R$', min_value=0.0,format='%.2f') * 1000000000
            TOTAL_PORTFEL = TOTAL_PL_CUSTOM

    # Df filtrado pelo multiselect
    df_bancarios_filtrados = df_bancario[['Total (R$)','Proteção FGC']].groupby(['Proteção FGC']).sum().sort_values(by='Total (R$)',ascending=False).loc[lista_ifs_selecionadas]
    df_bancarios_filtrados_percentual = df_bancarios_filtrados/TOTAL_BANCARIOS*100

    # Df para posições relativas as classes de ativos
    df_bancarios_posicoes_emissor_classficacao = df_posicoes[['Proteção FGC','Classificação','Valor']].groupby(['Proteção FGC','Classificação']).sum().reset_index().fillna('')
    df_bancarios_posicoes_emissor_classficacao = df_bancarios_posicoes_emissor_classficacao[df_bancarios_posicoes_emissor_classficacao['Proteção FGC'] != '']

    # Setor Select Box - Percentual acima do FGC por cliente
    df_contrato = df_contratos[['Nº Contrato', 'Email do Consultor']]
    df_agregado_fgc = df_bancario[['Contrato', 'Nome Cliente', 'Proteção FGC', 'Total (R$)']].groupby(
        ['Contrato', 'Nome Cliente', 'Proteção FGC']).sum().reset_index()
    df_agregado_fgc['E-mail'] = '0'

    df_agregado_fgc_banco = x9_consultores(lista_ifs_selecionadas, df_agregado_fgc, df_contrato)
    quantidade_clientes_acima_fgc = df_agregado_fgc_banco[df_agregado_fgc_banco['Total (R$)'] >= 250000.00].shape[0]
    quantidade_clientes_total_if = df_agregado_fgc_banco['Contrato'].unique().shape[0]
    percentual_acima_fgc = quantidade_clientes_acima_fgc / quantidade_clientes_total_if * 100

    # Compilador para calcular o montante que está acima do FGC dos bancos S3 e S4
    @st.cache_data
    def bancos_estourados(LISTA_BANCOS_S3_S4, df_agregado_fgc, df_contrato):
        banco_estourado = pd.DataFrame(columns=['Contrato', 'Nome Cliente', 'Proteção FGC', 'Total (R$)', 'E-mail'])
        for banco in range(len(LISTA_BANCOS_S3_S4)):
            bancos = x9_consultores(LISTA_BANCOS_S3_S4[banco], df_agregado_fgc, df_contrato)
            banco_estourado = pd.concat([banco_estourado, bancos])
        return banco_estourado

    # Todos os Bancos:
    banco_estourado = bancos_estourados(lista_ifs, df_agregado_fgc, df_contrato)
    banco_estourado['Acima do FGC'] = banco_estourado['Total (R$)'].apply(lambda x: x - 250000 if x >= 250000 else 0)
    montantes_estourados_por_if =  banco_estourado.groupby('Proteção FGC').sum()['Acima do FGC'].sort_values(
       ascending=False)

    st.markdown(
        f'<h1 style="color: black;font-size:25px;" >Clientes que possuem produtos da instituição: <span style="color: ForestGreen;">{lista_ifs_selecionadas.split('- ')[1]}</span></h1>',
        unsafe_allow_html=True)

    col_metrics_1, col_metrics_2, col_metrics_3, col_metrics_4 = st.columns([1,1,1,1])
    col_metrics_1.plotly_chart(plot_metric_fgc(percentual_acima_fgc,f'Clientes acima do FGC: {quantidade_clientes_acima_fgc}'),use_container_width=True)
    col_metrics_2.plotly_chart(plot_metric_percentual(quantidade_clientes_total_if/TOTAL_CLIENTES_PORTFEL*100,f'Clientes na instituição: {quantidade_clientes_total_if}'),use_container_width=True)
    col_metrics_3.plotly_chart(plot_metric_percentual(float(df_bancarios_filtrados_percentual.values),'% Montante/PL Bancários'),use_container_width=True)
    col_metrics_4.plotly_chart(plot_metric_fgc(float(df_bancarios_filtrados/TOTAL_PORTFEL*100),'% Montante/PL Portfel'),use_container_width=True)

    st.markdown(
        f'<h1 style="color: black;font-size:25px;" >Posições por categoria da instituição: <span style="color: ForestGreen;">{lista_ifs_selecionadas.split('- ')[1]}</span></h1>',
        unsafe_allow_html=True)
    col_metrics_class_1, col_metrics_class_2, col_metrics_class_3 = st.columns([1,1,1])
    df_if_class = df_bancarios_posicoes_emissor_classficacao[df_bancarios_posicoes_emissor_classficacao['Proteção FGC']==lista_ifs_selecionadas]
    TOTAL_POS_IF = float(df_if_class['Valor'].sum())
    df_if_class['Percentual'] = df_bancarios_posicoes_emissor_classficacao['Valor']/TOTAL_POS_IF*100
    df_if_class.index = df_if_class['Classificação']

    if 'Renda Fixa - CDI' in df_if_class['Classificação']:
        col_metrics_class_1.plotly_chart(
            plot_metric_percentual_cat(df_if_class.loc['Renda Fixa - CDI','Percentual'],f'Renda Fixa - CDI','Renda Fixa - CDI'),
            use_container_width=True)
    else:
        col_metrics_class_1.plotly_chart(
            plot_metric_percentual_cat(0, f'Renda Fixa - CDI',
                                       'Renda Fixa - CDI'),
            use_container_width=True)
    if 'Renda Fixa - Inflação' in df_if_class['Classificação']:
        col_metrics_class_2.plotly_chart(
            plot_metric_percentual_cat(df_if_class.loc['Renda Fixa - Inflação', 'Percentual'], f'Renda Fixa - Inflação','Renda Fixa - Inflação'),
            use_container_width=True)
    else:
        col_metrics_class_2.plotly_chart(
            plot_metric_percentual_cat(0, f'Renda Fixa - Inflação','Renda Fixa - Inflação'),
            use_container_width=True)
    if 'Renda Fixa - Pré-fixado' in df_if_class['Classificação']:
        col_metrics_class_3.plotly_chart(
            plot_metric_percentual_cat(df_if_class.loc['Renda Fixa - Pré-fixado', 'Percentual'], f'Renda Fixa - Pré-Fixado','Renda Fixa - Pré-Fixado'),
            use_container_width=True)
    else:
        col_metrics_class_3.plotly_chart(
            plot_metric_percentual_cat(0, f'Renda Fixa - Pré-Fixado','Renda Fixa - Pré-Fixado'),
            use_container_width=True)

    #df_bancarios_posicoes_emissor_classficacao



    banco_estourado_s3_s4 = bancos_estourados(LISTA_BANCOS_S3_S4, df_agregado_fgc, df_contrato)
    banco_estourado_s3_s4['Acima do FGC'] = banco_estourado_s3_s4['Total (R$)'].apply(lambda x: x - 250000 if x >= 250000 else 0)
    montantes_estourados_por_if_s3_s4 =  banco_estourado_s3_s4.groupby('Proteção FGC').sum()['Acima do FGC'].sort_values(
       ascending=False)

    g_barra_estourado = desenha_barra_formatado(montantes_estourados_por_if_s3_s4.iloc[0:15],
                                         'Montante total acima do FGC por instituição S3/S4',
                                         'Valor R$',
                                         '',
                                         'Acima do FGC',
                                         montantes_estourados_por_if_s3_s4.index[0:15])
    st.plotly_chart(g_barra_estourado)

    if ck_01:
        # Cálculo dos CDBs que representam 50% do total em CDB
        df_bancarios_completo_percentual = df_bancarios_completo.copy()
        df_bancarios_completo_percentual['Percentual'] = df_bancarios_completo_percentual['Total (R$)'] / TOTAL_PORTFEL * 100
        df_bancarios_completo_percentual["% Total"] = df_bancarios_completo_percentual["Percentual"].cumsum()
        df_bancarios_50 = df_bancarios_completo_percentual.iloc[0:5]
        df_bancarios_50['Diferença'] = 100 - df_bancarios_50['Percentual']

        g_barra_01 = desenha_barra_formatado(df_bancarios_50,
                                             'Emissores que representam 50% de toda captação em CDBs',
                                             'Valor R$',
                                             'Emissor',
                                             'Total (R$)',
                                             df_bancarios_50.index)
    else:
        # Cálculo dos CDBs que representam 50% do total em CDB
        df_bancarios_completo_percentual = df_bancarios_completo.copy()
        df_bancarios_completo_percentual['Percentual'] = df_bancarios_completo_percentual['Total (R$)']/df_bancarios_completo_percentual['Total (R$)'].sum() * 100
        df_bancarios_completo_percentual["% Total"] = df_bancarios_completo_percentual["Percentual"].cumsum()
        df_bancarios_50 = df_bancarios_completo_percentual[df_bancarios_completo_percentual['% Total'] <= 50.0]
        df_bancarios_50['Diferença'] = 100 - df_bancarios_50['Percentual']

        g_barra_01 = desenha_barra_formatado(df_bancarios_50,
                                             'Emissores que representam 50% de toda captação em CDBs',
                                             'Valor R$',
                                             'Emissor',
                                             'Total (R$)',
                                             df_bancarios_50.index)

    #st.dataframe(df_colagem)
    #st.dataframe(df_contratos)
    #st.dataframe(df_posicoes)

    st.plotly_chart(g_barra_01)
















else:
    st.warning("Por favor, anexe um arquivo para visualizar os dados.",icon='🚨')


