import React, { useState, useEffect } from "react";
import { Button, TextField, Box, Typography, Container } from "@mui/material";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";

// API URL
const API_URL = "http://raspberrypi.local:8000/api/relay";
const API_TIME_URL = "http://raspberrypi.local:8000/api/relay/schedule";

// リレーの状態を取得する
const fetchRelayStatus = async () => {
	const response = await axios.get(API_URL);
	return response.data;
};

// リレーの状態を切り替える
const toggleRelay = async (state: "on" | "off") => {
	const response = await axios.post(API_URL, { state });
	return response.data;
};

// 時刻を設定する
const setSchedule = async (schedule: { action: string, hour: number, minute: number }) => {
	const response = await axios.post(API_TIME_URL, schedule);
	console.log(response.data);
	return response.data;
};

const LampControl: React.FC = () => {
	const [onTime, setOnTime] = useState<string>("");
	const [offTime, setOffTime] = useState<string>("");
	const [relayState, setRelayState] = useState<"on" | "off">("off");

	useEffect(() => {
		const fetchStatus = async () => {
			const { state } = await fetchRelayStatus();
			setRelayState(state);
		};
		fetchStatus();
	}, []);

	const { mutate: toggleRelayMutation } = useMutation({mutationFn: toggleRelay});
	const { mutate: setScheduleMutation } = useMutation({mutationFn: setSchedule});

	const handleOnTimeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setOnTime(event.target.value);
	};

	const handleOffTimeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setOffTime(event.target.value);
	};

	const handleSetSchedule = (action: "on" | "off") => {
		const [hour, minute] = action === "on" ? onTime.split(":") : offTime.split(":");
		if (hour && minute) {
			setScheduleMutation({ action, hour: parseInt(hour, 10), minute: parseInt(minute, 10) });
		}
	};

	const handleToggleRelay = () => {
		const newState = relayState === "on" ? "off" : "on";
		toggleRelayMutation(newState);
		setRelayState(newState);
	};

	return (
		<Container>
			<Typography variant="h4" gutterBottom>
				リレーコントロール
			</Typography>
			<Box mb={2}>
				<TextField
					label="点灯時刻 (HH:MM)"
					type="time"
					value={onTime}
					onChange={handleOnTimeChange}
					fullWidth
				/>
				<Button
					variant="contained"
					color="primary"
					onClick={() => handleSetSchedule("on")}
					style={{ marginTop: 10 }}
				>
					点灯時刻設定
				</Button>
			</Box>
			<Box mb={2}>
				<TextField
					label="消灯時刻 (HH:MM)"
					type="time"
					value={offTime}
					onChange={handleOffTimeChange}
					fullWidth
				/>
				<Button
					variant="contained"
					color="primary"
					onClick={() => handleSetSchedule("off")}
					style={{ marginTop: 10 }}
				>
					消灯時刻設定
				</Button>
			</Box>
			<Button
				variant="contained"
				color={relayState === "on" ? "secondary" : "primary"}
				onClick={handleToggleRelay}
			>
				{relayState === "on" ? "リレーを消す" : "リレーを点ける"}
			</Button>
		</Container>
	);
};

export default LampControl;
