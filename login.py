from flet import *

colorPrimary="#73493F"
secondColor="#6E00C7"
colorBar="#D9AE96"
fontColor="#F2EDE4"
backgroundColor="#F2EDE4"
botao="#ffffff"

def main(page:Page):

    page.title = "MyGuide"
    page.bgcolor = backgroundColor
    imageLogin =Image(src="assets/logo (2).png",width=200,height=200)

    t_field_login = TextField(label="Usuario",icon=icons.LOGIN_OUTLINED)
    t_field_passWord = TextField(label="Senha",icon=icons.PASSWORD,password=True)
    btn_enter=ElevatedButton(text="Entrar",width=200,
                             style=ButtonStyle(
                                 shape=RoundedRectangleBorder(radius=10),
                                 bgcolor={
                                     MaterialState.DEFAULT:botao,
                                     MaterialState.HOVERED:secondColor,

                                 },
                                 color=fontColor
                             ))
    lineImg= Row(controls=[imageLogin],alignment=MainAxisAlignment.CENTER)
    line1=Row(controls=[t_field_login],alignment=MainAxisAlignment.CENTER)
    line2=Row(controls=[t_field_passWord],alignment=MainAxisAlignment.CENTER)
    line3=Row(controls=[btn_enter],alignment=MainAxisAlignment.CENTER)

    #O coluns tem que ser uma lista
    coluna=Column(controls=[lineImg,line1,line2,line3])

    #Permite que eu trabalhe com mais de um container:
    # page.add(t_field_login,t_field_passWord,btn_enter)

    page.add(coluna)
    page.update()

if __name__ == '__main__':
    app(target=main)