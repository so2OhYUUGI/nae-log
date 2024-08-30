import React from 'react';
import { Link } from 'gatsby';
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
				<Box mt={4}>
					<Link to="/main" style={{ textDecoration: 'none' }}>
						<Button variant="contained" color="primary" size="large">
							Get Started
						</Button>
					</Link>
				</Box>
			</Box>
		</Container>
);

export default IndexPage;
