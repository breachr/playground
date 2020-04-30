import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  return Router
}

// Ye Olde Shite
// import Vue from 'vue'
// import VueRouter from 'vue-router'
//
// import routes from './routes'
//
// Vue.use(VueRouter)
//
// const Router = new VueRouter({
//     /*
//       * NOTE! Change Vue Router mode from quasar.conf.js -> build -> vueRouterMode
//       *
//       * When going with "history" mode, please also make sure "build.publicPath"
//       * is set to something other than an empty string.
//       * Example: '/' instead of ''
//       */
//
//     // Leave as is and change from quasar.conf.js instead!
//     mode: process.env.VUE_ROUTER_MODE,
//     base: "/",
//     scrollBehavior: () => ({ y: 0 }),
//     routes,
//
//     // dont jump to top on route change
//     scrollBehavior (to, from, savedPosition) {
//         // pass
//     }
//
//
// })
//
// export default Router
