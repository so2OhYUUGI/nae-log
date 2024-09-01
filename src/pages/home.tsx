// src/pages/home.tsx
import React, { useState } from 'react';
import { Container, Box, Typography, Grid, IconButton, useMediaQuery } from '@mui/material';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

import FieldCard from '../components/FieldCard';
import Layout from '../components/Layout';
import { fieldData } from '../data/fieldData';

const HomePage = () => {
	const isTabletOrLarger = useMediaQuery('(min-width:768px)');
	const [currentIndex, setCurrentIndex] = useState(0);

	const handleNext = () => {
		setCurrentIndex((prevIndex) => (prevIndex + 1) % fieldData.length);
	};

	const handleBack = () => {
		setCurrentIndex((prevIndex) => (prevIndex - 1 + fieldData.length) % fieldData.length);
	};

	return (
		<Layout>
			<Container maxWidth="lg">
				<Box py={5}>
					<Typography variant="h4" component="h2" gutterBottom>
						NaeLOG Dashboard
					</Typography>
					{isTabletOrLarger ? (
						<Grid container spacing={4} direction="column" wrap="nowrap">
							{fieldData.map((field, index) => (
								<Grid item xs={12} key={index}>
									<FieldCard {...field} />
								</Grid>
							))}
						</Grid>
					) : (
						<Box
							position="relative"
							display="flex"
							alignItems="center"
							justifyContent="center"
							width="100%" // スマホ画面で幅を調整
							mx="auto"
						>
							<IconButton onClick={handleBack} style={{ position: 'absolute', left: '10px' }}>
								<ArrowBackIosIcon />
							</IconButton>
							<Box px={2} width="90%">
								<FieldCard {...fieldData[currentIndex]} />
							</Box>
							<IconButton onClick={handleNext} style={{ position: 'absolute', right: '10px' }}>
								<ArrowForwardIosIcon />
							</IconButton>
						</Box>
					)}
				</Box>
			</Container>
		</Layout>
	);
};

export default HomePage;
