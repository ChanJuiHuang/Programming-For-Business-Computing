import datetime
import csv


class MidtermInfo:
    def __init__(self, SubmissionID, StudentID, Problem, Status, Score, CodeLength, SubmissionTime):
        self.submissionID = SubmissionID
        self.studentID = StudentID
        self.problem = Problem
        self.status = Status
        self.score = int(Score)
        self.codeLength = int(CodeLength)
        self.submissionTime = datetime.datetime.strptime(
            SubmissionTime, '%H:%M:%S')


filename = 'midterm2.csv'
file = open(filename, 'r', encoding='utf8')

reader = csv.reader(file)
reader = csv.DictReader(file)

midterm_list = []
for midterm_data in reader:
    midterm_list.append(MidtermInfo(**midterm_data))
file.close()


# start_time起始時間, end_time結束時間
start_time, end_time = [datetime.datetime.strptime(
    t, '%H:%M:%S') for t in input().split()]

# question_dict, 題目計數
question_dict = {
    '1': {'Accepted': 0, 'Compile Error': 0, 'Runtime Error': 0, 'Wrong Answer': 0, 'Time Limit Exceed': 0},
    '2': {'Accepted': 0, 'Compile Error': 0, 'Runtime Error': 0, 'Wrong Answer': 0, 'Time Limit Exceed': 0},
    '3': {'Accepted': 0, 'Compile Error': 0, 'Runtime Error': 0, 'Wrong Answer': 0, 'Time Limit Exceed': 0},
    '4': {'Accepted': 0, 'Compile Error': 0, 'Runtime Error': 0, 'Wrong Answer': 0, 'Time Limit Exceed': 0}
}

for midterm_data in midterm_list:
    if start_time <= midterm_data.submissionTime <= end_time:
        question_dict[midterm_data.problem][midterm_data.status] += 1

for question in range(1, 5):
    print(question_dict[str(question)]['Accepted'],
          question_dict[str(question)]['Compile Error'],
          question_dict[str(question)]['Runtime Error'],
          question_dict[str(question)]['Time Limit Exceed'],
          question_dict[str(question)]['Wrong Answer'],
          end=';')
print()
