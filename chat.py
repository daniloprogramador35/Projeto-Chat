# Titulo: Hashzap
# Botão de iniciar chat
    # Clicou no botão:
    # popup / modal
        # Titulo: Bem vindo ao Hashzap
        # Campo: Escreva seu nome no chat
        # Botão: Entrar no chat

# Chat
# Embaixo do chat
    # Campo de digite sua mensagem
    # Botão de enviar

# Flet -> Framework do python

import flet as ft # importar

def main(pagina): # criar a função principal(main)
    
    texto = ft.Text('Hashzap')

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # adicionar mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print('Enviar Mensagem')
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        
        # limpe o campo mensagem
        campo_mensagem.value = '' 
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua Mensagem', on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print('Entrar no Chat')
        # fechar o popup
        popup.open = False
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # tirat o titulo hashzap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')
        # chat.controls.append(texto_entrada) 
        # colocar o campo de digitar mensagem
        # criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text('Bem vindo ao Hashzap')
    nome_usuario = ft.TextField(label='Escreva seu nome no chat')
    botao_entrar = ft.ElevatedButton('Entra no chat', on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Inciar Chat', on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a função principal comandos para abrir app e o site
