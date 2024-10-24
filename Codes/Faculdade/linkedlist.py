class Node:
    def __init__(self, posicao, adv_pos, qualidade=0):
        self.posicao = posicao
        self.adv_pos = adv_pos
        self.qualidade = qualidade
        self.next = None
        self.child = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, pos, adv_pos, qualidade):
        # antes de criar um no verifica se já existe um igual, não pode haver duplicatas como irmãos
        if self.existe(pos, adv_pos, self.head):
            raise ValueError("já existe um no na cabeça com essa posição e adv_pos.")

        novo_no = Node(pos, adv_pos, qualidade)

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
        self.sort()

    def append_child(self, pos_pai, pos, adv_pos, qualidade):
        if adv_pos == 0:
            raise ValueError("adv_pos não pode ser 0 para nós filhos")
        if pos_pai == pos:
            raise ValueError("O filho não pode ter a mesma posição do pai")

        aux = self.head

        while aux:
            if aux.pos == pos_pai:
                if self.existe(pos, adv_pos, aux):
                    raise ValueError("já existe um no filho com essa posição e adv_pos.")

                novo_no = Node(pos, adv_pos, qualidade)

                if aux.child is None:
                    aux.child = novo_no
                    return 1

                else:
                    ultimo_filho = aux.child

                    while ultimo_filho.next:
                        ultimo_filho = ultimo_filho.next

                    ultimo_filho.next = novo_no
                    self.sort_children(aux)
                    return 2
            aux = aux.next
        raise ValueError("No sem pai.")

    def sort(self):
        if self.head is None or self.head.next is None:
            # não existe lista para ordenar
            return
        # ponteiro para a lista ordenada
        sorted_list = None
        # estrutura auxiliar para navegar e prencher a nova estrutura
        aux = self.head
        while aux:
            proximo_no = aux.next
            sorted_list = self.sorted_insert(sorted_list, aux)
            aux = proximo_no
        # transfere a estrutura auxiliar para cabeça
        self.head = sorted_list

    def sorted_insert(self, head, node):
        if head is None or node.qualidade > head.qualidade:
            node.next = head
            return node
        aux = head
        while aux.next and aux.next.qualidade > node.qualidade:
            aux = aux.next
        node.next = aux.next
        aux.next = node
        return head

    def sort_children(self, no_pai):
        if no_pai.child is None or no_pai.child.next is None:
            return
        sorted_children = None
        aux = no_pai.child
        while aux:
            proximo_no = aux.next
            sorted_children = self.sorted_insert(sorted_children, aux)
            aux = proximo_no
        no_pai.child = sorted_children

    @staticmethod
    def existe(pos, adv_pos, lista):
        aux = lista

        while aux:
            if aux.pos == pos and aux.adv_pos == adv_pos:
                return True

            aux = aux.next

        return False

