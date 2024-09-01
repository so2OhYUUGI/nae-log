// src/pages/info.tsx
import React from 'react';
import { Container, Typography } from '@mui/material';

import Layout from '../components/Layout';

const InfoPage = () => (
	<Layout>
		<Container maxWidth="lg">
			<Typography variant="h4" component="h2" gutterBottom>
				Information
			</Typography>

		</Container>
	</Layout>
);

export default InfoPage;
