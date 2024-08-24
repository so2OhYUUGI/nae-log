import React from 'react';
import { Container, Grid, Box, Typography, Card, CardContent, Button } from '@mui/material';
import Layout from '../components/Layout';
import { Link } from 'gatsby';  // GatsbyのLinkコンポーネントをインポート

const MainPage = () => (
	<Layout>
		<Container maxWidth="lg">
			<Box py={5}>
				<Typography variant="h4" component="h2" gutterBottom>
					NaeLOG Dashboard
				</Typography>
				<Grid container spacing={4}>
					{/* Relay Management */}
					<Grid item xs={12} md={6}>
						<Card>
							<CardContent>
								<Typography variant="h5" component="h3" gutterBottom>
									Relay Management
								</Typography>
								<Typography variant="body1" gutterBottom>
									Control and monitor your relay settings. Turn devices on/off and set schedules easily.
								</Typography>
								<Button
									variant="contained"
									color="primary"
									component={Link}
									to="/relay-control" // GatsbyのLinkを使用してリレーコントロールページにリンク
								>
									Manage Relays
								</Button>
							</CardContent>
						</Card>
					</Grid>
					{/* Future Feature 1 */}
					<Grid item xs={12} md={6}>
						<Card>
							<CardContent>
								<Typography variant="h5" component="h3" gutterBottom>
									Feature Placeholder
								</Typography>
								<Typography variant="body1" gutterBottom>
									Future feature description goes here.
								</Typography>
								<Button variant="contained" color="primary" disabled>
									Coming Soon
								</Button>
							</CardContent>
						</Card>
					</Grid>
					{/* Future Feature 2 */}
					<Grid item xs={12} md={6}>
						<Card>
							<CardContent>
								<Typography variant="h5" component="h3" gutterBottom>
									Feature Placeholder
								</Typography>
								<Typography variant="body1" gutterBottom>
									Future feature description goes here.
								</Typography>
								<Button variant="contained" color="primary" disabled>
									Coming Soon
								</Button>
							</CardContent>
						</Card>
					</Grid>
				</Grid>
			</Box>
		</Container>
	</Layout>
);

export default MainPage;
