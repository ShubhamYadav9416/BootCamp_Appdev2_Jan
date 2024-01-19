import Vue from "vue";
import VueRouter from "vue-router";

import RegisterView from "../views/auth/RegisterView.vue"
import LoginView from "../views/auth/LoginView"

Vue.use(VueRouter)

const routes = [
    {
        path:"/register",
        name: "Registration-Page",
        component: RegisterView,
    },
    {
        path:"/login",
        name: "Login-Page",
        component: LoginView,
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router