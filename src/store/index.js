// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
        uid: null,
        name: '',  // 默认结构中包含 name
        inputUsername: ''  // 添加一个新的字段来存储用户输入的 username
      }
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    async login({ commit }, { username, password, identity }) {
      try {
        const response = await axios.post('http://127.0.0.1:8082/login', {
          username,
          password,
          identity
        });
        const user = response.data;
        user.inputUsername = username;  // 将用户输入的 username 添加到 user 对象中
        commit('setUser', user);
        return user;
      } catch (error) {
        console.error('登录失败', error);
        throw error;
      }
    }
  },
  getters: {
    getUser(state) {
      return state.user;
    }
  }
});
