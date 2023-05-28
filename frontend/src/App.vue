<template>
  <v-app id="app">
    <v-app-bar
        app
        flat
        color="background"
    >
      <img src="./assets/Vectorlogo.png" height="48" width="48"/>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>
        <RouterLink to="/">5Head</RouterLink>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <div class="d-flex align-center">
        <LoginForm v-if="!isLoggedIn"/>
        <RegisterForm v-if="!isLoggedIn" @success="successRegister"/>
        <v-btn
            v-if="isLoggedIn"
            :text="!isMobile"
            :icon="isMobile"
            to="/profile"
            class="mx-4"
        >
          <v-icon>mdi-account</v-icon>
          {{ !isMobile ? 'Профиль' : null }}
        </v-btn>
        <v-btn
            v-if="isLoggedIn"
            :text="!isMobile"
            :icon="isMobile"
            @click="logout"
        >
          <v-icon>mdi-logout</v-icon>
          Выйти
        </v-btn>
        <v-icon class="mr-2">mdi-weather-night</v-icon>
        <v-switch
            v-model="$vuetify.theme.dark"
            hide-details
        ></v-switch>
      </div>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view/>
      </v-container>

      <v-snackbar
        v-model="snackbar"
        color="success"
    >
      Регистрация прошла успешно, можете входить
      <template v-slot:action="{ attrs }">
        <v-btn
            color="primary"
            text
            v-bind="attrs"
            @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
    </v-main>
  </v-app>
</template>

<script>

import {mapActions} from "vuex";
import LoginForm from "@/components/auth/LoginForm.vue";
import RegisterForm from "@/components/auth/RegisterForm.vue";

export default {
  name: 'App',
  components: {LoginForm, RegisterForm},
  data() {
    return {
      showLoginForm: false,
      showRegisterForm: false,
      snackbar: false
    }
  },
  created() {
    this.checkToken()
    this.$setupAxios()
    this.loadCities()
    //this.loadAirlines()
  },
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mobile
    },
    isLoggedIn() {
      return this.$store.getters["auth/isLoggedIn"]
    }
  },
  methods: {
    ...mapActions("reference", ["loadCities"]),
    logout: function () {
      this.$store.dispatch('auth/logout')
          .then(() => {

          })
    },
    checkToken() {
      this.$axios.interceptors.response.use(undefined, function (err) {
        return new Promise(function () {
          if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
            this.$store.dispatch("logout")
          }
          throw err;
        });
      });
    },
    successRegister(){
      this.snackbar=true
    }
  }
};
</script>
<style lang="scss">
$color-pack: false;
.v-application {
  background-color: var(--v-background-base) !important;
}
</style>