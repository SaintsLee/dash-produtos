def x9_consultores(banco,df_agregado_fgc,df_contrato):
    df_agregado_fgc_banco = df_agregado_fgc[df_agregado_fgc['Proteção FGC'] == banco].sort_values(by='Total (R$)',
                                                                                                  ascending=False).reset_index(
        drop=True)

    for linha in range(df_agregado_fgc_banco.shape[0]):
        contrato = df_agregado_fgc_banco.loc[linha, 'Contrato']
        email = df_contrato.loc[df_contrato['Nº Contrato'] == contrato, 'Email do Consultor']

        if not email.empty:  # Verifica se encontrou um email correspondente
            df_agregado_fgc_banco.loc[linha, 'E-mail'] = email.values[0]  # Usa .loc para evitar Chained Assignment
    if banco == '145 - CONGLOMERADO: MASTER, WILL, VOITER E LETSBANK':
        banco = '145 - CONGLOMERADO THUG MASTER'
    return df_agregado_fgc_banco
    # df_agregado_fgc_banco.to_excel(f'C:/Users/guilh/Desktop/Produtos Estourados/{banco}.xlsx',index=False)

LISTA_BANCOS_S3_S4 = [
    "4 - BANCO ABC BRASIL S.A.",
    "6 - BANCO AGIBANK",
    "7 - BANCO AGIPLAN",
    "14 - BANCO BMG",
    "15 - BANCO BOCOM BBM",
    "17 - BANCO BS2",
    "19 - BANCO C6",
    "21 - BANCO CNH INDUSTRIAL",
    "24 - BANCO CSF",
    "25 - BANCO DA AMAZONIA",
    "26 - BANCO DAYCOVAL",
    "27 - BANCO DE DESENVOLVIMENTO DE MINAS GERAIS (BDMG)",
    "28 - BANCO DE LAGE LANDEN BRASIL S.A.",
    "33 - BANCO FIBRA",
    "35 - BANCO GMAC (CHEVROLET)",
    "37 - BANCO INDUSTRIAL DO BRASIL",
    "38 - BANCO INDUSVAL VOITER (MASTER)",
    "39 - BANCO INTER",
    "41 - BANCO JOHN DEERE",
    "42 - BANCO LETSBANK",
    "44 - BANCO MASTER",
    "45 - BANCO MERCANTIL DO BRASIL",
    "48 - BANCO ORIGINAL",
    "51 - BANCO PAN",
    "54 - BANCO PINE",
    "55 - BANCO RABOBANK INTERNATIONAL BRASIL",
    "56 - BANCO RCI BRASIL",
    "57 - BANCO REGIONAL DE DESENVOLVIMENTO DO EXTREMO SUL (BRDE)",
    "65 - BANCO SOFISA",
    "68 - BANCO TOYOTA DO BRASIL S/A",
    "71 - BANCO VOLKSWAGEN",
    "75 - BANESTES",
    "76 - BANPARA",
    "81 - BNP PARIBAS",
    "84 - BRB BANCO DE BRASILIA SA",
    "88 - CHINA CONSTRUCTION BANK BRASIL",
    "92 - COOPERATIVA CENTRAL AILOS",
    "105 - JP MORGAN",
    "115 - NUBANK",
    "120 - PICPAY BANK",
    "122 - PORTO SEGURO",
    "123 - POUPEX",
    "140 - WILL BANK (MASTER)",
    "145 - CONGLOMERADO: MASTER, WILL, VOITER E LETSBANK",
    "3 - AL5 SCFI",
    "5 - BANCO AFINZ S.A.",
    "8 - BANCO ALFA DE INVESTIMENTO S.A.",
    "10 - BANCO ANDBANK (BRASIL) S.A.",
    "11 - BANCO ARBI S/A",
    "12 - BANCO BARI DE INVESTIMENTOS E FINANCIAMENTOS S.A.",
    "13 - BANCO BBC",
    "20 - BANCO CAIXA GERAL - BRASIL S.A.",
    "29 - BANCO DE PERNAMBUCO",
    "30 - BANCO DIGIMAIS",
    "32 - BANCO FATOR",
    "34 - BANCO GENIAL",
    "36 - BANCO GUANABARA",
    "43 - BANCO LUSO BRASILEIRO",
    "46 - BANCO MIZUHO DO BRASIL",
    "49 - BANCO OURINVEST",
    "52 - BANCO PARANÁ",
    "53 - BANCO PAULISTA",
    "58 - BANCO RENDIMENTO",
    "59 - BANCO RIBEIRÃO PRETO",
    "60 - BANCO RNX",
    "61 - BANCO RODOBENS",
    "64 - BANCO SEMEAR",
    "66 - BANCO STELLANTIS",
    "67 - BANCO TOPÁZIO",
    "69 - BANCO TRIANGULO",
    "70 - BANCO UNICRED",
    "73 - BANCO XCMG BRASIL",
    "78 - BARIGUI SCFI",
    "79 - BIORC FINANCEIRA",
    "82 - BR PARTNERS",
    "83 - BRASIL PLURAL",
    "86 - CALCRED SCFI",
    "87 - CARUANA SCFI",
    "90 - CITROEN",
    "91 - COBUCCIO SCFI",
    "94 - CREDIARE SCFI",
    "96 - CRESOL",
    "97 - DEUTSCHE SPARKASSEN LEASING DO BRASIL BANCO MULTIP",
    "99 - ESTRELA MINEIRA CREDITO FINANCIAMENTO S.A",
    "100 - FACTA SCFI",
    "101 - HAITONG BANCO DE INVESTIMENTO DO BRASIL",
    "102 - HS FINANCEIRA S/A CFI",
    "103 - ICBC DO BRASIL",
    "107 - LECCA SCFI",
    "108 - M PAGAMENTOS SCFI",
    "109 - MERCADO CRÉDITO SCFI (MERCADO LIVRE)",
    "110 - MIDWAY SCFI (RIACHUELO)",
    "111 - BANCO SISTEMA",
    "112 - NBC BANK",
    "113 - NEON SCFI",
    "114 - NOVO BANCO CONTINENTAL",
    "116 - OMNI SCFI",
    "118 - PEFISA SCFI",
    "119 - PERNAMBUCANAS SCFI",
    "121 - PLANTAE SCFI",
    "124 - QISTA SCFI",
    "125 - REALIZE SCFI",
    "126 - RPW SCFI (EMPRESTA CAPITAL)",
    "129 - SENFF SCFI",
    "131 - SIMPALA SCFI",
    "132 - SINGULARE",
    "133 - SINOSSERRA SCFI",
    "135 - SOROCRED FINANCEIRA",
    "136 - STONE SCFI",
    "137 - TENTOS SCFI",
    "138 - UNIPRIME CENTRAL",
    "139 - VIA CERTA SCFI",
    "141 - ZEMA SCFI",
    "142 - OMNI BANCO",
    "143 - BANCO CIFRA",
    "146 - NEON/BIORC SCFI",
    "147 - OMNI BANCO/OMNI SCFI",
    "148 - PARANÁ BANCO S.A.",
    "144 - BANCO DIGIO S.A.",
    "1 - AGORACRED SCFI",
    "2 - AGROLEND SCFI",
    "9 - 99PAY",
    "89 - CIA HIPOTECARIA PIRATINI - CHP",
    "93 - COOPERATIVA DE CREDITO RURAL DE PRIMAVERA DO LESTE",
    "95 - CREDITÁ SCFI",
    "98 - DM SCFI",
    "104 - INCO SEP",
    "106 - LEBES SCFI",
    "117 - PAGSEGURO",
    "127 - SANTANA SCFI",
    "128 - SANTINVEST SCFI",
    "130 - SF3 SCFI",
    "134 - SOCINAL SCFI"
]