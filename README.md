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

Exemplo de postagem no Discord:

```
🔥 WallDrop: Wallpapers mais hypados do Wallpaper Engine! 🔥
[Embed]
Título: Neon Galaxy
Link: https://steamcommunity.com/sharedfiles/filedetails/?id=123456
Imagem: [Prévia do wallpaper]
Rodapé: Powered by WallDrop
```

## 🛠️ Solução de Problemas

- **Erro: "PrivilegedIntentsRequired**
  - Certifique-se de ativar a Message Content Intent no Discord Developer Portal.
- **Erro: "Connection refused"**
  - Confirme que a API (api.py) está rodando em http://localhost:8000.
- **Erro: "403 Forbidden (error code: 50001)"**
  - Verifique as permissões do bot no canal (Enviar Mensagens, Incorporar Links, Ler Mensagens).

- **Wallpapers não aparecem**
  - Confirme que o wallpapers.json contém dados (rode python3 scraper.py novamente).

## 📝 Notas
  - O scraping do Steam Workshop deve ser feito com moderação para evitar bloqueios. O script inclui um delay (`sleep`) para reduzir esse risco.

  - O token do Discord no `.env` é sensível. Não o compartilhe e não o envie ao repositório.
  - Para rodar **24/7**, use ferramentas como `screen` ou `tmux` no Linux:

  *bash*
  ```
screen -S api
python3 api.py
# Ctrl + A, D para desconectar
screen -S bot
python3 bot.py
# Ctrl + A, D para desconectar
```

## 🤝 Contribuições
O WallDrop é um projeto novo que vai passar por várias melhorias, então 
sinta-se à vontade para abrir issues ou pull requests com melhorias ou correções!


## 📜 Licença
Este projeto ainda não possui uma licença definida. Caso queira utilizá-lo, entre em contato comigo para mais informações.
