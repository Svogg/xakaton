<template>
  <div class="about">
    <h1>Профиль пользователя</h1>

    <h2>{{ getUser.username }}</h2>
    <h3>{{ getUser.email }}</h3>
    <v-autocomplete
        label="Город"
        :items="getCities"
        item-text="city_name"
        item-value="id"
        :value="getUser.citi"
        @change="setUserCiti"
    ></v-autocomplete>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  data(){
    return{
      citi: null
    }
  },
  computed: {
    ...mapGetters('auth', ['getUser']),
    ...mapGetters('reference', ['getCities'])
  },
  methods: {
    setUserCiti(event) {
      this.$store.commit('auth/setUserCiti', event)
    }
  },
}
</script>