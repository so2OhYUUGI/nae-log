import { defineConfig } from "cypress";

// const webpackConfig = require("./node_modules/gatsby/dist/utils/webpack.config.js");

export default defineConfig({
  e2e: {
    baseUrl: `http://localhost:8000`,
    specPattern: `cypress/e2e`
  },

  component: {
    devServer: {
      framework: "react",
      bundler: "webpack",
    },
  },
});

