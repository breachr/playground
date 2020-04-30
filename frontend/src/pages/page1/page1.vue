<template>
<q-page>

  <div class="daContainer bg1 dropShadow down" id="sect1" v-waypoint="{ active: true, callback: onWaypoint }">
    <sect1></sect1>
  </div>

  <div class="daContainer bg2" id="sect2" v-waypoint="{ active: true, callback: onWaypoint, options: intersectionOptions}">
    <sect2></sect2>
  </div>

  <div class="daContainer bg3" id="sect3" v-waypoint="{ active: true, callback: onWaypoint, options: intersectionOptions}">
    <sect3></sect3>
  </div>

  <div class="daContainer bg4" id="sect4" v-waypoint="{ active: true, callback: onWaypoint, options: intersectionOptions}">
    <sect4></sect4>
  </div>

  <div class="daContainer bg4" id="sect5" v-waypoint="{ active: true, callback: onWaypoint, options: intersectionOptions}">
    <sect5></sect5>
  </div>

</q-page>
</template>

<script>
import sect1 from './sect1/sect1'
import sect2 from './sect2/sect2'
import sect3 from './sect3/sect3'
import sect4 from './sect4/sect4'
import sect5 from './sect5/sect5'

export default {
  components: {
    sect1,
    sect2,
    sect3,
    sect4,
    sect5
  },
  data: () => ({
    intersectionOptions: {
      root: null,
      rootMargin: '0px 0px 0px 0px',
      threshold: [0, 1] // [0.25, 0.75] if you want a 25% offset!
    } // https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
  }),
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
/* CONTAINER */
// .daContainer
//   min-height: 1000px
//   overflow: hidden
//   margin-left: auto
//   margin-right: auto
//   max-width: 1920px

// Shadows
.dropShadow
  position: relative
  z-index: 2
  -webkit-box-shadow: 0px 3px 31px 8px rgba(0, 0, 0, 0.64)
  -moz-box-shadow: 0px 3px 31px 8px rgba(0, 0, 0, 0.64)
  box-shadow: 0px 3px 31px 8px rgba(0, 0, 0, 0.64)
.dropShadow.up
  -webkit-box-shadow: 0px -8px 50px -9px rgba(0, 0, 0, 0.64)
  -moz-box-shadow: 0px -8px 50px -9px rgba(0, 0, 0, 0.64)
  box-shadow: 0px -10px 50px -9px rgba(0, 0, 0, 0.64)
.dropShadow.down
  -webkit-box-shadow: 0px 17px 50px -9px rgba(0, 0, 0, 0.64)
  -moz-box-shadow: 0px 17px 50px -9px rgba(0, 0, 0, 0.64)
  box-shadow: 0px 17px 50px -9px rgba(0, 0, 0, 0.64)
</style>
