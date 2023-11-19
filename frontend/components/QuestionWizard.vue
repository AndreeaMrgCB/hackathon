<template>
  <div data-app>
    <section class="pen-description">
    </section>
    <section class="register" v-if="!hasSeenCongrats">
      <div class="register-icon">
        <img
          class="register-icon-item"
          src="https://vuejs.org/images/logo.png"
          alt="vue logo"
        />
      </div>

      <h2 class="register-title">Your details</h2>

      <div class="register-stepper">
        <div
          class="step"
          :class="{ 'step-active': step === 1, 'step-done': step > 1 }"
        >
          <span class="step-number">1</span>
        </div>
        <div
          class="step"
          :class="{ 'step-active': step === 2, 'step-done': step > 2 }"
        >
          <span class="step-number">2</span>
        </div>
        <div
          class="step"
          :class="{ 'step-active': step === 3, 'step-done': step > 3 }"
        >
          <span class="step-number">3</span>
        </div>
      </div>

      <transition name="slide-fade">
        <section v-show="step === 1">
          <form class="form" method="post" action="#" @submit.prevent="next">
            <div class="form-group">
              <v-checkbox
                v-model="selectedGender"
                color="#ba4130"
                label="Male"
                value="Male"
              ></v-checkbox>
              <v-checkbox
                v-model="selectedGender"
                color="#ba4130"
                label="Female"
                value="Female"
              ></v-checkbox>
            </div>

            <div class="form-group">
              <input
                type="text"
                v-model="customer.firstName"
                autocomplete="customer.firstName"
                placeholder="First name"
                required
              />
            </div>
            <div
              class="cta"
              data-style="see-through"
              data-alignment="right"
              data-text-color="custom"
            >
              <p class="cta-color">
                <span class="link_wrap">
                  <button type="submit" value="Next" class="form__button">
                    <span>Next</span>
                  </button>
                </span>
              </p>
            </div>
          </form>
        </section>
      </transition>
      <transition name="slide-fade">
        <section v-show="step === 2">
          <div class="form__heading">
            What are your symptons, {{ customer.firstName }}?
          </div>
          <form class="form" method="post" action="#" @submit.prevent="next">
            <div class="form-group">
              <v-expansion-panels>
                <v-expansion-panel
                  v-for="(item, i) in symptomsData.symptoms"
                  :key="i"
                >
                  <v-expansion-panel-header color="#ba4130">
                    {{ item.name }}
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row no-gutters>
                      <v-col
                        v-for="symptom in item.items"
                        :key="symptom.index"
                        cols="3"
                        sm="4"
                      >
                        <v-checkbox
                          v-model="selectedSymptoms"
                          color="#ba4130"
                          :label="symptom.name"
                          :value="symptom.name"
                        ></v-checkbox>
                      </v-col>
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
            <div v-if="selectedSymptoms.length" class="form__symptoms">
              <div>
                <span>Your Symptoms are:</span>
                <span>
                  <div
                    v-for="(selected, i) in selectedSymptoms"
                    :key="i"
                    class="form__symptoms-text"
                  >
                    {{ selected }}
                  </div></span
                >
              </div>
            </div>
            <div class="form-group cta-step">
              <div class="cta prev">
                <p class="cta-color">
                  <span class="link_wrap">
                    <button
                      class="form__button--reverse"
                      href="#"
                      @click.prevent="prev()"
                    >
                      Previous
                    </button>
                  </span>
                </p>
              </div>
              <div class="cta">
                <p class="cta-color">
                  <span class="text"></span>
                  <span class="link_wrap">
                    <div class="register-btn">
                      <button
                        type="submit"
                        value="Find diagnostic"
                        class="form__button"
                      >
                        Find diagnostic
                      </button>
                    </div>
                  </span>
                </p>
              </div>
            </div>
          </form>
        </section>
      </transition>
      <transition name="slide-fade">
        <section v-show="step === 3">
          <div class="form__heading">
            {{ customer.firstName }}, your diagnosic is common cold.
          </div>

          <div class="form-group cta-step">
            <div class="cta prev">
              <p class="cta-color">
                <span class="link_wrap">
                  <buton
                    class="form__button--reverse"
                    href="#"
                    @click.prevent="prev()"
                    >Previous
                  </buton>
                </span>
              </p>
            </div>
          </div>
        </section>
      </transition>
    </section>
    <section class="congrats register" v-if="hasSeenCongrats">
      <div class="register-icon">
        <img
          class="register-icon-item"
          src="https://vuejs.org/images/logo.png"
          alt="vue logo"
        />
      </div>
      <h2 class="congrats-title">Thank you !</h2>
      <p class="congrats-subtitle">
        You have successfully created your account and joined the<br />
        <strong>VueJS<br />multiple steps form</strong>
      </p>
    </section>
  </div>
</template>

<script>
import symptomDataJSON from "../data/symptoms.json";

