from fila import Fila
import copy
class PainelAtendimento:
    def __init__(self):
        self.fila = Fila()
        self.removidas = []

    def obtem_senha(self):
        if self.fila.is_empty():
            nova_senha = 0
            self.fila.enqueue(0)
        else:
            nova_senha = self.fila.front() + len(self.fila)
            self.fila.enqueue(nova_senha)
        return nova_senha
    
    def chama_proxima_senha(self):
        if self.fila.is_empty():
            senha_atendida = None
        else:
            proxima_senha = self.fila.front()
            self.removidas.append(proxima_senha)
            senha_atendida = proxima_senha 
            self.fila.dequeue()
        return senha_atendida

    def mostra_senhas_chamadas(self):
        if len(self.removidas) == 0:
            return None
        else: 
            return self.removidas

    def run(self):
        while True:
            try:
                print("Olá, bem-vindo(a) ao painel de atendimento! \n")
                opcao = int(input("Escolha uma das opções abaixo:\n 1 - Obter senha.\n 2 - Chamar próxima senha.\n 3 - Mostar as senhas chamadas.\n 4 - Encerrar sistema.\n")) 
                if opcao == 1:
                    senha = self.obtem_senha()
                    print(f"Sua senha é: {senha}\n")
                elif opcao == 2:
                    proxima_senha = self.chama_proxima_senha()
                    if proxima_senha == None:
                        print("Ainda não há nenhuma senha salva, ou todas já foram chamadas. Por gentileza cadastre uma senha.\n")
                    else:
                        print(f"A senha chamada foi: {proxima_senha}.\n")
                elif opcao == 3:
                    removidas = self.mostra_senhas_chamadas
                    if removidas == None:
                        print("Nenhuma senha foi removida até o momento.\n")
                    else:
                        print(f"As senhas chamadas foram: {self.removidas}.\n")
                elif opcao == 4:
                    print("Obrigada por utilizar o sistema!!")
                    break
            except:
                print("Opção inválida, tente novamente!")

painel = PainelAtendimento().run()