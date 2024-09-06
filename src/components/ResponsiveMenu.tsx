// src/components/ResponsiveMenu.tsx
import React from 'react';
import { Box, List, ListItemButton, ListItemIcon, ListItemText, BottomNavigation, BottomNavigationAction, useMediaQuery, IconButton, Menu, MenuItem } from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';

import { menuItems, moreMenuItems } from '../data/menuItems';

function ResponsiveMenu({ }) {
  const isTabletOrLarger = useMediaQuery('(min-width:768px)');
  const isSmallScreen = useMediaQuery('(max-width:767px)'); // スマホ画面のクエリ
  const [value, setValue] = React.useState(0);
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);

  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Box>
      {isTabletOrLarger ? (
        // 横画面（タブレット横置きまたはPC用）表示用のスタイル
        <List>
          {menuItems.concat(moreMenuItems).map((item, index) => (
            <ListItemButton key={index} href={item.href}>
              <ListItemIcon>
                {React.cloneElement(item.icon, { fontSize: 'large' })}
              </ListItemIcon>
              <ListItemText primary={<span style={{ fontSize: '1.25rem' }}>{item.label}</span>} />
            </ListItemButton>
          ))}
        </List>
      ) : (
        // 縦画面（モバイルやタブレット縦置き）表示用のスタイル
        <>
          <BottomNavigation
            value={value}
            onChange={(event, newValue) => {
              setValue(newValue);
            }}
            showLabels={isTabletOrLarger}
          >
            {menuItems.map((item, index) => (
              <BottomNavigationAction
                key={index}
                label={isTabletOrLarger ? item.label : ""}
                icon={React.cloneElement(item.icon, { fontSize: isSmallScreen ? 'small' : 'medium' })} // スマホ画面ではアイコンを小さく
                href={item.href}
              />
            ))}
            <BottomNavigationAction
              icon={<MoreVertIcon />}
              onClick={handleClick}
            />
          </BottomNavigation>

          <Menu
            anchorEl={anchorEl}
            open={open}
            onClose={handleClose}
          >
            {moreMenuItems.map((item, index) => (
              <MenuItem key={index} onClick={handleClose} component="a" href={item.href}>
                <ListItemIcon>
                  {React.cloneElement(item.icon, { fontSize: 'small' })}
                </ListItemIcon>
                <ListItemText primary={item.label} />
              </MenuItem>
            ))}
          </Menu>
        </>
      )}
    </Box>
  );
};

export default ResponsiveMenu;
