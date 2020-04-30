<template>
<div class="footor">
  <!-- Footer -->
  <q-footer class="bg6">
    <div class="footCont" v-scroll-reveal="{ delay: 0, origin: 'left'}">
      <a class="modaLink" href="www..de" @click.prevent="datenschutzModal = true">Datenschutz</a>
      <a class="modaLink" href="www..de" @click.prevent="impressumModal = true">Impressum</a>
    </div>
    <div class="copyRight" v-scroll-reveal="{ delay: 0, origin: 'right'}">
      <span>Designed and built by</span> <a href="https://www.mymacy.de"><img class="myMLogo" @click="goHome" src="../../statics/logo/mym_logo.svg" alt="myFortress"></a><span>2018 &copy;</span>
    </div>
    <div class="socialLinks">
      <a href="https://www.facebook.com/ma.cy.90">
        <q-icon class="fbLink" name="ion-logo-facebook" v-scroll-reveal="{ delay: 100, origin: 'bottom'}" />
      </a>
      <a href="https://github.com/mymacy">
        <q-icon class="xiLink" name="ion-logo-github" v-scroll-reveal="{ delay: 200, origin: 'bottom'}" />
      </a>
      <a href="https://www.instagram.com/marcelalbrink/">
        <q-icon class="inLink" name="ion-logo-instagram" v-scroll-reveal="{ delay: 300, origin: 'bottom'}" />
      </a>
    </div>
  </q-footer>

  <!--Modals -->
  <q-dialog class="aModal" v-model="datenschutzModal">
    <h4>Datenschutzerklärung:</h4>
    <p>
    Was gehört in die Datenschutzerklärung einer Homepage? Besteht eine Pflicht für alle Betreiber, Datenschutzhinweise unterzubringen? Gerade für Laien sind die Bestimmungen zum Datenschutz im Internet oftmals nur schwer nachzuvollziehen.
    Dieser Ratgeber erläutert, welchen Bestimmungen die Datenschutzerklärung für eine Webseite genügen muss und welche Folgen ein fehlender Datenschutzhinweis nach sich zieht. Ein kostenloses Muster einer Datenschutzerklärung für Webseiten finden Sie im Folgenden ebenfalls.
    Verbraucher haben das Recht zu erfahren, ob, inwieweit und zu welchem Zwecke ihre personenbezogenen Daten erhoben und gespeichert werden, bevor Sie ein entsprechendes Angebot nutzen.
    Dieses Prinzip gilt nicht nur für die Internetauftritte von Unternehmen oder Behörden: Auch private Diensteanbieter sind ihm unterworfen.
    Dies ergibt sich aus dem Telemediengesetz (TMG). § 13 des Gesetzes bestimmt:
    Der Diensteanbieter hat den Nutzer zu Beginn des Nutzungsvorgangs über Art, Umfang und Zwecke der Erhebung und Verwendung personenbezogener Daten […] in allgemein verständlicher Form zu unterrichten, sofern eine solche Unterrichtung nicht bereits erfolgt ist.
    Als „personenbezogene Daten“ gelten nicht nur offensichtlich persönliche Informationen wie Name, Wohnort oder E-Mail-Adresse einer Person, sondern auch deren IP-Adresse oder das Wissen darüber, welche Seiten sie im Internet besucht. Jede Website erhebt in diesem Sinne also personenbezogene Daten über ihre Nutzer.
    </p>
    <q-btn color="primary" @click="datenschutzModal = false" label="Close" />
  </q-dialog>
  <q-dialog class="aModal" v-model="impressumModal">
    <h4>Basic Modal</h4>
    <q-btn color="primary" @click="impressumModal = false" label="Close" />
  </q-dialog>

</div>
</template>

<script>
import {
  openURL
} from 'quasar'

// import preLoader from '../myM/preLoader.vue'
// import heador from './header/header'

export default {
  components: {
    // drawor
  },
  data () {
    return {
      datenschutzModal: false,
      impressumModal: false
    }
  },
  methods: {
    openURL,
    goHome () {
      location.reload()
    }
  },
  // COOKIE Notification
  mounted: function () {
    this.$q.notify({
      message: 'www.kfz-albrink.de benutzt Cookies um Ihnen als Nutzer die bestmögliche Erfahrung bieten zu können. Wenn sie damit einverstanden sind dann klicken Sie bitte auf Ja',
      timeout: 0, // in milliseconds; 0 means no timeout
      color: 'secondary',
      textColor: 'black', // if default 'white' doesn't fits
      icon: 'info',
      position: 'bottom', // 'top', 'left', 'bottom-left' etc
      actions: [{
        label: 'Ja',
        noDismiss: true, // optional, v0.15.11+
        handler: () => {
          console.log('acting')
        }
      },
      {
        label: 'Nein',
        handler: () => {
          console.log('dismissed')
        }
      }
      ]
    })
  }
}
</script>

<style lang="sass">
/* FOOTER ------------------------------------------------*/
footer
  z-index: 2 !important
  -webkit-box-shadow: inset 0px 19px 44px -8px rgba(0, 0, 0, 0.64) !important
  -moz-box-shadow: inset 0px 19px 44px -8px rgba(0, 0, 0, 0.64) !important
  box-shadow: inset 0px 19px 44px -8px rgba(0, 0, 0, 0.64) !important
  /* height: 25vh; */
  padding: 30px
  display: flex
  flex-direction: column
  justify-content: center
  align-items: center
  overflow: hidden
  z-index: 3
footer a,
footer span
  text-decoration: none
  color: #a6a6a6
  margin: 0px 3px
.modaLink
  padding: 30px 5px
.myMLogo
  position: relative
  width: 55px
  top: 6px
.copyRight
  margin-top: 10px
.socialLinks
  margin-top: 15px
  font-size: 25px
.fbLink
  transition: color 0.3s linear
  margin-right: 10px
.fbLink:hover
  color: #3D68AE
.xiLink
  transition: color 0.3s linear
.xiLink:hover
  color: #282D31
.inLink
  transition: color 0.3s linear
  margin-left: 10px
.inLink:hover
  color: #DC3076
/* BACK TO TOP */
.goHomeBtn
  z-index: 10

/* MODALS ------------------------------------------------*/
</style>
