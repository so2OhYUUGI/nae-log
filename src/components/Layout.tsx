import React, { PropsWithChildren } from 'react';
import ResponsiveMenu from './ResponsiveMenu';
import { useMediaQuery } from '@mui/material';

function Layout({ children }: PropsWithChildren) {
	const isTabletOrLarger = useMediaQuery('(min-width:768px)');

	return (
		<div style={{ display: 'flex', flexDirection: isTabletOrLarger ? 'row' : 'column', height: '100vh' }}>
			{isTabletOrLarger && (
				<aside style={{ width: '250px', backgroundColor: '#f4f4f4' }}>
					<ResponsiveMenu />
				</aside>
			)}
			<main style={{ flex: 1, overflowY: 'auto' }}>
				{children}
			</main>
			{!isTabletOrLarger && (
				<footer style={{ backgroundColor: '#f4f4f4' }}>
					<ResponsiveMenu />
				</footer>
			)}
		</div>
	);
};

export default Layout;
