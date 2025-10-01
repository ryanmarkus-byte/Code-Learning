informacoes__livro = {
    "Titulo" : "Chuva de Fogo" ,
    "Autor" : "Leonardo L. Mello" ,
    "Ano" : "2024" ,
    "Genero" : "Ficcao" ,
}
print(informacoes__livro)
print()
print(informacoes__livro["Autor"])
print()
informacoes__livro["Ano"] = "1965"
print(informacoes__livro)
print()
informacoes__livro["Editora"] = "Independente"
print(informacoes__livro)
print()

participantes_a = ["João", "Tiago", "Lucas"]
participantas_b = ["Ryan", "Lucas", "Carlos"]
participantes_a_unicos = set(participantes_a)
participantes_b_unicos = set(participantas_b)
print("União: ", participantes_a_unicos | participantes_b_unicos)
print()
print("Interseção: ", participantes_a_unicos & participantes_b_unicos)