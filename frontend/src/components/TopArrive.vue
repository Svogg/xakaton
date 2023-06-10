<template>
  <div class="top-arrive">
    <div class="image">
      <img :src="image" alt="img" height="236"/>
    </div>
    <div class="content">
      <div class="title">{{ title }}</div>
      <div class="price">{{ price }} руб.</div>
      <div class="dates">{{ dateText }}</div>
    </div>
  </div>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "TopArrive",
  props: {
    image: String,
    title: String,
    price: Number,
    dates: Array,
  },
  computed: {
    dateText() {
      if (!this.dates?.length) return null
      const dt1 = this.dates[0].substr(5)
      const dt2 = this.dates[1] ? ` ~ ${this.dates[1].substr(5)}` : ''
      return dt1 + dt2
    }
  }
})
</script>

<style scoped lang="scss">
.top-arrive {
  overflow: hidden;
  position: relative;
  border-radius: 24px;

  .image{
    object-fit: fill;
    img{
      border-radius: 24px;
    }
  }

  .content{
    position: absolute;
    left: 0;
    bottom: 0;
    color: white;
    background: #1D1D1D99;
    width: 248px;
    padding: 8px 8px;
  }
}
</style>