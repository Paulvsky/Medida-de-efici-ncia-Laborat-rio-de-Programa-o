def buscarPermissao(sistemaPermissoes, perfil, indicePermissao):
    try:
        listaPermissoes = sistemaPermissoes[perfil]
        return listaPermissoes[indicePermissao]
    except (KeyError, IndexError):
        return "Acesso_restrito"

dadosDeAcesso = {
    "admin": ["opcao1", "opcao2", "opcao3"],
    "funcionario": ["opcao4", "opcao5"]
}

print(buscarPermissao(dadosDeAcesso, "admin", 1))
print(buscarPermissao(dadosDeAcesso,"visitante", 2 ))
print(buscarPermissao(dadosDeAcesso,"funcionario", 2 ))