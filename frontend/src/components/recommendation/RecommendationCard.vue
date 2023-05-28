<template>
  <v-card

      class="recommendation-card"
  >
    <v-carousel
        :continuous="false"
        cycle
        :show-arrows="false"
        hide-delimiter-background
        height="286"
        class="carousel-block"
    >
      <v-carousel-item
          v-for="i in 5"
          :key="i"
      >
        <v-img class="carousel-block-image" :src="require(`./../../assets/img${i}.jpeg`)" height="286"></v-img>
      </v-carousel-item>
    </v-carousel>
    <div class="scroll-block">
      <AviaCard
          v-if="airline"
          :item="airline"
      />
      <AviaCard
          v-if="airlineBack"
          :item="airlineBack"
      />
      <HotelCard
          v-if="hotel"
          :item="hotel"
      />
      <div class="px-3">{{moreText}}</div>
    </div>
    <v-card-actions>
      <CustomButton
          title="Подробнее"
      />
    </v-card-actions>
  </v-card>
</template>

<script>
import AviaCard from "@/components/recommendation/AviaCard.vue";
import HotelCard from "@/components/recommendation/HotelCard.vue";
import CustomButton from "@/components/ui/CustomButton.vue";

export default {
  name: "RecommendationCard",
  components: {AviaCard, HotelCard, CustomButton},
  props: {
    item: Object
  },
  data() {
    return {}
  },
  computed: {
    airline() {
      return this.item.airline
    },
    airlineBack() {
      return this.item.airlineBack
    },
    hotel() {
      return this.item.hotel
    },
    moreText() {
      return this.item.moreText
    },
  }
}
</script>

<style scoped lang="scss">
.recommendation-card {
  border-radius: 20px;
  border: 1px solid var(--v-primary-base);

  .carousel-block {
    border-radius: 20px;
    padding: 4px;

    .carousel-block-image {
      border-radius: 20px;
    }
  }

  .scroll-block{
    max-height: calc(150px + 170px + 24px);
    height: calc(150px + 170px + 24px);
    overflow: hidden;
    overflow-y: auto;

    &::-webkit-scrollbar {
      width: 8px;               /* width of the entire scrollbar */
    }

    &::-webkit-scrollbar-track {
      background: inherit;        /* color of the tracking area */
    }

    &::-webkit-scrollbar-thumb {
      background-color: var(--v-primary-base);    /* color of the scroll thumb */
      border-radius: 20px;       /* roundness of the scroll thumb */
    }
  }
}
</style>