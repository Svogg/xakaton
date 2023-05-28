<template>
  <v-menu offset-y :close-on-content-click="false">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
          class="mr-2"
          :text="!isMobile"
          :icon="isMobile"
          v-bind="attrs"
          v-on="on"
      >
        <v-icon>mdi-login</v-icon>
        {{ !isMobile ? 'Войти' : null }}
      </v-btn>
    </template>
    <v-card flat>
      <v-card-text>
        <v-form
            ref="form"
            v-model="valid"
        >
          <v-text-field
              v-model="username"
              :rules="requiredRules"
              label="Имя пользователя"
              clearable
              required
          ></v-text-field>

          <v-text-field
              v-model="password"
              :rules="requiredRules"
              label="Пароль"
              type="password"
              clearable
              required
          ></v-text-field>

          <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="login"
              block
          >
            Войти
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      username: "",
      password: "",
      valid: false,
      requiredRules: [
        v => !!v || 'Поле обязательно для заполнения'
      ],
    }
  },
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mobile
    },
  },
  methods: {
    login: function () {
      let username = this.username
      let password = this.password
      this.$store.dispatch("auth/login", {username, password})
          .then()
          .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>