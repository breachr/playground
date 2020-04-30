<template>
<div class="sectContainer bg2">
  <h3 class="mylink">Template</h3>
  <!-- <downfador acti="true"></downfador> -->
</div>
</template>

<script>
// import downfador from './i_simple_token'
export default {
  components: {
    // downfador
    // sect2,
    // sect3,
    // sect4,
    // sect5
  },
  data: () => ({
    iamData: 'lol',
    imgs: [
      'https://via.placeholder.com/450.png/',
      'https://via.placeholder.com/300.png/',
      'https://via.placeholder.com/150.png/'
    ]
  }),
  methods: {
    doGallery () {
      console.log('immel')
    }
  }
}
</script>

<style scoped lang="sass">
.sectContainer
  height: 2000px
  padding-top: 20px
</style>
