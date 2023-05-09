"""
Autor: Francisco Moya
Fecha:
Descripción:
"""
from flask import Flask, request, abort, render_template
import openai
import config

openai.api_key = config.api_key

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("form.html")


@app.route('/answer', methods=['POST'])
def answer():
    pregunta = request.form.get("pregunta")
    respuesta1 = request.form.get("respuesta1")
    respuesta2 = request.form.get("respuesta2")
    respuesta3 = request.form.get("respuesta3")
    content = pregunta + '\n' + respuesta1 + '\n' + respuesta2 + '\n' + respuesta3
    CONTEXT = "Prueba de tráfico en España. Responde preguntas y justifica cómo aplicar las normas en situaciones " \
              "reales, de forma breve. "

    messages = [{'role': 'system',
                 'content': CONTEXT}, {'role': 'user', 'content': content}]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', messages=messages)

    response_content = response.choices[0].message.content

    return render_template("answer.html", response=response_content, pregunta=pregunta)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
