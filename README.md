
# 🛡️ SOMPO | Risk Analytics

### Inteligência para prevenção de sinistros agrícolas

**Challenge SOMPO — Machine Learning — Sprint 4**

## Integrantes do grupo

- Aline Delphino Chiaramonte — RM569860
- Gabriel Gomes dos Santos — RM573836
- Gustavo Luiz Vilella Santin — RM573213
- Victor Dias Rodrigues Bandeira de Azevedo — RM574108

## 1. Sobre o projeto

O SOMPO Risk Analytics é uma solução baseada em Machine Learning desenvolvida para estimar o risco de sinistros em equipamentos agrícolas, considerando características operacionais, ambientais e históricas.

A proposta busca apoiar a tomada de decisão e facilitar a identificação de fatores de risco, contribuindo para a adoção de medidas preventivas.

## 2. Acesso à aplicação

🔗 **Aplicação:** https://sompo-risk-analytics.streamlit.app/

🔗 **GitHub:** https://github.com/Aline-17/SOMPO-Risk-Analytics

## 3. Problema de negócio

A identificação antecipada de condições associadas à ocorrência de sinistros em equipamentos agrícolas pode contribuir para a gestão de riscos e para o planejamento de ações preventivas.

A solução transforma dados operacionais em informações acessíveis e interpretáveis para o usuário.

## 4. Modelo de Machine Learning

O modelo selecionado foi o Random Forest, otimizado por meio do GridSearchCV.

O pipeline integra o pré-processamento dos dados e o modelo treinado, garantindo a consistência entre o ambiente de desenvolvimento e a aplicação publicada.

### Métricas de desempenho

| Métrica | Resultado |
|---|---:|
| Accuracy | 94,75% |
| Precision | 95,86% |
| Recall | 92,05% |
| F1-score | 93,91% |
| AUC | 94,18% |

## 5. Funcionalidades

- Formulário interativo com 11 variáveis de entrada;
- Predição do score de risco de sinistro;
- Classificação em risco baixo, médio ou alto;
- Explicabilidade individual por aproximação dos valores de Shapley;
- Identificação dos principais drivers de risco;
- Gráfico interativo das contribuições;
- Orientações preventivas;
- Alerta de manutenção atrasada;
- Exportação da análise em CSV;
- Carregamento automático de um cenário demonstrativo.

## 6. Classificação dos níveis de risco

| Classificação | Score | Orientação |
|---|---|---|
| Baixo | Inferior a 30% | Manter o monitoramento preventivo |
| Médio | De 30% a menos de 70% | Reavaliar as condições operacionais |
| Alto | Igual ou superior a 70% | Priorizar a avaliação do equipamento |

Os limites possuem caráter demonstrativo e acadêmico.

## 7. Explicabilidade do modelo

A solução utiliza uma aproximação dos valores de Shapley por permutações para identificar a contribuição individual de cada variável.

As contribuições são apresentadas em pontos percentuais, indicando os fatores que aumentam ou reduzem o score estimado em relação aos dados de referência.

Essa abordagem facilita a interpretação das previsões e aumenta a transparência do modelo.

## 8. Demonstração e validação

O cenário demonstrativo disponível na aplicação reproduz a análise realizada no notebook da Sprint 4.

| Indicador | Resultado |
|---|---:|
| Score de risco | 10,87% |
| Score de referência | 41,54% |
| Classificação | Baixo |
| Velocidade média | -13,47 p.p. |
| Tempo de uso | -9,79 p.p. |
| Manutenção atrasada | +7,09 p.p. |

Os resultados foram reproduzidos tanto no Google Colab quanto na aplicação Streamlit.

## 9. Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- GridSearchCV
- Joblib
- Altair
- Streamlit
- Google Colab
- GitHub
- Streamlit Community Cloud

## 10. Estrutura do repositório

    SOMPO-Risk-Analytics/
    ├── .streamlit/
    │   └── config.toml
    ├── app.py
    ├── motor.py
    ├── modelo_sompo.pkl
    ├── referencia_sompo.csv
    ├── especificacoes_sompo.json
    ├── requirements.txt
    └── README.md

## 11. Execução local

Recomenda-se utilizar Python 3.13.

    git clone https://github.com/Aline-17/SOMPO-Risk-Analytics.git
    cd SOMPO-Risk-Analytics
    pip install -r requirements.txt
    streamlit run app.py

## 12. Evolução do projeto

A Sprint 4 consolidou os trabalhos desenvolvidos nas etapas anteriores, transformando o modelo treinado em uma aplicação web interativa, acessível e interpretável.

A solução integra predição, explicabilidade e orientações preventivas em uma interface voltada ao usuário.

## 13. Limitações

O projeto possui finalidade acadêmica e utiliza dados simulados.

Os scores apresentados representam estimativas do modelo, não probabilidades de sinistro validadas atuarialmente.

As contribuições individuais não representam relações comprovadas de causa e efeito.

A solução não substitui avaliações técnicas ou atuariais.

## 14. Perspectivas futuras

- Integração com dados reais;
- Calibração das probabilidades;
- Validação dos critérios de classificação;
- Monitoramento do desempenho;
- Integração com sistemas corporativos.

---

**Challenge SOMPO | Machine Learning | Sprint 4**
