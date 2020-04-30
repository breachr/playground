<template>
<div class="">
  <h3>Unsere Arbeit</h3>
  <p class="overCards lighted">Quisque non erat mi. Etiam congue et augue sed tempus. Aenean sed ipsum luctus, scelerisque ipsum nec, iaculis justo. Sed at vestibulum purus, sit amet viverra diam. Nulla ac nisi rhoncus,</p>
  <div class="demCards row">
    <div v-scroll-reveal.reset="{ delay: 0, origin: 'bottom'}" class="cardWrapper col-sm-12 col-md-4">
      <q-card class="anItem">
        <q-icon class="cardIcon text-secondary" name="security" />
        <h4 class="cardHead">Zuverlässig</h4>
        <p class="cardText lighted">Sie können beruhigt losfahren denn wir arbeiten sorgfältig und mit Liebe zum Detail</p>
      </q-card>
    </div>
    <div v-scroll-reveal.reset="{ delay: 300, origin: 'bottom'}" class="cardWrapper col-sm-12 col-md-4">
      <q-card class="anItem">
        <q-icon class="cardIcon text-secondary" name="fast_forward" />
        <h4 class="cardHead">Zuverlässig</h4>
        <p class="cardText lighted">Sie können beruhigt losfahren denn wir arbeiten sorgfältig und mit Liebe zum Detail</p>
      </q-card>
    </div>
    <div v-scroll-reveal.reset="{ delay: 600, origin: 'bottom'}" class="cardWrapper col-sm-12 col-md-4">
      <q-card class="anItem">
        <q-icon class="cardIcon text-secondary" name="attach_money" />
        <h4 class="cardHead">Zuverlässig</h4>
        <p class="cardText lighted">Sie können beruhigt losfahren denn wir arbeiten sorgfältig und mit Liebe zum Detail</p>
      </q-card>
    </div>
  </div>
</div>
</template>

<style scoped>
.overCards {
  margin: 20px auto;
  max-width: 700px;
}

.demCards {
  justify-content: center;
  padding: 5vh 5px;
  padding-bottom: 15vh;
}

/* COME UP */

.anItem:hover {
  -webkit-box-shadow: 0px 10px 41px 4px rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0px 10px 41px 4px rgba(0, 0, 0, 0.24);
  box-shadow: 0px 10px 41px 4px rgba(0, 0, 0, 0.24);
  transform: translateY(-2px);
}

/* CHANGE BG */

/* .anItem:hover {
                background: #99cc33;
                color: white;
        }
        .anItem:hover .cardIcon,
        .anItem:hover .cardHead,
        .anItem:hover .cardText {
                transition: color 0.2s linear;
                color: white !important;
        } */

.anItem {
  margin: 10px;
  padding: 15px 10px;
  transition: all 0.2s linear;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.cardIcon {
  font-size: 50px;
}

.cardHead {
  font-size: 25px;
}
</style>
