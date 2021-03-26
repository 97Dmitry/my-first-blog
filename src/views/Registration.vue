<template>
<form class="card auth-card border-secondary mb-3" v-on:submit.prevent="submitHandler()">
  <div class="auth-container">
    <div class="auth-title">
      <span>Регистрация</span>
    </div>
    <div class="form-control">
      <label for="username" class="auth-label">Username</label>
      <input type="text"
             class="form-control"
             id="username"
             placeholder="Введите имя аккаунта"
             v-model.trim="username"
             :class="{ red_border: v$.username.$error }">
      <small
        class="helper-text invalid"
        v-for="(error, index) in v$.username.$errors" :key="index">
        {{ printError(error.$validator, error.$params) }}
      </small>
    </div>
    <div class="form-control">
      <label for="email" class="auth-label">Email</label>
      <input type="email"
             class="form-control"
             id="email"
             placeholder="Введите email"
             v-model.trim="email"
             :class="{ red_border: v$.email.$error }">
      <small
        class="helper-text invalid"
        v-for="(error, index) in v$.email.$errors" :key="index">
        {{ printError(error.$validator, error.$params) }}
      </small>
    </div>
    <div class="form-control">
      <label for="password1" class="auth-label">Password</label>
      <input type="password"
             class="form-control"
             id="password1"
             placeholder="Введите пароль"
             v-model="password1"
             :class="{ red_border: v$.password1.$error }">
      <small
        class="helper-text invalid"
        v-for="(error, index) in v$.password1.$errors" :key="index">
        {{ printError(error.$validator, error.$params) }}
      </small>
    </div>
    <div class="form-control">
      <label for="password2" class="auth-label">Confirm password</label>
      <input type="password"
             class="form-control"
             id="password2"
             placeholder="Подтвердите пароль"
             v-model="password2"
             :class="{ red_border: v$.password2.$error }">
      <small
        class="helper-text invalid"
        v-for="(error, index) in v$.password2.$errors" :key="index">
        {{ printError(error.$validator, error.$params) }}
      </small>
    </div>
    <div class="form-check" style="color: #0f0f0f; margin-bottom: 25px">
      <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate"
       v-on:click="agree = !agree" v-model="agree">
      <label class="form-check-label" for="flexCheckIndeterminate">
        С правилами согласен
      </label>
    </div>
    <div class="d-grid gap-2">
      <button class="btn btn-success" type="submit">Зарегистрироваться <i class="bi bi-arrow-right-square"></i></button>
    </div>
    <p class="text-center" style="color: #0f0f0f; margin-top: 5px">
      Уже есть аккаунт?
      <router-link to="/login">Войти!</router-link>
    </p>
  </div>
</form>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import {required, email, minLength} from "@vuelidate/validators";

export default {
  name: "Registration",
  setup() {
    return {v$: useVuelidate()};
  },
  data() {
    return {
      email: "",
      password1: "",
      password2: "",
      username: "",
      agree: false
    };
  },
  validations() {
    return {
      email: {required, email},
      password1: {required, minLength: minLength(8)},
      password2: {required, minLength: minLength(8)},
      username: {required, minLength: minLength(4)},
      agree: {checked: v => v}
    };
  },
  methods: {
    submitHandler() {
      this.v$.$touch();
      if (this.v$.$error) {
        return;
      }

      const formData = {
        email: this.email,
        password1: this.password1,
        password2: this.password2,
        username: this.username
      }

      console.log(formData)

      this.$router.push({name: "Home"});
    },

    printError($name, $param) {
      if ($name === "required") {
        return "Поле не должно быть пустым";
      } else if ($name === "email") {
        return "Введите корректный email";
      } else if ($name === "minLength") {
        return "Минимальная длина должна быть " + $param.min + " символов";
      }

    },
  },
};
</script>

<style scoped></style>