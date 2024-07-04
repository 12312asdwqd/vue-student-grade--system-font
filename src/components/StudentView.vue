<template>
  <div class="student-view">
    <h2>学生界面</h2>
    <div class="header">
     <!--  <span>ID: {{ studentId }}</span> -->
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
        <h3>科目列表</h3>
        <ul>
          <li v-for="subject in courses" :key="subject.courseId">
            <button @click="fetchCourseGrade(subject.courseId)">{{ subject.courseName }}</button>
          </li>
        </ul>
      </div>
      <div class="right-panel">
        <h3>成绩详情</h3>
        <p>课程：{{ courseName }}</p>
        <p>教师：{{ teacherName }}</p>
        <p>卷面分：{{ examScore }}</p>
        <p>平时成绩：{{ regularScore }}</p>
        <p>额外加分：{{ extraScore }}</p>
        <p>总分：{{ totalScore }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'StudentView',
  setup() {
    const route = useRoute();
    const studentId = ref(route.params.studentId);
    const name = ref(route.params.name);
    const username = ref(route.params.username);
    const courses = ref([]);
    const courseName = ref("");
    const teacherName = ref("");
    const examScore = ref(0);
    const regularScore = ref(0);
    const extraScore = ref(0);
    const totalScore = ref(0);

    const fetchCourses = async () => {
      try {
        const response = await axios.get('http://192.168.179.219:8088/student/getStudentCourseList', {
          params: { studentId: studentId.value }
        });
        console.log(response.data);
        courses.value = response.data.data;
        console.log(courses.value); // 打印获取到的课程列表
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    };

    const fetchCourseGrade = async (courseId) => {
      try {
        const response = await axios.get('http://192.168.179.219:8088/grade/getCourseGrade', {
          params: {
            studentId: studentId.value,
            courseId: courseId
          }
        });
        const grade = response.data.data;
        courseName.value = grade.courseName;
        teacherName.value = grade.teacherName;
        examScore.value = grade.examScore;
        regularScore.value = grade.regularScore;
        extraScore.value = grade.extraScore;
        totalScore.value = grade.totalScore;
      } catch (error) {
        console.error('Error fetching course grade:', error);
      }
    };

    onMounted(() => {
      // 打印传递的登录信息到控制台
      console.log(`Student ID: ${studentId.value}`);
      console.log(`Name: ${name.value}`);
      console.log(`Username: ${username.value}`);
      // 获取课程列表
      fetchCourses();
    });

    return {
      studentId,
      name,
      username,
      courses,
      courseName,
      teacherName,
      examScore,
      regularScore,
      extraScore,
      totalScore,
      fetchCourseGrade
    };
  }
};
</script>

<style>
.student-view {
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

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
