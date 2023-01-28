<template>
  <b-container>
    <b-card width="400" class="mx-auto mt-5" title="Login">
      <b-card-text>
        <b-form id="login-form" v-model="valid" @submit.prevent="loginUser">
          <b-input-group>
            <b-input-group-prepend is-text>
              <b-icon icon="person-circle"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              id="username-field"
              v-model="login.username"
              placeholder="username"
              :rules="rules_username"
            ></b-form-input>
          </b-input-group>
          <b-input-group>
            <b-input-group-prepend is-text>
                <b-icon icon="shield-lock"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              id="password-field"
              v-model="login.password"
              placeholder="password"
              type="password"
              :rules="rules_password"
            ></b-form-input>
          </b-input-group>
          <b-row>
            <b-col>
              <b-btn color="info" :disabled="!valid" type="submit">
                Login
              </b-btn>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-btn type="link" small text to="/Register" color="error">
                Need an account? Register.
              </b-btn>
            </b-col>
          </b-row>
        </b-form>
      </b-card-text>
      <b-alert v-if="loginError" dense text type="error">
        {{ loginErrorMessage }}
      </b-alert>
    </b-card>
    <b-card>
        <b-card-text>
            {{ $store.state.auth.strategy }}
        </b-card-text>
    </b-card>
  </b-container>
</template>
  
  <script>
import {} from "bootstrap-vue";
export default {
  auth: false,
  name: "Login",
  data() {
    return {
      valid: false,
      rules_username: [(value) => !!value || "Required"],
      rules_password: [(value) => !!value || "Required"],
      showPassword: false,
      login: {
        username: "",
        password: "",
      },
      loginError: false,
      loginErrorMessage:
        "Something went wrong when logging in. Check your Username & Password, and try again.",
    };
  },
  methods: {
    loginUser() {
      this.loginError = false;
      this.$auth
        .loginWith("local", {
          data: this.login,
        })
        .then((resp) => {
          this.$auth.setToken("local", "Bearer " + resp.data.access);
          this.$auth.setRefreshToken("local", resp.data.refresh);
          this.$axios.setHeader("Authorization", "Bearer " + resp.data.access);
          this.$auth.ctx.app.$axios.setHeader(
            "Authorization",
            "Bearer " + resp.data.access
          );
          if (resp.status === 200) this.$router.push({ name: "index" });
        })
        .catch((error) => {
          console.log(error);
          this.loginError = true;
        });
    },
  },
  head() {
    return {
      title: "Login",
      meta: [
        {
          hid: "description",
          name: "description",
          content: "Login to manage your own recipes, food, and ingredients",
        },
      ],
    };
  },
};
</script>
  
  <style lang="scss" scoped></style>
