<template>
  <div>
    <div class="hero container--wide">
      <div class="hero__content">
        <span class="branding">Health Detective</span>
        <h1 class="hero__text">
          Input <br />Discover <br /><span class="hero__highlight"
            >Empower Your Health</span
          >
        </h1>
        <!--         <span class="hero__mask"
          >Input <br />Discover <br />Empower Your Health</span
        > -->
        <WordRotator heading="Made for" />

        <a href="#question-wizard" role="button" class="hero__button"
          ><span>Diagnose Me</span></a
        >
      </div>
      <div class="hero__image"></div>
    </div>
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
  margin-top: 60px;

  @include media-breakpoint-down(md) {
    margin-top: 10px;
    padding-right: 0;
  }

  &__highlight {
    // background-color: $primary;
    color: $secondary;
  }

  &__image {
    flex: 1 0 50%;
    background-image: url("@/static/img/Doctor-loop.gif");
    height: 600px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;

    @include media-breakpoint-down(md) {
      flex: 100%;
      height: 440px;
    }
  }

  &__content {
    position: relative;
    z-index: 99999;
    flex: 1 0 50%;
    background-color: transparent;

    @include media-breakpoint-down(md) {
      flex: 100%;
    }
  }

  &__text {
    font-family: "obvia", serif;
    font-size: 50px;
    margin-bottom: 50px;
    margin-top: 20px;
    max-width: 600px;
    text-transform: uppercase;

    @include media-breakpoint-down(md) {
      font-size: 25px;
    }
  }

  &__paragraph {
    font-family: "obvia", sans-serif;
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
    font-family: "interstate", sans-serif;

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
      background-color: rgb(186, 65, 48);
    }

    &::before {
      bottom: 0;
      left: 0;
      border-left: 1px solid rgb(186, 65, 48);
      border-bottom: 1px solid rgb(186, 65, 48);
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
      border-right: 1px solid rgb(186, 65, 48);
      border-top: 1px solid rgb(186, 65, 48);
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
        border-left: 1px solid rgb(186, 65, 48);
        border-bottom: 1px solid rgb(186, 65, 48);
      }

      &::after {
        top: 0;
        right: 0;
        border-right: 1px solid rgb(186, 65, 48);
        border-top: 1px solid rgb(186, 65, 48);
      }

      &::before,
      &::after {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
