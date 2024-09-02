// src/data/menuItems.tsx
import React from 'react';
import HomeIcon from '@mui/icons-material/Home';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import LightbulbIcon from '@mui/icons-material/Lightbulb';
import ThermostatIcon from '@mui/icons-material/Thermostat';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import SettingsIcon from '@mui/icons-material/Settings';
import HelpIcon from '@mui/icons-material/Help';
import { MenuItemType } from '../types/MenuTypes';

export const menuItems: MenuItemType[] = [
	{ icon: <HomeIcon />, href: "/home", label: "ホーム" },
	{ icon: <CameraAltIcon />, href: "/camera", label: "カメラ" },
	{ icon: <LightbulbIcon />, href: "/relay-control", label: "照明管理" },
	{ icon: <ThermostatIcon />, href: "/lamp", label: "温度 / 湿度記録" },
	{ icon: <CalendarTodayIcon />, href: "/calendar", label: "カレンダー" }
];

export const moreMenuItems: MenuItemType[] = [
	{ icon: <SettingsIcon />, href: "/settings", label: "設定" },
	{ icon: <HelpIcon />, href: "/help", label: "ヘルプ" }
];
