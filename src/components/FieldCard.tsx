// src/components/FieldCard.tsx
import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import ThermostatIcon from '@mui/icons-material/Thermostat';
import OpacityIcon from '@mui/icons-material/Opacity';
import PowerIcon from '@mui/icons-material/Power';

import { FieldCardProps } from '../types/FieldCardTypes'; // 型をインポート

const FieldCard: React.FC<FieldCardProps> = ({ fieldName, camera, temperature, humidity, powerStatus }) => {
	return (
		<Card>
			<CardContent>
				<Typography variant="h5" component="h2" gutterBottom>
					{fieldName}
				</Typography>
				<Box display="flex" alignItems="center" mb={2}>
					<CameraAltIcon />
					<Typography variant="body1" ml={1}>
						カメラ: {camera ? "使用中" : "未使用"}
					</Typography>
				</Box>
				<Box display="flex" alignItems="center" mb={2}>
					<ThermostatIcon />
					<Typography variant="body1" ml={1}>
						温度: {temperature}°C
					</Typography>
				</Box>
				<Box display="flex" alignItems="center" mb={2}>
					<OpacityIcon />
					<Typography variant="body1" ml={1}>
						湿度: {humidity}%
					</Typography>
				</Box>
				<Box display="flex" alignItems="center" mb={2}>
					<PowerIcon />
					<Typography variant="body1" ml={1}>
						電源1: {powerStatus[0] ? "オン" : "オフ"}
					</Typography>
				</Box>
				<Box display="flex" alignItems="center" mb={2}>
					<PowerIcon />
					<Typography variant="body1" ml={1}>
						電源2: {powerStatus[1] ? "オン" : "オフ"}
					</Typography>
				</Box>
				<Box display="flex" alignItems="center">
					<PowerIcon />
					<Typography variant="body1" ml={1}>
						電源3: {powerStatus[2] ? "オン" : "オフ"}
					</Typography>
				</Box>
			</CardContent>
		</Card>
	);
};

export default FieldCard;
