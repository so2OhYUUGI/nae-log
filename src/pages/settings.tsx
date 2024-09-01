// src/pages/settings.tsx
import React from 'react';
import { Container, Typography } from '@mui/material';

import Layout from '../components/Layout';

const SettingsPage = () => (
	<Layout>
		<Container maxWidth="lg">
			<Typography variant="h4" component="h2" gutterBottom>
				Settings
			</Typography>
		</Container>
	</Layout>
);

export default SettingsPage;
