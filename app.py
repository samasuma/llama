from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.base.response.schema import Response, PydanticResponse

app = Flask(__name__)

# Load documents and create index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Route to serve the single-page application
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint for handling AJAX requests
@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data['question'].strip()
    answer = generate_answer(question)
    return jsonify({'answer': answer})

def generate_answer(question):
    # Query llama_index and retrieve response
    response = query_engine.query(question)
    
    # Process the response based on its type
    if isinstance(response, (Response, PydanticResponse)):
        return response.response if response.response else "No relevant information found."
    else:
        return "No relevant information found."

if __name__ == '__main__':
    app.run(debug=True)
