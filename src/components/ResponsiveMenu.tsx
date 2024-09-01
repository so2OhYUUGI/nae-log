import React from 'react';
import { Box, List, ListItemButton, ListItemIcon, ListItemText, BottomNavigation, BottomNavigationAction, useMediaQuery } from '@mui/material';
import HomeIcon from '@mui/icons-material/Home';
import SettingsIcon from '@mui/icons-material/Settings';
import InfoIcon from '@mui/icons-material/Info';

type MenuItem = {
  icon: JSX.Element;
  href: string;
  label: string;
};

const menuItems: MenuItem[] = [
  { icon: <HomeIcon fontSize="large" />, href: "/main", label: "Home" },
  { icon: <SettingsIcon fontSize="large" />, href: "/settings", label: "Settings" },
  { icon: <InfoIcon fontSize="large" />, href: "/info", label: "Info" }
];

const ResponsiveMenu: React.FC = () => {
  const isTabletOrLarger = useMediaQuery('(min-width:768px)');
  const [value, setValue] = React.useState(0);

  return (
    <Box>
      {isTabletOrLarger ? (
        // 横画面（タブレット横置きまたはPC用）表示用のスタイル
        <List>
          {menuItems.map((item, index) => (
            <ListItemButton key={index} href={item.href}>
              <ListItemIcon>
                {item.icon}
              </ListItemIcon>
              <ListItemText primary={<span style={{ fontSize: '1.25rem' }}>{item.label}</span>} />
            </ListItemButton>
          ))}
        </List>
      ) : (
        // 縦画面（モバイルやタブレット縦置き）表示用のスタイル
        <BottomNavigation
          value={value}
          onChange={(event, newValue) => {
            setValue(newValue);
          }}
          showLabels
        >
          {menuItems.map((item, index) => (
            <BottomNavigationAction
              key={index}
              label={item.label}
              icon={item.icon}
              href={item.href}
            />
          ))}
        </BottomNavigation>
      )}
    </Box>
  );
};

export default ResponsiveMenu;