export default {
  name: "QuestionWizard",
  data: () => {
    return {
      symptomsData: symptomDataJSON,
      selectedSymptoms: [],
      steps: {},
      step: 1,
      customer: {
        gender: "1",
        firstName: "",
        lastName: "",
        phoneNumber: "",
        address: "",
        zipCode: "",
        city: "",
        birthDay: "",
        termOfService: "",
        pinCode: "",
        eMail: "",
      },
      symptoms: [
        {
          name: "Skin Symptoms",
          items: [
            {
              name: "Itching",
              value: false,
            },
            {
              name: "Skin Rash",
              value: false,
            },
          ],
        },
        {
          name: "General Symptoms",
          items: [
            {
              name: "Sunken Eyes",
              value: false,
            },
            {
              name: "Sweating",
              value: false,
            },
          ],
        },
      ],
      hasSeenCongrats: false,
      tempCustomer: {
        gender: "",
        firstName: "",
        lastName: "",
        phoneNumber: "",
        address: "",
        zipCode: "",
        city: "",
        birthDay: "",
        termOfService: "",
        pinCode: "",
        eMail: "",
      },
    };
  },
  methods: {
    prev() {
      this.step--;
    },

    next() {
      this.step++;
    },

    customerRegister() {
      this.hasSeenCongrats = true;
    },
  },
};
</script>

<style lang="scss">
/* VARIABLES */
/* COLORS */
$brand-primary: $secondary;
$brand-secondary: #dedc00;
$brand-lemon: #fff219;
$brand-quaternary: #f282a5;
$brand-menthol: #14877d;
$brand-coral: rgb(250, 90, 85);
$brand-paprika: rgb(205, 0, 125);
$color-white: #fff;
$color-dark: #676767;
$color-gray: $secondary;
$color-lightgray: #ededed;
$color-jungle: #fff;
$black: $black;

/* FONT */
$font-montserrat: "Montserrat", sans-serif;
$font-weight-bold: 700;

