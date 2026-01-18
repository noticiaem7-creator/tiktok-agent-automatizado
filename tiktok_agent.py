# -*- coding: utf-8 -*-
# Agente Automatizado TikTok - Monitoramento de Comentários
# Autor: Sistema de Automação
# Data: 2026

import time
import sys
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import schedule

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tiktok_agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurar stdout para UTF-8 no Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class TikTokAgent:
    def __init__(self, headless=False):
        """Inicializa o agente"""
        self.driver = None
        self.headless = headless
        self.resposta_probabilidade = 0.4
        self.curtir_probabilidade = 0.6
        self.comentarios_processados = set()
        
    def iniciar_driver(self):
        """Inicia o driver Selenium"""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        logger.info('🚀 Driver Selenium iniciado')
        
    def conectar_tiktok(self):
        """Conecta ao TikTok Studio"""
        try:
            self.driver.get("https://www.tiktok.com/tiktokstudio/comment")
            time.sleep(3)
            logger.info('✅ Conectado ao TikTok Studio')
        except Exception as e:
            logger.error(f'❌ Erro ao conectar: {e}')
            
    def monitorar_comentarios(self):
        """Monitora novos comentários"""
        try:
            wait = WebDriverWait(self.driver, 10)
            # Aguarda os comentarios carregarem
            comentarios = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='comment-item']"))
            )
            logger.info(f'📊 {len(comentarios)} comentários encontrados')
            return comentarios
        except Exception as e:
            logger.error(f'❌ Erro ao monitorar: {e}')
            return []
            
    def curtir_aleatoriamente(self, comentario_id):
        """Curte comentário aleatoriamente"""
        if random.random() < self.curtir_probabilidade:
            try:
                # Encontra e clica no botão de like
                botao_like = self.driver.find_element(By.CSS_SELECTOR, f"[data-comment-id='{comentario_id}'] [data-testid='like-button']")
                botao_like.click()
                logger.info(f'❤️ Comentário {comentario_id} curtido!')
                return True
            except Exception as e:
                logger.debug(f'Erro ao curtir: {e}')
        return False
        
    def gerar_resposta_ia(self, texto_comentario):
        """Gera resposta inteligente com base no conteúdo"""
        palavras_chave = {
            'corrupt': 'Verdade! Precisamos de transparência total! 🔍',
            'impeachment': 'Isso! A luta é legítima! Vamo junto nessa luta? 🙋',
            'presidente': 'Boa ideia! Precisamos de líderes com atitude! 💪',
            'voto': 'Segue com a gente aqui! 💪',
            'deus': 'Que bom debater isso com vocês por aqui! 🗒️',
            'governo': 'Cansão demais! Clamamos por mudança real. Vota junto? 👏',
            'verdade': 'Kkk bora! Segue com a gente aqui! 💪',
        }
        
        texto_lower = texto_comentario.lower()
        for palavra, resposta in palavras_chave.items():
            if palavra in texto_lower:
                return resposta
                
        return 'Que bom debater isso com vocês! 🙋'
        
    def responder_aleatoriamente(self, comentario_id, texto_comentario):
        """Responde comentário aleatoriamente"""
        if random.random() < self.resposta_probabilidade:
            resposta = self.gerar_resposta_ia(texto_comentario)
            return self.postar_resposta(comentario_id, resposta)
        return False
        
    def postar_resposta(self, comentario_id, resposta):
        """Posta resposta no comentário"""
        try:
            # Clica em responder
            botao_responder = self.driver.find_element(By.CSS_SELECTOR, f"[data-comment-id='{comentario_id}'] [data-testid='reply-button']")
            botao_responder.click()
            time.sleep(1)
            
            # Escreve a resposta
            campo_texto = self.driver.find_element(By.CSS_SELECTOR, "textarea[placeholder*='Responder']")
            campo_texto.send_keys(resposta)
            time.sleep(0.5)
            
            # Envia
            botao_enviar = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Enviar']")
            botao_enviar.click()
            
            logger.info(f'💬 Resposta postada no comentário {comentario_id}: {resposta}')
            return True
        except Exception as e:
            logger.debug(f'Erro ao postar resposta: {e}')
            return False
            
    def processar_comentarios(self):
        """Processa todos os comentários"""
        logger.info('\n=== CICLO DE PROCESSAMENTO ==="')
        comentarios = self.monitorar_comentarios()
        
        if not comentarios:
            logger.info('Nenhum comentário para processar')
            return
            
        for idx, comentario in enumerate(comentarios):
            try:
                # Extrai ID e texto do comentário
                comentario_id = comentario.get_attribute('data-comment-id')
                texto = comentario.text
                
                if comentario_id not in self.comentarios_processados:
                    # Acões aleatórias
                    self.curtir_aleatoriamente(comentario_id)
                    self.responder_aleatoriamente(comentario_id, texto)
                    
                    self.comentarios_processados.add(comentario_id)
                    time.sleep(random.uniform(2, 5))
            except Exception as e:
                logger.debug(f'Erro ao processar comentário {idx}: {e}')
                
        logger.info(f'✅ Ciclo concluido com {len(self.comentarios_processados)} comentários processados')
        
    def executar(self, intervalo=300):
        """Executa o agente continuamente"""
        logger.info('\n' + '='*50)
        logger.info('🤖 AGENTE TikTok INICIADO!')
        logger.info('='*50)
        
        try:
            self.iniciar_driver()
            self.conectar_tiktok()
            
            # Agenda o processamento
            schedule.every(intervalo).seconds.do(self.processar_comentarios)
            
            logger.info(f'\n⏰ Monitorando a cada {intervalo} segundos...\n')
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
        except KeyboardInterrupt:
            logger.info('\n❌ Agente interrompido pelo usuário')
        except Exception as e:
            logger.error(f'❌ Erro fatal: {e}')
        finally:
            if self.driver:
                self.driver.quit()
            logger.info('🛑 Agente finalizado')

if __name__ == '__main__':
    # Configurações
    INTERVALO = 300  # 5 minutos
    HEADLESS = False  # Mostra a janela do navegador
    
    # Inicia o agente
    agente = TikTokAgent(headless=HEADLESS)
    agente.executar(intervalo=INTERVALO)
