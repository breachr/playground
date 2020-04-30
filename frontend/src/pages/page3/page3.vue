<template>
<q-page>

  <div class="daContainer bg1" id="sect1" v-waypoint="{ active: true, callback: onWaypoint }">
    <div class="contentReducer">
      <sect1></sect1>
    </div>
  </div>

  <div class="daContainer bg1" id="sect2" v-waypoint="{ active: true, callback: onWaypoint }">
    <div class="contentReducer">
      <sect2></sect2>
    </div>
  </div>

  <div class="daContainer bg2 withSepa" id="sect3" v-waypoint="{ active: true, callback: onWaypoint }">
    <div class="contentReducer">
      <sect3></sect3>
    </div>
  </div>

  <skew></skew>

  <div class="daContainer bg3 dropShadow down" id="sect4" v-waypoint="{ active: true, callback: onWaypoint }">
    <div class="contentReducer">
      <sect4></sect4>
    </div>
  </div>

  <!-- <s_parallax></s_parallax> -->

  <div class="daContainer bg4 dropShadow" id="sect5" v-waypoint="{ active: true, callback: onWaypoint }">
    <div class="contentReducer">
      <sect5></sect5>
    </div>
  </div>

</q-page>
</template>

<script>
import sect1 from './sect1'
import sect2 from './sect2'
import sect3 from './sect3'
import sect4 from './sect4'
import sect5 from './sect5'

export default {
  components: {
    sect1,
    sect2,
    sect3,
    sect4,
    sect5
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
/* CONTAINER */
.daContainer
  overflow: hidden

  padding: 14vh 15px
  min-height: 120vh

  display: flex
  flex-direction: column
  justify-content: center
  align-items: center
  text-align: center

.contentReducer
  margin-left: auto
  margin-right: auto
  max-width: 1200px

/* SHADOWS */
.withSepa
  position: relative
  z-index: 4
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
