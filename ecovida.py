from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Lista de hábitos registrados
habitos = []

# Hábitos disponíveis
opcoes_habitos = {
    "reciclagem": {
        "nome": "Reciclei meu lixo",
        "icone": "♻️",
        "pontos": 10
    },
    "agua": {
        "nome": "Economizei água",
        "icone": "💧",
        "pontos": 10
    },
    "plastico": {
        "nome": "Evitei usar plástico",
        "icone": "🌱",
        "pontos": 10
    },
    "bicicleta": {
        "nome": "Fui de bicicleta ou caminhei",
        "icone": "🚲",
        "pontos": 15
    },
    "arvore": {
        "nome": "Plantei uma árvore",
        "icone": "🌳",
        "pontos": 20
    },
    "energia": {
        "nome": "Economizei energia",
        "icone": "💡",
        "pontos": 10
    }
}

# Dicas ecológicas
dicas = [
    "Feche a torneira enquanto escova os dentes.",
    "Use uma garrafa reutilizável em vez de comprar garrafas descartáveis.",
    "Separe o lixo reciclável do lixo comum.",
    "Apague as luzes quando sair de um cômodo.",
    "Sempre que possível, caminhe ou use bicicleta.",
    "Evite usar sacolas plásticas desnecessariamente.",
    "Cuide das árvores e das áreas verdes da sua cidade."
]


@app.route("/")
def inicio():
    pontos = sum(habito["pontos"] for habito in habitos)

    return render_template(
        "index.html",
        habitos=habitos,
        opcoes=opcoes_habitos,
        pontos=pontos,
        dica=random.choice(dicas)
    )


@app.route("/registrar", methods=["POST"])
def registrar():
    habito_id = request.form.get("habito")

    if habito_id in opcoes_habitos:
        habito = opcoes_habitos[habito_id]

        habitos.append({
            "nome": habito["nome"],
            "icone": habito["icone"],
            "pontos": habito["pontos"]
        })

    return redirect(url_for("inicio"))


@app.route("/limpar", methods=["POST"])
def limpar():
    habitos.clear()

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)