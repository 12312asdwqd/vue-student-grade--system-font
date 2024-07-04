<template>
  <div class="teacher-view">
    <h2>教师界面</h2>
    <div class="header">
      <button @click="fetchData">获取数据</button>
      <div style="display: flex;">
        <div style="height:100%;width:40px;background-image:url(https://img.17sucai.com/attachment/3/2023-02-21/2023022159657.png?x-oss-process=style/ready);background-size: cover;"></div>
        <div id="user-message">
          <div>{{ name }}</div>
          <div>{{ username }}</div>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="left-panel">
        <h3>教学列表</h3>
        <ul>
          <li v-for="course in courses" :key="course.courseId">
            <button @click="fetchStudents(course)">
               {{ course.courseName }}
            </button>
            <ul v-if="course.isVisible">
              <li v-for="student in students" :key="student.studentId">
                <button @click="showStudentDetails(student)">
                  {{ student.studentName }}
                </button>
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="right-panel">
        <h3>学生详情</h3>
        <p>课程名：{{ selectedStudent.courseName }}</p>
        <p>学生名：{{ selectedStudent.studentName }}</p>
        <div>
          <label>平时成绩：</label>
          <input v-model="selectedStudent.regularScore" type="number" />
        </div>
        <div>
          <label>期末成绩：</label>
          <input v-model="selectedStudent.examScore" type="number" />
        </div>
        <div>
          <label>特殊加分：</label>
          <input v-model="selectedStudent.extraScore" type="number" />
        </div>
        <div>
          <label>总分：</label>
          <input v-model="selectedStudent.totalScore" type="number" />
        </div>
        <button @click="submitData">提交</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'TeacherView',
  setup() {
    const route = useRoute();
    const teacherId = ref(route.params.teacherId);
    const name = ref(route.params.name);
    const username = ref(route.params.username);

   /*  const selectcourse = courses; */
    const courses = ref([]);
    const students = ref([]);
    const selectedStudent = ref({
      courseName: '',
      studentName: '',
      regularScore: '',
      examScore: '',
      extraScore: '',
      totalScore: '',
      courseId: '' // 确保courseId在selectedStudent中存在
    });

    onMounted(() => {
      console.log('Teacher ID:', teacherId.value);
      console.log('Name:', name.value);
      console.log('Username:', username.value);
      fetchData();
    });

    const fetchData = async () => {
      try {
        const response = await axios.get('http://192.168.179.219:8088/teacher/getTeacherCourseList', {
          params: {
            teacherId: teacherId.value
          }
        });
        courses.value = response.data.data
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const fetchStudents = async (course) => {
      console.log(course,"dddd");
      try {
        const response = await axios.get('http://192.168.179.219:8088/teacher/getStudentList', {
          params: {
            teacherId: teacherId.value,
            courseId: course.courseId
          },
        });
        selectedStudent.value=course;
        students.value = response.data.data;
        courses.value.forEach(c => {
          if (c.courseId === course.courseId) {
            c.isVisible = !c.isVisible; // 切换 isVisible 属性
          } else {
            c.isVisible = false; // 隐藏其他课程的学生列表
          }
        });
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    };

    const showStudentDetails = (student) => {
       selectedStudent.value = { ...student, ...selectedStudent.value };
/*       selectedStudent.value = { ...student, courseId }; */
      console.log('Selected Student:', selectedStudent.value);
      fetchCourseGrade()
    };

    const fetchCourseGrade = async () => {
      try {
        const response = await axios.get('http://192.168.179.219:8088/grade/getCourseGrade', {
          params: {
            studentId: selectedStudent.value.studentId,
            courseId: selectedStudent.value.courseId
          }
        });
        const grade = response.data.data;
        selectedStudent.value.examScore = grade.examScore;
        selectedStudent.value.regularScore = grade.regularScore;
        selectedStudent.value.extraScore = grade.extraScore;
        selectedStudent.value.totalScore = grade.totalScore;
      } catch (error) {
        console.error('Error fetching course grade:', error);
      }
    };

    const submitData = async () => {
      try {
        const response = await axios.post('http://192.168.179.219:8088/grade/updateCourseGrade', {
          studentId: selectedStudent.value.studentId,
          courseId: selectedStudent.value.courseId, // 确保courseId存在
          regularScore: selectedStudent.value.regularScore,
          examScore: selectedStudent.value.examScore,
          extraScore: selectedStudent.value.extraScore,
          totalScore: selectedStudent.value.totalScore
        });
        console.log('提交成功:', response.data);
        if(response.data.code !=1)
        alert('成绩修改失败');
      } catch (error) {
        console.error('Error submitting data:', error);
      }
    };

    return {
      teacherId,
      name,
      username,
      courses,
      students,
      selectedStudent,
      fetchData,
      fetchStudents,
      showStudentDetails,
      submitData,
      fetchCourseGrade
    };
  }
};
</script>

<style>
.teacher-view {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding: 10px;
  background-color: #f0f0f0;
}

.content {
  display: flex;
  width: 100%;
  margin-top: 20px;
}

.left-panel, .right-panel {
  flex: 1;
  padding: 20px;
  border: 1px solid #ddd;
  margin: 10px;
}

.left-panel {
  max-width: 200px;
}

.right-panel {
  flex: 2;
}

ul li ul {
  list-style-type: none;
  padding: 0;
}

ul li ul li {
  margin: 5px 0;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
