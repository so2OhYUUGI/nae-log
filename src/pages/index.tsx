// src/pages/index.tsx

import React from 'react';
import { graphql } from 'gatsby';
import { Typography } from '@mui/material';

// Gatsbyのデータをクエリする
export const query = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`;

const IndexPage = ({ data }: any) => {
	const title = data.site.siteMetadata.title;

	return (
		<div>
			<Typography variant="h1" component="h1">
				{title}
			</Typography>
			<p>楽しい育苗管理を始めよう！</p>
		</div>
	);
};

export default IndexPage;

// 印象的なタイトル
export const Head = () => (
	<title>NaeLOG - ラクする育苗管理</title>
);
