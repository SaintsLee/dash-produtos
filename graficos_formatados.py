import plotly.express as px
import plotly.graph_objects as go

# Cor do tema
tema = False
if tema:
    back_color = "#0E1117"
    text_color = "#FAFAFA"
    zero_line = "#FFFFFF"
    fil_color = "#A0A0A0"
else:
    back_color = "#FFFFFF"
    text_color = "#31333F"
    zero_line = "#000000"
    fil_color = "#4A4A4A"

# Função para a formatação dos gráficos Boxplot
def desenha_box_formatado(dataset, title, titulo_y, titulo_x):
    fig = px.box(dataset, color_discrete_sequence=["black"], title = title)

    fig.update_layout(xaxis_title=titulo_x, yaxis_title=titulo_y, showlegend=False, height=650, plot_bgcolor=back_color,
                      xaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo X
                      ),
                      yaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo Y

                      ),
                      xaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo X
                      yaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo Y
                      )

    # Personalizar o grid
    fig.update_xaxes(
        showgrid=False,  # Exibir a grade no eixo X
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo X)
        zerolinecolor=text_color,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo,
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    fig.update_yaxes(
        showgrid=True,  # Exibir a grade no eixo Y
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo Y)
        zerolinecolor=zero_line,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    # Personalização das cores
    # "#392B84"
    fig.update_traces(
        marker_color="Red",  # Cor da caixa
        line_color=text_color,  # Cor da linha da borda
        fillcolor=fil_color,
        marker_size=4,  # Tamanho dos pontos
        marker_opacity=1  # Opacidade dos pontos
    )
    return fig

# Função para a formatação dos gráficos Linha
def desenha_linha_formatado(dataset, title,titulo_y, titulo_x):
    cores_personalizadas = ["#6faf5f","#dfe300","#fca620", "#ff0100"]

    fig = px.line(dataset,
                  title = title,
                  color_discrete_sequence= cores_personalizadas)

    fig.update_layout(xaxis_title=titulo_x, yaxis_title=titulo_y, showlegend=True, legend_title_text = "Carteiras",height=650, plot_bgcolor=back_color,
                      xaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo X
                          showticklabels = False
                      ),
                      yaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo Y

                      ),
                      xaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo X
                      yaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo Y
                      )

    # Personalizar o grid
    fig.update_xaxes(
        showgrid=False,  # Exibir a grade no eixo X
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo X)
        zerolinecolor=zero_line,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo,
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    fig.update_yaxes(
        showgrid=True,  # Exibir a grade no eixo Y
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo Y)
        zerolinecolor=text_color,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    return fig

# Função para a formatação dos gráficos Treemap
def desenha_treemap_formatado(dataset, title):
    # Lista de cores customizadas
    cores_personalizadas = ["#6faf5f","#dfe300","#fca620", "#ff0100"]

    fig = px.treemap(dataset,
                     path= [px.Constant("Carteiras"), 'Tipo', 'Classe', 'Ativos'],
                     values="Pesos",
                     title=title,
                     hover_data = {"Pesos":":.2f%"},
                     color_discrete_sequence= cores_personalizadas
                     )

    fig.update_layout(showlegend=True, legend_title_text="Carteiras",
                      height=800, plot_bgcolor=back_color,
                      xaxis=dict(
                          tickfont=dict(size=18, color=text_color),  # Tamanho da fonte para os números no eixo X
                          showticklabels=False
                      ),
                      yaxis=dict(
                          tickfont=dict(size=18, color=text_color),  # Tamanho da fonte para os números no eixo Y

                      ),
                      xaxis_title_font=dict(size=18, color=text_color),  # Tamanho da fonte do eixo X
                      yaxis_title_font=dict(size=18, color=text_color),  # Tamanho da fonte do eixo Y
                      font=dict(color="rgba(0,0,0,0)") # Altera a cor do nó raíz
                      )
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>Peso: %{value}%<br><extra></extra>",
        texttemplate='%{label}<br>%{value}%',
        textfont_size = 16,
        textposition = "middle center",
        marker_line_color = "white",
        root_color= "rgba(0,0,0,0)"
    )


    return fig

# Função para a formatação dos gráficos de Barra
def desenha_barra_formatado(dataset, title,titulo_y, titulo_x, valor_y,valor_x):

    cores_personalizadas = ["#0095CC","#F76D4D","#fca620", "#ff0100"]
    fig = px.bar(dataset,
                 x=valor_x,
                 y=valor_y,
                 title = title,
                 color_discrete_sequence= cores_personalizadas,)

    fig.update_layout(xaxis_title=titulo_x, yaxis_title=titulo_y, showlegend=False, legend_title_text = 'Montante',height=650, plot_bgcolor=back_color,
                      xaxis=dict(
                          tickfont=dict(size=13, color = text_color),  # Tamanho da fonte para os números no eixo X
                          showticklabels = True,

                      ),
                      yaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo Y

                      ),
                      xaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo X
                      yaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo Y
                      )

    # Personalizar o grid
    fig.update_xaxes(
        showgrid=False,  # Exibir a grade no eixo X
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo X)
        zerolinecolor=zero_line,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo,
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    fig.update_yaxes(
        showgrid=True,  # Exibir a grade no eixo Y
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo Y)
        zerolinecolor=text_color,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    return fig

