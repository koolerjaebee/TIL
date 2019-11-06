import Vue from 'vue';
import App from './App.vue';  // .vue 는 안써도 알아서 동작함.

new Vue({
    // [el: '#app'] === [.$mount('#app')]
    // method(함수 in 객체) 정의할 때, () => {} 금기이지만, 여기서만 쓴다.
    render: h => h(App),
}).$mount('#app')