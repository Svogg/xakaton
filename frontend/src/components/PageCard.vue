<template>
  <v-sheet class="page-card" color="backgroundDefault">
    <div class="page-card-banner">

    </div>
    <div class="choice-line">
      <ChoiceLine/>
    </div>
    <div class="search-bar-block">
      <SearchBar/>
    </div>
    <div class="question">
      <v-row>
        <v-col cols="12" lg="4" sm="6" xs="12" v-if="activeChoice.includes('hotel')">
          <QuestionHotelCard/>
        </v-col>
        <v-col cols="12" lg="4" sm="6" xs="12" v-if="activeChoice.includes('restaurant')">
          <QuestionRestaurantCard/>
        </v-col>
        <v-col cols="12" lg="4" sm="6" xs="12" v-if="activeChoice.includes('avia')">
          <QuestionAviaCard/>
        </v-col>
      </v-row>

    </div>

    <div class="content">
      <v-row>
        <v-col cols="12" lg="4" sm="6" xs="12"
               v-for="(item, index) of recommendation"
               :key="index"
        >
          <RecommendationCard

              :item="item"
          />
        </v-col>
      </v-row>
    </div>
  </v-sheet>
</template>

<script>
import ChoiceLine from "@/components/choice/ChoiceLine.vue";
import SearchBar from "@/components/search/SearchBar.vue";
import QuestionHotelCard from "@/components/question/QuestionHotelCard.vue";
import {mapGetters} from "vuex";
import QuestionRestaurantCard from "@/components/question/QuestionRestaurantCard.vue";
import QuestionAviaCard from "@/components/question/QuestionAviaCard.vue";
import RecommendationCard from "@/components/recommendation/RecommendationCard.vue";
import recommendation from "/recomendation.json"

export default {
  name: 'PageCard',
  components: {ChoiceLine, SearchBar, QuestionHotelCard, QuestionRestaurantCard, QuestionAviaCard, RecommendationCard},
  data() {
    return {
      recommendation: recommendation
    }
  },
  computed: {
    ...mapGetters('user', ["getChoiceCategories"]),
    activeChoice() {
      return Object.keys(this.getChoiceCategories)
          .filter(key => this.getChoiceCategories[key].active)
          .reduce((obj, key) => {
            obj.push(key)
            return obj
          }, [])
    }
  }
}
</script>

<style scoped lang="scss">
.page-card {
  border-radius: 48px;
  padding: 48px 48px 52px;

  .choice-line {
    margin-bottom: 16px;
  }

  .search-bar-block {
    margin-bottom: 24px;
  }
}
</style>