# Função para a formatação dos gráficos de Barra
def desenha_pie_formatado(dataset, title,titulo_y, titulo_x, valor_x,valor_y):
    cores_personalizadas = ["#0095CC","#F76D4D","#fca620", "#ff0100"]
    fig = px.pie(dataset,
                 names=valor_x,
                 values=valor_y,
                 title = title,
                 hole =.5,
                 color_discrete_sequence= cores_personalizadas)

    fig.update_layout(xaxis_title=titulo_x, yaxis_title=titulo_y, showlegend=False, legend_title_text = 'Montante',height=350, plot_bgcolor=back_color,
                      xaxis=dict(
                          tickfont=dict(size=13, color = text_color),  # Tamanho da fonte para os números no eixo X
                          showticklabels = True
                      ),
                      yaxis=dict(
                          tickfont=dict(size=18, color = text_color),  # Tamanho da fonte para os números no eixo Y

                      ),
                      xaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo X
                      yaxis_title_font=dict(size=18, color = text_color),  # Tamanho da fonte do eixo Y
                      title={'font': {'size': 13}}
                      )

    # Personalizar o grid
    fig.update_xaxes(
        showgrid=False,  # Exibir a grade no eixo X
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo X)
        zerolinecolor=zero_line,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo,
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    fig.update_yaxes(
        showgrid=True,  # Exibir a grade no eixo Y
        gridcolor=text_color,  # Cor das linhas da grade
        gridwidth=0.5,  # Largura das linhas da grade
        zeroline=True,  # Exibir linha de zero (para eixo Y)
        zerolinecolor=text_color,  # Cor da linha de zero
        zerolinewidth=1.2,  # Largura da linha de zero
        showline=True,  # Exibir a linha do eixo
        linecolor=text_color,  # Cor da linha do eixo
        linewidth=0.8,  # Largura da linha do eixo
        griddash='dot',
        layer="below traces"  # Coloca o Grid atrás
    )

    # Desativando o hover
    fig.update_traces(hoverinfo="none", hovertemplate=None)
    return fig

def plot_metric_fgc(value,titulo):
    ponto_otimo = 1.5
    delta_color = "green" if value <= ponto_otimo else "red"

    if value > 3.5:
        bar_color = 'Maroon'
    elif value > 2.0:
        bar_color = 'OrangeRed'
    elif value > 1.0:
        bar_color = 'ForestGreen'
    else:
        bar_color = 'RoyalBlue'

    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=value,
        mode="gauge+number",
        title={'text': titulo},
        delta={'reference': ponto_otimo,
               'increasing': {'color': "red"},  # Se o valor subir, fica vermelho
               'decreasing': {'color': "green"}  # Se o valor cair, fica verde
               },
        number = {'suffix':'%','valueformat':'.2f'},
        gauge={'axis': {'range': [None, 5], 'tickwidth': 1,'tickcolor':'black'},
               'bar': {'color': bar_color},
               'steps': [
                   {'range': [0, 1.0], 'color': "LightSkyBlue"},
                   {'range': [1.0, 2.0], 'color': "LightGreen"},
                   {'range': [2.0, 3.5], 'color': "Orange"},
                   {'range': [3.5, 5], 'color': "Tomato"}
                    ],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': value}
               }))
    fig.update_layout(font={'color': "black"},
                      margin=dict(t=0, b=0, l=30, r=30))
    return fig

def plot_metric_percentual(value,titulo):
    ponto_otimo = 15

    if value > 75:
        bar_color = 'Maroon'
    elif value > 50:
        bar_color = 'OrangeRed'
    elif value > 25:
        bar_color = 'ForestGreen'
    else:
        bar_color = 'RoyalBlue'

    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=value,
        mode="gauge+number",
        title={'text': titulo},
        delta={'reference': ponto_otimo,
               'increasing': {'color': "red"},  # Se o valor subir, fica vermelho
               'decreasing': {'color': "green"}  # Se o valor cair, fica verde
               },
        number={'suffix': '%', 'valueformat': '.2f'},
        gauge={'axis': {'range': [None, 100], 'tickwidth': 1,'tickcolor':'black'},
               'bar': {'color': bar_color},
               'steps': [
                   {'range': [0, 25], 'color': "LightSkyBlue"},
                   {'range': [25, 50], 'color': "LightGreen"},
                   {'range': [50, 75], 'color': "Orange"},
                   {'range': [75, 100], 'color': "Tomato"}
                    ],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': value}
               }))
    fig.update_layout(font={'color': "black"},
                      margin=dict(t=0, b=0, l=30, r=30))
    return fig

def plot_metric_percentual_cat(value,titulo,categoria):
    ponto_otimo = 15


    if categoria == 'Renda Fixa - CDI':
       bar_color = 'ForestGreen'
    if categoria == 'Renda Fixa - Pré-Fixado':
        if value > 50:
            bar_color = 'Maroon'
        elif value > 20:
            bar_color = 'Gold'
        else:
            bar_color = 'ForestGreen'
    if categoria == 'Renda Fixa - Inflação':
        if value > 50:
            bar_color = 'Maroon'
        elif value > 30:
            bar_color = 'Gold'
        else:
            bar_color = 'ForestGreen'



    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=value,
        mode="gauge+number",
        title={'text': titulo},
        delta={'reference': ponto_otimo,
               'increasing': {'color': "red"},  # Se o valor subir, fica vermelho
               'decreasing': {'color': "green"}  # Se o valor cair, fica verde
               },
        number={'suffix': '%', 'valueformat': '.2f'},
        gauge={'axis': {'range': [None, 100], 'tickwidth': 1,'tickcolor':'black'},
               'bar': {'color': bar_color},
               'steps': [],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': value}
               }))
    fig.update_layout(font={'color': "black"},
                      margin=dict(t=0, b=0, l=30, r=30))
    return fig