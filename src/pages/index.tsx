// src/pages/index.tsx
import React from 'react';
import { Link } from 'gatsby';
import { StaticImage } from "gatsby-plugin-image"

import { Container, Box, Typography, Button } from '@mui/material';

const IndexPage = () => (
	<Container maxWidth="lg">
		<Box textAlign="center" py={10}>
			<Typography variant="h2" component="h1" gutterBottom>
				Welcome to NaeLOG
			</Typography>
			<Typography variant="h6" component="p" gutterBottom>
				Seamlessly manage and monitor your seedling growth with NaeLOG's advanced features.
			</Typography>
			<StaticImage
				src="../images/naelog-icon.png"
				loading="eager"
				width={64}
				quality={95}
				formats={["auto", "webp", "avif"]}
				alt=""
				style={{ marginBottom: `var(--space-3)` }}
			/>
			<Box mt={4}>
				<Link to="/home" style={{ textDecoration: 'none' }}>
					<Button variant="contained" color="primary" size="large">
						Get Started
					</Button>
				</Link>
			</Box>
		</Box>
	</Container>
);

export default IndexPage;
