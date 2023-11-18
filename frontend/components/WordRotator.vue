<template>
  <div class="heading__wrapper word-rotator">
    <div class="heading heading--sm" :class="{ text: words.length }">
      <h2 v-if="heading">{{ heading }}</h2>
      <h3 v-if="words.length">
        <span v-for="(word, i) in words" :key="i" ref="word" class="word">{{
          word
        }}</span>
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "WordRotatorComponent",

  props: {
    heading: {
      type: String,
      default: "",
    },
    words: {
        type: Array,
        default: () => ["Adults", "Seniors", "Children"],
    }
  },

  data() {
    return {
    };
  },

  mounted() {
    const words = document.getElementsByClassName("word");
    if (words.length) {
      const wordArray = [];
      let currentWord = 0;

      words[currentWord].style.opacity = 1;
      for (let i = 0; i < words.length; i++) {
        splitLetters(words[i]);
      }

      function changeWord() {
        const cw = wordArray[currentWord];
        const nw =
          currentWord === words.length - 1
            ? wordArray[0]
            : wordArray[currentWord + 1];

        for (let i = 0; i < cw.length; i++) {
          animateLetterOut(cw, i);
        }

        for (let i = 0; i < nw.length; i++) {
          nw[i].className = "letter behind";
          nw[0].parentElement.style.opacity = 1;
          animateLetterIn(nw, i);
        }

        currentWord =
          currentWord === wordArray.length - 1 ? 0 : currentWord + 1;
      }

      function animateLetterOut(cw, i) {
        setTimeout(function () {
          cw[i].className = "letter out";
        }, 1);
      }

      function animateLetterIn(nw, i) {
        setTimeout(function () {
          nw[i].className = "letter in";
        }, 340);
      }

      function splitLetters(word) {
        const content = word.innerHTML;
        word.innerHTML = "";
        const letters = [];
        for (let i = 0; i < content.length; i++) {
          const letter = document.createElement("span");
          letter.className = "letter";
          letter.innerHTML = content[i] !== " " ? content[i] : "&nbsp;";
          word.appendChild(letter);
          letters.push(letter);
        }

        wordArray.push(letters);
      }

      changeWord();
      setInterval(changeWord, 2500);
    }
  },
};
</script>

<style lang="scss">
.heading__wrapper.word-rotator {
  width: 100%;
  display: flex;
  align-items: center;
  margin-top: 15px;

  .text {
    margin-top: 0;
    display: flex;
  }

  @include media-breakpoint-down(xs) {
    .words {
      display: inline-block;
    }
  }

  h2,
  h3 {
    font-size: 20px;
    font-family: "Playfair Display", serif;
    font-size: 30px;
    margin-bottom: 50px;
    max-width: 400px;
    text-transform: uppercase;

    @include media-breakpoint-down(md) {
      font-size: 20px;
    }
  }

  .word {
    position: absolute;
    left: 0;
    width: 480px;
    opacity: 0;
    text-align: center;
    color: blue;
  }

  .letter {
    display: inline-flex;
    position: relative;
    transform: translateZ(25px);
    transform-origin: 50% 50% 25px;
  }

  .letter.out {
    transform: rotateX(90deg);
    transition: transform 0.32s cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }

  .letter.behind {
    transform: rotateX(-90deg);
  }

  .letter.in {
    transform: rotateX(0deg);
    transition: transform 0.38s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
}
</style>
