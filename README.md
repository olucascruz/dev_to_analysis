# Dev.to analysis
> Bot faz web scraping no site [dev.to](https://dev.to/) pegando os dados dos artigos mais populares da semana e gera um csv com esses dados. <br>
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

na Pasta visualization\src

streamlit run streamlit.py

```

## Project Tree
```
dev_to_analysis
├─ .gitignore
├─ bot_dev_to
│  ├─ analysis.ipynb
│  ├─ bot.py
│  ├─ bot_dev_to.botproj
│  ├─ build.bat
│  ├─ build.ps1
│  ├─ build.sh
│  ├─ config
│  │  └─ bot_config.py
│  ├─ resources
│  │  └─ start.png
│  ├─ results
│  └─ scraping_data.py
├─ README.md
├─ requirements.txt
└─ visualization
   └─ src
      ├─ streamlit.py
      ├─ style.css
      └─ utils.py
```
