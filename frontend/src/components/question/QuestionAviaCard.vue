<template>
<div class="question-avia">
    <div>
     <v-autocomplete
          label="Авиакомпания"
          :value="category.airline"
          :items="getAirlines"
          @change="setAirline"
          dense
          multiple
          chips
          small-chips
      ></v-autocomplete>
    </div>
    <div>
      <div>Интервал стоимости: {{priceText}}</div>
      <v-range-slider
          :value="category.price"
          max="100000"
          min="0"
          step="1000"
          @input="priceInput"
          dense
          hide-details
      ></v-range-slider>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "QuestionAviaCard",
   data() {
    return {
      CODE: 'avia'
    }
  },
  computed: {
    category() {
      return this.$store.getters["user/getChoiceCategory"](this.CODE)
    },
    priceText() {
      return this.category.price.join(', ')
    },
    ...mapGetters('reference', ["getAirlines"]),
  },
  methods: {
    setAirline(value) {
      this.$store.commit("user/setChoiceCategoryAviaAirline", value)
    },
    priceInput(value) {
      this.$store.commit("user/setChoiceCategoryAviaPrice", value)
    }
  }
}
</script>

<style scoped lang="scss">
.question-avia {
  box-sizing: border-box;
  border: 2px solid var(--background-accent);
  border-radius: 24px;
  padding: 12px;
  height: 148px;
}
</style>