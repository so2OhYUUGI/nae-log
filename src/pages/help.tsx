// src/pages/help.tsx
import React from 'react';
import { Container, Typography, Box, Button, Grid } from '@mui/material';
import Layout from '../components/Layout';

const ColorSample = ({ colorName, colorValue }: { colorName: string, colorValue: string }) => (
	<Box
		sx={{
			backgroundColor: colorValue,
			color: colorName.includes('contrast') ? colorValue : '#FFF',
			padding: '16px',
			borderRadius: '8px',
			textAlign: 'center',
		}}
	>
		<Typography variant="body1" component="p">
			{colorName}: {colorValue}
		</Typography>
	</Box>
);

const HelpPage = () => (
	<Layout>
		<Container maxWidth="lg">
			<Typography variant="h4" component="h2" gutterBottom>
				Information
			</Typography>

			<Typography variant="h5" component="h3" gutterBottom>
				Color Palette Samples
			</Typography>

			<Grid container spacing={4}>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Primary - Main" colorValue="#4CAF50" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Primary - Light" colorValue="#81C784" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Primary - Dark" colorValue="#388E3C" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Secondary - Main" colorValue="#FF5722" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Secondary - Light" colorValue="#FF8A65" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Secondary - Dark" colorValue="#E64A19" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Error - Main" colorValue="#F44336" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Warning - Main" colorValue="#FFC107" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Info - Main" colorValue="#03A9F4" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Success - Main" colorValue="#4CAF50" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Background - Default" colorValue="#F5F5F5" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Text - Primary" colorValue="#212121" />
				</Grid>
				<Grid item xs={12} sm={6} md={4}>
					<ColorSample colorName="Text - Secondary" colorValue="#757575" />
				</Grid>
			</Grid>

			<Typography variant="h5" component="h3" gutterBottom style={{ marginTop: '2rem' }}>
				Buttons with Palette Colors
			</Typography>

			<Box sx={{ '& button': { m: 1 } }}>
				<Button variant="contained" color="primary">Primary Button</Button>
				<Button variant="contained" color="secondary">Secondary Button</Button>
				<Button variant="contained" color="error">Error Button</Button>
				<Button variant="contained" color="warning">Warning Button</Button>
				<Button variant="contained" color="info">Info Button</Button>
				<Button variant="contained" color="success">Success Button</Button>
			</Box>
		</Container>
	</Layout>
);

export default HelpPage;
