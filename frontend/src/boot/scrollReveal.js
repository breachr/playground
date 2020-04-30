import scrollReveal from 'vue-scroll-reveal'

export default ({ Vue }) => {
  Vue.use(scrollReveal, {
    class: 'v-scroll-reveal', // A CSS class applied to elements with the v-scroll-reveal directive; useful for animation overrides.
    duration: 1200,
    scale: 1,
    opacity: 0,
    distance: '800px',
    mobile: true,
    viewFactor: 0.3 // how much % must be sivible to be considerded
  })
}
