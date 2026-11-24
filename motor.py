import numpy as np
import pandas as pd

def classificar_risco(p):
    if not 0 <= p <= 1: raise ValueError('Score inválido')
    if p < .30: return 'BAIXO', 'Manter o monitoramento preventivo.'
    if p < .70: return 'MÉDIO', 'Reavaliar as condições operacionais.'
    return 'ALTO', 'Priorizar a avaliação do equipamento.'

def explicar_previsao(modelo, amostra, referencia, n_permutacoes=100, random_state=42):
    rng=np.random.default_rng(random_state)
    colunas=list(amostra.columns)
    indice=list(modelo.classes_).index(1)
    estados=[]; ordens=[]
    for _ in range(n_permutacoes):
        atual=referencia.iloc[[rng.integers(len(referencia))]].copy()
        ordem=rng.permutation(len(colunas)); ordens.append(ordem)
        estados.append(atual.copy())
        for j in ordem:
            atual[colunas[j]]=amostra[colunas[j]].iloc[0]
            estados.append(atual.copy())
    probs=modelo.predict_proba(pd.concat(estados,ignore_index=True))[:,indice].reshape(n_permutacoes,len(colunas)+1)
    contrib=np.zeros(len(colunas))
    for ordem, p in zip(ordens,probs): contrib[ordem]+=np.diff(p)
    contrib*=100/n_permutacoes
    df=pd.DataFrame({'Variável':colunas,'Valor':amostra.iloc[0].values,'Contribuição (p.p.)':contrib})
    df['Magnitude']=abs(contrib)
    return df.sort_values('Magnitude',ascending=False), float(probs[:,0].mean())
