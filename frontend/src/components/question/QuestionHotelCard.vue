<template>
  <div class="question-hotel">
    <div>Минимальный рейтинг отеля:</div>
    <div>
      <v-rating
          color="primary"
          empty-icon="mdi-star-outline"
          full-icon="mdi-star"
          half-icon="mdi-star-half-full"
          hover
          length="5"
          :value="category.rating"
          @input="setRating"
      ></v-rating>
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
export default {
  name: "QuestionHotelCard",
  data() {
    return {
      CODE: 'hotel'
    }
  },
  computed: {
    category() {
      return this.$store.getters["user/getChoiceCategory"](this.CODE)
    },
    priceText(){
      return this.category.price.join(', ')
    }
  },
  methods: {
    setRating(value) {
      this.$store.commit("user/setChoiceCategoryHotelRating", value)
    },
    priceInput(value){
      this.$store.commit("user/setChoiceCategoryHotelPrice", value)
    }
  }
}
</script>

<style scoped lang="scss">
.question-hotel {
  box-sizing: border-box;
  border: 2px solid var(--background-accent);
  border-radius: 24px;
  padding: 12px;
  height: 148px;
}
</style>