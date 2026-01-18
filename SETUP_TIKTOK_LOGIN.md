# Como Fazer Login no TikTok com o Agente

## Problema
Quando você executa o agente, o Chrome abre mas você precisa fazer login no TikTok Studio manualmente.

## Solução

### Opção 1: Login Manual (Recomendado) - Máis Fácil

1. **Execute o agente:**
   ```bash
   python tiktok_agent.py
   ```

2. **Uma janela do Chrome abrirá automaticamente**

3. **Você estará em:** `https://www.tiktok.com/tiktokstudio/comment`

4. **Faça o login:**
   - Clique em "Fazer login" ou "Log in"
   - Digite seu email/telefone
   - Digite sua senha
   - Complete a verificação de segurança (se necessário)

5. **Aguarde o carregamento:**
   - O agente já estará monitorando
   - Você verá a mensagem no terminal: "Monitorando a cada 300 segundos..."

6. **Deixe a janela aberta:**
   - Não feche a janela do Chrome
   - O agente continuará trabalhando em background

7. **Pronto! O agente está ativo**
   - Curtingários serão curtidos automaticamente
   - Comentarios serão respondidos automaticamente

---

### Opção 2: Usar Cookies de Login Anterior (Avançado)

Se já fez login uma vez, o Chrome salva os cookies. Na próxima execução, você pode estar já logado automaticamente!

---

## Dévidas Comuns

### "O Chrome pedindo verificação de segurança"
- Aceite a verificação de código SMS ou email
- Aguarde alguns segundos para que o agente continue

### "Chrome fechou sozinho"
- Execue o script novamente: `python tiktok_agent.py`
- O agente estará rodando enquanto o terminal estiver aberto

### "Não quero manter o Chrome aberto"
- Infelizmente o Selenium precisa do navegador aberto para funcionar
- Mas vocé pode minimizar a janela normalmente

### "Erro: 'Chromedrive not found'"
- Verifique se o ChromeDriver está na pasta do projeto
- Ou instale: `pip install webdriver-manager`

---

## Fluxo de Execução

```
1. Executa: python tiktok_agent.py
   |
2. Abre Chrome (vêc este)
   |
3. Navega para TikTok Studio
   |
4. Vocé faz login (vêc fazer isso na janela)
   |
5. Agente monitora automaticamente
   |
6. Agenda processo a cada 5 minutos
   |
7. Curte e responde comentarios aleatoriamente
```

---

## Dicas Ñ

- **Deixe rodando por mais tempo:** Quanto mais tempo o agente rodar, mais engajamento vocé terá
- **Personalize as respostas:** Edite `tiktok_agent.py` linha ~75 para adicionar mais respostas
- **Monitore os logs:** Verifique `tiktok_agent.log` para ver o que o agente está fazendo
- **Use uma segunda conta:** Para testes, crie uma conta só do TikTok para o agente

---

Qualquer dúvida? Verifique o [README.md](README.md)
