<template>
  <div class="choice-line">
    <ChoiceButton
        v-for="key of Object.keys(getChoiceCategories)"
        :key="getChoiceCategories[key].id"
        :icon="getChoiceCategories[key].icon"
        :title="getChoiceCategories[key].title"
        :active="getChoiceCategories[key].active"
        :small="smallView"
        @click="toggleChoiceButton(key)"
    />
  </div>
</template>

<script>
import ChoiceButton from "@/components/choice/ChoiceButton.vue";
import vuetify from "@/plugins/vuetify";
import {mapGetters} from "vuex";

export default {
  name: "ChoiceLine",
  components: {
    ChoiceButton
  },
  data() {
    return {}
  },
  computed: {
    smallView() {
      return this.$vuetify.breakpoint.mdAndDown
    },
    ...mapGetters('user', ["getChoiceCategories"]),
  },
  methods: {
    vuetify() {
      return vuetify
    },
    toggleChoiceButton(key) {
      this.$store.commit("user/toggleChoiceCategoryActive", key)
    }
  }
}
</script>

<style scoped lang="scss">
.choice-line {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0 16px;
  gap: 8px;
}
</style>