# WallDrop 🖼️

**WallDrop** é um bot do Discord que coleta os wallpapers mais populares do **Wallpaper Engine** (via Steam Workshop) e os posta automaticamente em um canal do Discord. Ele exibe o título, link, imagem de prévia e um rodapé em um embed elegante.

## 📋 Funcionalidades

- **Scraping de Wallpapers**: Coleta os wallpapers mais populares do Wallpaper Engine diretamente do Steam Workshop.
- **API Local**: Fornece uma API simples para acessar os dados dos wallpapers.
- **Bot do Discord**: Posta os wallpapers em um canal do Discord com:
  - Título do wallpaper.
  - Link para o Steam Workshop.
  - Imagem de prévia.
  - Rodapé personalizado.
- **Postagem Automática e Manual**:
  - Posta wallpapers automaticamente a cada 24 horas (o horário pode ser modificado).
  - Permite postagem manual com o comando `!wallpapers`.

## 🛠️ Pré-requisitos

    Antes de começar, certifique-se de ter:

- **Sistema Operacional**: Linux (Usado no projeto), Windows ou macOS.
- **Python**: Versão 3.8 ou superior.
- **Git**: Para clonar o repositório.
- **Conta no Discord**: Com um servidor onde você tenha permissões de administrador.
- **Discord Developer Portal**: Para criar o bot e obter o token.

## 🚀 Instalação

    Siga os passos abaixo para configurar e executar o **WallDrop**:

### 1. Clone o Repositório

bash
```
    git clone https://github.com/seu-usuario/walldrop-bot.git
    cd walldrop-bot
```
 - Substitua seu-usuario pelo seu nome de usuário do GitHub.

### 2. Crie e Ative um Ambiente Virtual

bash

```
python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instale as Dependências
- Com o ambiente virtual ativo, instale as bibliotecas necessárias:

bash

```
pip install requests beautifulsoup4 fastapi uvicorn discord.py python-dotenv
```

### 4. Configure o Bot no Discord

 1 - Acesse o <a source/>
<a href="https://discord.com/developers/applications" target="_blank">Discord Developer Portal<a> 

 2 - Crie uma nova aplicação chamada WallDrop (Ou outro nome específico, como quiser).

 3 - Na aba Bot:
- Adicione um bot e copie o Token.
- Ative a intent Message Content Intent na seção Privileged Gateway Intents.

4 - Na aba OAuth2 > URL Generator:
- Marque Scopes: `bot`
- Marque Bot Permissions:

  `messages.read` (Read Messages/View Channels)

  `dm_channels.messages.write` (Send Messages)

  `dm_channels.messages.read` (Read Message History)

- Copie a URL gerada e use-a para convidar o bot ao seu servidor.

5 - No Discord, ative o Modo Desenvolvedor
- Configurações do Usuário > Aparência > Modo Desenvolvedor.
- Copie o ID do canal onde o bot deve postar (ex.: #wallpapers).

### 5. Configure o Arquivo .env
*Crie um arquivo chamado .env na raiz do projeto e adicione:*

.env

```
DISCORD_TOKEN=seu_token_aqui
CHANNEL_ID=seu_canal_id_aqui
```
- Substitua `seu_token_aqui` pelo token do bot.
- Substitua `seu_canal_id_aqui` pelo ID do canal.

### 6. Execute o Projeto
 1 - Colete os Wallpapers:

bash
```
python3 scraper.py
```
*Isso cria o arquivo wallpapers.json com os dados dos wallpapers.*

2 - Inicie a API:

bash
```
python3 api.py
```

*A API estará disponível em `http://localhost:8000/wallpapers`*

3 - Inicie o Bot:

bash
```
python3 bot.py
```
*O bot se conectará ao Discord e começará a postar wallpapers.*

## 📖 Uso

Postagem Automática: O bot posta wallpapers a cada 24 horas no canal especificado.
Postagem Manual: Use o comando !wallpapers no canal para postar wallpapers sob demanda.