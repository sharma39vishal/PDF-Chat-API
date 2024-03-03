from flask import Flask, request, jsonify
from searching_logic import PDFQuestionAnswerSystem

app = Flask(__name__)
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '')
    pdf_qa_system = PDFQuestionAnswerSystem()
    pdf_files = ["first.pdf","second.pdf"]  # Add more PDF files as needed
    pdf_qa_system.load_documents_from_pdfs(pdf_files)
    
    answer = pdf_qa_system.ask_question(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)