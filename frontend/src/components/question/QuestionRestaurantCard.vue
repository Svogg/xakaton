<template>
  <div class="question-restaurant">
    <div>
      <v-autocomplete
          label="Тип кухни"
          :value="category.kitchenType"
          :items="kitchenTypes"
          @change="setKitchenType"
          dense
          multiple
          chips
          small-chips
      ></v-autocomplete>
    </div>
    <div>
      <div>Средний чек: {{ priceText }}</div>
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
  name: "QuestionRestaurantCard",
  data() {
    return {
      CODE: 'restaurant',
      kitchenTypes: ["Азиатская", "Русская", "Кавказская", "Европейская"]
    }
  },
  computed: {
    category() {
      return this.$store.getters["user/getChoiceCategory"](this.CODE)
    },
    priceText() {
      return this.category.price.join(', ')
    },
    ...mapGetters('reference', ["getCities"]),
  },
  methods: {
    setKitchenType(value) {
      this.$store.commit("user/setChoiceCategoryRestaurantKitchenType", value)
    },
    priceInput(value) {
      this.$store.commit("user/setChoiceCategoryRestaurantPrice", value)
    }
  }
}
</script>

<style scoped lang="scss">
.question-restaurant {
  box-sizing: border-box;
  border: 2px solid var(--background-accent);
  border-radius: 24px;
  padding: 12px;
  height: 148px;
}
</style>