// src/pages/home.tsx
import React, { useState } from 'react';
import { Container, Box, Typography, Grid, IconButton, useMediaQuery } from '@mui/material';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

import FieldCard from '../components/FieldCard';
import Layout from '../components/Layout';
import { FieldCardProps } from '../types/FieldCardTypes'; // 型をインポート

const fieldData: FieldCardProps[] = [
	{ fieldName: '圃場1', camera: true, temperature: 25, humidity: 60, powerStatus: [true, false, true] },
	{ fieldName: '圃場2', camera: false, temperature: 22, humidity: 55, powerStatus: [false, false, true] },
	{ fieldName: '圃場3', camera: true, temperature: 28, humidity: 70, powerStatus: [true, true, false] },
	// 他の圃場データも追加可能
];

const MainPage = () => {
	const isTabletOrLarger = useMediaQuery('(min-width:768px)');
	const isMobile = useMediaQuery('(max-width:767px)'); // スマホ画面用のクエリ
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
							width={isMobile ? '80%' : '90%'}  // スマホ画面で幅を調整
							mx="auto"
						>
							<IconButton onClick={handleBack} style={{ position: 'absolute', left: '10px' }}>
								<ArrowBackIosIcon />
							</IconButton>
							<Box px={2}>
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

export default MainPage;
