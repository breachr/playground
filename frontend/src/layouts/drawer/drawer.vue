<template>
<q-drawer class="myDrawer bg-grey-7  text-white" side="left" v-model="showDrawer">

    <div class="drawerHeader" @click="goHome">
      <h2>KFZ-Albrink</h2>
    </div>

    <q-list grey no-border separator style="max-width: 318px">

      <!-- Scroll Tos -->
      <q-item clickable v-ripple :active="selectedTab=='homy'" @click="scrollTo('#sect1')" active-class="activeDrawer">
        <q-item-section avatar><q-icon name="inbox" /></q-item-section>
        <q-item-section class="text-bold">Dashboard</q-item-section>
      </q-item>

      <q-item clickable v-ripple :active="selectedTab=='sect2'" @click="scrollTo('#sect2')" active-class="activeDrawer">
        <q-item-section avatar><q-icon name="ion-logo-linkedin" /></q-item-section>
        <q-item-section class="text-bold">Inbox</q-item-section>
      </q-item>

      <q-item clickable v-ripple :active="selectedTab=='sect3'" @click="scrollTo('#sect3')" active-class="activeDrawer">
        <q-item-section avatar><q-icon name="class" /></q-item-section>
        <q-item-section class="text-bold">Motion Detectors</q-item-section>
      </q-item>

      <q-item clickable v-ripple :active="selectedTab=='sect4'" @click="scrollTo('#sect4')" active-class="activeDrawer">
        <q-item-section avatar><q-icon name="inbox" /></q-item-section>
        <q-item-section class="text-bold">Audio Detectors</q-item-section>
      </q-item>

      <!-- Routes -->
      <router-link to="/" v-scroll-to="{ el: '#homy', onStart: closeDrawer,}">
        <q-item clickable v-ripple :active="currentSite=='/'" active-class="activeDrawer">
          <q-item-section avatar><q-icon name="class" /></q-item-section>
          <q-item-section>Home</q-item-section>
        </q-item>
      </router-link>

      <!-- Route + automatic scroll to -->
      <router-link to="/banane" v-scroll-to="{ el: '#sect4', onStart: closeDrawer,}">
        <q-item clickable v-ripple :active="currentSite=='/banane'" active-class="activeDrawer">
          <q-item-section avatar><q-icon name="class" /></q-item-section>
          <q-item-section>Banane</q-item-section>
        </q-item>
      </router-link>

    </q-list>

    <!-- Drawer Footer -->
    <div class="times q-list-header">
      <br> Öffnungszeiten:
      <br> Mo-Do 8-17 Uhr | Fr 8-16 Uhr
      <br>
      <q-btn class="draworBtn" icon="phone" label="05222 123456" />
      <!-- <q-btn color="secondary" icon="mail" label="info@kfz-albrink.de" />
      <q-btn color="secondary" icon="location_on" label="05222 123456" /> -->
    </div>

</q-drawer>
</template>

<script>
import {
  openURL
} from 'quasar' // for tel links etc.

var VueScrollTo = require('vue-scrollto') // directives dont work here

export default {
  methods: {
    openURL,
    goHome () {
      location.reload()
    },
    closeDrawer () {
      this.$store.state.showDrawer = false
    },
    scrollTo (target) {
      this.closeDrawer()
      setTimeout(() => { VueScrollTo.scrollTo(target) }, 500)
    }
  },
  computed: { // basic states
    selectedTab () {
      return this.$store.state.daWaypoint
    },
    currentSite () {
      return this.$route.path
    },
    showDrawer: { // FOR V-MODELS
      get () {
        return this.$store.state.showDrawer
      },
      set (value) {
        this.$store.commit('setDrawerState', value)
      }
    }
  }
}
</script>

<style lang="sass">
.q-drawer__content
  background-color: #888
.activeDrawer
  background-color: $secondary
.drawerHeader
  background-color: $primary
  position: relative
  height: 160px
.drawerHeader h2
  font-size: 22px
  position: absolute
  bottom: 0px
  left: 15px
  color: white
.times
  position: absolute
  bottom: 35px
  margin-top: 20vh
  margin-left: 40px
.draworBtn
  margin-top: 20px
  background-color: $secondary
</style>
