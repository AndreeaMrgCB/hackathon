<template>
  <div>
    <HeroComponent></HeroComponent>
    <section class="description">
      <p class="description__paragraph container--wide">
        Input your symptoms effortlessly, and discover instant insights to
        empower your health decisions. Say goodbye to uncertainties and hello to
        a healthier, more confident you. Embrace the everyday journey to
        well-being with our intuitive platform – because your health matters,
        every day.
      </p>
    </section>
    <div id="question-wizard" />
    <QuestionWizard />
    <div class="footer">
      <span>Created by </span>
      <ul>
        <li>Andreea</li>
        <li>Divya</li>
        <li>Niz</li>
        <li>Owen</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexPage",
};
</script>

<style lang="scss">
.footer {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-bottom: 30px;
  font-family: "interstate", sans-serif;
  font-size: 16px;
  line-height: 30px;

  span {
    color: $tertiary;
  }

  ul {
    list-style: none;
    display: flex;
    gap: 20px;
  }
}
.description {
  text-align: center;
  margin: 0 auto;
  background-color: $tertiary;
  color: $white;
  padding-top: 60px;
  padding-bottom: 60px;
  font-family: "interstate", sans-serif;
  font-size: 20px;
  line-height: 30px;

  @include media-breakpoint-down(md) {
    padding-top: 30px;
    padding-bottom: 30px;
  }
}

.branding {
  font-family: "interstate", sans-serif;
  color: $secondary;
  font-weight: 700;
}
</style>
