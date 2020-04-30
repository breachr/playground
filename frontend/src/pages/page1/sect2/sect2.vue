<template>
<div class="sectContainer bg2">
  <h3 class="mylink">Template</h3>
</div>
</template>

<script>

export default {
  components: {
    // gallery
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