body {
  background-color: $color-jungle;
  font-family: $font-montserrat;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.pen-description {
  display: flex;
  flex-flow: column;
  align-items: center;
  font-family: $font-montserrat;

  h1 {
    text-align: center;
    margin-top: 2rem;
    color: $black;
  }

  p {
    margin: 0;
    line-height: 1;
  }

  .pen-copyright {
    img {
      border-radius: 25px;
      padding: 5px;
      margin: 5px;
      transition: box-shadow 0.5s ease-in-out;
    }

    &:hover img {
      box-shadow: 0 10px 20px #fff;
    }
  }
}

.register {
  font-family: "interstate", sans-serif !important;
  display: block;
  color: $black;
  max-width: 840px;
  margin: 80px auto;
  padding: 2rem;
  border-radius: 4rem;
  border: 1px solid $secondary;

  .cta {
    margin-top: 20px;
  }

  &-icon {
    display: flex;
    background: $black;
    border-radius: 2rem;
    width: 50px;
    height: 50px;
    padding: 1rem;
    margin: -50px auto 20px;

    &-item {
      width: 100%;
    }
  }

  &-title {
    font-weight: 300;
    font-size: 1.5rem;
    text-transform: uppercase;
    letter-spacing: 0.2rem;
    text-align: center;
    color: $black;
    padding: 0 2rem;
    margin-top: 2rem;
  }

  &-stepper {
    display: flex;
    justify-content: space-between;
    width: 100%;
    position: relative;
    margin: 0 auto 1.5em;

    &::before {
      z-index: 0;
      content: "";
      display: block;
      position: absolute;
      height: 2px;
      top: calc(50% - 1px);
      background: $color-gray;
      width: calc(100% - 46px);
      opacity: 0.3;
      left: 25px;
    }

    .step {
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 2;
      border: 2px solid $color-gray;
      color: $color-gray;
      background-color: $white;
      border-radius: 50%;
      min-width: 25px;
      min-height: 25px;
      line-height: 20px;
      font-size: 16px;
      opacity: 0.3;

      &-active {
        color: $brand-primary;
        background-color: $white;
        border-color: $brand-primary;
        opacity: 1;
      }

      &-done {
        border: 2px solid $color-gray;
        color: $color-gray;
        background-color: $white;
      }

      &-number {
        font-family: $font-montserrat;
        font-weight: 800;
        line-height: 1;
        vertical-align: middle;
      }
    }
  }

  .form {
    &__heading {
      margin-bottom: 20px;
      font-family: "interstate", sans-serif;
      font-size: 20px;
      line-height: 30px;
      text-align: center;
    }
    &__symptoms {
      margin-top: 20px;
      font-family: "interstate", sans-serif;
      font-size: 20px;
      line-height: 30px;
      &-text {
        display: flex;
        &::before {
          /*Add another block-level blank space*/
          content: "";
          display: block;
          margin-right: 10px;

          /*Make it a small rectangle so the border will create an L-shape*/
          width: 8px;
          height: 20px;

          /*Add a white border on the bottom and left, creating that 'L' */
          border: solid $secondary;
          border-width: 0 3px 3px 0;

          /*Rotate the L 45 degrees to turn it into a checkmark*/
          transform: rotate(45deg);
        }
      }
    }
    &__button {
      position: relative;
      display: block;
      overflow: hidden;
      width: fit-content;
      padding: 10px 25px;
      max-width: 250px;
      margin: 1rem auto;
      text-transform: uppercase;
      font-weight: 600;
      border: 1px solid $tertiary;
      color: $tertiary;
      transition: 0.5s ease-in-out;
      z-index: 100;
      font-family: "interstate", sans-serif;
      cursor: pointer;

      &--reverse {
        position: relative;
        display: block;
        overflow: hidden;
        width: fit-content;
        padding: 10px 25px;
        max-width: 250px;
        margin: 1rem auto;
        text-transform: uppercase;
        font-weight: 600;
        border: 1px solid $tertiary;
        color: $tertiary;
        transition: 0.5s ease-in-out;
        z-index: 100;
        cursor: pointer;

        &::before {
          content: "";
          position: absolute;
          top: 0;
          right: 0;
          bottom: 0;
          left: 0;
          background-color: $tertiary;
          transform: translateX(100%);
          transition: 0.5s ease-in-out;
          z-index: -1;
        }

        &:hover {
          color: $white;
          &::before {
            transform: translateX(0);
          }
        }
      }

      &::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background-color: $tertiary;
        transform: translateX(-100%);
        transition: 0.5s ease-in-out;
        z-index: -1;

        &:hover {
          transform: translateX(0);
        }
      }

      &:hover {
        color: $white;

        &::before {
          transform: translateX(0);
        }
      }
    }
    &__grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;

      @include media-breakpoint-down(md) {
        grid-template-columns: 1fr 1fr 1fr;
      }
    }

    &-group {
      display: flex;
      flex-flow: row;
      justify-content: flex-start;
      align-items: baseline;
      gap: 10px;

      label {
        text-align: left;
        font-size: 1.1rem;
        line-height: 1.1;
      }

      &.cta-step {
        color: $black;
        justify-content: space-between;
      }

      &.new-password {
        margin-top: 2rem;
      }
    }

    .cta-color .link_wrap {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;

      .arrow-prev {
        position: relative;
        display: inline-block;
        transform: translate(0);
        transition: transform 0.3s ease-in-out;

        &::before {
          content: "<";
          position: absolute;
          top: -17px;
          left: -25px;
        }
      }

      .arrow-next {
        position: relative;
        display: inline-block;
        transform: translate(0);
        transition: transform 0.3s ease-in-out;

        &::before {
          content: ">";
          position: absolute;
          top: -10px;
          left: -25px;
        }
      }

      &:hover .arrow-prev {
        transform: translate(-5px);
      }

      &:hover .arrow-next {
        transform: translate(5px);
      }
    }
  }
  // Override styles for input
  input[type="submit"],
  input[type="text"],
  input[type="tel"],
  input[type="email"],
  input[type="date"] {
    -webkit-appearance: none;
    padding: 1.3rem 1rem;
    width: 100%;
    margin: 0.5rem;
    background-color: transparent;
    border-bottom: 2px solid #ba4130;
  }

  input[type="submit"] {
    cursor: pointer;
    position: relative;
    padding-right: 36px;
    background: none;
    width: fit-content;

    &:hover,
    &:focus {
      box-shadow: unset;
      transform: none;
    }

    &::after {
      content: "";
      display: block;
      position: absolute;
      right: 0;
      top: 50%;
      border-radius: 50px;
      border: 1px solid $brand-primary;
      height: 25px;
      width: 25px;
      margin-top: -14px;
      pointer-events: none;
      transition: all 0.33s cubic-bezier(0.12, 0.75, 0.4, 1);
    }
  }

  &-btn input {
    color: $black;
    font-size: 1.2rem;
    font-family: $font-montserrat;
    font-weight: 800;
    line-height: 1;
    width: fit-content;
    background: linear-gradient(145deg, #1b3c05, #173205);
    box-shadow: 20px 20px 60px #142c04, -20px -20px 60px #1f4406;

    &:hover {
      background: linear-gradient(145deg, #173205, #1b3c05);
      box-shadow: 20px 20px 60px #142c04, -20px -20px 60px #1f4406;
    }
  }

  // Transition SLIDE FADE
  .slide-fade-enter-active {
    transition: all 0.3s ease;
  }
  .slide-fade-leave-active {
    display: none;
    transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
  }
  .slide-fade-enter,
  .slide-fade-leave-to {
    transform: translateX(10px);
    opacity: 0;
  }
}

.congrats {
  background: $black;
  color: $brand-primary;
  padding: 4rem;
  text-align: center;

  &-subtitle {
    line-height: 1.3;

    strong {
      font-size: 2rem;
    }
  }
}

.v-expansion-panel-header {
  color: $white;
  font-family: "interstate", sans-serif;
  font-size: 20px;
  line-height: 30px;
}

.v-expansion-panel-content__wrap {
  font-family: "interstate", sans-serif;
}

.mdi-chevron-down {
  color: $white !important;
}

.v-expansion-panel-header__icon {
  position: absolute !important;
  right: 20px !important;
}

.v-expansion-panel::before {
  box-shadow: none !important;
}

.v-input--selection-controls .v-input__slot > .v-label,
.v-input--selection-controls .v-radio > .v-label {
  color: $black;
}
</style>
