<template>
<div class="dabg">
  <figure class="snip1554" :class="{active: launched}">
    <!-- <img @load="imageLoaded" src="https://images7.alphacoders.com/411/thumb-1920-411820.jpg" alt="sample104" /> -->
    <img @load="imageLoaded" src="https://www.kfz-koethmann.de/typo3temp/_processed_/csm_u74_0136619_fa1_lc_200007w3t_2000x789_slider_3eb57e992c.jpg" alt="sample104" />

    <figcaption class="heador text-center">

      <div class="bigLogoWrapper">
        <transition name="fadeMove">
          <div v-if="bigLogo" class="bigLogo">
            <h2>KFZ Meisterbetrieb</h2>
            <h2>Rolf Albrink</h2>
            <img src="../../statics/logo/mym_logo.svg" alt="">
            <q-btn id="home" @click="openURL('tel:+495222-21069')" color="secondary" icon="phone" label="MO-FR 8-17 Uhr" />
            <div class="downfador"></div>
          </div>
        </transition>
      </div>

      <div class="smallLogoWrapper">
        <transition name="fadeReverse">
          <div v-if="smallLogo" class="smallLogo">
            <h2 id="home">KFZ-Albrink</h2>
          </div>
        </transition>
      </div>

    </figcaption>
  </figure>
</div>
</template>

<script>
import {
  openURL
} from 'quasar'
export default {
  data () {
    return {
      smallLogo: false,
      // bigLogo: true,
      launched: false
    }
  },
  methods: {
    openURL,
    imageLoaded () {
      this.$store.state.showPreloader = false
      var that = this // need to pass this as setimeout takes window!
      setTimeout(function () {
        that.launched = true
        console.log(that)
      }, 2000)
    }
  },
  computed: {
    bigLogo () {
      return (this.$store.state.daWaypoint === 'homy')
    }
  }
}
</script>

<style scoped>
#home {
  margin-top: 15px;
}

#daBG {}

.dabg {
  height: 100vh;
  background-color: black;
  max-width: 100%;
}

.bgwWelcome {}

.snip1554 {
  background-color: #3C4858;
  color: #ffffff;
  display: inline-block;
  /* margin: 8px; */

  overflow: hidden;
  position: relative;
  text-align: left;
  width: 100vw;
  height: 100%;
  margin: 0px;
}

.snip1554 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.85s ease;
  transition: all 0.85s ease;
}

.snip1554:after {
  background-color: white;
  opacity: 0.6;
  top: 0;
  bottom: 0;
  content: '';
  left: -150%;
  position: absolute;
  width: 400px;
  box-shadow: 0 0 100px white;
  -webkit-transform: skew(-20deg);
  transform: skew(-20deg);
  -webkit-transition: all 0.6s ease;
  transition: all 0.9s ease;
}

.snip1554 img {
  vertical-align: top;
  max-width: 300%;
  min-height: 100vh;
  backface-visibility: hidden;
}

.snip1554 figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
  line-height: 1em;
  opacity: 0;
  transition: opacity 2s ease-in;
}

figcaption .bigLogoWrapper {
  position: absolute;
  left: 50%;
  top: 55vh;
  transform: translate(-50%, -50%);

}

figcaption .smallLogoWrapper {
  position: absolute;
  left: 50%;
  top: 85vh;
  width: 100%;
  transform: translate(-50%, -50%);
}

.heador h2 {
  margin: 10px 0px;
  font-weight: bold;
  color: white;
  margin-bottom: 30px;
}

.heador img {
  width: 30vw;
  min-height: 10px;
  max-width: 200px !important;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 15px;
}

.snip1554 h3 {
  position: absolute;
  left: 10px;
  bottom: 10px;
  font-size: 1.4em;
  font-weight: 400;
  line-height: 1.1em;
  margin: 0;
  text-transform: uppercase;
}

.snip1554.active>img {
  opacity: 0.4;
  -webkit-filter: grayscale(50%);
  filter: grayscale(50%);
}

.snip1554.active:after {
  left: 200%;
}

.snip1554.active figcaption {
  opacity: 1;
}

#animations {}

.fade-enter {
  opacity: 0;
}

.fade-leave-active {
  transition: opacity 0.5s linear, transform 0.3s linear;
  /* transform: translate(-100%, 0%); */
  opacity: 0;
}

.fadeMove-enter {
  opacity: 0;
  transform: translate(0px, 50px);
}

.fadeMove-leave-active {
  transform: translate(0px, 50px);
  transition: opacity 0.5s linear, transform 0.3s linear;
  /* transform: translate(-100%, 0%); */
  opacity: 0;
}

.fadeReverse-enter {
  opacity: 0;
  transform: translate(0px, -50px);
}

.fadeReverse-leave-active {
  transform: translate(0px, -50px);
  transition: opacity 0.5s linear, transform 0.3s linear;
  /* transform: translate(-100%, 0%); */
  opacity: 0;
}

.downfador {
  position: relative;
  top: 0;
  left: 50%;
  width: 15px;
  height: 15px;
  margin-left: -12px;
  margin-top: 15px;
  border-left: 2px solid #fff;
  border-bottom: 2px solid #fff;
  -webkit-transform: rotate(-45deg);
  transform: rotate(-45deg);
  -webkit-animation: sdb05 2s infinite;
  animation: sdb05 2s infinite;
  box-sizing: border-box;
}

@-webkit-keyframes sdb05 {
  0% {
    -webkit-transform: rotate(-45deg) translate(0, 0);
    opacity: 0;
  }

  50% {
    opacity: 1;
  }

  100% {
    -webkit-transform: rotate(-45deg) translate(-20px, 20px);
    opacity: 0;
  }
}

@keyframes sdb05 {
  0% {
    transform: rotate(-45deg) translate(0, 0);
    opacity: 0;
  }

  50% {
    opacity: 1;
  }

  100% {
    transform: rotate(-45deg) translate(-20px, 20px);
    opacity: 0;
  }
}
</style>
