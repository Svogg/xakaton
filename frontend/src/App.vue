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
        <v-btn
            :text="!isMobile"
            :icon="isMobile"
            to="/profile"
            class="mx-4"
        >
          <v-icon>mdi-account</v-icon>
          {{ !isMobile ? 'Профиль' : null }}
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
    </v-main>
  </v-app>
</template>

<script>

import {mapActions} from "vuex";

export default {
  name: 'App',
  created() {
    this.$setupAxios()
    this.loadCities()
    //this.loadAirlines()
  },
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mobile
    }
  },
  methods:{
    ...mapActions("reference", ["loadCities"]),
  }
};
</script>
<style lang="scss">
$color-pack: false;
.v-application {
  background-color: var(--v-background-base) !important;
}
</style>