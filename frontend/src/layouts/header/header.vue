<template>
<q-header class="headerBar bg-primary" :class="{outSide: outSider, 'shadow-0': !outSider}">
  <!-- LOGO  -->
  <img class="myLogo" @click="goHome" src="../../statics/logo/logo_icon_only_setted.svg" alt="myFortress">

  <!-- QUICKLAUNCH -->
  <div class="quicklaunch">
    <q-btn class="quickBtn" :class="{outSide: !outSider}" flat icon="email"       @click="openURL('mailto:info@kfz-albrink.de')" />
    <q-btn class="quickBtn" :class="{outSide: !outSider}" flat icon="location_on" @click="openURL('https://www.google.com/maps/dir/?api=1&destination=Albrink+Kfz-Meisterbetrieb,+Lagesche+Str.+105A,+32108+Bad+Salzuflen&travelmode=driving')" />
    <q-btn class="quickBtn" :class="{outSide: !outSider}" flat icon="phone"       @click="openURL('tel:+495222-21069')" />
  </div>

  <!-- NAVIGATION -->
  <div class="navigation gt-md">
    <q-tabs :value="selectedTab">
      <q-tab class="navBtn" :class="{outSide: !outSider}" label="Home"      name="sect1" v-scroll-to="'#sect1'" />
      <q-tab class="navBtn" :class="{outSide: !outSider}" label="Leistung"  name="sect2" v-scroll-to="'#sect2'" />
      <q-tab class="navBtn" :class="{outSide: !outSider}" label="Team"      name="sect3" v-scroll-to="'#sect3'" />
      <q-tab class="navBtn" :class="{outSide: !outSider}" label="Kontakt"   name="sect4" v-scroll-to="'#sect4'" />
    </q-tabs>
  </div>

  <!-- HAMBURGER -->
  <q-btn :class="{outSide: !outSider}" class="mobBtn lt-lg" flat dense @click="toggleDaDrawer">
    <button class="hamburger hamburger--collapse" :class="{'is-active': showDrawer}" type="button">
      <span class="hamburger-box">
        <span class="hamburger-inner"></span>
      </span>
    </button>
  </q-btn>

  <!-- DRAWER -->
  <drawor></drawor>
</q-header>
</template>

<script>
import {
  openURL
} from 'quasar' // for tel links etc.

import drawor from '../drawer/drawer'

