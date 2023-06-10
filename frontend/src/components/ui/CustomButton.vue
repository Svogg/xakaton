<template>
  <div class="custom-button" :class="{gap:icon, disabled}" @click="clickHandler">
    <v-icon v-text="icon"></v-icon>
    <div>{{ title }}</div>
  </div>
</template>

<script>
export default {
  name: "CustomButton",
  props: {
    title: String,
    icon: String,
    disabled: Boolean
  },
  methods:{
    clickHandler(){
      if(this.disabled) return
      this.$emit('click')
    }
  }
}
</script>

<style scoped lang="scss">
.custom-button {
  background: var(--v-primary-base);
  border-radius: 12px;
  font-weight: 500;
  font-size: 16px;
  line-height: 22px;
  box-sizing: border-box;
  height: 48px;
  cursor: pointer;
  border: 2px solid var(--v-primary-base);
  color: var(--text-primary);
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0 16px;
  width: 100%;

  &.gap{
    gap: 8px;
  }

  &:hover {
    border: 2px solid var(--v-primary-base);
    color: var(--text-secondary);
  }

  &.disabled{
    cursor: no-drop;
    opacity: 0.1;
  }
}

.theme--dark {
  .choice-button {
    color: var(--text-secondary-solid);

    &.active {
      color: var(--color-white);
    }
  }
}
</style>