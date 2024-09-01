import type { GatsbyConfig } from "gatsby"

const config: GatsbyConfig = {
  siteMetadata: {
    title: `NaeLOG`,
    siteUrl: `https://www.yourdomain.tld`,
  },
  pathPrefix: '/app',
  // More easily incorporate content into your pages through automatic TypeScript type generation and better GraphQL IntelliSense.
  // If you use VSCode you can also use the GraphQL plugin
  // Learn more at: https://gatsby.dev/graphql-typegen
  graphqlTypegen: true,
  plugins: [
    `gatsby-plugin-image`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`,
      },
    },
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `NaeLOG`,
        short_name: `naelog`,
        start_url: `/app/`,
        icon: `src/images/favicon.png`, // 使用するファビコン画像のパス
      },
    },
    {
      resolve: `gatsby-plugin-material-ui`,
      options: {
        // Disable autoprefixing of CSS properties.
        disableAutoprefixing: true,
        // Disable minification of CSS.
        disableMinification: true,
      },
    },
  ],
}

export default config