export default {
  components: {
    drawor
  },
  methods: {
    openURL,
    toggleDaDrawer () {
      this.$store.state.showDrawer = !this.$store.state.showDrawer
    },
    goHome () {
      location.reload()
    }
  },
  computed: { // basic states
    selectedTab () { // selected tab from store
      return this.$store.state.daWaypoint
    },
    outSider () { // header is outside of start
      return this.$store.state.homyOut
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
/* Header ------------------------------------------------*/
.headerBar
  width: 100vw
  height: 80px
  transition: box-shadow 0.6s linear, height 0.4s linear
  display: grid
  grid-template-columns: 0% 80% 20%
  /*                LOGO ^ QUICK ^  NAV ^ HAMBUR ^   */
  grid-template-rows: 100%
.headerBar.outSide
  height: 48px
  box-shadow: 7px 28px 54px -6px rgba(0,0,0,0.5)

.myLogo
  margin: 3px auto
  height: 0%

@media only screen and (min-width: 769px)
  .headerBar
    grid-template-columns: 30% 55% 15%
  .myLogo
    height: 90%
@media only screen and (min-width: 1024px)
  .headerBar
    grid-template-columns: 25% 20% 55% 0%
  .myLogo
    height: 90%

.quickBtn
  font-size: 17px !important
  height: 100%
  width: 33%
  transition: font-size 0.4s linear
.quickBtn.outSide
  font-size: 22px !important

.navigation
  margin: 0px auto
.navBtn
  height: 48px
  transition: height 0.4s linear
.navBtn.outSide
  height: 80px

/* Hamburger ---------------------------------------------*/
.hamburger
  z-index: 3001
  padding: 0px
  display: inline-block
  cursor: pointer
  transition-property: opacity, filter
  transition-duration: 0.15s
  transition-timing-function: linear
  font: inherit
  color: inherit
  text-transform: none
  background-color: transparent
  border: 0
  margin: 0
  overflow: visible
.hamburger:hover
  opacity: 0.7
.hamburger-box
  /* CHANGE THIS */
  width: 25px
  height: 27px
  display: inline-block
  position: relative
.hamburger-inner
  display: block
  top: 50%
  margin-top: -2px
.hamburger-inner,
.hamburger-inner::before,
.hamburger-inner::after
  /* AND THIS */
  width: 25px
  height: 3px
  /* BACKGROUND */
  background-color: white
  position: absolute
  /* z-index: 3000 */
  border-radius: 5px
  transition-property: transform
  transition-duration: 0.25s
  transition-timing-function: ease
.hamburger-inner::before,
.hamburger-inner::after
  content: ""
  display: block
.hamburger-inner::before
  /* position: relative */
  top: -10px
.hamburger-inner::after
  /* position: relative */
  bottom: -10px
// hamburger--arrowturn- -----------------------------------
.hamburger--arrowturn.is-active .hamburger-inner
  transform: rotate(-180deg)
.hamburger--arrowturn.is-active .hamburger-inner::before
  transform: translate3d(6px, 0, 0) rotate(45deg) scale(0.7, 1)
.hamburger--arrowturn.is-active .hamburger-inner::after
  transform: translate3d(6px, 0, 0) rotate(-45deg) scale(0.7, 1)
// hamburger--arrowturn-r ----------------------------------
.hamburger--arrowturn-r.is-active .hamburger-inner
  transform: rotate(-180deg)
.hamburger--arrowturn-r.is-active .hamburger-inner::before
  transform: translate3d(-8px, 0, 0) rotate(-45deg) scale(0.7, 1)
.hamburger--arrowturn-r.is-active .hamburger-inner::after
  transform: translate3d(-8px, 0, 0) rotate(45deg) scale(0.7, 1)
// hamburger--collapse -------------------------------------
.hamburger--collapse .hamburger-inner
  top: auto
  bottom: 0
  transition-duration: 0.13s
  transition-delay: 0.13s
  transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--collapse .hamburger-inner::after
  top: -20px
  transition: top 0.2s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), opacity 0.1s linear
.hamburger--collapse .hamburger-inner::before
  transition: top 0.12s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), transform 0.13s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--collapse.is-active .hamburger-inner
  transform: translate3d(0, -10px, 0) rotate(-45deg)
  transition-delay: 0.22s
  transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1)
.hamburger--collapse.is-active .hamburger-inner::after
  top: 0
  opacity: 0
  transition: top 0.2s cubic-bezier(0.33333, 0, 0.66667, 0.33333), opacity 0.1s 0.22s linear
.hamburger--collapse.is-active .hamburger-inner::before
  top: 0
  transform: rotate(-90deg)
  transition: top 0.1s 0.16s cubic-bezier(0.33333, 0, 0.66667, 0.33333), transform 0.13s 0.25s cubic-bezier(0.215, 0.61, 0.355, 1)
// hamburger--collapse-r -----------------------------------
.hamburger--collapse-r .hamburger-inner
  top: auto
  bottom: 0
  transition-duration: 0.13s
  transition-delay: 0.13s
  transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--collapse-r .hamburger-inner::after
  top: -20px
  transition: top 0.2s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), opacity 0.1s linear
.hamburger--collapse-r .hamburger-inner::before
  transition: top 0.12s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), transform 0.13s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--collapse-r.is-active .hamburger-inner
  transform: translate3d(0, -10px, 0) rotate(45deg)
  transition-delay: 0.22s
  transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1)
.hamburger--collapse-r.is-active .hamburger-inner::after
  top: 0
  opacity: 0
  transition: top 0.2s cubic-bezier(0.33333, 0, 0.66667, 0.33333), opacity 0.1s 0.22s linear
