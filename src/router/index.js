import { createRouter, createWebHistory } from 'vue-router';
import TeacherView from '../components/TeacherView.vue';
import StudentView from '../components/StudentView.vue';
import LoginView from '../components/LoginView.vue';

const routes = [
  {
    path: '/teacher/:teacherId/:name/:username',
    name: 'Teacher',
    component: TeacherView,
    props: true
  },
  { 
    path: '/student/:studentId/:name/:username', 
    name: 'Student', 
    component: StudentView,
    props: true // 通过 props 传递参数
  },
  { path: '/teacher', component: TeacherView },
  { path: '/student', component: StudentView },
  { path: '/', component: LoginView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 添加路由守卫
router.beforeEach((to, from, next) => {
  console.log('Route params:', to.params);
  next();
});

export default router;
