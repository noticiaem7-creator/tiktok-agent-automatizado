# 🤖 Agente TikTok Automatizado

> Agente inteligente para monitorar, curtir e responder comentários no TikTok Studio automaticamente com IA.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Recursos Principais

- 🗒️ **Monitoramento 24/7**: Monitora continuamente novos comentários
- ❤️ **Curtidas Aleatórias**: 60% de chance de curtir comentários (configurável)
- 💬 **Respostas com IA**: 40% de chance de responder inteligentemente (configurável)
- 🗓️ **Logs Detalhados**: Sistema de logging completo para rastreamento
- 🔢 **Detecção de Tópicos**: Reconhece e responde apropriadamente a diferentes temas
- 🔀 **Infinito**: Executa continuamente a cada 5 minutos (configurável)

## 💼 Instalação

### Pré-requisitos

- Python 3.8+
- Google Chrome/Chromium instalado
- ChromeDriver ([Download aqui](https://chromedriver.chromium.org/))
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/noticiaem7-creator/tiktok-agent-automatizado.git
cd tiktok-agent-automatizado
```

### Passo 2: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Variáveis de Ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```ini
INTERVALO=300                 # 5 minutos
HEADLESS=false                # Mostrar navegador
PROBABILIDADE_CURTIDA=0.6     # 60%
PROBABILIDADE_RESPOSTA=0.4    # 40%
```

## 🚀 Como Usar

### Execução Básica

```bash
python tiktok_agent.py
```

### Execução em Background (Linux/Mac)

```bash
nohup python tiktok_agent.py > agent.log 2>&1 &
```

### Monitorar Logs

```bash
tail -f tiktok_agent.log
```

## ⚡ Personalização

### Alterar Probabilidades

Edite o arquivo `tiktok_agent.py`:

```python
agente = TikTokAgent(headless=False)
agente.resposta_probabilidade = 0.5    # 50% de chance
agente.curtir_probabilidade = 0.7      # 70% de chance
agente.executar(intervalo=600)         # 10 minutos
```

### Adicionar Mais Respostas

Edite a função `gerar_resposta_ia()`:

```python
palavras_chave = {
    'sua_palavra': 'Sua resposta aqui! 🤟',
    'outra_palavra': 'Outra resposta! 🌟',
}
```

## 📊 Exemplos de Respostas

O agente detecta automaticamente:

- 📊 **Corrupção**: "Verdade! Precisamos de transparência total! 🔍"
- 📝 **Impeachment**: "Isso! A luta é legítima! Vamo junto? 🙋"
- 👋 **Presidente**: "Boa ideia! Precisamos de líderes com atitude! 💪"
- 🗣️ **Debate**: "Que bom debater isso com vocês! 🙋"

## 📄 Estrutura de Pastas

```
tiktok-agent-automatizado/
├─ tiktok_agent.py          # Arquivo principal do agente
├─ requirements.txt          # Dependências Python
├─ .env.example              # Exemplo de variáveis de ambiente
├─ README.md                 # Este arquivo
├─ logs/                     # Pasta de logs (criada automaticamente)
└─ tiktok_agent.log          # Arquivo de log do agente
```

## 📚 Log de Ações

Todas as ações são registradas automaticamente:

```
2026-01-18 09:15:32 - INFO - 🤖 AGENTE TikTok INICIADO!
2026-01-18 09:15:35 - INFO - ✅ Conectado ao TikTok Studio
2026-01-18 09:15:40 - INFO - 📊 15 comentários encontrados
2026-01-18 09:15:45 - INFO - ❤️ Comentário curtido!
2026-01-18 09:15:50 - INFO - 💬 Resposta postada
```

## ⚠️ Aviso Legal

Este agente é fornecido como ferramenta educacional. O usuário é responsável por:

- Usar de forma responsável e ética
- Respeitar os termos de serviço do TikTok
- Não violar políticas de automação do TikTok
- Monitorar o comportamento da conta

## 🐛 Reportar Problemas

Encontre um bug? Abra uma [Issue](https://github.com/noticiaem7-creator/tiktok-agent-automatizado/issues)

## 👋 Contribuir

Tem ideias? Envie um [Pull Request](https://github.com/noticiaem7-creator/tiktok-agent-automatizado/pulls)

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

Feito com ❤️ por [Sistema de Automação](https://github.com/noticiaem7-creator)

[Estrele este projeto! ⭐️](https://github.com/noticiaem7-creator/tiktok-agent-automatizado/stargazers)

</div>