.hamburger--collapse-r.is-active .hamburger-inner::before
  top: 0
  transform: rotate(90deg)
  transition: top 0.1s 0.16s cubic-bezier(0.33333, 0, 0.66667, 0.33333), transform 0.13s 0.25s cubic-bezier(0.215, 0.61, 0.355, 1)
// hamburger--elastic --------------------------------------
.hamburger--elastic .hamburger-inner
  top: 2px
  transition-duration: 0.275s
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55)
.hamburger--elastic .hamburger-inner::before
  top: 10px
  transition: opacity 0.125s 0.275s ease
.hamburger--elastic .hamburger-inner::after
  top: 20px
  transition: transform 0.275s cubic-bezier(0.68, -0.55, 0.265, 1.55)
.hamburger--elastic.is-active .hamburger-inner
  transform: translate3d(0, 10px, 0) rotate(135deg)
  transition-delay: 0.075s
.hamburger--elastic.is-active .hamburger-inner::before
  transition-delay: 0s
  opacity: 0
.hamburger--elastic.is-active .hamburger-inner::after
  transform: translate3d(0, -20px, 0) rotate(-270deg)
  transition-delay: 0.075s
// hamburger--elastic-r ------------------------------------
.hamburger--elastic-r .hamburger-inner
  top: 2px
  transition-duration: 0.275s
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55)
.hamburger--elastic-r .hamburger-inner::before
  top: 10px
  transition: opacity 0.125s 0.275s ease
.hamburger--elastic-r .hamburger-inner::after
  top: 20px
  transition: transform 0.275s cubic-bezier(0.68, -0.55, 0.265, 1.55)
.hamburger--elastic-r.is-active .hamburger-inner
  transform: translate3d(0, 10px, 0) rotate(-135deg)
  transition-delay: 0.075s
.hamburger--elastic-r.is-active .hamburger-inner::before
  transition-delay: 0s
  opacity: 0
.hamburger--elastic-r.is-active .hamburger-inner::after
  transform: translate3d(0, -20px, 0) rotate(270deg)
  transition-delay: 0.075s
// hambuer--emphatic ---------------------------------------
.hamburger--emphatic
  overflow: hidden
.hamburger--emphatic .hamburger-inner
  transition: background-color 0.125s 0.175s ease-in
.hamburger--emphatic .hamburger-inner::before
  left: 0
  transition: transform 0.125s cubic-bezier(0.6, 0.04, 0.98, 0.335), top 0.05s 0.125s linear, left 0.125s 0.175s ease-in
.hamburger--emphatic .hamburger-inner::after
  top: 10px
  right: 0
  transition: transform 0.125s cubic-bezier(0.6, 0.04, 0.98, 0.335), top 0.05s 0.125s linear, right 0.125s 0.175s ease-in
.hamburger--emphatic.is-active .hamburger-inner
  transition-delay: 0s
  transition-timing-function: ease-out
  background-color: transparent
.hamburger--emphatic.is-active .hamburger-inner::before
  left: -80px
  top: -80px
  transform: translate3d(80px, 80px, 0) rotate(45deg)
  transition: left 0.125s ease-out, top 0.05s 0.125s linear, transform 0.125s 0.175s cubic-bezier(0.075, 0.82, 0.165, 1)
.hamburger--emphatic.is-active .hamburger-inner::after
  right: -80px
  top: -80px
  transform: translate3d(-80px, 80px, 0) rotate(-45deg)
  transition: right 0.125s ease-out, top 0.05s 0.125s linear, transform 0.125s 0.175s cubic-bezier(0.075, 0.82, 0.165, 1)
// hamburger--emphatic-r -----------------------------------
.hamburger--emphatic-r
  overflow: hidden
.hamburger--emphatic-r .hamburger-inner
  transition: background-color 0.125s 0.175s ease-in
