# SOMPO | Risk Analytics — Sprint 4
Protótipo acadêmico de análise de risco de sinistros em equipamentos agrícolas. Utiliza Random Forest otimizado e pipeline de pré-processamento da Sprint 3. Dados simulados; não é ferramenta atuarial validada.

## Executar
Recomendado Python 3.13. Instale `pip install -r requirements.txt` e execute `streamlit run app.py`.
No Streamlit Community Cloud, selecione `app.py` e Python 3.13.

## Funcionalidades
11 entradas, score da classe positiva, faixas demonstrativas (30% e 70%), contribuições individuais aproximadas por 100 permutações de Shapley, orientações e exportação CSV.

## Demonstração
Clique em Carregar exemplo da Sprint 4 e depois em Analisar risco do equipamento. Score esperado: 10,87%, risco baixo; manutenção atrasada +7,09 p.p. aproximadamente.

## Arquivos
`app.py`: interface; `motor.py`: classificação e explicabilidade; `modelo_sompo.pkl`: pipeline; `referencia_sompo.csv`: 100 registros; `especificacoes_sompo.json`: limites e categorias; `requirements.txt`: dependências.

## Resultados da Sprint 3
Accuracy 94,75%; Precision 95,86%; Recall 92,05%; F1 93,91%; AUC 94,18%.

## Limitações
Dados simulados, score não calibrado para uso real, contribuições não causais. Limites de risco demonstrativos. As versões de NumPy e Joblib admitem faixas para facilitar instalação; validar a previsão após deploy.
