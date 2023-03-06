from homework import Homework
from exam import Exam
from grade import ExamD
from weakgrade import ExamW

print("___________ HOMEWORK _______________")
st1 = Homework()
st1.grade = 97
print(st1.grade)
assert st1.grade == 97


print("___________ EXAM _______________")
st2 = Exam()
st2.writing_grade = 88
st2.math_grade = 76

print(f"writing: {st2.writing_grade}, math: {st2.math_grade}")


print("___________ EXAMD _______________")

st3_fe = ExamD()
st3_fe.math_grade = 34
st3_fe.writing_grade = 50
st3_fe.science_grade = 55
print("PIERWSZE PODEJŚCIE")
print(f'math: {st3_fe.math_grade}')
print(f'writing: {st3_fe.writing_grade}')
print(f'science: {st3_fe.science_grade}')

st3_se = ExamD()
st3_se.math_grade = 55
st3_se.writing_grade = 57
st3_se.science_grade = 88
print("DRUGIE PODEJŚCIE")
print(f'math: {st3_se.math_grade}')
print(f'writing: {st3_se.writing_grade}')
print(f'science: {st3_se.science_grade}')


print("PONOWNIE PIERWSZE PODEJŚCIE ______________________")
print(f'math: {st3_fe.math_grade}')
print(f'writing: {st3_fe.writing_grade}')
print(f'science: {st3_fe.science_grade}')


print("___________ EXAMW _______________")

st4_fe = ExamW()
st4_fe.math_grade = 34
st4_fe.writing_grade = 50
st4_fe.science_grade = 55
print("PIERWSZE PODEJŚCIE")
print(f'math: {st4_fe.math_grade}')
print(f'writing: {st4_fe.writing_grade}')
print(f'science: {st4_fe.science_grade}')

st4_se = ExamW()
st4_se.math_grade = 55
st4_se.writing_grade = 57
st4_se.science_grade = 88
print("DRUGIE PODEJŚCIE")
print(f'math: {st4_se.math_grade}')
print(f'writing: {st4_se.writing_grade}')
print(f'science: {st4_se.science_grade}')


print("PONOWNIE PIERWSZE PODEJŚCIE ______________________")
print(f'math: {st4_fe.math_grade}')
print(f'writing: {st4_fe.writing_grade}')
print(f'science: {st4_fe.science_grade}')
