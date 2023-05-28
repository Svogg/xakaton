<template>
  <v-menu v-model="show" offset-y :close-on-content-click="false">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
          class="mr-2"
          :text="!isMobile"
          :icon="isMobile"
          v-bind="attrs"
          v-on="on"
      >
        <v-icon>mdi-account-plus</v-icon>
        {{ !isMobile ? 'Зарегистрироваться' : null }}
      </v-btn>
    </template>
    <v-card flat>
      <v-card-text>
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >
          <v-text-field
              v-model="username"
              :rules="requiredRules"
              label="Имя пользователя"
              clearable
              required
          ></v-text-field>

          <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              type="email"
              clearable
              required
          ></v-text-field>

          <v-text-field
              v-model="hashed_password"
              :rules="requiredRules"
              label="Пароль"
              type="password"
              clearable
              required
          ></v-text-field>

          <v-text-field
              v-model="password_confirmation"
              :rules="passwordRules"
              label="Потверждение пароля"
              type="password"
              clearable
              required
          ></v-text-field>

          <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="register"
              block
          >
            Зарегистрироваться
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      show: false,
      valid: false,
      username: "",
      email: "",
      hashed_password: "",
      password_confirmation: "",
      emailRules: [(v) => !!v && /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || "Введите валидный email"],
      requiredRules: [v => !!v || "Поле обязательно для заполнения"],
      passwordRules: [
        v => !!v || "Поле обязательно для заполнения",
        v => v === this.hashed_password || "Пароли не совпадают"
      ]

    }
  },
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mobile
    },
  },
  methods: {
    register: function () {
      this.$refs.form.validate()
      if (!this.valid) return
      let data = {
        username: this.username,
        email: this.email,
        hashed_password: this.hashed_password
      }
      this.$store.dispatch("auth/register", data)
          .then(() => {
            this.show = false
            this.$emit("success")
          })
          .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>