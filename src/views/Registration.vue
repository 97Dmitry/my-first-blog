<template>
  <form class="card auth-card col s12 m2" v-on:submit.prevent="submitHandler()">
    <div class="card-content">
      <span class="card-title">Регистрация</span>
      <div class="input-field">
        <input
          id="username"
          type="text"
          v-model.trim="username"
          :class="{ invalid: v$.username.$error }"
        />
        <label for="username">Имя аккаунта</label>
        <small
          class="helper-text invalid"
          v-for="(error, index) of v$.username.$errors"
        >
          {{ printError(error.$validator, error.$params) }}
        </small>
      </div>
      <div class="input-field">
        <input
          id="email"
          type="email"
          v-model.trim="email"
          :class="{ invalid: v$.email.$error }"
        />
        <label for="email">Электронная почта"</label>
        <small
          class="helper-text invalid"
          v-for="(error, index) of v$.email.$errors"
        >
          {{ printError(error.$validator, error.$params) }}
        </small>
      </div>
      <div class="input-field">
        <input
          id="password"
          type="password"
          v-model.trim="password"
          :class="{ invalid: v$.password.$error }"
        />
        <label for="password">Пароль</label>
        <small
          class="helper-text invalid"
          v-for="(error, index) of v$.password.$errors"
        >
          {{ printError(error.$validator, error.$params) }}
        </small>
      </div>
      <div class="input-field">
        <input
          id="passwordConfirmation"
          type="password"
          v-model.trim="passwordConfirmation"
          :class="{ invalid: v$.passwordConfirmation.$error }"
        />
        <label for="passwordConfirmation">Пароль</label>
        <small
          class="helper-text invalid"
          v-for="(error, index) of v$.passwordConfirmation.$errors"
        >
          {{ printError(error.$validator, error.$params) }}
        </small>
      </div>
      <div>
        <p>
          <label>
            <input type="checkbox" v-on:click="agree = !agree" v-model="agree"/>
            <span>С правилами согласен</span>
          </label>
        </p>
      </div>
      <div class="d-grid gap-2">
        <button class="btn btn-success" type="submit">Зарегистрироваться <i class="bi bi-arrow-right-square"></i>
        </button>
      </div>
      <p class="text-center"
         style="color: #0f0f0f;
         margin-top: 5px">
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
      password: "",
      passwordConfirmation: "",
      username: "",
      agree: false
    };
  },
  validations() {
    return {
      email: {required, email},
      password: {required, minLength: minLength(8)},
      passwordConfirmation: {required, minLength: minLength(8)},
      username: {required, minLength: minLength(4)},
      agree: {checked: v => v}
    };
  },
  methods: {
    async submitHandler() {
      this.v$.$touch();
      if (this.v$.$error) {
        console.log(this.$store.getters.getServerUrl)
        return;
      } else if (this.password !== this.passwordConfirmation) {
        this.$error("Пароль должен совпадать")
        return
      }
      const formData = {
        email: this.email,
        password: this.password,
        username: this.username
      }
      try {
        await this.$store.dispatch("accountRegistration", formData)
      } catch (e) {
        console.log(e)
      }
      this.$message("Аккаунт успешно зарегистрирован")
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