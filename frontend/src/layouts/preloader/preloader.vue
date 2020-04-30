<template>
<div class="preloader">
  <!-- PRELOAD DEACTIVTOR | PUT ANY PIC FROM PAGE IN HERE-->
  <img class="deactivator" @load="imageLoaded" src="https://images7.alphacoders.com/411/thumb-1920-411820.jpg" alt="sample104" />

  <transition name="fade">
    <div v-if="!fullHide" class="preLoadBg">
      <transition name="fade" @after-leave="fullHide = !fullHide">
        <div v-if="showPreloader" class="preLoadContent">
          <!-- <h2>Bitte warten..</h2> -->
          <!-- <q-spinner color="secondary" :size="50" /> -->
          <!-- <q-spinner-audio color="primary" size="2em" /> -->
          <!-- <q-spinner-audio color="primary" size="2em" /> -->
          <!-- <q-spinner-ball color="primary" size="2em" /> -->
          <!-- <q-spinner-bars color="primary" size="2em" /> -->
          <!-- <q-spinner-comment color="primary" size="2em" /> -->
          <!-- <q-spinner-cube color="primary" size="2em" /> -->
          <!-- <q-spinner-dots color="primary" size="2em" /> -->
          <!-- <q-spinner-facebook color="primary" size="2em" /> -->
          <!-- <q-spinner-gears color="primary" size="2em" /> -->
          <!-- <q-spinner-grid color="primary" size="2em" /> -->
          <!-- <q-spinner-hearts color="primary" size="2em" /> -->
          <!-- <q-spinner-hourglass color="primary" size="2em" /> -->
          <!-- <q-spinner-infinity color="primary" size="2em" /> -->
          <!-- <q-spinner-ios color="primary" size="2em" /> -->
          <!-- <q-spinner-oval color="primary" size="2em" /> -->
          <!-- <q-spinner-pie color="primary" size="2em" /> -->
          <!-- <q-spinner-puff color="primary" size="2em" /> -->
          <!-- <q-spinner-radio color="primary" size="2em" /> -->
          <!-- <q-spinner-rings color="primary" size="2em" /> -->
          <!-- <q-spinner-tail color="primary" size="2em" /> -->
        </div>
      </transition>
    </div>
  </transition>
</div>
</template>

<script>
export default {
  data () {
    return {
      fullHide: false, // this kicks in to first hide the spinner then the background!
      showPreloader: true
    }
  },
  methods: {
    imageLoaded () {
      this.$store.state.showPreloader = false
      this.showPreloader = false
      var that = this // need to pass this as setimeout takes window!
      setTimeout(function () {
        that.$store.state.siteLaunched = true
      }, 2000)
    }
  },
  computed: { // basic watch - could chain events here
    showPreloaders () {
      return this.$store.state.showPreloader
    }
  }
}
</script>

<style lang="sass">
.deactivator
  display: none
.preLoadBg
  position: absolute
  height: 100%
  width: 100%
  z-index: 9000
  background-color: black
  overflow-x: hidden
.preLoadContent
  position: absolute
  left: 50%
  top: 50vh
  transform: translate(-50%, -50%)
</style>
