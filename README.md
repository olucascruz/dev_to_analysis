# Dev.to analysis
> Bot faz scraping no dev.to pegando os melhores artigos da semana (em números) e gera um csv com esses dados. <br>
> Gera um painel com os dados obtidos do site.


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou  `Python >= 3.10`
- Você tem uma máquina `<Windows>`.

## 🚀 Clonando Dev.to analysis

Para clonar o Dev.to analysis, siga estas etapas:

Windows:

```
git clone https://github.com/olucascruz/dev_to_analysis.git
```

## ☕ Usando Dev.to analysis

Para usar Dev.to analysis, siga estas etapas:

```
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt

na Pasta bot_dev_to

python bot.py

na Pasta visualizatin\src

streamlit run streamlit.py

```
