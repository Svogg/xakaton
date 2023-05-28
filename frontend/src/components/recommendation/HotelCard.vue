<template>
  <v-card class="hotel-card" flat>
    <v-card-title>
      <v-icon class="mr-2">mdi-bed</v-icon>
      {{ item.title }}
      <v-spacer></v-spacer>
      {{ item.rating }}
      <v-icon color="primary">mdi-star</v-icon>
    </v-card-title>
    <v-card-subtitle class="d-flex">{{ item.rooms }}
      <v-spacer></v-spacer>
      <span class="hotel-card-price">{{ item.price }}</span></v-card-subtitle>
    <v-card-text>
      <div>{{ item.address }}</div>
      <div class="d-flex justify-space-between">
        <div>{{ item.distance }}</div>
        <div>
          <v-icon>mdi-wifi</v-icon>
          <v-icon>mdi-food-fork-drink</v-icon>
          <v-icon>mdi-parking</v-icon>
          <v-icon>mdi-desktop-classic</v-icon>
          <v-icon>mdi-pool-thermometer</v-icon>
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "HotelCard",
  props: {
    item: Object
  }
}
</script>

<style scoped lang="scss">
.hotel-card {
  .hotel-card-price {
    font-weight: 500;
    color: var(--v-primary-base);
  }
}
</style>