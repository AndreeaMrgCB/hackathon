<template>
  <div>
    <div class="hero">
      <div class="hero__image"></div>
      <div class="hero__content">
        <h1 class="hero__text">
          Input <br />Discover <br />Empower Your Health
        </h1>
<!--         <span class="hero__mask"
          >Input <br />Discover <br />Empower Your Health</span
        > -->
        <WordRotator heading="Made for" />

        <a href="/diagnose" role="button" class="hero__button"
          ><span>Diagnose Me</span></a
        >
      </div>
    </div>
    <section class="description">
      <p class="description__paragraph">
        Input your symptoms effortlessly, and discover instant insights to
        empower your health decisions. Say goodbye to uncertainties and hello to
        a healthier, more confident you. Embrace the everyday journey to
        well-being with our intuitive platform – because your health matters,
        every day.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: "HeroComponent",
};
</script>

<style lang="scss">
.hero {
  display: flex;
  justify-content: center;
  align-items: center;
  max-height: 500px;

  &__mask {
    font-size: 40px;
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    background-image: url(https://media.giphy.com/media/xULW8Fw2ZhznUptrYA/giphy.gif);
    background-size: cover;
    background-position: center;
    font-weight: 700;
    text-align: center;
    text-transform: uppercase;
  }

  &__image {
    flex: 1 0 70%;
    background-image: url("@/static/img/hero-img.jpg");
    height: 500px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;

    &::after {
      background: linear-gradient(to right, transparent 0, #fff 66%);
      content: "";
      display: block;
      height: 100%;
      position: absolute;
      bottom: 0;
      width: 50%;
      z-index: 100;
      top: 0;
      right: initial;
      left: 38em;
    }
  }

  &__content {
    position: relative;
    z-index: 99999;
    flex: 1 0 30%;
  }

  &__text {
    font-size: 20px;
    font-family: "Lato", serif;
    font-size: 30px;
    margin-bottom: 50px;
    max-width: 400px;
    text-transform: uppercase;
  }

  &__paragraph {
    font-family: "Lato", sans-serif;
    font-size: 16px;
    max-width: 400px;
    line-height: 20px;
  }

  &__button {
    position: relative;
    display: inline-block;
    width: auto;
    height: auto;
    background-color: transparent;
    border: none;
    cursor: pointer;
    margin: 15px 0;
    min-width: 150px;
    padding: 5px;

    span {
      position: relative;
      display: inline-block;
      font-size: 14px;
      font-weight: bold;
      letter-spacing: 2px;
      text-transform: uppercase;
      top: 0;
      left: 0;
      width: 100%;
      padding: 15px 20px;
      transition: 0.3s;
      color: rgb(255, 255, 255);
      background-color: rgb(54, 56, 55);
    }

    &::before {
      bottom: 0;
      left: 0;
      border-left: 1px solid rgb(28, 31, 30);
      border-bottom: 1px solid rgb(28, 31, 30);
      width: 10%;
      height: 25%;
      transition: 0.35s;
      background: transparent;
      z-index: 2;
      position: absolute;
      content: "";
    }

    &::after {
      top: 0;
      right: 0;
      border-right: 1px solid rgb(28, 31, 30);
      border-top: 1px solid rgb(28, 31, 30);
      width: 10%;
      height: 25%;
      transition: 0.35s;
      background: transparent;
      z-index: 2;
      position: absolute;
      content: "";
    }

    &:hover {
      outline: 0 !important;
      outline-offset: 0;

      &::before {
        bottom: 0;
        left: 0;
        border-left: 1px solid rgb(28, 31, 30);
        border-bottom: 1px solid rgb(28, 31, 30);
      }

      &::after {
        top: 0;
        right: 0;
        border-right: 1px solid rgb(28, 31, 30);
        border-top: 1px solid rgb(28, 31, 30);
      }

      &::before,
      &::after {
        width: 100%;
        height: 100%;
      }
    }
  }
}

.description {
  max-width: 1440px;
  padding: 30px 120px;
  text-align: center;
  margin: 0 auto;
}
</style>
