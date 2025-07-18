import json
import os
from datetime import datetime

# Nome do arquivo para salvar os dados
NOME_ARQUIVO = "compras.json"

class Compra:
    """Representa uma única compra online."""

    def __init__(self, item, preco, loja, status="Processando", codigo_rastreio=None):
        self.item = item
        self.preco = float(preco)
        self.loja = loja
        self.data_compra = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.status = status
        self.codigo_rastreio = codigo_rastreio

    def to_dict(self):
        """Converte o objeto Compra para um dicionário para ser salvo em JSON."""
        return self.__dict__

    def mostrar_detalhes(self):
        """Exibe os detalhes da compra de forma formatada."""
        print(f"  - Item: {self.item}")
        print(f"    Loja: {self.loja}")
        print(f"    Preço: R$ {self.preco:.2f}")
        print(f"    Data: {self.data_compra}")
        print(f"    Status: {self.status}")
        if self.codigo_rastreio:
            print(f"    Rastreio: {self.codigo_rastreio}")

class GerenciadorCompras:
    """Gerencia a lista de compras, incluindo salvar e carregar."""

    def __init__(self):
        self.compras = []
        self.carregar_compras()

    def carregar_compras(self):
        """Carrega as compras do arquivo JSON."""
        if not os.path.exists(NOME_ARQUIVO):
            return  # Se o arquivo não existe, não faz nada

        try:
            with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for item_dado in dados:
                    # Cria uma instância de Compra a partir do dicionário
                    compra = Compra(item_dado['item'], item_dado['preco'], item_dado['loja'])
                    # Atualiza os outros atributos que podem ter sido modificados
                    compra.data_compra = item_dado['data_compra']
                    compra.status = item_dado['status']
                    compra.codigo_rastreio = item_dado['codigo_rastreio']
                    self.compras.append(compra)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar o arquivo de compras: {e}")

    def salvar_compras(self):
        """Salva a lista de compras atual no arquivo JSON."""
        try:
            with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
                # Converte a lista de objetos Compra para uma lista de dicionários
                lista_de_compras_dict = [compra.to_dict() for compra in self.compras]
                json.dump(lista_de_compras_dict, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Não foi possível salvar as compras: {e}")

    def adicionar_compra(self):
        """Solicita informações do usuário e adiciona uma nova compra."""
        print("\n--- Adicionar Nova Compra ---")
        item = input("Nome do item: ")
        while True:
            try:
                preco = float(input("Preço do item (ex: 49.99): "))
                break
            except ValueError:
                print("Preço inválido. Por favor, use um número.")
        loja = input("Nome da loja: ")

        nova_compra = Compra(item, preco, loja)
        self.compras.append(nova_compra)
        self.salvar_compras()
        print("\n✅ Compra adicionada com sucesso!")

    def listar_compras(self):
        """Lista todas as compras registradas."""
        print("\n--- Suas Compras Registradas ---")
        if not self.compras:
            print("Nenhuma compra registrada ainda.")
            return

        for i, compra in enumerate(self.compras):
            print(f"\nCompra #{i + 1}")
            compra.mostrar_detalhes()
        print("-" * 30)

    def atualizar_status(self):
        """Atualiza o status e o código de rastreio de uma compra existente."""
        self.listar_compras()
        if not self.compras:
            return

        try:
            escolha = int(input("\nDigite o número da compra que deseja atualizar: ")) - 1
            if 0 <= escolha < len(self.compras):
                compra_selecionada = self.compras[escolha]
                print(f"\nAtualizando status para '{compra_selecionada.item}'...")
                novo_status = input(f"Novo status (atual: {compra_selecionada.status}): ")
                novo_rastreio = input(f"Código de rastreio (deixe em branco para não alterar): ")

                if novo_status:
                    compra_selecionada.status = novo_status
                if novo_rastreio:
                    compra_selecionada.codigo_rastreio = novo_rastreio

                self.salvar_compras()
                print("\n✅ Status atualizado com sucesso!")
            else:
                print("Número de compra inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def calcular_gasto_total(self):
        """Calcula e exibe o valor total gasto em todas as compras."""
        if not self.compras:
            print("\nNenhuma compra para calcular.")
            return

        total = sum(compra.preco for compra in self.compras)
        print(f"\n--- Gasto Total ---")
        print(f"Você gastou um total de R$ {total:.2f} em {len(self.compras)} compras.")


def menu_principal():
    """Exibe o menu principal e gerencia a entrada do usuário."""
    gerenciador = GerenciadorCompras()

    while True:
        print("\n===== Gerenciador de Compras Online =====")
        print("1. Adicionar Nova Compra")
        print("2. Listar Todas as Compras")
        print("3. Atualizar Status de uma Compra")
        print("4. Ver Gasto Total")
        print("5. Sair")
        print("=" * 39)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciador.adicionar_compra()
        elif opcao == '2':
            gerenciador.listar_compras()
        elif opcao == '3':
            gerenciador.atualizar_status()
        elif opcao == '4':
            gerenciador.calcular_gasto_total()
        elif opcao == '5':
            print("\nAté logo! 👋")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
