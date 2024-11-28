from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Base de datos simulada
cursos = []

@app.route('/cursos', methods=['POST'])
def crear_curso():
    """
    Crear un curso nuevo
    """
    data = request.json
    curso = {
        "id": str(uuid.uuid4()),
        "titulo": data.get("titulo", ""),
        "descripcion": data.get("descripcion", ""),
        "categoria": data.get("categoria", ""),
        "precio": data.get("precio", 0.0),
        "duracion": data.get("duracion", 0),
        "certificado": data.get("certificado", False)
    }
    cursos.append(curso)
    return jsonify({"message": "Curso creado exitosamente", "curso": curso}), 201

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    """
    Listar todos los cursos
    """
    return jsonify(cursos), 200

@app.route('/cursos/<string:curso_id>', methods=['GET'])
def obtener_curso(curso_id):
    """
    Obtener detalles de un curso por ID
    """
    curso = next((c for c in cursos if c["id"] == curso_id), None)
    if not curso:
        return jsonify({"error": "Curso no encontrado"}), 404
    return jsonify(curso), 200

@app.route('/cursos/<string:curso_id>', methods=['PUT'])
def actualizar_curso(curso_id):
    """
    Actualizar información de un curso
    """
    curso = next((c for c in cursos if c["id"] == curso_id), None)
    if not curso:
        return jsonify({"error": "Curso no encontrado"}), 404
    data = request.json
    curso.update({
        "titulo": data.get("titulo", curso["titulo"]),
        "descripcion": data.get("descripcion", curso["descripcion"]),
        "categoria": data.get("categoria", curso["categoria"]),
        "precio": data.get("precio", curso["precio"]),
        "duracion": data.get("duracion", curso["duracion"]),
        "certificado": data.get("certificado", curso["certificado"]),
    })
    return jsonify({"message": "Curso actualizado exitosamente", "curso": curso}), 200

@app.route('/cursos/<string:curso_id>', methods=['DELETE'])
def eliminar_curso(curso_id):
    """
    Eliminar un curso por ID
    """
    global cursos
    cursos = [c for c in cursos if c["id"] != curso_id]
    return jsonify({"message": "Curso eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
