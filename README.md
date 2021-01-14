# GithubForkDiff
Eu fiz para ganhar um hamburguer, se ficar top eu ajeito isso aqui

Crie um ambiente virtual (usando o virtualenv como exemplo)

$virtualenv env

Ative o ambiente 

$source env/bin/activate

Instale as dependências

pip install -r requirements.txt

Para rodar o código, instancie a classe GithubForksDiff, passando como argumentos

GithubForksDiff("usuario","repositorio","branch")

e utilize o método 'generate_output'