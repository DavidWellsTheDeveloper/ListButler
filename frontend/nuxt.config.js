const development = process.env.NODE_ENV !== 'production'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/scss/style.scss'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    // '@nuxtjs/eslint-module'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    '@nuxtjs/auth-next',
    '@nuxtjs/axios'
  ],

  bootstrapVue: {
    icons: true
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: development
      ? 'http://localhost:8000'
      : 'https://listbutlers.com/api',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  middleware: 'auth',

  auth: {
    strategies: {
      // JWT token auth
      local: {
        scheme: 'refresh',
        endpoints: {
          login: {
            url: '/api/token/',
            method: 'post',
            propertyName: 'access',
          },
          refreshToken: {
            url: 'api/token/refresh/',
            method: 'post',
            property: 'refresh',
          },
          logout: false,
          user: {
            url: '/user/users/',
            method: 'get',
            propertyName: false,
          },
        },
      },
    },
  },
  router: {
    // By default, views will require login.
    middleware: ['auth'],
  },
}
