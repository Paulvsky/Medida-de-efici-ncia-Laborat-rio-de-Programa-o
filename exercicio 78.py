def calcular_media(n1, n2, n3):
    notas = [n1, n2, n3]
    
    for i, nota in enumerate(notas, 1):
        if not isinstance(nota, (int, float)):
            raise TypeError(f"A nota {i} ({nota}) inválida! Insira apenas números.")
            
    for i, nota in enumerate(notas, 1):
        if not (0 <= nota <= 10):
            raise ValueError(f"A nota {i} ({nota}) deve estar entre 0 e 10.")
            
    media = sum(notas) / len(notas)
    
    if media >= 7.0:
        situacao = "Aprovado"
    elif 5.0 <= media < 7.0:
        situacao = "em Recuperação"
    else:
        situacao = "Reprovado"
        
    print(f"Média: {media:.2f} - Situação: {situacao}")
    return media

try:
    calcular_media(7.0, 8.5, 9.0)
except (TypeError, ValueError) as e:
    print(f"Erro: {e}")