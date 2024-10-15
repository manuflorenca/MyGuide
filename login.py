from flet import *

colorPrimary="#73493F"
secondColor="#A6705D"
colorBar="#D9AE96"
fontColor="#F2EDE4"
backgroundColor="#F2EDE4"

def main(page:Page):

    page.title = "Login"
    page.bgcolor = backgroundColor
    imageLogin =Image(src="login.png",width=200,height=200)

    t_field_login = TextField(label="Login",icon=icons.LOGIN)
    t_field_passWord = TextField(label="PassWord",icon=icons.PASSWORD,password=True)
    btn_enter=ElevatedButton(text="Enter",width=250,
                             style=ButtonStyle(
                                 shape=RoundedRectangleBorder(radius=0),
                                 bgcolor={
                                     MaterialState.DEFAULT:colorPrimary,
                                     MaterialState.HOVERED:secondColor
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