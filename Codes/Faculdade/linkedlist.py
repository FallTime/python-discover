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
            no_existente = self.buscar_no(pos, adv_pos)
            no_existente.qualidade += qualidade
            return 0

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

    def append_child(self, no_pai, pos, adv_pos, qualidade):
        if adv_pos == 0:
            raise ValueError("adv_pos não pode ser 0 para nós filhos")

        if no_pai is None:
            raise ValueError("No sem pai")

        if no_pai.posicao == pos:
            raise ValueError("O filho não pode ter a mesma posição do pai")


        if self.existe(pos, adv_pos, no_pai.child):
            no_existente = self.buscar_no(pos, adv_pos)
            no_existente.qualidade += qualidade
            return 0

        novo_no = Node(pos, adv_pos, qualidade)

        if no_pai.child is None:
            no_pai.child = novo_no
            return 1

        ultimo_filho = no_pai.child
        while ultimo_filho.next:
            ultimo_filho = ultimo_filho.next
        ultimo_filho.next = novo_no

        self.sort_children(no_pai)
        return 2


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

    def buscar_no(self, pos, adv_pos):
        def buscar_recursivo(node, pos, adv_pos):
            if node is None:
                return None
            if node.posicao == pos and node.adv_pos == adv_pos:
                return node
            result = buscar_recursivo(node.child, pos, adv_pos)
            if result is not None:
                return result
            return buscar_recursivo(node.next, pos, adv_pos)

        return buscar_recursivo(self.head, pos, adv_pos)

    @staticmethod
    def sorted_insert(head, node):
        if head is None or node.qualidade > head.qualidade:
            node.next = head
            return node
        aux = head
        while aux.next and aux.next.qualidade > node.qualidade:
            aux = aux.next
        node.next = aux.next
        aux.next = node
        return head

    @staticmethod
    def existe(pos, adv_pos, lista):
        aux = lista

        while aux:
            if aux.posicao == pos and aux.adv_pos == adv_pos:
                return True

            aux = aux.next

        return False

    def print_list(self):
        def print_children(node, level):
            child = node.child
            while child:
                print(
                    f"{'  ' * level}Child - Posição: {child.posicao}, Adv_pos: {child.adv_pos}, Qualidade: {child.qualidade}")
                print_children(child, level + 1)
                child = child.next

        aux = self.head
        while aux:
            print(f"Posição: {aux.posicao}, Adv_pos: {aux.adv_pos}, Qualidade: {aux.qualidade}")
            print_children(aux, 1)
            aux = aux.next

