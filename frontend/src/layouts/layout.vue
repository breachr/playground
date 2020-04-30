<template>
<q-layout view="hHh Lpr fff">
  <div id="homy" v-waypoint="{active: true, callback: onWaypoint}"></div>

  <!-- PRELOADER -->
  <!-- <preloader></preloader> -->

  <!-- HEADER -->
  <heador></heador>

  <!--  PAGES -->
  <q-page-container>
    <transition appear enter-active-class="animated fadeInLeft" leave-active-class="animated fadeOutRight" mode="out-in" duration="900">
      <router-view />
    </transition>
  </q-page-container>

  <!-- FOOTER -->
  <footor></footor>

  <!-- BACK TO TOP -->
  <q-page-scroller round position="bottom-right" :scroll-offset="150" :duration="400" :offset="[18, 18]">
    <q-btn fab icon="keyboard_arrow_up" color="primary" />
  </q-page-scroller>

</q-layout>
</template>

<script>
// import preloader from './preloader/preloader'
import heador from './header/header'
// drawer is inside header!
import footor from './footer/footer'

export default {
  components: {
    // preloader,
    heador,
    footor
  },
  methods: {
    onWaypoint ({
      going,
      direction,
      el
    }) {
      if (going === 'in') {
        console.log(el.id)
        this.$store.state.daWaypoint = el.id
      }
      if (el.id === 'homy') {
        if (going === 'out') {
          this.$store.state.homyOut = true
        } else {
          this.$store.state.homyOut = false
        }
      }
    }
  }
}
</script>

<style lang="sass">

// /* LAYOUT ------------------------------------------------*/
.q-layout
  overflow: hidden
  max-width: 1920px
  margin-left: auto
  margin-right: auto

// /* BACK TO TOP -------------------------------------------*/
.goHomeBtn
  z-index: 10
  margin: 0 15px 15px 0

</style>
