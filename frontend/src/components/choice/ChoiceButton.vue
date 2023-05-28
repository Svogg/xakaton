<template>
  <div class="choice-button" :class="{active}" @click="$emit('click')">
    <v-icon v-text="icon"></v-icon>
    <div v-if="!small">{{ title }}</div>
  </div>
</template>

<script>
export default {
  name: "ChoiceButton",
  props: {
    title: String,
    icon: String,
    active: Boolean,
    small: Boolean
  }
}
</script>

<style scoped lang="scss">
.choice-button {
  background: var(--v-background-base);
  border-radius: 12px;
  font-weight: 500;
  font-size: 16px;
  line-height: 22px;
  box-sizing: border-box;
  height: 48px;
  color: var(--text-secondary);
  cursor: pointer;
  border: 2px solid var(--v-background-base);

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0 16px;
  gap: 8px;

  &:hover {
    color: var(--text-primary);
  }

  &.active {
    border: 2px solid var(--v-primary-base);
    color: var(--text-primary);
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