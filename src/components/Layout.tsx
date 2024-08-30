import React, { ReactNode } from 'react';
import { Container, AppBar, Toolbar, Typography, Box } from '@mui/material';

interface LayoutProps {
	children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
	return (
		<Box>
			<AppBar position="static">
				<Toolbar>
					<Typography variant="h6" color="inherit">
						NaeLOG
					</Typography>
				</Toolbar>
			</AppBar>
			<Container maxWidth="lg">
				<Box mt={2}>{children}</Box>
			</Container>
		</Box>
	);
};

export default Layout;
