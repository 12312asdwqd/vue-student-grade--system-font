from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

# 简单的用户数据
users = {
    "testuser": {"password": "password123", "identity": "0"},
    "tea": {"password": "123", "identity": "0"},
    "stu": {"password": "123", "identity": "1"}
}

# 登录部分
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    identity = data.get('identity')
    
    print(username)
    print(password)
    print(identity)
    if username in users and users[username]["password"] == password and users[username]["identity"] == identity:
        return jsonify({
            "message": "登录成功",
            "data":{
                "uid":1,
                "name": "李xx"
            }
            
            }), 200
    else:
        return jsonify({"message": "用户名、密码或身份错误"}), 401

# 学生部分
# 学生获取课程
@app.route('/student/getStudentCourseList', methods=['GET'])
def get_student_course_list():
    student_id = request.args.get('studentId')
    # 假设这里你有一个函数get_courses_by_student_id来获取课程列表
    courses = get_courses_by_student_id(student_id)
    return jsonify({
        "studentId": student_id,
        "courses": courses
    }), 200

def get_courses_by_student_id(student_id):

    # 这里我是直接返回的，但是在数据库中是需要根据student_id来找的
    return[
        {
            "courseId":1,
            "corseName":"高数"
        },
        {
            "courseId":2,
            "corseName":"线代"
        }
    ]

# 学生获取该课程的信息成绩
@app.route('/grade/getCourseGrade', methods=['GET'])
def getCourseGrade():
    student_id = request.args.get('studentId')
    course_id = request.args.get('courseId')

    grade=get_Grade(student_id,course_id)
    return jsonify({
        "grade": grade,

    }), 200

def get_Grade(student_id,course_id):
    # 同理
    return {
        "courseName":"高数",
        "teacherName":"李老师",
        "examScore":60,
        "regularScore":100,
        "extraScore":0,
        "totalScore":88,
    }

# 教师部分
# 获取教师的课程
@app.route('/teacher/getTeacherCourseList', methods=['GET'])
def getTeacherCourseList():
    teacher_id=request.args.get('teacherId')
    courses=get_teacher_courses(teacher_id)
    return jsonify({
            "courses": courses,

    }), 200


def get_teacher_courses(teacher_id):
    return [
        {
            "courseId":1,
            "courseName":"高数"
        },
        {
            "courseId":2,
            "courseName":"高数2"
        }
    ]

# 获取教师在该课程的学生
@app.route('/teacher/getStudentList', methods=['GET'])
def getStudentList():
    teacher_id=request.args.get('teacherId')
    course_id=request.args.get('courseId')

    student_list=get_student_list(teacher_id,course_id)
    return jsonify({
            "students": student_list,
    }), 200


def get_student_list(teacher_id,course_id):
    return [
        {
            "studentId":1,
            "studentName":"王xx"
        },
        {
            "studentId":2,
            "studentName":"赵xx"
        }
    ]

# 教师获取学生该课程成绩  这个可以直接和学生的一样处理，就不写了，直接访问学生的即可，见64行
# @app.route('/grade/getCourseGrade', methods=['GET'])


# post请求，教师修改学生成绩
@app.route('/grade/updateCourseGrade', methods=['POST'])
def updataCourseGrade():
    data = request.json
    studentid=data.get("studentId")
    courseid=data.get("courseId")    
    examScore=data.get("examScore") 
    regularScore=data.get("regularScore")    
    extraScore=data.get("extraScore")   
    totalScore=data.get("totalScore")

    # 接下来是数据库中的处理，省略


    return jsonify({
            "message":"修改成功"
    }), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082)