.hamburger--emphatic-r .hamburger-inner::before
  left: 0
  transition: transform 0.125s cubic-bezier(0.6, 0.04, 0.98, 0.335), top 0.05s 0.125s linear, left 0.125s 0.175s ease-in
.hamburger--emphatic-r .hamburger-inner::after
  top: 10px
  right: 0
  transition: transform 0.125s cubic-bezier(0.6, 0.04, 0.98, 0.335), top 0.05s 0.125s linear, right 0.125s 0.175s ease-in
.hamburger--emphatic-r.is-active .hamburger-inner
  transition-delay: 0s
  transition-timing-function: ease-out
  background-color: transparent
.hamburger--emphatic-r.is-active .hamburger-inner::before
  left: -80px
  top: 80px
  transform: translate3d(80px, -80px, 0) rotate(-45deg)
  transition: left 0.125s ease-out, top 0.05s 0.125s linear, transform 0.125s 0.175s cubic-bezier(0.075, 0.82, 0.165, 1)
.hamburger--emphatic-r.is-active .hamburger-inner::after
  right: -80px
  top: 80px
  transform: translate3d(-80px, -80px, 0) rotate(45deg)
  transition: right 0.125s ease-out, top 0.05s 0.125s linear, transform 0.125s 0.175s cubic-bezier(0.075, 0.82, 0.165, 1)
// hamburger--slider ---------------------------------------
.hamburger--slider .hamburger-inner
  top: 2px
.hamburger--slider .hamburger-inner::before
  top: 10px
  transition-property: transform, opacity
  transition-timing-function: ease
  transition-duration: 0.15s
.hamburger--slider .hamburger-inner::after
  top: 20px
.hamburger--slider.is-active .hamburger-inner
  transform: translate3d(0, 10px, 0) rotate(45deg)
.hamburger--slider.is-active .hamburger-inner::before
  transform: rotate(-45deg) translate3d(-5.71429px, -6px, 0)
  opacity: 0
.hamburger--slider.is-active .hamburger-inner::after
  transform: translate3d(0, -20px, 0) rotate(-90deg)
// hamburger--slider-r -------------------------------------
.hamburger--slider-r .hamburger-inner
  top: 2px
.hamburger--slider-r .hamburger-inner::before
  top: 10px
  transition-property: transform, opacity
  transition-timing-function: ease
  transition-duration: 0.15s
.hamburger--slider-r .hamburger-inner::after
  top: 20px
.hamburger--slider-r.is-active .hamburger-inner
  transform: translate3d(0, 10px, 0) rotate(-45deg)
.hamburger--slider-r.is-active .hamburger-inner::before
  transform: rotate(45deg) translate3d(5.71429px, -6px, 0)
  opacity: 0
.hamburger--slider-r.is-active .hamburger-inner::after
  transform: translate3d(0, -20px, 0) rotate(90deg)
// hamburger--spin -----------------------------------------
.hamburger--spin .hamburger-inner
  transition-duration: 0.22s
  transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spin .hamburger-inner::before
  transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in
.hamburger--spin .hamburger-inner::after
  transition: bottom 0.1s 0.25s ease-in, transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spin.is-active .hamburger-inner
  transform: rotate(225deg)
  transition-delay: 0.12s
  transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1)
.hamburger--spin.is-active .hamburger-inner::before
  top: 0
  opacity: 0
  transition: top 0.1s ease-out, opacity 0.1s 0.12s ease-out
.hamburger--spin.is-active .hamburger-inner::after
  bottom: 0
  transform: rotate(-90deg)
  transition: bottom 0.1s ease-out, transform 0.22s 0.12s cubic-bezier(0.215, 0.61, 0.355, 1)
// hamburger--spin-r ---------------------------------------
.hamburger--spin-r .hamburger-inner
  transition-duration: 0.22s
  transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spin-r .hamburger-inner::before
  transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in
.hamburger--spin-r .hamburger-inner::after
  transition: bottom 0.1s 0.25s ease-in, transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spin-r.is-active .hamburger-inner
  transform: rotate(-225deg)
  transition-delay: 0.12s
  transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1)
