from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from motor import classificar_risco, explicar_previsao

st.set_page_config(page_title='SOMPO | Risk Analytics', page_icon='🛡️', layout='wide')
ROOT=Path(__file__).resolve().parent
LABELS={'tipo_operacao':'Tipo de operação','velocidade_media':'Velocidade média (km/h)','tempo_uso_anos':'Tempo de uso (anos)','distancia_percorrida_km':'Distância percorrida (km)','chuva':'Chuva','proximidade_agua':'Proximidade de água','temperatura':'Temperatura (°C)','operacao_noturna':'Operação noturna','regiao_risco':'Região de risco','historico_sinistro':'Histórico de sinistro','manutencao_atrasada':'Manutenção atrasada'}
EXEMPLO=dict(zip(LABELS,['campo',47,8,834,'nao','nao',24,'nao','baixa','nao','sim']))
@st.cache_resource
def carregar():
    return joblib.load(ROOT/'modelo_sompo.pkl'), pd.read_csv(ROOT/'referencia_sompo.csv'), json.loads((ROOT/'especificacoes_sompo.json').read_text(encoding='utf-8'))
try: modelo, referencia, specs=carregar()
except Exception as e:
    st.error(f'Não foi possível carregar os recursos: {e}'); st.stop()
st.markdown('## SOMPO | Risk Analytics')
st.caption('CHALLENGE SOMPO  /  MACHINE LEARNING  /  SPRINT 4')
st.title('Inteligência para prevenção de sinistros agrícolas')
st.info('Protótipo acadêmico com dados simulados. Não substitui avaliação técnica ou atuarial.')
with st.sidebar:
    st.header('Sobre o modelo')
    st.write('Random Forest otimizado com GridSearchCV')
    for k,v in [('Accuracy','94,75%'),('Precision','95,86%'),('Recall','92,05%'),('F1-score','93,91%'),('AUC','94,18%')]: st.metric(k,v)
    st.caption('Métricas do conjunto de teste da Sprint 3.')
st.subheader('01 / Dados do equipamento')
if st.button('Carregar exemplo da Sprint 4'):
    for k,v in EXEMPLO.items(): st.session_state[k]=v
    st.session_state.pop('resultado',None)
with st.form('equipamento'):
    cols=st.columns(3); dados={}
    for i,(k,s) in enumerate(specs.items()):
        with cols[i%3]:
            if s['tipo']=='numerico':
                dados[k]=st.number_input(LABELS[k],min_value=int(s['minimo']),max_value=int(s['maximo']),value=int(s['mediana']),step=1,key=k)
            else:
                dados[k]=st.selectbox(LABELS[k],s['categorias'],format_func=lambda x:{'nao':'Não','media':'Média'}.get(x,x.capitalize()),key=k)
    enviar=st.form_submit_button('Analisar risco do equipamento',type='primary',use_container_width=True)
if enviar:
    with st.spinner('Calculando previsão e contribuições individuais...'):
        amostra=pd.DataFrame([dados],columns=list(specs))
        p=float(modelo.predict_proba(amostra)[0,list(modelo.classes_).index(1)])
        drivers,base=explicar_previsao(modelo,amostra,referencia)
        np.testing.assert_allclose(p,base+drivers['Contribuição (p.p.)'].sum()/100,atol=1e-8)
        st.session_state['resultado']=(p,drivers,base,dados.copy())
if 'resultado' in st.session_state:
    p,drivers,base,entrada=st.session_state['resultado']; nivel,orientacao=classificar_risco(p)
    st.subheader('02 / Resultado da última análise')
    a,b,c=st.columns(3); a.metric('Score de risco',f'{p:.2%}'); b.metric('Nível de risco',nivel); c.metric('Score de referência',f'{base:.2%}')
    st.progress(p); st.caption('Baixo: < 30% | Médio: 30% a < 70% | Alto: ≥ 70% — limites demonstrativos.')
    {'BAIXO':st.success,'MÉDIO':st.warning,'ALTO':st.error}[nivel](orientacao)
    if entrada['manutencao_atrasada']=='sim': st.warning('Ponto de atenção: verificar a manutenção atrasada do equipamento.')
    st.subheader('03 / O que influenciou a previsão?')
    df=drivers.copy(); df['Fator']=df['Variável'].map(LABELS); df['Impacto']=np.where(df['Contribuição (p.p.)']>0,'Aumenta',np.where(df['Contribuição (p.p.)']<0,'Reduz','Neutro'))
    for _,r in df.head(3).iterrows(): st.write(f"**{r['Fator']}** — {r['Impacto']} o score: {r['Contribuição (p.p.)']:+.2f} p.p.")

    # Preparação dos dados para visualização
    df_grafico = df.rename(
        columns={'Contribuição (p.p.)': 'contribuicao_pp'}
    ).copy()

    df_grafico['contribuicao_pp'] = pd.to_numeric(
        df_grafico['contribuicao_pp'],
        errors='raise'
    )

    # Gráfico horizontal dos drivers de risco
    chart = alt.Chart(df_grafico).mark_bar(
        cornerRadiusEnd=3,
        size=22
    ).encode(
        x=alt.X(
            'contribuicao_pp:Q',
            title='Contribuição (pontos percentuais)',
            scale=alt.Scale(zero=True)
        ),
        y=alt.Y(
            'Fator:N',
            sort=df_grafico['Fator'].tolist(),
            title=None,
            axis=alt.Axis(labelLimit=300)
        ),
        color=alt.Color(
            'Impacto:N',
            scale=alt.Scale(
                domain=['Aumenta', 'Reduz', 'Neutro'],
                range=['#DC2626', '#15803D', '#9CA3AF']
            ),
            legend=alt.Legend(title='Impacto')
        ),
        tooltip=[
            alt.Tooltip('Fator:N'),
            alt.Tooltip('Impacto:N'),
            alt.Tooltip(
                'contribuicao_pp:Q',
                title='Contribuição (p.p.)',
                format='+.2f'
            )
        ]
    ).properties(
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    st.caption('Contribuições aproximadas por permutações de Shapley, relativas à referência; não indicam causalidade.')
    with st.expander('Detalhes e dados da última análise'):
        st.dataframe(df[['Fator','Valor','Contribuição (p.p.)','Impacto']],hide_index=True)
        st.json(entrada)
        st.download_button('Baixar análise CSV',df.to_csv(index=False).encode('utf-8-sig'),'analise_sompo.csv','text/csv')
else: st.caption('Preencha os campos e clique em Analisar risco do equipamento.')
