class Node:
    def __init__(self, posicao, adv_pos):
        self.posicao = posicao
        self.adv_pos = adv_pos
        self.qualidade = 0
        self.next = None
        self.child = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, pos, adv_pos):
        # antes de criar um no verifica se já existe um igual, não pode haver duplicatas como irmãos
        if self.existe(pos, adv_pos, self.head):
            raise ValueError("já existe um no na cabeça com essa posição e adv_pos.")

        novo_no = Node(pos, adv_pos)

        # se não tem cabeça na estrutura, insira nela
        if self.head is None:
            self.head = novo_no
            return 1

        # estrutura de navegação horizontal
        ultimo_no = self.head
        # enquanto ultimo_no.next não for igual a None, continue para o proximo
        while ultimo_no.next:
            ultimo_no = ultimo_no.next

        # quando ultimo_no.next igual a None, novo_no é apontado pelo ultimo nó
        ultimo_no.next = novo_no

    def append_child(self, pos_pai, pos, adv_pos):
        if adv_pos == 0:
            raise ValueError("adv_pos não pode ser 0 para nós filhos")
        if pos_pai == pos:
            raise ValueError("O filho não pode ter a mesma posição do pai")

        aux = self.head

        while aux:
            if aux.pos == pos_pai:
                if self.existe(pos, adv_pos, aux):
                    raise ValueError("já existe um no filho com essa posição e adv_pos.")

                novo_no = Node(pos, adv_pos)

                if aux.child is None:
                    aux.child = novo_no
                    return 1

                else:
                    ultimo_filho = aux.child

                    while ultimo_filho.next:
                        ultimo_filho = ultimo_filho.next

                    ultimo_filho.next = novo_no
                    return 2
            aux = aux.next
        raise ValueError("No sem pai.")

    @staticmethod
    def existe(pos, adv_pos, lista):
        aux = lista

        while aux:
            if aux.pos == pos and aux.adv_pos == adv_pos:
                return True

            aux = aux.next

        return False