.hamburger--spin-r.is-active .hamburger-inner::before
  top: 0
  opacity: 0
  transition: top 0.1s ease-out, opacity 0.1s 0.12s ease-out
.hamburger--spin-r.is-active .hamburger-inner::after
  bottom: 0
  transform: rotate(90deg)
  transition: bottom 0.1s ease-out, transform 0.22s 0.12s cubic-bezier(0.215, 0.61, 0.355, 1)
// hamburger--spring ---------------------------------------
.hamburger--spring .hamburger-inner
  top: 2px
  transition: background-color 0s 0.13s linear
.hamburger--spring .hamburger-inner::before
  top: 10px
  transition: top 0.1s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), transform 0.13s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spring .hamburger-inner::after
  top: 20px
  transition: top 0.2s 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1), transform 0.13s cubic-bezier(0.55, 0.055, 0.675, 0.19)
.hamburger--spring.is-active .hamburger-inner
  transition-delay: 0.22s
  background-color: transparent
.hamburger--spring.is-active .hamburger-inner::before
  top: 0
  transition: top 0.1s 0.15s cubic-bezier(0.33333, 0, 0.66667, 0.33333), transform 0.13s 0.22s cubic-bezier(0.215, 0.61, 0.355, 1)
  transform: translate3d(0, 10px, 0) rotate(45deg)
.hamburger--spring.is-active .hamburger-inner::after
  top: 0
  transition: top 0.2s cubic-bezier(0.33333, 0, 0.66667, 0.33333), transform 0.13s 0.22s cubic-bezier(0.215, 0.61, 0.355, 1)
  transform: translate3d(0, 10px, 0) rotate(-45deg)
// hamburger--vortex ---------------------------------------
.hamburger--vortex .hamburger-inner
  transition-duration: 0.2s
  transition-timing-function: cubic-bezier(0.19, 1, 0.22, 1)
.hamburger--vortex .hamburger-inner::before,
.hamburger--vortex .hamburger-inner::after
  transition-duration: 0s
  transition-delay: 0.1s
  transition-timing-function: linear
.hamburger--vortex .hamburger-inner::before
  transition-property: top, opacity
.hamburger--vortex .hamburger-inner::after
  transition-property: bottom, transform
.hamburger--vortex.is-active .hamburger-inner
  transform: rotate(765deg)
  transition-timing-function: cubic-bezier(0.19, 1, 0.22, 1)
.hamburger--vortex.is-active .hamburger-inner::before,
.hamburger--vortex.is-active .hamburger-inner::after
  transition-delay: 0s
.hamburger--vortex.is-active .hamburger-inner::before
  top: 0
  opacity: 0
.hamburger--vortex.is-active .hamburger-inner::after
  bottom: 0
  transform: rotate(90deg)
// hamburger--vortex-r -------------------------------------
.hamburger--vortex-r .hamburger-inner
  transition-duration: 0.2s
  transition-timing-function: cubic-bezier(0.19, 1, 0.22, 1)
.hamburger--vortex-r .hamburger-inner::before,
.hamburger--vortex-r .hamburger-inner::after
  transition-duration: 0s
  transition-delay: 0.1s
  transition-timing-function: linear
.hamburger--vortex-r .hamburger-inner::before
  transition-property: top, opacity
.hamburger--vortex-r .hamburger-inner::after
  transition-property: bottom, transform
.hamburger--vortex-r.is-active .hamburger-inner
  transform: rotate(-765deg)
  transition-timing-function: cubic-bezier(0.19, 1, 0.22, 1)
.hamburger--vortex-r.is-active .hamburger-inner::before,
.hamburger--vortex-r.is-active .hamburger-inner::after
  transition-delay: 0s
.hamburger--vortex-r.is-active .hamburger-inner::before
  top: 0
  opacity: 0
.hamburger--vortex-r.is-active .hamburger-inner::after
  bottom: 0
  transform: rotate(-90deg)

</style>
