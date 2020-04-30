import Vue from 'vue'
import Vuex from 'vuex'

// import myMaster from './myMaster'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    showDrawer: false,
    showPreloader: true,
    siteLaunched: false,
    daWaypoint: 'base',
    homyOut: false,
    daToken: ''
  },
  mutations: {
    // increment: state => {
    //     state.counter++;
    // },
    setDrawerState (state, value) { // FOR v-models !!
      state.showDrawer = value
    }
  }
  // modules: {
  //     myMaster
  // },
  // getters: { // for special shit and methods
  //     doubleCounter: state => {
  //         return state.counter * 2;
  //     },
  //     stringCounter: state => {
  //         return state.counter + 'Clicks';
  //     }
  // },

})

export default store
