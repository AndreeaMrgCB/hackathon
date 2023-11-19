// import axios from 'axios'

export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Health Detective',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [
      {
        rel: 'stylesheet',
        type: 'text/css',
        href: 'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto:wght@500&display=swap',
      },
      {
        rel: 'stylesheet',
        type: 'text/css',
        href: 'https://fonts.googleapis.com/css2?family=Lato&family=Playfair+Display&family=Roboto:wght@500&display=swap',
      },
      {
        rel: 'stylesheet',
        type: 'text/css',
        href: 'https://cdnjs.cloudflare.com/ajax/libs/material-design-iconic-font/2.2.0/css/material-design-iconic-font.min.css',
        async: true,
        defer: true,
      },
    ],
    script: [
    ],
  },
/* 
  env: {
    API_KEY: process.env.BBPA_apiKey,
    API_BASE: process.env.BBPA_apiBase,
    MEDIA_BASE: process.env.BBPA_mediaBase,
    PREVIEW_BASE: process.env.BBPA_previewBase,
    UI_BASE: process.env.BBPA_uiBase,
  }, */

  compilerOptions: {
    types: ['@nuxt/types'],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~assets/scss/main.scss'],

   styleResources: {
    scss: [
      './assets/scss/mixins/*.scss',
      './assets/scss/global/_breakpoints.scss',
      './assets/scss/global/_colours.scss'
    ],
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
/*     {
      src: '~/plugins/axios.js',
    }, */
  ],

/*   axios: {
    baseURL: process.env.BBPA_apiBase,
  },
  publicRuntimeConfig: {
    imageBase: process.env.BBPA_mediaBase || '',
    apiKey: process.env.BBPA_apiKey || '',
  }, */

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: [
    '~/components',
  ],

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/vuetify',
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/style-resources',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: ['@nuxtjs/axios'],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: null,
  },

/*   generate: {
    fallback: '404.html',
    routes: async () => {
      const settings = await axios
        .get(`${process.env.BBPA_apiBase}/settings`, {
          headers: {
            Accept: 'application/json',
            'x-api-key': process.env.BBPA_apiKey,
          },
        })
        .then((resp) => {
          return resp.data.fields
        })

      const allPages = await axios
        .get(`${process.env.BBPA_apiBase}/pages`, {
          headers: {
            Accept: 'application/json',
            'x-api-key': process.env.BBPA_apiKey,
          },
        })
        .then((resp) => {
          return resp.data
        })

      const routes = allPages.map((page) => {
        return {
          route: page.system.url,
          payload: {
            page,
            settings,
          },
        }
      })

      return ['/preview', ...routes]
    },
  }, */

  server: {
    host: '0.0.0.0',
  },
}
