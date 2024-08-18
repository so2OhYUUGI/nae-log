import type { GatsbyConfig } from "gatsby"

const config: GatsbyConfig = {
  siteMetadata: {
    title: `NaeLOG`,
    siteUrl: `https://www.yourdomain.tld`,
  },
  // More easily incorporate content into your pages through automatic TypeScript type generation and better GraphQL IntelliSense.
  // If you use VSCode you can also use the GraphQL plugin
  // Learn more at: https://gatsby.dev/graphql-typegen
  graphqlTypegen: true,
  plugins: [
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
