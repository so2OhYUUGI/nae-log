import { createTheme } from '@mui/material/styles';

const theme = createTheme({
	palette: {
		primary: {
			main: '#4CAF50',    // メインカラー: 緑 (Main shade for primary elements)
			light: '#81C784',   // 薄い緑 (Lighter shade of primary)
			dark: '#388E3C',    // 濃い緑 (Darker shade of primary)
			contrastText: '#FFFFFF',  // 白 (Text color to contrast with primary)
		},
		secondary: {
			main: '#FF5722',    // サブカラー: オレンジ系赤 (Main shade for secondary elements)
			light: '#FF8A65',   // 薄いオレンジ (Lighter shade of secondary)
			dark: '#E64A19',    // 濃いオレンジ系赤 (Darker shade of secondary)
			contrastText: '#FFFFFF',  // 白 (Text color to contrast with secondary)
		},
		error: {
			main: '#F44336',    // 赤 (Main shade for error elements)
			light: '#E57373',   // 薄い赤 (Lighter shade of error)
			dark: '#D32F2F',    // 濃い赤 (Darker shade of error)
			contrastText: '#FFFFFF',  // 白 (Text color to contrast with error)
		},
		warning: {
			main: '#FFC107',    // 黄色 (Main shade for warning elements)
			light: '#FFD54F',   // 薄い黄色 (Lighter shade of warning)
			dark: '#FFA000',    // 濃い黄色 (Darker shade of warning)
			contrastText: '#000000',  // 黒 (Text color to contrast with warning)
		},
		info: {
			main: '#03A9F4',    // ブルー (Main shade for info elements)
			light: '#4FC3F7',   // 薄いブルー (Lighter shade of info)
			dark: '#0288D1',    // 濃いブルー (Darker shade of info)
			contrastText: '#FFFFFF',  // 白 (Text color to contrast with info)
		},
		success: {
			main: '#4CAF50',    // 緑 (Main shade for success elements)
			light: '#81C784',   // 薄い緑 (Lighter shade of success)
			dark: '#388E3C',    // 濃い緑 (Darker shade of success)
			contrastText: '#FFFFFF',  // 白 (Text color to contrast with success)
		},
		background: {
			default: '#F5F5F5', // 背景の薄いグレー (Background color)
		},
		text: {
			primary: '#212121', // 黒 (Primary text color)
			secondary: '#757575', // グレー (Secondary text color)
		},
	},
});

export default theme;
