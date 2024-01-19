<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Login</a>
                        </li>


                    </ul>

                </div>
            </div>
        </nav>
        <div class="container text-center flex">
            <div class="row">
                <div class="col-3">
                </div>

                <div class="col-6">
                    <h2>Login Form</h2>
                    <form @submit.prevent>
                        <div class="mb-3">
                            <label for="exampleInputEmail1" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                                v-model="u_mail" required>
                            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputPassword1" class="form-label">Password</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                        </div>
                        <button type="button" class="btn btn-primary" @click="loginUser()">Register</button>
                    </form>
                </div>
                <div class="col-3">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: "LoginUserView",
    data() {
        return {
            u_mail: "",
            password: "",
            re_password: "",
        }
    },
    methods: {
        loginUser() {


            if (!this.u_mail || !this.password) {
                alert("All fields Required !!")
                return;
            }
            if (!this.u_mail.includes("@") || !this.u_mail.endsWith(".com")) {
                alert("Invalid email format !! Email must include '@' and end with '.com'");
                return;
            }

            axios.post('http://127.0.0.1:8081/api/login', {
                u_mail: this.u_mail,
                password: this.password,
            })
                .then((response) => {
                    if (response.data.status === "success") {
                        const access_token = response.data.access_token;
                        const refresh_token = response.data.refresh_token;
                        const u_mail = response.data.u_mail;

                        console.log(u_mail)
                        console.log(access_token)
                        console.log(refresh_token)
                        localStorage.setItem("access_token", access_token);
                        localStorage.setItem("refresh_token", refresh_token);
                        localStorage.setItem("user_mail", u_mail);
                        
                        this.$router.push("/home");
                        return;
                    }
                    if (response.data.status === "failed") {
                        alert(response.data.message)
                    }
                })
                .catch((error) => {
                    console.error(error);
                    alert("An error occurred while registering the user");
                });



        }
    }
}
</script>

<style scoped></style>
