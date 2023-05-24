
class Cadastro:
    def __init__(self, email, conf_email, senha, conf_senha):
        self.email = email
        self.conf_email = conf_email
        self.senha = senha
        self.conf_senha = conf_senha
        
    def verificaçao_email(self):
        if self.email == self.conf_email:
            bd[email] = senha
            return True
            
        else:
            print('Emails não estão coincidindo! Digite novamente!')
            return False
            
    
    def verificaçao_senha(self):

        if self.senha == self.conf_senha:
            bd[email] = senha
            return True
        else:
            print('Senhas não estão coincidindo! Digite novamente!')
            return False
            
            
        
            
   
class Login:
    def __init__(self, login_email, login_senha):
        self.login_email = login_email
        self.login_senha = login_senha
        
    def verificar_lista_vazia(self, lista):
        self.lista = lista
        if len(lista) == 0:
            print('')
            

bd = {} 

texto = "SISTEMA DE CADASTRO E LOGIN!"
print('+'*50)
largura_total = 50
texto_centralizado = texto.center(largura_total)
print(texto_centralizado)
print('+'*50)
while True:
    print('='*50)
    opçao = str(input("Já tem login? [S/N]: " )).upper()
    print('='*50)
    
    if opçao == 'S':
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        new_login = Login(login, senha)
        new_login.verificar_lista_vazia(bd)
        
    
        if login in bd and bd[login] == senha:
            print('Login efetuado com sucesso!')
                 
                
                
        else:
            print('Email ou senha incorretas!')
                    
        print('='*50)
        sair = input('Deseja sair do sistema de cadastro e login? [S/N]: ').upper()
        if sair == 'S':
            break
        elif sair == 'N':
            continue
        else:
            print('Por favor! Digite [S/N]')
            break
        

                

                
    elif opçao == 'N':
        email = input('Cadastre seu login: ')
        conf_email = input('Confirme seu login: ')
        senha = input('Cadastre sua senha: ')
        conf_senha = input('Confirme sua senha: ')
            
        usuario = Cadastro(email, conf_email, senha, conf_senha) 
        
        
    
        
        if usuario.verificaçao_email() == False:
            break
        if usuario.verificaçao_senha() == False:
            break
         
         
    else:
        print('Por favor! Digite [S/N]')
        break
        
            

        