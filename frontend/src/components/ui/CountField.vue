<template>
  <div class="count-field">
    <v-btn icon @click="clickMinusHandler" :disabled="disabledMinus">
      <v-icon>mdi-minus</v-icon>
    </v-btn>
    <div class="counter">{{ value }}</div>
    <v-btn icon @click="clickPlusHandler" :disabled="disabledPlus">
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "CountField",
  props: {
    value: Number,
    min: Number,
    max: Number
  },
  computed: {
    disabledMinus() {
      return this.min !== null && this.min !== undefined && this.min > this.value - 1
    },
    disabledPlus() {
      return this.max !== null && this.max !== undefined && this.value + 1 > this.max
    }
  },
  methods: {
    clickMinusHandler() {
      if (this.disabledMinus) {
        return
      }
      this.$emit('input', this.value - 1)
    },
    clickPlusHandler() {
      if (this.disabledPlus) {
        return
      }
      this.$emit('input', this.value + 1)
    }
  }
}
</script>

<style scoped lang="scss">
.count-field {
  display: flex;
  align-items: center;
  width: 120px;

  .counter {
    font-weight: 500;
    margin: 0 12px;
    text-align: center;
    width: 24px;
  }
}
</style>