<template>
  <div class="search-bar" :class="{
    'search-bar__md': $vuetify.breakpoint.md,
    'search-bar__sm': $vuetify.breakpoint.sm,
    'search-bar__xs': $vuetify.breakpoint.xs,
    }">
    <v-row dense>
      <v-col cols="12" lg="3" md="6" sm="6" class="px-0"
             v-if="getActiveChoice.includes('avia')"
      >
        <div class="element arrive-from">
          <v-autocomplete
              label="ОТКУДА"
              :items="getCities"
              item-text="city_name"
              item-value="id"
              v-model="citi_from"
              hide-details
              dense
              clearable
          ></v-autocomplete>
        </div>
      </v-col>
      <v-col cols="12" :lg="getActiveChoice.includes('avia') ? 3 : 6"
             :md="getActiveChoice.includes('avia') ? 6 : 12"
             :sm="getActiveChoice.includes('avia') ? 6 : 12" class="px-0">
        <div class="element arrive-to" :class="{'only-to': !getActiveChoice.includes('avia')}">
          <v-autocomplete
              label="КУДА"
              :items="toCities"
              item-text="city_name"
              item-value="id"
              v-model="citi_to"
              hide-details
              dense
              clearable
          ></v-autocomplete>
        </div>
      </v-col>
      <v-col cols="9" lg="3" md="8" sm="8" class="px-0">
        <div class="element travel-period">
          <DatePicker
              :value.sync="dates"
          />
        </div>
      </v-col>
      <v-col cols="3" lg="1" md="4" sm="4" class="px-0">
        <div class="element passengers">
          <PassengersCounter
              :adult.sync="adult"
              :children.sync="children"
          />
        </div>
      </v-col>
      <v-col cols="12" lg="2" offset-lg="0" offset-md="4" md="4" class="px-0">
        <div class="element pick-up">
          <CustomButton
              title="Подобрать"
              @click="searchHandler"
              :disabled="!canSearch"
          />

        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import DatePicker from "@/components/ui/DatePicker.vue";
import CustomButton from "@/components/ui/CustomButton.vue";
import PassengersCounter from "@/components/PassengersCounter.vue";
import {mapGetters} from "vuex";

export default {
  name: "SearchBar",
  components: {
    DatePicker,
    CustomButton,
    PassengersCounter
  },
  data() {
    return {
      citi_from: null,
      citi_to: null,
      adult: 1,
      children: 0,
      dates: []
    }
  },
  mounted() {
    this.citi_from = this.getUser.citi
  },
  computed: {
    ...mapGetters('user', ["getChoice", "getActiveChoice"]),
    ...mapGetters('auth', ["getUser"]),
    ...mapGetters('reference', ['getCities']),
    toCities() {
      return this.getCities.filter(el => el.id !== this.citi_from)
    },
    canSearch() {
      return (this.getActiveChoice.includes('avia') ? this.citi_from : true)
          && this.citi_to && this.dates.length
    }
  },
  methods: {
    searchHandler() {
      this.$emit('search', {
        citi_from: this.citi_from,
        citi_to: this.citi_to,
        adult: this.adult,
        children: this.children,
        dates: this.dates
      })
    }
  }
}
</script>

<style scoped lang="scss">
.search-bar {
  background: transparent;

  //display: grid;
  //grid-template-columns: 3fr 3fr 2fr 1fr 1fr;
  //gap: 0 12px;
  //align-items: center;
  .element {
    padding: 12px;
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;

    /* box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);*/
    background: var(--color-white);

    height: 72px;
  }

  .arrive-from {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-bottom: 1px solid #cccccc;
  }

  .arrive-to {
    border-bottom: 1px solid #cccccc;

    &.only-to {
      border-top-left-radius: 20px;
      border-bottom-left-radius: 20px;
    }
  }

  .travel-period {
    border-bottom: 1px solid #cccccc;
  }

  .passengers {
    border-bottom: 1px solid #cccccc;
  }

  .pick-up {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
    width: 100%;
    border-bottom: 1px solid #cccccc;
  }
}

.search-bar__md {
  .arrive-from {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }

  .arrive-to {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }

  .travel-period {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }

  .passengers {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }

  .pick-up {
    border-radius: 0;
    background: transparent;
    border-bottom: none;
  }
}

.search-bar__sm {
  .arrive-from {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }

  .arrive-to {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }

  .travel-period {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }

  .passengers {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }

  .pick-up {
    border-radius: 0;
    background: transparent;
    border-bottom: none;
  }
}

.search-bar__xs {
  .arrive-from {
    border-radius: 20px;
  }

  .arrive-to {
    border-radius: 20px;
  }

  .travel-period {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }

  .passengers {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }

  .pick-up {
    border-radius: 0;
    background: transparent;
    border-bottom: none;
  }
}

.theme--dark {
  .search-bar {
    .element {
      background: inherit;
    }
  }

}
</style>