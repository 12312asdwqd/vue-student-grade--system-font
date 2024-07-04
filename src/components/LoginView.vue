<template>
  <div class="login">
    <h2>登录</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">用户名:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="password">密码:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="identity">身份:</label>
        <select v-model="identity" required>
          <option value="0">老师</option>
          <option value="1">学生</option>
        </select>
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      identity: '0'  // 默认选择老师
    };
  },
  methods: {
    async login() {
      // 在这里处理表单提交逻辑
      try {
        const response = await axios.post('http://127.0.0.1:8082/auth/login', {
          username: this.username,
          password: this.password,
          identity: this.identity
        });
        const user = response.data;

        console.log(user)
        console.log(user.data.name)
        console.log(user.data.uid)
        console.log(this.username)
        if (this.identity === '0') {// uid不需要显示 name是名字 username是学号或者是工号
          this.$router.push({ name: 'Teacher', params: { teacherId: user.data.uid, name: user.data.name ,username:this.username} });
        } else {
          this.$router.push({ name: 'Student', params: { studentId: user.data.uid, name: user.data.name ,username:this.username} });
        }
      } 
      catch (error) {
        console.error('登录失败', error);
      }
    }
  }
};
</script>

<style>
/* 添加一些简单的样式 */
.login {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.login h2 {
  margin-bottom: 20px;
}

.login form div {
  margin-bottom: 10px;
}

.login form label {
  display: block;
  margin-bottom: 5px;
}

.login form input, .login form select {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

.login form button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.login form button:hover {
  background-color: #0056b3;
}
</style>
