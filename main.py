from flask import Flask, render_template, request, jsonify
from urllib.request import urlopen
import json
import random
import sys
import ast
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'xyz'




@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "GET":
     url = "https://opentdb.com/api.php?amount=5"
     response = urlopen(url)
     data_json = json.loads(response.read())
     allquestiondata = data_json['results']
     #print(allquestiondata)

     Questions = []
     Correct_Answers = []
     All_Answers = []


     for question in allquestiondata:
        thisanswer = []
        thiscorrect = []
        questtext = question['question']
        Questions.append(questtext)
        c_ans = question['correct_answer']
        thiscorrect.append(c_ans)
        thisanswer.append(c_ans)
        incorr_ans = question['incorrect_answers']
        for eachanswer in incorr_ans:
          thisanswer.append(eachanswer)
        random.shuffle(thisanswer)
        All_Answers.append(thisanswer)
        Correct_Answers.append(c_ans)

     #print(Questions)
     #print(All_Answers)

    # for record in All_Answers:
    #     for i in record:
    #         print(i)
    #     print("")
     #print(Correct_Answers)
     print(All_Answers)
     print(All_Answers[0])
     questioncount = (len(All_Answers))
     print(questioncount)

     return render_template('TakeQuiz.html', webquestions=Questions, all_answers=All_Answers, correct_answers=Correct_Answers, Answer_Count=questioncount)

    if request.method == "POST":
      print('working')
      qtc_data = request.get_json()
      print(qtc_data)
      return render_template('Results.html', status='bruh')


        # data['score'] = request.json['score']
        # print('bozo')
        # print(data, file=sys.stderr)


        # UserAnswer = request.form.get("Answer")
        # split_data = ast.literal_eval(UserAnswer)
        # answer = split_data[0]
        # print(f'your answer is {answer}')
        # quiz_id = split_data[1]
        # Correct_Answer = request.form.get(f"CorrectQuestion{quiz_id}")
        # print(f'The correct answer is: {Correct_Answer}')
        # if [Correct_Answer] == answer:
        #     print("score + 1")


if __name__ == "__main__":
   app.run(debug=True)
