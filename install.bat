@echo off
REM Agente TikTok Automatizado - Script de Instalacao Windows
REM Este script clona, instala e executa o agente automaticamente

echo.
echo =========================================
echo   INSTALADOR - Agente TikTok Automatizado
echo =========================================
echo.

REM Definir diretorio de instalacao
set INSTALL_DIR=%USERPROFILE%\tiktok-agent

echo [1/4] Preparando diretorio...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo Diretorio criado em: %INSTALL_DIR%
) else (
    echo Diretorio ja existe. Usando: %INSTALL_DIR%
)

cd /d "%INSTALL_DIR%"

echo.
echo [2/4] Clonando repositorio do GitHub...
git clone https://github.com/noticiaem7-creator/tiktok-agent-automatizado.git . 2>nul
if %ERRORLEVEL% EQU 0 (
    echo OK - Repositorio clonado com sucesso
) else (
    echo ERRO ao clonar. Verifique se Git esta instalado.
    pause
    exit /b 1
)

echo.
echo [3/4] Instalando dependencias Python...
pip install -r requirements.txt
if %ERRORLEVEL% EQU 0 (
    echo OK - Dependencias instaladas
) else (
    echo ERRO ao instalar dependencias
    pause
    exit /b 1
)

echo.
echo [4/4] Executando o agente...
echo.
echo =========================================
echo   AGENTE INICIADO!
echo =========================================
echo.

python tiktok_agent.py

pause
