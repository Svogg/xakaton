<template>
  <div class="about">
    <h1>Профиль пользователя</h1>

    <h2>{{ getUser.name }}</h2>
    <h3>{{ getUser.login }}</h3>
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
    ...mapGetters('user', ['getUser']),
    ...mapGetters('reference', ['getCities'])
  },
  methods: {
    setUserCiti(event) {
      this.$store.commit('user/setUserCiti', event)
    }
  },
}
</script>