from time import sleep
from main import GithubForksDiff


def processar_link(link):
    novo_link = link.split("/")
    repositorio = novo_link[-1]
    usuario = novo_link[-2]
    return usuario,repositorio



print("O github tem o limite de 60 solicitações")
print("caso o seu limite seja excedido, aguarde 3 horas e tente novamente ")
sleep(1.5)

print("cole o link do projeto ou apenas o final do link")
print("https://github.com/{usuario}/{repositorio}} ou /{usuario}/{repositorio}")
link = input("link: ")
usuario,repositorio = processar_link(link)

print("Coloque a branch")
branch = input(">>>: ")

Gfd = GithubForksDiff(usuario,repositorio,branch)
Gfd.generate_output()

