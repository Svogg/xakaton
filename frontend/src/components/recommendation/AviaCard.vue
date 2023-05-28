<template>
  <v-card class="avia-card" flat
  >
    <v-card-title><v-icon class="mr-2">mdi-airplane</v-icon><span class="avia-card-title">{{ item.title }}</span>
      <v-spacer></v-spacer>
      <span class="avia-card-price">{{ item.price }}</span>
    </v-card-title>
    <v-card-text>
      <div class="avia-card-info">
        <div class="avia-card-info-from">
          <div class="time">{{ item.timeFrom }}</div>
          <div class="city">{{ item.citiFrom }}</div>
          <div class="date">{{ item.dateFrom }}</div>
        </div>
        <div class="duration">
          <v-icon>mdi-airplane-takeoff</v-icon>
          <div>{{ item.duration }}</div>
          <v-icon>mdi-airplane-landing</v-icon>
        </div>
        <div class="avia-card-info-to">
          <div class="time">{{ item.timeTo }}</div>
          <div class="city">{{ item.citiTo }}</div>
          <div class="date">{{ item.dateTo }}</div>
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "AviaCard",
  props: {
    item: Object
  }
}
</script>

<style scoped lang="scss">
.avia-card {
  .avia-card-price {
    font-weight: 500;
    color: var(--v-primary-base);
  }

  .avia-card-info {
    display: grid;
    grid-template-columns: 80px auto 80px;
    align-items: center;
    justify-items: center;

    .avia-card-info-from{
      justify-self: start;
    }

    .duration {
      justify-self: stretch;
      font-size: .75rem;
      display: flex;
      justify-content: center;

      div {
        flex-grow: 1;
        text-align: center;
      }
    }

    .avia-card-info-to{
      justify-self: end;
      text-align: right;
    }

    .time {
      font-size: 1.625rem;
      line-height: 2.125rem;
      font-weight: 500;
    }

    .city {
      font-size: .75rem;
      line-height: 1.5em;
    }

    .date{
      font-size: .75rem;
      line-height: 1.5em;
    }
  }
}
</style>